import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
from scipy.stats import skew
from sklearn.linear_model import Ridge
import xgboost as xgb
import lightgbm as lgb
from catboost import CatBoostRegressor
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

train_df = pd.read_csv(
    "/kaggle/input/house-price-prediction/train.csv"
)
test_df = pd.read_csv(
    "/kaggle/input/house-price-prediction/test.csv"
)

train_ID = train_df['Id']
test_ID = test_df['Id']
train_df.drop("Id", axis=1, inplace=True)
test_df.drop("Id", axis=1, inplace=True)

print(f"Number of training examples: {len(train_df)}")
print(f"Number of testing examples: {len(test_df)}")

print(f"Shape of train data: {train_df.shape}")
print(f"Shape of test data: {test_df.shape}")

columns = list(test_df.columns)
target_col = set(train_df.columns) - set(test_df.columns)
print(f"Features:\n{columns}\n")
print(f"Target:\n{target_col}")

full_df = pd.concat([train_df, test_df], axis=0)
full_df.shape

full_df.head()

full_df.info()

numeric_df = full_df.select_dtypes(include='number')
object_df = full_df.select_dtypes(include='object')

numeric_df.describe()

