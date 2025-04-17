
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Automobile Dataset Analysis", layout="wide")
st.title("🚗 Automobile Dataset - Full Analysis")
st.markdown("**Author:** Prashant Puri  **Banner ID:** 001397936")

# Section 1: Load Data
st.header("1. Import Data")
code = '''
import pandas as pd
path = "https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv"
df = pd.read_csv(path)
df.head()
'''
st.code(code, language='python')
path = "https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv"
df = pd.read_csv(path)
st.dataframe(df.head())

# Section 2: Describe Data
st.header("2. Descriptive Statistics")
st.code("df.describe()", language="python")
st.dataframe(df.describe())

# Section 3: Value Counts
st.header("3. Drive Wheels Value Count")
st.code("df['drive-wheels'].value_counts()", language="python")
st.dataframe(df['drive-wheels'].value_counts())

# Section 4: Grouping and Pivot Table
st.header("4. Grouping by Drive-Wheels and Body-Style")
group_code = '''
df_group = df[['drive-wheels','body-style','price']]
grouped = df_group.groupby(['drive-wheels','body-style'], as_index=False).mean()
pivot = grouped.pivot(index='drive-wheels', columns='body-style', values='price').fillna(0)
'''
st.code(group_code, language='python')
df_group = df[['drive-wheels','body-style','price']]
grouped = df_group.groupby(['drive-wheels','body-style'], as_index=False).mean()
pivot = grouped.pivot(index='drive-wheels', columns='body-style', values='price').fillna(0)
st.dataframe(pivot)

fig, ax = plt.subplots()
pivot.plot(kind='bar', ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# Section 5: Correlation
st.header("5. Correlation Analysis")
st.code("df.corr(numeric_only=True)", language="python")
corr_matrix = df.corr(numeric_only=True)
st.dataframe(corr_matrix)

fig_corr, ax_corr = plt.subplots(figsize=(12, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax_corr)
st.pyplot(fig_corr)

# Section 6: Regression Plots
st.header("6. Regression Plots")
for col in ["engine-size", "highway-mpg", "peak-rpm", "horsepower"]:
    st.subheader(f"Price vs {col}")
    code = f"sns.regplot(x='{col}', y='price', data=df)"
    st.code(code, language="python")
    fig, ax = plt.subplots()
    sns.regplot(x=col, y="price", data=df, ax=ax)
    st.pyplot(fig)

# Section 7: Boxplots
st.header("7. Boxplots of Categorical Features")
for cat_col in ["drive-wheels", "body-style", "engine-location"]:
    st.subheader(f"Price by {cat_col}")
    code = f"sns.boxplot(x='{cat_col}', y='price', data=df)"
    st.code(code, language="python")
    fig, ax = plt.subplots()
    sns.boxplot(x=cat_col, y="price", data=df, ax=ax)
    st.pyplot(fig)

# Section 8: Specific Feature Correlation
st.header("8. Specific Feature Correlation Checks")
st.subheader("peak-rpm vs price")
st.code("df[['peak-rpm', 'price']].corr()", language="python")
st.dataframe(df[['peak-rpm', 'price']].corr())

st.subheader("horsepower vs price")
st.code("df[['horsepower', 'price']].corr()", language="python")
st.dataframe(df[['horsepower', 'price']].corr())

# Summary
st.header("9. Summary of Insights")
st.markdown("""
- **Engine size** and **horsepower** show strong positive correlation with price.
- **Peak RPM** has a weak correlation, suggesting it’s not a strong predictor.
- **Drive-wheels** and **engine-location** clearly separate price distributions in boxplots.
- Grouped averages by **drive-wheels and body-style** show price differences across configurations.
- Correlation heatmap provides a holistic view of linear associations.
""")
