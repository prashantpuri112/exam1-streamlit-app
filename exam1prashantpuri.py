
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Car Price Analysis", layout="wide")
st.title("🚗 Car Price Analysis - Streamlit App")
st.markdown("#### Prashant Puri | Banner ID: 001397936")

# 1. Import Data
path = 'https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv'
df = pd.read_csv(path)

st.header("📥 Loaded Dataset")
st.dataframe(df.head())

# 2. Feature Visualization
st.header("📊 Analyzing Individual Feature Patterns")
fig1, ax1 = plt.subplots(figsize=(10, 4))
sns.regplot(x="engine-size", y="price", data=df, ax=ax1)
st.pyplot(fig1)

fig2, ax2 = plt.subplots(figsize=(10, 4))
sns.boxplot(x="body-style", y="price", data=df, ax=ax2)
st.pyplot(fig2)

fig3, ax3 = plt.subplots(figsize=(10, 4))
sns.boxplot(x="drive-wheels", y="price", data=df, ax=ax3)
st.pyplot(fig3)

fig4, ax4 = plt.subplots(figsize=(10, 4))
sns.regplot(x="highway-mpg", y="price", data=df, ax=ax4)
st.pyplot(fig4)

# 3. Descriptive Statistics
st.header("📈 Descriptive Statistics")
desc_stats = df.describe()
st.dataframe(desc_stats)

# 4. Basics of Grouping
st.header("🔍 Grouped Analysis")
df_group_test1 = df[['drive-wheels','body-style','price']]
grouped_test2 = df_group_test1.groupby(['drive-wheels','body-style'],as_index=False).mean()
pivot = grouped_test2.pivot(index='drive-wheels', columns='body-style')
pivot = pivot.fillna(0)

st.subheader("Average Price (Pivot Table)")
st.dataframe(pivot)

fig5, ax5 = plt.subplots(figsize=(10, 6))
pivot.plot(kind='bar', ax=ax5)
st.pyplot(fig5)

# 5. Correlation and Causation
st.header("📌 Correlation and Causation")
corr_matrix = df.corr(numeric_only=True)
st.subheader("Correlation Matrix")
st.dataframe(corr_matrix)

fig6, ax6 = plt.subplots(figsize=(12, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax6)
st.pyplot(fig6)

fig7, ax7 = plt.subplots(figsize=(10, 4))
sns.regplot(x="engine-size", y="price", data=df, ax=ax7)
st.pyplot(fig7)

fig8, ax8 = plt.subplots(figsize=(10, 4))
sns.regplot(x="highway-mpg", y="price", data=df, ax=ax8)
st.pyplot(fig8)

fig9, ax9 = plt.subplots(figsize=(10, 4))
sns.boxplot(x="drive-wheels", y="price", data=df, ax=ax9)
st.pyplot(fig9)

fig10, ax10 = plt.subplots(figsize=(10, 4))
sns.boxplot(x="engine-location", y="price", data=df, ax=ax10)
st.pyplot(fig10)
