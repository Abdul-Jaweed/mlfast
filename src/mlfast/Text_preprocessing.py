import nltk

nltk.download("stopwords")
from nltk.corpus import stopwords

stopwords.words("english")
nltk.download("punkt")
nltk.download("wordnet")
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import re


def Text_preprocessing(
    text,
    stem=False,
    lemmatize=False,
    remove_html=True,
    remove_emoji=True,
    remove_special_chars=True,
    remove_extra_spaces=True,
    remove_url=True,
):
    # Removing HTML tags
    if remove_html:
        html_pattern = re.compile("<.*?>")
        text = html_pattern.sub("", text)

    # Removing URLs
    if remove_url:
        url_pattern = re.compile(r"https?://\S+|www\.\S+")
        text = url_pattern.sub("", text)

    # # Removing emojis
    # if remove_emoji:
    #     text = emoji.demojize(text)
    #     text = re.sub(r":[a-zA-Z_]+:", "", text)

    # Removing emojis
    if remove_emoji:
        emoji_pattern = re.compile(
            "["
            "\U0001F600-\U0001F64F"  # emoticons
            "\U0001F300-\U0001F5FF"  # symbols & pictographs
            "\U0001F680-\U0001F6FF"  # transport & map symbols
            "\U0001F1E0-\U0001F1FF"  # flags (iOS)
            "\U00002702-\U000027B0"  # other miscellaneous symbols
            "\U000024C2-\U0001F251"
            "]+",
            flags=re.UNICODE,
        )
    text = emoji_pattern.sub(r"", text)
    text = re.sub(r":[a-zA-Z_]+:", "", text)  # Remove emoji names within colons
    text = re.sub(r"\s+", " ", text)  # Remove extra spaces

    # Removing special characters
    if remove_special_chars:
        text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    # Removing extra spaces
    if remove_extra_spaces:
        text = re.sub(r"\s+", " ", text).strip()

    # Tokenization
    words = word_tokenize(text)

    # Stop word removal
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word.casefold() not in stop_words]

    # Stemming or Lemmatization
    if stem and not lemmatize:
        stemmer = PorterStemmer()
        stemmed_words = [stemmer.stem(word) for word in filtered_words]
        return " ".join(stemmed_words)

    elif not stem and lemmatize:
        lemmatizer = WordNetLemmatizer()
        lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
        return " ".join(lemmatized_words)

    elif not stem and not lemmatize:
        return " ".join(filtered_words)

    else:
        raise ValueError("Only one of 'stem' or 'lemmatize' can be set to True.")
