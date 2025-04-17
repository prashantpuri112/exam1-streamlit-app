
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Car Price Analysis with Code", layout="wide")
st.title("🚗 Car Price Analysis - Full Report with Code")
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

# Section 1
st.header("📥 Import Data")
st.markdown("We import the automobile dataset using pandas and display the first few rows.")
code1 = '''
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

path = 'https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv'
df = pd.read_csv(path)
df.head()
'''
st.code(code1, language='python')
df = pd.read_csv('https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv')
st.dataframe(df.head())

# Section 2
st.header("📊 Analyzing Individual Feature Patterns")
st.markdown("We visualize relationships between features and price.")

code2 = '''
sns.regplot(x="engine-size", y="price", data=df)
sns.boxplot(x="body-style", y="price", data=df)
sns.boxplot(x="drive-wheels", y="price", data=df)
sns.regplot(x="highway-mpg", y="price", data=df)
'''
st.code(code2, language='python')

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

# Section 3
st.header("📈 Descriptive Statistical Analysis")
st.markdown("We generate summary statistics for numerical features.")

code3 = '''
df.describe()
'''
st.code(code3, language='python')
st.dataframe(df.describe())

# Section 4
st.header("🔍 Basics of Grouping")
st.markdown("We group by `drive-wheels` and `body-style` to calculate average prices.")

code4 = '''
df_group_test1 = df[['drive-wheels', 'body-style', 'price']]
grouped_test2 = df_group_test1.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
pivot = grouped_test2.pivot(index='drive-wheels', columns='body-style').fillna(0)
pivot
'''
st.code(code4, language='python')
df_group_test1 = df[['drive-wheels', 'body-style', 'price']]
grouped_test2 = df_group_test1.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
pivot = grouped_test2.pivot(index='drive-wheels', columns='body-style').fillna(0)
st.dataframe(pivot)

fig5, ax5 = plt.subplots(figsize=(10, 5))
pivot.plot(kind='bar', ax=ax5)
plt.xticks(rotation=45)
st.pyplot(fig5)

# Section 5
st.header("📌 Correlation and Causation")
st.markdown("We check for relationships between features using correlation matrix and visualizations.")

code5 = '''
df.corr(numeric_only=True)
sns.heatmap(corr, annot=True)
sns.regplot(x="engine-size", y="price", data=df)
sns.regplot(x="highway-mpg", y="price", data=df)
sns.boxplot(x="drive-wheels", y="price", data=df)
sns.boxplot(x="engine-location", y="price", data=df)
'''
st.code(code5, language='python')

corr = df.corr(numeric_only=True)
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

st.success("✅ All code and outputs included. Full report complete.")
