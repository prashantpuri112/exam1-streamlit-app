
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Exam 1 - Full Automobile Analysis", layout="wide")
st.title("🚗 Exam 1 - Full Automobile Data Analysis")
st.markdown("Prepared by **Prashant Puri** | MS in Analytics | Saint Louis University")

# Load dataset
st.header("📥 Load Dataset")
DATA_URL = 'https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv'
df = pd.read_csv(DATA_URL)
st.success("Dataset loaded successfully!")
st.dataframe(df.head())


st.markdown("""
#Prashant Puri

##Banner ID:001397936
""")



st.markdown("""
<h2>Table of Contents</h2>



<div class="alert alert-block alert-info" style="margin-top: 20px">

<ol>

    <li><a href="#import_data">Import Data from Module</a></li>

    <li><a href="#pattern_visualization">Analyzing Individual Feature Patterns using Visualization</a></li>

    <li><a href="#discriptive_statistics">Descriptive Statistical Analysis</a></li>

    <li><a href="#basic_grouping">Basics of Grouping</a></li>

    <li><a href="#correlation_causation">Correlation and Causation</a></li>

</ol>



</div>



<hr>


""")



st.markdown("""
<h3>What are the main characteristics that have the most impact on the car price?</h3>


""")



st.markdown("""
<h2 id="import_data">1. Import Data from Part 1</h2>


""")



st.markdown("""
<h4>Setup</h4>


""")



st.markdown("""
Import libraries:


""")


with st.expander("🔹 Code Cell 7", expanded=False):
    st.code("""import pandas as pd
import numpy as np""")
    try:
        import pandas as pd
        import numpy as np
    except Exception as e:
        st.warning(f"⚠️ Error in cell 7: {e}")


st.markdown("""
Load the data and store it in dataframe `df`:


""")



st.markdown("""
This dataset was hosted on IBM Cloud object. Click <a href="https://cocl.us/DA101EN_object_storage">HERE</a> for free storage.


""")


with st.expander("🔹 Code Cell 10", expanded=False):
    st.code("""path='https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv'
df = pd.read_csv(path)
df.head()""")
    try:
        path='https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv'
        df = pd.read_csv(path)
        df.head()
    except Exception as e:
        st.warning(f"⚠️ Error in cell 10: {e}")


st.markdown("""
<h2 id="pattern_visualization">2. Analyzing Individual Feature Patterns Using Visualization</h2>


""")



st.markdown("""
To install Seaborn we use pip, the Python package manager.


""")



st.markdown("""
Import visualization packages "Matplotlib" and "Seaborn". Don't forget about "%matplotlib inline" to plot in a Jupyter notebook.


""")


with st.expander("🔹 Code Cell 14", expanded=False):
    st.code("""import matplotlib.pyplot as plt
import seaborn as sns""")
    try:
        import matplotlib.pyplot as plt
        import seaborn as sns
    except Exception as e:
        st.warning(f"⚠️ Error in cell 14: {e}")


st.markdown("""
<h4>How to choose the right visualization method?</h4>

<p>When visualizing individual variables, it is important to first understand what type of variable you are dealing with. This will help us find the right visualization method for that variable.</p>


""")


with st.expander("🔹 Code Cell 16", expanded=False):
    st.code("""# list the data types for each column
print(df.dtypes)""")
    try:
        # list the data types for each column
        print(df.dtypes)
    except Exception as e:
        st.warning(f"⚠️ Error in cell 16: {e}")


st.markdown("""
<div class="alert alert-danger alertdanger" style="margin-top: 20px">

<h3>Question  #1:</h3>



<b>What is the data type of the column "peak-rpm"? </b>

</div>


""")


with st.expander("🔹 Code Cell 18", expanded=False):
    st.code("""# Write your code below and press Shift+Enter to execute
print(df['peak-rpm'].dtype)""")
    try:
        # Write your code below and press Shift+Enter to execute
        print(df['peak-rpm'].dtype)
    except Exception as e:
        st.warning(f"⚠️ Error in cell 18: {e}")


st.markdown("""
For example, we can calculate the correlation between variables  of type "int64" or "float64" using the method "corr":


""")


with st.expander("🔹 Code Cell 20", expanded=False):
    st.code("""# Correlation

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
correlation_matrix = df[numeric_cols].corr()
print(correlation_matrix)""")
    try:
        # Correlation
        
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
        correlation_matrix = df[numeric_cols].corr()
        print(correlation_matrix)
    except Exception as e:
        st.warning(f"⚠️ Error in cell 20: {e}")


st.markdown("""
The diagonal elements are always one; we will study correlation more precisely Pearson correlation in-depth at the end of the notebook.


""")



st.markdown("""
<div class="alert alert-danger alertdanger" style="margin-top: 20px">

<h3> Question  #2: </h3>



<p>Find the correlation between the following columns: bore, stroke, compression-ratio, and horsepower.</p>

<p>Hint: if you would like to select those columns, use the following syntax: df[['bore','stroke','compression-ratio','horsepower']]</p>

</div>


""")


with st.expander("🔹 Code Cell 23", expanded=False):
    st.code("""# Write your code below and press Shift+Enter to execute
df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr()""")
    try:
        # Write your code below and press Shift+Enter to execute
        df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr()
    except Exception as e:
        st.warning(f"⚠️ Error in cell 23: {e}")


st.markdown("""
<h2>Continuous Numerical Variables:</h2>



<p>Continuous numerical variables are variables that may contain any value within some range. They can be of type "int64" or "float64". A great way to visualize these variables is by using scatterplots with fitted lines.</p>



<p>In order to start understanding the (linear) relationship between an individual variable and the price, we can use "regplot" which plots the scatterplot plus the fitted regression line for the data. This will be useful later on for visualizing the fit of the simple linear regression model as well. </p>


""")



st.markdown("""
 Let's see several examples of different linear relationships:


""")



st.markdown("""
<h3>Positive Linear Relationship</h4>


""")



st.markdown("""
Let's find the scatterplot of "engine-size" and "price".


""")


with st.expander("🔹 Code Cell 28", expanded=False):
    st.code("""# Engine size as potential predictor variable of price
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)""")
    try:
        # Engine size as potential predictor variable of price
        sns.regplot(x="engine-size", y="price", data=df)
        plt.ylim(0,)
    except Exception as e:
        st.warning(f"⚠️ Error in cell 28: {e}")


st.markdown("""
<p>As the engine-size goes up, the price goes up: this indicates a positive direct correlation between these two variables. Engine size seems like a pretty good predictor of price since the regression line is almost a perfect diagonal line.</p>


""")



st.markdown("""
 We can examine the correlation between 'engine-size' and 'price' and see that it's approximately 0.87.


""")


with st.expander("🔹 Code Cell 31", expanded=False):
    st.code("""df[["engine-size", "price"]].corr()""")
    try:
        df[["engine-size", "price"]].corr()
    except Exception as e:
        st.warning(f"⚠️ Error in cell 31: {e}")


st.markdown("""
Highway mpg is a potential predictor variable of price. Let's find the scatterplot of "highway-mpg" and "price".


""")


with st.expander("🔹 Code Cell 33", expanded=False):
    st.code("""sns.regplot(x="highway-mpg", y="price", data=df)""")
    try:
        sns.regplot(x="highway-mpg", y="price", data=df)
    except Exception as e:
        st.warning(f"⚠️ Error in cell 33: {e}")


st.markdown("""
<p>As highway-mpg goes up, the price goes down: this indicates an inverse/negative relationship between these two variables. Highway mpg could potentially be a predictor of price.</p>


""")



st.markdown("""
We can examine the correlation between 'highway-mpg' and 'price' and see it's approximately -0.704.


""")


with st.expander("🔹 Code Cell 36", expanded=False):
    st.code("""df[['highway-mpg', 'price']].corr()""")
    try:
        df[['highway-mpg', 'price']].corr()
    except Exception as e:
        st.warning(f"⚠️ Error in cell 36: {e}")


st.markdown("""
<h3>Weak Linear Relationship</h3>


""")



st.markdown("""
Let's see if "peak-rpm" is a predictor variable of "price".


""")


with st.expander("🔹 Code Cell 39", expanded=False):
    st.code("""sns.regplot(x="peak-rpm", y="price", data=df)""")
    try:
        sns.regplot(x="peak-rpm", y="price", data=df)
    except Exception as e:
        st.warning(f"⚠️ Error in cell 39: {e}")


st.markdown("""
<p>Peak rpm does not seem like a good predictor of the price at all since the regression line is close to horizontal. Also, the data points are very scattered and far from the fitted line, showing lots of variability. Therefore, it's not a reliable variable.</p>


""")



st.markdown("""
We can examine the correlation between 'peak-rpm' and 'price' and see it's approximately -0.101616.


""")


with st.expander("🔹 Code Cell 42", expanded=False):
    st.code("""df[['peak-rpm','price']].corr()""")
    try:
        df[['peak-rpm','price']].corr()
    except Exception as e:
        st.warning(f"⚠️ Error in cell 42: {e}")


st.markdown("""
 <div class="alert alert-danger alertdanger" style="margin-top: 20px">

<h1> Question  3 a): </h1>



<p>Find the correlation  between x="stroke" and y="price".</p>

<p>Hint: if you would like to select those columns, use the following syntax: df[["stroke","price"]].  </p>

</div>


""")


with st.expander("🔹 Code Cell 44", expanded=False):
    st.code("""# Write your code below and press Shift+Enter to execute
df[["stroke","price"]].corr()""")
    try:
        # Write your code below and press Shift+Enter to execute
        df[["stroke","price"]].corr()
    except Exception as e:
        st.warning(f"⚠️ Error in cell 44: {e}")


st.markdown("""
<div class="alert alert-danger alertdanger" style="margin-top: 20px">

<h1>Question  3 b):</h1>



<p>Given the correlation results between "price" and "stroke", do you expect a linear relationship?</p>

<p>Verify your results using the function "regplot()".</p>

</div>


""")


with st.expander("🔹 Code Cell 46", expanded=False):
    st.code("""# Write your code below and press Shift+Enter to execute
sns.regplot(x="stroke", y="price", data=df)""")
    try:
        # Write your code below and press Shift+Enter to execute
        sns.regplot(x="stroke", y="price", data=df)
    except Exception as e:
        st.warning(f"⚠️ Error in cell 46: {e}")


st.markdown("""
<h3>Categorical Variables</h3>



<p>These are variables that describe a 'characteristic' of a data unit, and are selected from a small group of categories. The categorical variables can have the type "object" or "int64". A good way to visualize categorical variables is by using boxplots.</p>


""")



st.markdown("""
Let's look at the relationship between "body-style" and "price".


""")


with st.expander("🔹 Code Cell 49", expanded=False):
    st.code("""sns.boxplot(x="body-style", y="price", data=df)""")
    try:
        sns.boxplot(x="body-style", y="price", data=df)
    except Exception as e:
        st.warning(f"⚠️ Error in cell 49: {e}")


st.markdown("""
<p>We see that the distributions of price between the different body-style categories have a significant overlap, so body-style would not be a good predictor of price. Let's examine engine "engine-location" and "price":</p>


""")


with st.expander("🔹 Code Cell 51", expanded=False):
    st.code("""sns.boxplot(x="engine-location", y="price", data=df)""")
    try:
        sns.boxplot(x="engine-location", y="price", data=df)
    except Exception as e:
        st.warning(f"⚠️ Error in cell 51: {e}")


st.markdown("""
<p>Here we see that the distribution of price between these two engine-location categories, front and rear, are distinct enough to take engine-location as a potential good predictor of price.</p>


""")



st.markdown("""
 Let's examine "drive-wheels" and "price".


""")


with st.expander("🔹 Code Cell 54", expanded=False):
    st.code("""# drive-wheels
sns.boxplot(x="drive-wheels", y="price", data=df)""")
    try:
        # drive-wheels
        sns.boxplot(x="drive-wheels", y="price", data=df)
    except Exception as e:
        st.warning(f"⚠️ Error in cell 54: {e}")


st.markdown("""
<p>Here we see that the distribution of price between the different drive-wheels categories differs. As such, drive-wheels could potentially be a predictor of price.</p>


""")



st.markdown("""
<h2 id="discriptive_statistics">3. Descriptive Statistical Analysis</h2>


""")



st.markdown("""
<p>Let's first take a look at the variables by utilizing a description method.</p>



<p>The <b>describe</b> function automatically computes basic statistics for all continuous variables. Any NaN values are automatically skipped in these statistics.</p>



This will show:

<ul>

    <li>the count of that variable</li>

    <li>the mean</li>

    <li>the standard deviation (std)</li>

    <li>the minimum value</li>

    <li>the IQR (Interquartile Range: 25%, 50% and 75%)</li>

    <li>the maximum value</li>

<ul>


""")



st.markdown("""
 We can apply the method "describe" as follows:


""")


with st.expander("🔹 Code Cell 59", expanded=False):
    st.code("""df.describe()""")
    try:
        df.describe()
    except Exception as e:
        st.warning(f"⚠️ Error in cell 59: {e}")


st.markdown("""
 The default setting of "describe" skips variables of type object. We can apply the method "describe" on the variables of type 'object' as follows:


""")


with st.expander("🔹 Code Cell 61", expanded=False):
    st.code("""df.describe(include=['object'])""")
    try:
        df.describe(include=['object'])
    except Exception as e:
        st.warning(f"⚠️ Error in cell 61: {e}")


st.markdown("""
<h3>Value Counts</h3>


""")



st.markdown("""
<p>Value counts is a good way of understanding how many units of each characteristic/variable we have. We can apply the "value_counts" method on the column "drive-wheels". Don’t forget the method "value_counts" only works on pandas series, not pandas dataframes. As a result, we only include one bracket <code>df['drive-wheels']</code>, not two brackets <code>df[['drive-wheels']]</code>.</p>


""")


with st.expander("🔹 Code Cell 64", expanded=False):
    st.code("""df['drive-wheels'].value_counts()""")
    try:
        df['drive-wheels'].value_counts()
    except Exception as e:
        st.warning(f"⚠️ Error in cell 64: {e}")


st.markdown("""
We can convert the series to a dataframe as follows:


""")


with st.expander("🔹 Code Cell 66", expanded=False):
    st.code("""df['drive-wheels'].value_counts().to_frame()""")
    try:
        df['drive-wheels'].value_counts().to_frame()
    except Exception as e:
        st.warning(f"⚠️ Error in cell 66: {e}")


st.markdown("""
Let's repeat the above steps but save the results to the dataframe "drive_wheels_counts" and rename the column  'drive-wheels' to 'value_counts'.


""")


with st.expander("🔹 Code Cell 68", expanded=False):
    st.code("""drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
drive_wheels_counts""")
    try:
        drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
        drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
        drive_wheels_counts
    except Exception as e:
        st.warning(f"⚠️ Error in cell 68: {e}")


st.markdown("""
 Now let's rename the index to 'drive-wheels':


""")


with st.expander("🔹 Code Cell 70", expanded=False):
    st.code("""drive_wheels_counts.index.name = 'drive-wheels'
drive_wheels_counts""")
    try:
        drive_wheels_counts.index.name = 'drive-wheels'
        drive_wheels_counts
    except Exception as e:
        st.warning(f"⚠️ Error in cell 70: {e}")


st.markdown("""
We can repeat the above process for the variable 'engine-location'.


""")


with st.expander("🔹 Code Cell 72", expanded=False):
    st.code("""# engine-location as variable
engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'
engine_loc_counts.head(10)""")
    try:
        # engine-location as variable
        engine_loc_counts = df['engine-location'].value_counts().to_frame()
        engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
        engine_loc_counts.index.name = 'engine-location'
        engine_loc_counts.head(10)
    except Exception as e:
        st.warning(f"⚠️ Error in cell 72: {e}")


st.markdown("""
<p>After examining the value counts of the engine location, we see that engine location would not be a good predictor variable for the price. This is because we only have three cars with a rear engine and 198 with an engine in the front, so this result is skewed. Thus, we are not able to draw any conclusions about the engine location.</p>


""")



st.markdown("""
<h2 id="basic_grouping">4. Basics of Grouping</h2>


""")



st.markdown("""
<p>The "groupby" method groups data by different categories. The data is grouped based on one or several variables, and analysis is performed on the individual groups.</p>



<p>For example, let's group by the variable "drive-wheels". We see that there are 3 different categories of drive wheels.</p>


""")


with st.expander("🔹 Code Cell 76", expanded=False):
    st.code("""df['drive-wheels'].unique()""")
    try:
        df['drive-wheels'].unique()
    except Exception as e:
        st.warning(f"⚠️ Error in cell 76: {e}")


st.markdown("""
<p>If we want to know, on average, which type of drive wheel is most valuable, we can group "drive-wheels" and then average them.</p>



<p>We can select the columns 'drive-wheels', 'body-style' and 'price', then assign it to the variable "df_group_one".</p>


""")


with st.expander("🔹 Code Cell 78", expanded=False):
    st.code("""df_group_one = df[['drive-wheels','body-style','price']]""")
    try:
        df_group_one = df[['drive-wheels','body-style','price']]
    except Exception as e:
        st.warning(f"⚠️ Error in cell 78: {e}")


st.markdown("""
We can then calculate the average price for each of the different categories of data.


""")


with st.expander("🔹 Code Cell 80", expanded=False):
    st.code("""# grouping results
df_group_one = df_group_one.groupby(['drive-wheels'],as_index=False)['price'].mean()
df_group_one""")
    try:
        # grouping results
        df_group_one = df_group_one.groupby(['drive-wheels'],as_index=False)['price'].mean()
        df_group_one
    except Exception as e:
        st.warning(f"⚠️ Error in cell 80: {e}")

with st.expander("🔹 Code Cell 81", expanded=False):
    st.code("""# grouping results
df_group_one = df_group_one.groupby(['drive-wheels'],as_index=False).mean()
df_group_one""")
    try:
        # grouping results
        df_group_one = df_group_one.groupby(['drive-wheels'],as_index=False).mean()
        df_group_one
    except Exception as e:
        st.warning(f"⚠️ Error in cell 81: {e}")


st.markdown("""
<p>From our data, it seems rear-wheel drive vehicles are, on average, the most expensive, while 4-wheel and front-wheel are approximately the same in price.</p>



<p>You can also group by multiple variables. For example, let's group by both 'drive-wheels' and 'body-style'. This groups the dataframe by the unique combination of 'drive-wheels' and 'body-style'. We can store the results in the variable 'grouped_test1'.</p>


""")



st.markdown("""
<p>This grouped data is much easier to visualize when it is made into a pivot table. A pivot table is like an Excel spreadsheet, with one variable along the column and another along the row. We can convert the dataframe to a pivot table using the method "pivot" to create a pivot table from the groups.</p>



<p>In this case, we will leave the drive-wheels variable as the rows of the table, and pivot body-style to become the columns of the table:</p>


""")


with st.expander("🔹 Code Cell 84", expanded=False):
    st.code("""# grouping results
df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
grouped_test1""")
    try:
        # grouping results
        df_gptest = df[['drive-wheels','body-style','price']]
        grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
        grouped_test1
    except Exception as e:
        st.warning(f"⚠️ Error in cell 84: {e}")

with st.expander("🔹 Code Cell 85", expanded=False):
    st.code("""grouped_pivot = grouped_pivot.fillna(0) #fill missing values with 0
grouped_pivot""")
    try:
        grouped_pivot = grouped_pivot.fillna(0) #fill missing values with 0
        grouped_pivot
    except Exception as e:
        st.warning(f"⚠️ Error in cell 85: {e}")


st.markdown("""
<p>Often, we won't have data for some of the pivot cells. We can fill these missing cells with the value 0, but any other value could potentially be used as well. It should be mentioned that missing data is quite a complex subject and is an entire course on its own.</p>


""")



st.markdown("""
<div class="alert alert-danger alertdanger" style="margin-top: 20px">

<h1>Question 4:</h1>



<p>Use the "groupby" function to find the average "price" of each car based on "body-style".</p>

</div>


""")


with st.expander("🔹 Code Cell 88", expanded=False):
    st.code("""# Write your code below and press Shift+Enter to execute
# Group by body-style and calculate the mean price
body_style_avg_price = df.groupby('body-style')['price'].mean()
body_style_avg_price""")
    try:
        # Write your code below and press Shift+Enter to execute
        # Group by body-style and calculate the mean price
        body_style_avg_price = df.groupby('body-style')['price'].mean()
        body_style_avg_price
    except Exception as e:
        st.warning(f"⚠️ Error in cell 88: {e}")


st.markdown("""
If you did not import "pyplot", let's do it again.


""")


with st.expander("🔹 Code Cell 90", expanded=False):
    st.code("""import matplotlib.pyplot as plt""")
    try:
        import matplotlib.pyplot as plt
    except Exception as e:
        st.warning(f"⚠️ Error in cell 90: {e}")


st.markdown("""
<h4>Variables: Drive Wheels and Body Style vs. Price</h4>


""")



st.markdown("""
Let's use a heat map to visualize the relationship between Body Style vs Price.


""")


with st.expander("🔹 Code Cell 93", expanded=False):
    st.code("""#use the grouped results
plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.show()""")
    try:
        #use the grouped results
        plt.pcolor(grouped_pivot, cmap='RdBu')
        plt.colorbar()
        plt.show()
    except Exception as e:
        st.warning(f"⚠️ Error in cell 93: {e}")


st.markdown("""
<p>The heatmap plots the target variable (price) proportional to colour with respect to the variables 'drive-wheel' and 'body-style' on the vertical and horizontal axis, respectively. This allows us to visualize how the price is related to 'drive-wheel' and 'body-style'.</p>



<p>The default labels convey no useful information to us. Let's change that:</p>


""")


with st.expander("🔹 Code Cell 95", expanded=False):
    st.code("""fig, ax = plt.subplots()
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
plt.show()""")
    try:
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
    except Exception as e:
        st.warning(f"⚠️ Error in cell 95: {e}")


st.markdown("""
<p>Visualization is very important in data science, and Python visualization packages provide great freedom. We will go more in-depth in a separate visualizations courses, probably in your second year.</p>



<p>The main question we want to answer in this module is, "What are the main characteristics which have the most impact on the car price?".</p>



<p>To get a better measure of the important characteristics, we look at the correlation of these variables with the car price. In other words: how is the car price dependent on this variable?</p>


""")



st.markdown("""
<h2 id="correlation_causation">5. Correlation and Causation</h2>


""")



st.markdown("""
<p><b>Correlation</b>: a measure of the extent of interdependence between variables.</p>



<p><b>Causation</b>: the relationship between cause and effect between two variables.</p>



<p>It is important to know the difference between these two. Correlation does not imply causation. Determining correlation is much simpler  the determining causation as causation may require independent experimentation.</p>


""")



st.markdown("""
<p><b>Pearson Correlation</b></p>

<p>The Pearson Correlation measures the linear dependence between two variables X and Y.</p>

<p>The resulting coefficient is a value between -1 and 1 inclusive, where:</p>

<ul>

    <li><b>1</b>: Perfect positive linear correlation.</li>

    <li><b>0</b>: No linear correlation, the two variables most likely do not affect each other.</li>

    <li><b>-1</b>: Perfect negative linear correlation.</li>

</ul>


""")



st.markdown("""
<p>Pearson Correlation is the default method of the function "corr". Like before, we can calculate the Pearson Correlation of the of the 'int64' or 'float64'  variables.</p>


""")


with st.expander("🔹 Code Cell 101", expanded=False):
    st.code("""# Calculate the Pearson correlation of numeric columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
correlation_matrix = df[numeric_cols].corr()
print(correlation_matrix)""")
    try:
        # Calculate the Pearson correlation of numeric columns
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
        correlation_matrix = df[numeric_cols].corr()
        print(correlation_matrix)
    except Exception as e:
        st.warning(f"⚠️ Error in cell 101: {e}")


st.markdown("""
Sometimes we would like to know the significant of the correlation estimate.


""")



st.markdown("""
<b>P-value</b>

<p>What is this P-value? The P-value is the probability value that the correlation between these two variables is statistically significant. Normally, we choose a significance level of 0.05, which means that we are 95% confident that the correlation between the variables is significant.</p>



By convention, when the

<ul>

    <li>p-value is $<$ 0.001: we say there is strong evidence that the correlation is significant.</li>

    <li>the p-value is $<$ 0.05: there is moderate evidence that the correlation is significant.</li>

    <li>the p-value is $<$ 0.1: there is weak evidence that the correlation is significant.</li>

    <li>the p-value is $>$ 0.1: there is no evidence that the correlation is significant.</li>

</ul>


""")



st.markdown("""
 We can obtain this information using  "stats" module in the "scipy"  library.


""")


with st.expander("🔹 Code Cell 105", expanded=False):
    st.code("""from scipy import stats""")
    try:
        from scipy import stats
    except Exception as e:
        st.warning(f"⚠️ Error in cell 105: {e}")


st.markdown("""
<h3>Wheel-Base vs. Price</h3>


""")



st.markdown("""
Let's calculate the  Pearson Correlation Coefficient and P-value of 'wheel-base' and 'price'.


""")


with st.expander("🔹 Code Cell 108", expanded=False):
    st.code("""pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)""")
    try:
        pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
        print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)
    except Exception as e:
        st.warning(f"⚠️ Error in cell 108: {e}")


st.markdown("""
<h4>Conclusion:</h4>

<p>Since the p-value is $<$ 0.001, the correlation between wheel-base and price is statistically significant, although the linear relationship isn't extremely strong (~0.585).</p>


""")



st.markdown("""
<h3>Horsepower vs. Price</h3>


""")



st.markdown("""
 Let's calculate the  Pearson Correlation Coefficient and P-value of 'horsepower' and 'price'.


""")


with st.expander("🔹 Code Cell 112", expanded=False):
    st.code("""pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)""")
    try:
        pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
        print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)
    except Exception as e:
        st.warning(f"⚠️ Error in cell 112: {e}")


st.markdown("""
<h4>Conclusion:</h4>



<p>Since the p-value is $<$ 0.001, the correlation between horsepower and price is statistically significant, and the linear relationship is quite strong (~0.809, close to 1).</p>


""")



st.markdown("""
<h3>Length vs. Price</h3>



Let's calculate the  Pearson Correlation Coefficient and P-value of 'length' and 'price'.


""")


with st.expander("🔹 Code Cell 115", expanded=False):
    st.code("""pearson_coef, p_value = stats.pearsonr(df['length'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)""")
    try:
        pearson_coef, p_value = stats.pearsonr(df['length'], df['price'])
        print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)
    except Exception as e:
        st.warning(f"⚠️ Error in cell 115: {e}")


st.markdown("""
<h4>Conclusion:</h4>

<p>Since the p-value is $<$ 0.001, the correlation between length and price is statistically significant, and the linear relationship is moderately strong (~0.691).</p>


""")



st.markdown("""
<h3>Width vs. Price</h3>


""")



st.markdown("""
 Let's calculate the Pearson Correlation Coefficient and P-value of 'width' and 'price':


""")


with st.expander("🔹 Code Cell 119", expanded=False):
    st.code("""pearson_coef, p_value = stats.pearsonr(df['width'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value )""")
    try:
        pearson_coef, p_value = stats.pearsonr(df['width'], df['price'])
        print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value )
    except Exception as e:
        st.warning(f"⚠️ Error in cell 119: {e}")


st.markdown("""
#### Conclusion:



Since the p-value is < 0.001, the correlation between width and price is statistically significant, and the linear relationship is quite strong (~0.751).


""")



st.markdown("""
### Curb-Weight vs. Price


""")



st.markdown("""
 Let's calculate the Pearson Correlation Coefficient and P-value of 'curb-weight' and 'price':


""")


with st.expander("🔹 Code Cell 123", expanded=False):
    st.code("""pearson_coef, p_value = stats.pearsonr(df['curb-weight'], df['price'])
print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)""")
    try:
        pearson_coef, p_value = stats.pearsonr(df['curb-weight'], df['price'])
        print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)
    except Exception as e:
        st.warning(f"⚠️ Error in cell 123: {e}")


st.markdown("""
<h4>Conclusion:</h4>

<p>Since the p-value is $<$ 0.001, the correlation between curb-weight and price is statistically significant, and the linear relationship is quite strong (~0.834).</p>


""")



st.markdown("""
<h3>Engine-Size vs. Price</h3>



Let's calculate the Pearson Correlation Coefficient and P-value of 'engine-size' and 'price':


""")


with st.expander("🔹 Code Cell 126", expanded=False):
    st.code("""pearson_coef, p_value = stats.pearsonr(df['engine-size'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)""")
    try:
        pearson_coef, p_value = stats.pearsonr(df['engine-size'], df['price'])
        print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)
    except Exception as e:
        st.warning(f"⚠️ Error in cell 126: {e}")


st.markdown("""
<h4>Conclusion:</h4>



<p>Since the p-value is $<$ 0.001, the correlation between engine-size and price is statistically significant, and the linear relationship is very strong (~0.872).</p>


""")



st.markdown("""
<h3>Bore vs. Price</h3>


""")



st.markdown("""
 Let's calculate the  Pearson Correlation Coefficient and P-value of 'bore' and 'price':


""")


with st.expander("🔹 Code Cell 130", expanded=False):
    st.code("""pearson_coef, p_value = stats.pearsonr(df['bore'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =  ", p_value )""")
    try:
        pearson_coef, p_value = stats.pearsonr(df['bore'], df['price'])
        print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =  ", p_value )
    except Exception as e:
        st.warning(f"⚠️ Error in cell 130: {e}")


st.markdown("""
<h4>Conclusion:</h4>

<p>Since the p-value is $<$ 0.001, the correlation between bore and price is statistically significant, but the linear relationship is only moderate (~0.521).</p>


""")



st.markdown("""
 We can relate the process for each 'city-mpg'  and 'highway-mpg':


""")



st.markdown("""
<h3>City-mpg vs. Price</h3>


""")


with st.expander("🔹 Code Cell 134", expanded=False):
    st.code("""pearson_coef, p_value = stats.pearsonr(df['city-mpg'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)""")
    try:
        pearson_coef, p_value = stats.pearsonr(df['city-mpg'], df['price'])
        print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)
    except Exception as e:
        st.warning(f"⚠️ Error in cell 134: {e}")


st.markdown("""
<h4>Conclusion:</h4>

<p>Since the p-value is $<$ 0.001, the correlation between city-mpg and price is statistically significant, and the coefficient of about -0.687 shows that the relationship is negative and moderately strong.</p>


""")



st.markdown("""
<h3>Highway-mpg vs. Price</h3>


""")


with st.expander("🔹 Code Cell 137", expanded=False):
    st.code("""pearson_coef, p_value = stats.pearsonr(df['highway-mpg'], df['price'])
print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value )""")
    try:
        pearson_coef, p_value = stats.pearsonr(df['highway-mpg'], df['price'])
        print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value )
    except Exception as e:
        st.warning(f"⚠️ Error in cell 137: {e}")


st.markdown("""
#### Conclusion:

Since the p-value is < 0.001, the correlation between highway-mpg and price is statistically significant, and the coefficient of about -0.705 shows that the relationship is negative and moderately strong.


""")



st.markdown("""
<h3>Conclusion: Important Variables</h3>


""")



st.markdown("""
<p>We now have a better idea of what our data looks like and which variables are important to take into account when predicting the car price. We have narrowed it down to the following variables:</p>



Continuous numerical variables:

<ul>

    <li>Length</li>

    <li>Width</li>

    <li>Curb-weight</li>

    <li>Engine-size</li>

    <li>Horsepower</li>

    <li>City-mpg</li>

    <li>Highway-mpg</li>

    <li>Wheel-base</li>

    <li>Bore</li>

</ul>

    

Categorical variables:

<ul>

    <li>Drive-wheels</li>

</ul>



<p>As we now move into building machine learning models to automate our analysis, feeding the model with variables that meaningfully affect our target variable will improve our model's prediction performance.</p>


""")


st.markdown("---")
st.caption("Fully Cleaned & Streamlit-Ready App | © 2025 Prashant Puri")
