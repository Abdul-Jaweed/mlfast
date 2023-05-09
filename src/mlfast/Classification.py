# importing Libraries

import os
import sys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier,
    AdaBoostClassifier,
)
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import xgboost as xgb
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import (
    StandardScaler,
    RobustScaler,
    OneHotEncoder,
    LabelEncoder,
)
from sklearn.compose import ColumnTransformer
import pickle
import warnings

warnings.filterwarnings("ignore")


def Classification(X, y, model="lr", scaler=None, cat=False):
    import warnings

    warnings.filterwarnings("ignore")

    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=52
    )

    # One-hot encoding
    if cat:
        categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()
        if categorical_cols:
            transformer = ColumnTransformer(
                transformers=[("ohe", OneHotEncoder(), categorical_cols)],
                remainder="passthrough",
            )
            X_train = transformer.fit_transform(X_train)
            X_test = transformer.transform(X_test)

    # Encoding the target variable if it is categorical
    if y_train.dtype == "O":
        le = LabelEncoder()
        y_train = le.fit_transform(y_train)
        y_test = le.transform(y_test)

    # Scaling the data
    if scaler == "standard":
        scaler = StandardScaler()
    elif scaler == "robust":
        scaler = RobustScaler()
    else:
        scaler = None

    if scaler is not None:
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

    # Selecting the Model
    if model == "lr":
        clf = LogisticRegression()
    elif model == "dt":
        clf = DecisionTreeClassifier()
    elif model == "rf":
        clf = RandomForestClassifier()
    elif model == "svm":
        clf = SVC()
    elif model == "knn":
        clf = KNeighborsClassifier()
    elif model == "gb":
        clf = GradientBoostingClassifier()
    elif model == "ada":
        clf = AdaBoostClassifier()
    elif model == "xbg":
        clf = xgb.XGBClassifier(n_estimators=100, learning_rate=0.05, random_state=42)
    else:
        return print("Invalid model name")

    # Fitting the Model
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    # Printing Metrics
    print(
        f"Accuracy Score :{accuracy_score(y_test, y_pred)}, \
    \n \n Classification Report  \n {classification_report(y_test, y_pred)} "
    )

    # Saving the Model
    model_dir = "model"
    if not os.path.exists(model_dir):
        os.mkdir(model_dir)

    filename = os.path.join(model_dir, f"{model}.pkl")
    with open(filename, "wb") as file:
        pickle.dump(clf, file)

    print(f" \n Model saved successfully in {filename}")
