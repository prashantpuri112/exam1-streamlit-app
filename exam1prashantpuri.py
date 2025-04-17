
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(page_title="Automobile Data Analysis", layout="wide")

# Load data
st.title("🚗 Automobile Dataset - Exploratory Data Analysis")
path = 'https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv'
df = pd.read_csv(path)
st.success("Dataset Loaded Successfully!")
st.write("Here's a preview of the data:")
st.dataframe(df.head())

# Section: Data Types
st.header("🔍 Data Types")
st.code(df.dtypes.astype(str).to_string())

# Section: Correlation Matrix
st.header("📊 Correlation Analysis")
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
correlation_matrix = df[numeric_cols].corr()
st.subheader("Correlation Matrix (All Numeric Columns)")
st.dataframe(correlation_matrix)

st.subheader("Selected Correlations")
selected_corr = df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr()
st.dataframe(selected_corr)

# Section: Regression Visualizations
st.header("📈 Regression Plots")
def regplot(x, y):
    fig, ax = plt.subplots()
    sns.regplot(x=x, y=y, data=df, ax=ax)
    st.pyplot(fig)
    st.write(df[[x, y]].corr())

st.subheader("Engine Size vs Price")
regplot("engine-size", "price")

st.subheader("Highway MPG vs Price")
regplot("highway-mpg", "price")

st.subheader("Peak RPM vs Price")
regplot("peak-rpm", "price")

st.subheader("Stroke vs Price")
regplot("stroke", "price")

# Section: Box Plots
st.header("📦 Box Plots")
def boxplot(x, y="price"):
    fig, ax = plt.subplots()
    sns.boxplot(x=x, y=y, data=df, ax=ax)
    st.pyplot(fig)

st.subheader("Body Style vs Price")
boxplot("body-style")

st.subheader("Engine Location vs Price")
boxplot("engine-location")

st.subheader("Drive Wheels vs Price")
boxplot("drive-wheels")

# Section: Value Counts
st.header("🔢 Value Counts")
drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
drive_wheels_counts.index.name = 'drive-wheels'
st.subheader("Drive Wheels Value Counts")
st.dataframe(drive_wheels_counts)

engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'
st.subheader("Engine Location Value Counts")
st.dataframe(engine_loc_counts)

# Section: Grouping and Pivot Table
st.header("📐 Pivot Table: Drive-Wheels vs Body-Style Average Prices")
grouped = df[['drive-wheels', 'body-style', 'price']]
grouped_test = grouped.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
grouped_pivot = grouped_test.pivot(index='drive-wheels', columns='body-style', values='price')
grouped_pivot = grouped_pivot.fillna(0)
st.dataframe(grouped_pivot)

# Heatmap
st.subheader("🔍 Heatmap of Average Prices")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(grouped_pivot, annot=True, fmt=".1f", cmap="YlGnBu", ax=ax)
st.pyplot(fig)

# Footer
st.markdown("---")
st.caption("Developed by Prashant Puri | Exam 1 | MS Analytics | Saint Louis University")
