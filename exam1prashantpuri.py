
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Streamlit App Setup
st.set_page_config(page_title="Exam 1 - Automobile Data Analysis", layout="wide")
st.title("🚗 Exam 1 - Automobile Dataset Analysis")
st.markdown("Prepared by **Prashant Puri** | Banner ID: 001397936")

# Load dataset
st.header("1. Import Data from Part 1")
path = 'https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv'
df = pd.read_csv(path)
st.dataframe(df.head())

# Data types
st.subheader("Data Types in the Dataset")
st.code(df.dtypes.astype(str).to_string())

# Correlation matrix (all numerics)
st.subheader("Correlation Matrix")
st.dataframe(df.corr(numeric_only=True))

# Correlation subset
st.subheader("Correlation: bore, stroke, compression-ratio, horsepower")
st.dataframe(df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr())

# Visualizations
st.header("2. Visualization of Individual Features")

def reg_plot(x, y):
    fig, ax = plt.subplots()
    sns.regplot(x=x, y=y, data=df, ax=ax)
    ax.set_title(f"{x} vs {y}")
    st.pyplot(fig)

reg_plot('engine-size', 'price')
reg_plot('highway-mpg', 'price')
reg_plot('peak-rpm', 'price')
reg_plot('stroke', 'price')

def box_plot(x, y='price'):
    fig, ax = plt.subplots()
    sns.boxplot(x=x, y=y, data=df, ax=ax)
    ax.set_title(f"{x} vs {y}")
    st.pyplot(fig)

box_plot('body-style')
box_plot('engine-location')
box_plot('drive-wheels')

# Descriptive Stats
st.header("3. Descriptive Statistical Analysis")
st.subheader("Numerical Features")
st.dataframe(df.describe())
st.subheader("Categorical Features")
st.dataframe(df.describe(include=['object']))

# Frequency
st.subheader("Value Counts for drive-wheels")
st.dataframe(df['drive-wheels'].value_counts().to_frame())

# Grouping
st.header("4. Grouping and Pivot Tables")
grouped = df[['drive-wheels', 'body-style', 'price']]
grouped_avg = grouped.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
pivot_table = grouped_avg.pivot(index='drive-wheels', columns='body-style', values='price').fillna(0)
st.dataframe(pivot_table)

# Heatmap
st.subheader("Heatmap of Drive-Wheels and Body-Style vs Price")
fig, ax = plt.subplots()
sns.heatmap(pivot_table, annot=True, fmt=".1f", cmap="YlGnBu", ax=ax)
st.pyplot(fig)

# Correlation and Causation
st.header("5. Correlation and Causation")

def corr_test(feature, target='price'):
    coef, p = stats.pearsonr(df[feature], df[target])
    st.write(f"**{feature} vs {target}**: Coefficient = {coef:.3f}, P-value = {p:.5f}")

features_to_test = [
    'wheel-base', 'horsepower', 'length', 'width',
    'curb-weight', 'engine-size', 'bore', 'city-mpg', 'highway-mpg'
]

for feature in features_to_test:
    corr_test(feature)

# Conclusion
st.header("Conclusion")
st.markdown("""
**Most influential variables on price:**

- Continuous: engine-size, horsepower, width, curb-weight, length, wheel-base
- Categorical: drive-wheels

These variables show high correlation with price and are significant for modeling.
""")

# Footer
st.markdown("---")
st.caption("Streamlit App | Exam 1 Submission | © Prashant Puri 2025")
