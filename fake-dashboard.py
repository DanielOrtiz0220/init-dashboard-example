# import necessary libraries
import streamlit as st
import pandas as pd
import altair as alt
import random

# Streamlit App Title
st.title("INIT Internship Dashboard")

# Example data for total internships
st.subheader("INIT Internship Count")
init_internship_count = random.randint(100, 200) # Fake count
st.write(init_internship_count)

# Example data for internships on a year-by-year basis
st.subheader("Internships by Year")
by_year_data = pd.DataFrame({
    'Year': [2018, 2019, 2020, 2021],
    'Counts': [50, 60, 70, 80]
})
st.line_chart(by_year_data.set_index('Year'))

# Example data for weekly active users by Guild name
st.subheader("Weekly Active Users by Guild Name")
weekly_data = pd.DataFrame({
    'Guild name': ['Guild A', 'Guild B'] * 10,
    'Week': list(range(1, 11)) * 2,
    'Weekly Active Users': [random.randint(100, 200) for _ in range(20)]
})
chart_weekly = alt.Chart(weekly_data).mark_line().encode(
    x='Week',
    y='Weekly Active Users',
    color='Guild name'
)
st.altair_chart(chart_weekly, use_container_width=True)

# Example data for daily active users by Guild name
st.subheader("Daily Active Users by Guild Name")
daily_data = pd.DataFrame({
    'Guild name': ['Guild A', 'Guild B'] * 30,
    'Day': list(range(1, 31)) * 2,
    'Daily Active Users': [random.randint(50, 100) for _ in range(60)]
})
chart_daily = alt.Chart(daily_data).mark_line().encode(
    x='Day',
    y='Daily Active Users',
    color='Guild name'
)
st.altair_chart(chart_daily, use_container_width=True)
