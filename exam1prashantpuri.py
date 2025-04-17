
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Automobile Data Analysis", layout="wide")
st.title("🚗 Automobile Dataset Analysis")
st.markdown("**Name:** Prashant Puri  
**Banner ID:** 001397936")

# Load dataset
st.header("1. 📥 Import Data")
code_import = '''
import pandas as pd
path = 'https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv'
df = pd.read_csv(path)
df.head()
'''
st.code(code_import, language='python')
path = 'https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv'
df = pd.read_csv(path)
st.dataframe(df.head())

# Visual inspection of variable relationships
st.header("2. 📊 Regression Plots for Numerical Features")
st.markdown("Visualizing relationships using `regplot` and `boxplot` for better understanding of how each feature impacts price.")

for x_col in ["engine-size", "highway-mpg", "peak-rpm", "horsepower"]:
    fig, ax = plt.subplots()
    sns.regplot(x=x_col, y="price", data=df, ax=ax)
    st.subheader(f"Price vs {x_col}")
    st.pyplot(fig)

# Boxplots
st.header("3. 📦 Boxplot Visualizations for Categorical Features")
for x_col in ["drive-wheels", "body-style", "engine-location"]:
    fig, ax = plt.subplots()
    sns.boxplot(x=x_col, y="price", data=df, ax=ax)
    st.subheader(f"Price Distribution by {x_col}")
    st.pyplot(fig)

# Descriptive statistics
st.header("4. 📈 Descriptive Statistical Analysis")
code_stats = "df.describe()"
st.code(code_stats, language='python')
st.dataframe(df.describe())

# Value counts
st.header("5. 🔢 Value Counts")
code_counts = "df['drive-wheels'].value_counts()"
st.code(code_counts, language='python')
st.dataframe(df['drive-wheels'].value_counts())

# Grouping
st.header("6. 🧮 Grouping and Pivot Table")
code_group = '''
df_group = df[['drive-wheels','body-style','price']]
grouped = df_group.groupby(['drive-wheels','body-style'], as_index=False).mean()
pivot = grouped.pivot(index='drive-wheels', columns='body-style', values='price').fillna(0)
'''
st.code(code_group, language='python')
df_group = df[['drive-wheels','body-style','price']]
grouped = df_group.groupby(['drive-wheels','body-style'], as_index=False).mean()
pivot = grouped.pivot(index='drive-wheels', columns='body-style', values='price').fillna(0)
st.dataframe(pivot)

fig, ax = plt.subplots()
pivot.plot(kind='bar', ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# Correlation matrix
st.header("7. 🧠 Correlation and Heatmap")
code_corr = "df.corr(numeric_only=True)"
st.code(code_corr, language='python')
corr_matrix = df.corr(numeric_only=True)
st.dataframe(corr_matrix)

fig_corr, ax_corr = plt.subplots(figsize=(12, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax_corr)
st.pyplot(fig_corr)

# Specific correlation check
st.header("8. 🔍 Feature-specific Correlation Checks")
corr_code = '''
df[['peak-rpm', 'price']].corr()
df[['horsepower', 'price']].corr()
'''
st.code(corr_code, language='python')
st.write("**peak-rpm vs price correlation:**")
st.dataframe(df[['peak-rpm', 'price']].corr())

st.write("**horsepower vs price correlation:**")
st.dataframe(df[['horsepower', 'price']].corr())

# Summary
st.header("✅ Summary and Insights")
st.markdown("""
- Engine size and horsepower have a **strong positive correlation** with price.
- Peak RPM has a **weak correlation** and is likely not a good predictor of price.
- Drive-wheels and engine-location show **clear differences** in boxplots.
- Grouped analysis shows that **drive-wheels and body-style combinations** impact average prices.
""")
