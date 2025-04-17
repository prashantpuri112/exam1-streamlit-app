
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Setup page
st.set_page_config(page_title="Car Price Analysis Full Output", layout="wide")
st.title("🚗 Car Price Analysis Full Report")
st.markdown("**Name:** Prashant Puri  
**Banner ID:** 001397936")

# Table of Contents
st.markdown("""
## 📘 Table of Contents
1. [Import Data](#import-data)
2. [Analyzing Individual Feature Patterns](#analyzing-individual-feature-patterns)
3. [Descriptive Statistical Analysis](#descriptive-statistical-analysis)
4. [Basics of Grouping](#basics-of-grouping)
5. [Correlation and Causation](#correlation-and-causation)
""", unsafe_allow_html=True)

# Section 1: Import Data
st.header("📥 Import Data")
st.markdown("We will import the automobile dataset which includes features such as engine size, body style, drive wheels, and price.")
path = 'https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv'
df = pd.read_csv(path)
st.dataframe(df.head())

# Section 2: Feature Visualization
st.header("📊 Analyzing Individual Feature Patterns")
st.markdown("Visualizing relationships using `regplot` and `boxplot` for better understanding of how each feature impacts price.")

fig1, ax1 = plt.subplots()
sns.regplot(x="engine-size", y="price", data=df, ax=ax1)
st.pyplot(fig1)

fig2, ax2 = plt.subplots()
sns.boxplot(x="body-style", y="price", data=df, ax=ax2)
st.pyplot(fig2)

fig3, ax3 = plt.subplots()
sns.boxplot(x="drive-wheels", y="price", data=df, ax=ax3)
st.pyplot(fig3)

fig4, ax4 = plt.subplots()
sns.regplot(x="highway-mpg", y="price", data=df, ax=ax4)
st.pyplot(fig4)

# Section 3: Descriptive Statistics
st.header("📈 Descriptive Statistical Analysis")
st.markdown("We use `describe()` to get summary statistics for each numerical feature.")
desc = df.describe()
st.dataframe(desc)

# Section 4: Basics of Grouping
st.header("🔍 Basics of Grouping")
st.markdown("We group by `drive-wheels` and `body-style` to analyze average prices.")

df_group_test1 = df[['drive-wheels', 'body-style', 'price']]
grouped_test2 = df_group_test1.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
pivot = grouped_test2.pivot(index='drive-wheels', columns='body-style').fillna(0)
st.dataframe(pivot)

fig5, ax5 = plt.subplots(figsize=(10, 5))
pivot.plot(kind='bar', ax=ax5)
plt.xticks(rotation=45)
st.pyplot(fig5)

# Section 5: Correlation and Causation
st.header("📌 Correlation and Causation")
st.markdown("We use correlation matrix and visualizations to understand numerical relationships.")

corr = df.corr(numeric_only=True)
st.subheader("Correlation Matrix")
st.dataframe(corr)

fig6, ax6 = plt.subplots(figsize=(12, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax6)
st.pyplot(fig6)

fig7, ax7 = plt.subplots()
sns.regplot(x="engine-size", y="price", data=df, ax=ax7)
st.pyplot(fig7)

fig8, ax8 = plt.subplots()
sns.regplot(x="highway-mpg", y="price", data=df, ax=ax8)
st.pyplot(fig8)

fig9, ax9 = plt.subplots()
sns.boxplot(x="drive-wheels", y="price", data=df, ax=ax9)
st.pyplot(fig9)

fig10, ax10 = plt.subplots()
sns.boxplot(x="engine-location", y="price", data=df, ax=ax10)
st.pyplot(fig10)

st.success("✅ Full analysis complete. All outputs have been printed as per the notebook.")
