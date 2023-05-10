# mlfast

This Python machine learning package is built on top of scikit-learn and provides a simple API for regression and classification modeling. The main function in this package is called Regression() and Classification() which takes in the following arguments:

`X`: The independent variables (features) of the data set

`y`: The dependent variable (target) of the data set

`model`: The name of the regression and classification algorithm to be used (e.g. `lr` for Linear Regression, or `rf` for Random Forest Classifier, etc.)

`scaler`: The name of the data scaler to be used (e.g. "standard" for StandardScaler, "robust" for RobustScaler, etc.)

`cat`: A boolean indicating [`True` or `False`] whether the data set has categorical variables that need to be one-hot encoded



- PYPI link for this package - [mlfast](https://pypi.org/project/mlfast/)


## Getting Started

### Installations

!!! note "Installation steps"
    First let's do an easy pip installation of the library by running the following command -
    ```python
    pip install mlfast
    ```

## Usage

### Regression Algorithms

!!! note "For Regression Modeling"
    Import Regression Model -
    ```python
    from mlfast import Regression
    ```





**Linear Regression**  -> 'lr' 
```python

Regression(X, y, model = 'lr')

```


**Ridge Regression**  -> 'ridge ' 
```python

Regression(X, y, model = 'ridge', scaler =  'standard')

```

**Lasso Regression**  -> 'lasso' 
```python

Regression(X, y, model = 'lasso', scaler =  'robust')

```

**ElasticNet**  -> 'enet' 
```python

Regression(X, y, model = 'enet', cat=True)

```


**Random Forest Regressor**  -> 'rf' 
```python

Regression(X, y, model = 'rf',scaler = 'standard', cat=True)

```



**Decision Tree Regressor**  -> 'dt' 
```python

Regression(X, y, model = 'dt')

```


**Support Vector Machine Regression**  -> 'svm ' 
```python

Regression(X, y, model = 'svm', scaler =  'standard')

```

**KNeighbors Regressor**  -> 'knn' 
```python

Regression(X, y, model = 'knn', scaler =  'robust')

```

**Gradient Boosting Regressor**  -> 'gb' 
```python

Regression(X, y, model = 'gb', cat=True)

```


**AdaBoost Regressor**  -> 'ada' 
```python

Regression(X, y, model = 'ada',scaler = 'standard', cat=True)

```


**XGBoost Regressor**  -> 'xbg' 
```python

Regression(X, y, model = 'xbg',scaler = 'standard', cat=True)

```





### Classification Algorithms


!!! note "For Classification Modeling"
    Import Classification Model -
    ```python
    from mlfast import Classification
    ```





**Logistic Regression**  -> 'lr' 
```python

Classification(X, y, model = 'lr')

```


**Random Forest Classifier**  -> 'rf' 
```python

Classification(X, y, model = 'rf',scaler = 'standard', cat=True)

```



**Decision Tree Classifier**  -> 'dt' 
```python

Classification(X, y, model = 'dt')

```


**Support Vector Machine Classifier**  -> 'svm ' 
```python

Classification(X, y, model = 'svm', scaler =  'standard')

```

**KNeighbors Classifier**  -> 'knn' 
```python

Classification(X, y, model = 'knn', scaler =  'robust')

```

**Gradient Boosting Classifier**  -> 'gb' 
```python

Classification(X, y, model = 'gb', cat=True)

```


**AdaBoost Classifier**  -> 'ada' 
```python

Classification(X, y, model = 'ada',scaler = 'standard', cat=True)

```


**XGBoost Classifier**  -> 'xbg'

```python

Classification(X, y, model = 'xbg',scaler = 'standard', cat=True)
```




## Announcement

- Unsupervised Machine Learning Algorithms
- Hyperparameter Tuning
- Text Preprocessing
- Image Preprocessing
- And many more



**ADDED SOON**