
# Prashant Puri - Exam 1 Full Automobile Data Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
path = 'https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv'
df = pd.read_csv(path)
print("Data preview:")
print(df.head())


# --- Code Cell ---
import pandas as pd
import numpy as np


# --- Code Cell ---
path='https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv'
df = pd.read_csv(path)
df.head()


# --- Code Cell ---
import matplotlib.pyplot as plt
import seaborn as sns


# --- Code Cell ---
# list the data types for each column
print(df.dtypes)


# --- Code Cell ---
# Write your code below and press Shift+Enter to execute
print(df['peak-rpm'].dtype)


# --- Code Cell ---
# Correlation

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
correlation_matrix = df[numeric_cols].corr()
print(correlation_matrix)


# --- Code Cell ---
# Write your code below and press Shift+Enter to execute
df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr()


# --- Code Cell ---
# Engine size as potential predictor variable of price
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)


# --- Code Cell ---
df[["engine-size", "price"]].corr()


# --- Code Cell ---
sns.regplot(x="highway-mpg", y="price", data=df)


# --- Code Cell ---
df[['highway-mpg', 'price']].corr()


# --- Code Cell ---
sns.regplot(x="peak-rpm", y="price", data=df)


# --- Code Cell ---
df[['peak-rpm','price']].corr()


# --- Code Cell ---
# Write your code below and press Shift+Enter to execute
df[["stroke","price"]].corr()


# --- Code Cell ---
# Write your code below and press Shift+Enter to execute
sns.regplot(x="stroke", y="price", data=df)


# --- Code Cell ---
sns.boxplot(x="body-style", y="price", data=df)


# --- Code Cell ---
sns.boxplot(x="engine-location", y="price", data=df)


# --- Code Cell ---
# drive-wheels
sns.boxplot(x="drive-wheels", y="price", data=df)


# --- Code Cell ---
df.describe()


# --- Code Cell ---
df.describe(include=['object'])


# --- Code Cell ---
df['drive-wheels'].value_counts()


# --- Code Cell ---
df['drive-wheels'].value_counts().to_frame()


# --- Code Cell ---
drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
drive_wheels_counts


# --- Code Cell ---
drive_wheels_counts.index.name = 'drive-wheels'
drive_wheels_counts


# --- Code Cell ---
# engine-location as variable
engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'
engine_loc_counts.head(10)


# --- Code Cell ---
df['drive-wheels'].unique()


# --- Code Cell ---
df_group_one = df[['drive-wheels','body-style','price']]


# --- Code Cell ---
# grouping results
df_group_one = df_group_one.groupby(['drive-wheels'],as_index=False)['price'].mean()
df_group_one


# --- Code Cell ---
# grouping results
df_group_one = df_group_one.groupby(['drive-wheels'],as_index=False).mean()
df_group_one


# --- Code Cell ---
# grouping results
df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
grouped_test1


# --- Code Cell ---
grouped_pivot = grouped_pivot.fillna(0) #fill missing values with 0
grouped_pivot


# --- Code Cell ---
# Write your code below and press Shift+Enter to execute
# Group by body-style and calculate the mean price
body_style_avg_price = df.groupby('body-style')['price'].mean()
body_style_avg_price


# --- Code Cell ---
import matplotlib.pyplot as plt


# --- Code Cell ---
#use the grouped results
plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.show()


# --- Code Cell ---
fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap='RdBu')

#label names
row_labels = grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index

#move ticks and labels to the center
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

#insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

#rotate label if too long
plt.xticks(rotation=90)

fig.colorbar(im)
plt.show()


# --- Code Cell ---
# Calculate the Pearson correlation of numeric columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
correlation_matrix = df[numeric_cols].corr()
print(correlation_matrix)


# --- Code Cell ---
from scipy import stats


# --- Code Cell ---
pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)


# --- Code Cell ---
pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)


# --- Code Cell ---
pearson_coef, p_value = stats.pearsonr(df['length'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)


# --- Code Cell ---
pearson_coef, p_value = stats.pearsonr(df['width'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value )


# --- Code Cell ---
pearson_coef, p_value = stats.pearsonr(df['curb-weight'], df['price'])
print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)


# --- Code Cell ---
pearson_coef, p_value = stats.pearsonr(df['engine-size'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)


# --- Code Cell ---
pearson_coef, p_value = stats.pearsonr(df['bore'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =  ", p_value )


# --- Code Cell ---
pearson_coef, p_value = stats.pearsonr(df['city-mpg'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)


# --- Code Cell ---
pearson_coef, p_value = stats.pearsonr(df['highway-mpg'], df['price'])
print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value )
