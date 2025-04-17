import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

st.set_page_config(page_title='Exam 1 - Full Notebook View', layout='wide')
st.title('🚗 Exam 1 - Automobile Data Analysis (Notebook Style)')

# Load dataset from GitHub
df = pd.read_csv('https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv')
st.success('✅ Dataset loaded from GitHub')
st.dataframe(df.head())

st.code("""
import pandas as pd
import numpy as np
""")
st.code("""

path = 'CleanedAutomobile.csv'
df = pd.read_csv(path)
""")
st.code("""
# list the data types for each column
print(df.dtypes)
""")
st.code("""
# Write your code below and press Shift+Enter to execute
print(df['peak-rpm'].dtype)
""")
st.code("""
# Correlation

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
correlation_matrix = df[numeric_cols].corr()
print(correlation_matrix)
""")
st.code("""
# Write your code below and press Shift+Enter to execute
df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr()
""")
st.code("""
# Engine size as potential predictor variable of price
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)
""")
st.code("""
df[["engine-size", "price"]].corr()
""")
st.code("""
sns.regplot(x="highway-mpg", y="price", data=df)
""")
st.code("""
df[['highway-mpg', 'price']].corr()
""")
st.code("""
sns.regplot(x="peak-rpm", y="price", data=df)
""")
st.code("""
df[['peak-rpm','price']].corr()
""")
st.code("""
# Write your code below and press Shift+Enter to execute
df[["stroke","price"]].corr()
""")
st.code("""
# Write your code below and press Shift+Enter to execute
sns.regplot(x="stroke", y="price", data=df)
""")
st.code("""
sns.boxplot(x="body-style", y="price", data=df)
""")
st.code("""
sns.boxplot(x="engine-location", y="price", data=df)
""")
st.code("""
# drive-wheels
sns.boxplot(x="drive-wheels", y="price", data=df)
""")
st.code("""
df.describe()
""")
st.code("""
df.describe(include=['object'])
""")
st.code("""
df['drive-wheels'].value_counts()
""")
st.code("""
df['drive-wheels'].value_counts().to_frame()
""")
st.code("""
drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
drive_wheels_counts
""")
st.code("""
drive_wheels_counts.index.name = 'drive-wheels'
drive_wheels_counts
""")
st.code("""
# engine-location as variable
engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'
engine_loc_counts.head(10)
""")
st.code("""
df['drive-wheels'].unique()
""")
st.code("""
df_group_one = df[['drive-wheels','body-style','price']]
""")
st.code("""
# grouping results
df_group_one = df_group_one.groupby(['drive-wheels'],as_index=False)['price'].mean()
df_group_one
""")
st.code("""
# grouping results
df_group_one = df_group_one.groupby(['drive-wheels'],as_index=False).mean()
df_group_one
""")
st.code("""
# grouping results
df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
grouped_test1
""")
st.code("""

df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'], as_index=False).mean()
grouped_pivot = grouped_test1.pivot(index='drive-wheels', columns='body-style', values='price')
""")
st.code("""
grouped_pivot = grouped_pivot.fillna(0) #fill missing values with 0
grouped_pivot
""")
st.code("""
# Write your code below and press Shift+Enter to execute
# Group by body-style and calculate the mean price
body_style_avg_price = df.groupby('body-style')['price'].mean()
body_style_avg_price
""")
st.code("""
#use the grouped results
plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.show()
""")
st.pyplot(plt.gcf())
st.code("""

fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap='RdBu')

# label names
row_labels = grouped_pivot.columns
col_labels = grouped_pivot.index

# move ticks and labels to the center
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

# insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

# rotate label if too long
plt.xticks(rotation=90)

fig.colorbar(im)
plt.show()
""")
st.pyplot(plt.gcf())
st.code("""
# Calculate the Pearson correlation of numeric columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
correlation_matrix = df[numeric_cols].corr()
print(correlation_matrix)
""")
st.code("""
from scipy import stats
""")
st.code("""
pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)
""")
st.code("""
pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)
""")
st.code("""
pearson_coef, p_value = stats.pearsonr(df['length'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)
""")
st.code("""
pearson_coef, p_value = stats.pearsonr(df['width'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value )
""")
st.code("""
pearson_coef, p_value = stats.pearsonr(df['curb-weight'], df['price'])
print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)
""")
st.code("""
pearson_coef, p_value = stats.pearsonr(df['engine-size'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)
""")
st.code("""
pearson_coef, p_value = stats.pearsonr(df['bore'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =  ", p_value )
""")
st.code("""
pearson_coef, p_value = stats.pearsonr(df['city-mpg'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)
""")
st.code("""
pearson_coef, p_value = stats.pearsonr(df['highway-mpg'], df['price'])
print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value )
""")
