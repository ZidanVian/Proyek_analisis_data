import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Set up basic config
st.title('Bike Sharing Data Dashboard')
st.write("Dashboard ini menampilkan berbagai analisis data penggunaan Bike Sharing berdasarkan dataset yang diberikan.")

#Load dataset
df = pd.read_csv('hour.csv')

#Converting the 'dteday' column to datetime format for better time-based analysis
df['dteday'] = pd.to_datetime(df['dteday'])

#Sidebar for user selections
st.sidebar.header("Filter Data")
month_filter = st.sidebar.selectbox("Select Month", range(1, 13))
day_filter = st.sidebar.selectbox("Select Day of the Week", range(7))

#Data Overview Section
st.header('Dataset Overview')
st.write(df.head())

#Monthly Usage Trend
st.header("Monthly Usage Trend")
monthly_usage = df.groupby('mnth')['cnt'].mean()

fig, ax = plt.subplots(figsize = (10, 6))
sns.lineplot(data = monthly_usage, marker = 'o', color = 'b', ax = ax)
ax.set_title('Monthly Average Usage Trend for Bike-Sharing')
ax.set_xlabel('Month')
ax.set_ylabel('Average Daily Usage Count')
ax.set_xticks(range(1, 13))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
st.pyplot(fig)

#Weekday vs. Holiday Usage
st.header("Usage Based on Weekday and Holidays")
weekday_usage = df.groupby('weekday')['cnt'].mean()

fig, ax = plt.subplots(figsize = (6, 4))
sns.barplot(x = weekday_usage.index, y = weekday_usage.values, palette = "Blues", ax = ax)
ax.set_title('Average Usage by Weekday')
ax.set_xlabel('Weekday (0=Sunday)')
ax.set_ylabel('Average Daily Usage Count')
st.pyplot(fig)

holiday_usage = df.groupby('holiday')['cnt'].mean()

fig, ax = plt.subplots(figsize = (6, 4))
sns.barplot(x =['Non-Holiday', 'Holiday'], y = holiday_usage.values, palette = "Blues", ax = ax)
ax.set_title('Average Usage on Holidays vs Non-Holidays')
ax.set_ylabel('Average Daily Usage Count')
st.pyplot(fig)

#Weather Impact Analysis: Usage by Weather
st.header("Impact of Weather on Usage")
fig, ax = plt.subplots(figsize = (10, 6))
sns.boxplot(x = 'weathersit', y = 'cnt', data = df, palette = 'viridis', ax = ax)
ax.set_xlabel("Weather Situation (1=Clear, 4=Heavy Rain/Snow)")
ax.set_ylabel("Daily Usage Count")
ax.set_title("Effect of Weather Condition on Daily Usage")
st.pyplot(fig)

#Usage by Hour of the Day
st.header("Hourly Distribution of Bike Rentals")
fig, ax = plt.subplots(figsize = (12, 6))
sns.boxplot(x = 'hr', y = 'cnt', data = df, ax = ax)
ax.set_title('Distribution of bike rentals per hour')
medians = df.groupby('hr')['cnt'].median()
for x,y in enumerate(medians):
	ax.text(x, y, f'{y:.2f}', ha='center', va='bottom')
st.pyplot(fig)

#Usage by Days of the Week
st.header("Bike Rentals per Day of the Week")
fig, ax = plt.subplots(figsize = (12, 6))
sns.boxplot(x = 'weekday', y = 'cnt', data = df, ax = ax)
ax.set_title('Distribution of bike rentals V/S days of the week')
st.pyplot(fig)

#Usage by Month
st.header("Bike Rentals per Month")
fig, ax = plt.subplots(figsize = (12, 6))
sns.boxplot(x = 'mnth', y = 'cnt', data = df, ax = ax)
ax.set_title('Distribution of bike rentals V/S months')
st.pyplot(fig)

st.write("Data analysis complete. Explore various trends using the charts above.")
