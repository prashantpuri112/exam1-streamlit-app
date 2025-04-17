# Rebuild the full script from earlier steps (reloaded kernel removed previous content)
# Since re-adding everything here, let's include the full final Streamlit script used earlier

full_streamlit_script = """
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

st.set_page_config(page_title="Exam 1 - Automobile Data Analysis", layout="wide")
st.title("🚗 Exam 1 - Automobile Data Analysis")
st.markdown("Prepared by **Prashant Puri** | MS in Analytics | Saint Louis University")

# Load dataset
st.header("📥 Load Dataset")
DATA_URL = 'https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv'
df = pd.read_csv(DATA_URL)
st.success("Dataset loaded successfully!")
st.dataframe(df.head())

st.markdown("## Table of Contents")
st.markdown(\"""1. Import Data from Part 1  
2. Analyzing Individual Feature Patterns using Visualization  
3. Descriptive Statistical Analysis  
4. Basics of Grouping  
5. Correlation and Causation  
\""")

# Show data types
st.header("Data Types")
st.text(df.dtypes.to_string())

# Correlation matrix
st.header("Correlation Matrix")
st.dataframe(df.corr(numeric_only=True))

# Selected correlation
st.subheader("Correlation: bore, stroke, compression-ratio, horsepower")
st.dataframe(df[['bore','stroke','compression-ratio','horsepower']].corr())

# Regression Plots
def reg_plot(x, y):
    fig, ax = plt.subplots()
    sns.regplot(x=x, y=y, data=df, ax=ax)
    ax.set_title(f"{x} vs {y}")
    st.pyplot(fig)

st.header("📈 Regression Plots")
reg_plot('engine-size', 'price')
reg_plot('highway-mpg', 'price')
reg_plot('peak-rpm', 'price')
reg_plot('stroke', 'price')

# Box Plots
def box_plot(x, y="price"):
    fig, ax = plt.subplots()
    sns.boxplot(x=x, y=y, data=df, ax=ax)
    ax.set_title(f"{x} vs {y}")
    st.pyplot(fig)

st.header("📦 Box Plots")
box_plot('body-style')
box_plot('engine-location')
box_plot('drive-wheels')

# Descriptive Statistics
st.header("📊 Descriptive Statistics")
st.dataframe(df.describe())
st.subheader("Categorical Descriptions")
st.dataframe(df.describe(include=['object']))

# Value Counts
st.subheader("Drive Wheels Count")
st.dataframe(df['drive-wheels'].value_counts().to_frame())

# Grouping
st.header("📐 Grouped Analysis")
grouped = df[['drive-wheels','body-style','price']]
grouped_test = grouped.groupby(['drive-wheels','body-style'], as_index=False).mean()
grouped_pivot = grouped_test.pivot(index='drive-wheels', columns='body-style', values='price')
grouped_pivot = grouped_pivot.fillna(0)
st.dataframe(grouped_pivot)

# Heatmap
fig, ax = plt.subplots()
sns.heatmap(grouped_pivot, annot=True, fmt=".1f", cmap="YlGnBu", ax=ax)
st.pyplot(fig)

# Pearson Correlations
st.header("📌 Pearson Correlation Tests")
features = ['wheel-base', 'horsepower', 'length', 'width', 'curb-weight', 'engine-size', 'bore', 'city-mpg', 'highway-mpg']
for feature in features:
    pearson_coef, p_value = stats.pearsonr(df[feature], df['price'])
    st.markdown(f"**{feature} vs price** — Coef: `{pearson_coef:.4f}`, P-value: `{p_value:.4g}`")

st.markdown("---")
st.caption("Exam 1 Project — Converted to Streamlit App | © Prashant Puri, 2025")
"""

# Save to file
streamlit_final_path = "/mnt/data/exam1prashantpuri_full_streamlit_app.py"
with open(streamlit_final_path, "w") as f:
    f.write(full_streamlit_script)

streamlit_final_path
