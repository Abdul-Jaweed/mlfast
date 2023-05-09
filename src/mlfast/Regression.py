# importing Libraries
import os
import sys
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    AdaBoostRegressor,
)
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
import xgboost as xgb
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, RobustScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import pickle
import warnings

warnings.filterwarnings("ignore")


def Regression(X, y, model="lr", scaler=None, cat=False):
    import warnings

    warnings.filterwarnings("ignore")

    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=52
    )

    # One-hot encoding
    if cat:
        categorical_cols = X.select_dtypes(include=["O"]).columns.tolist()
        if categorical_cols:
            transformer = ColumnTransformer(
                transformers=[("ohe", OneHotEncoder(), categorical_cols)],
                remainder="passthrough",
            )
            X_train = transformer.fit_transform(X_train)
            X_test = transformer.transform(X_test)

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
        reg = LinearRegression()
    elif model == "ridge":
        reg = Ridge()
    elif model == "lasso":
        reg = Lasso()
    elif model == "enet":
        reg = ElasticNet()
    elif model == "dt":
        reg = DecisionTreeRegressor()
    elif model == "rf":
        reg = RandomForestRegressor()
    elif model == "svm":
        reg = SVR()
    elif model == "knn":
        reg = KNeighborsRegressor()
    elif model == "gb":
        reg = GradientBoostingRegressor()
    elif model == "ada":
        reg = AdaBoostRegressor()
    elif model == "xbg":
        reg = xgb.XGBRegressor(n_estimators=100, learning_rate=0.05, random_state=42)
    else:
        return print("Invalid model name")

    # Fitting the Model
    reg.fit(X_train, y_train)
    y_pred = reg.predict(X_test)

    # Printing Metrics
    print(
        f" Mean Absolute Error :{mean_absolute_error(y_test, y_pred)},\
    \n \n Mean Squared Error :{mean_squared_error(y_test, y_pred)},\
    \n \n Root Mean Squared Error :{np.sqrt(mean_squared_error(y_test, y_pred))},\
    \n \n R2 Score :{r2_score(y_test, y_pred)}"
    )

    # Saving the Model
    model_dir = "model"
    if not os.path.exists(model_dir):
        os.mkdir(model_dir)

    filename = os.path.join(model_dir, f"{model}.pkl")
    with open(filename, "wb") as file:
        pickle.dump(reg, file)

    print(f" \n Model saved successfully in {filename}")
