# import necessary libraries
import streamlit as st
import pandas as pd
import altair as alt
from airtable import Airtable
import time

# Airtable API Configuration
AIRTABLE_BASE_ID = 'your_base_id'
AIRTABLE_API_KEY = 'your_api_key'
AIRTABLE_TABLE_NAME = 'your_table_name'
airtable = Airtable(AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME, AIRTABLE_API_KEY)

# Streamlit App Title
st.title("INIT Internship Dashboard")

# Live counter for total internships
st.subheader("INIT Internship Count")
init_internship_count = len(airtable.get_all())
st.write(init_internship_count)

# Live counter for internships on a year-by-year basis
st.subheader("Internships by Year")
# Assuming there is a 'Year' column in the Airtable data
by_year_data = pd.DataFrame(airtable.get_all()).groupby('Year').size().reset_index(name='Counts')
st.line_chart(by_year_data)

# Graph for weekly active users by Guild name
st.subheader("Weekly Active Users by Guild Name")
# Assuming you have a dataframe (weekly_data) structured with "Guild name", "Week", "Weekly Active Users"
weekly_data = pd.DataFrame(...) # Fetch or create this data
chart_weekly = alt.Chart(weekly_data).mark_line().encode(
    x='Week',
    y='Weekly Active Users',
    color='Guild name'
)
st.altair_chart(chart_weekly, use_container_width=True)

# Graph for daily active users by Guild name
st.subheader("Daily Active Users by Guild Name")
# Assuming you have a dataframe (daily_data) structured with "Guild name", "Day", "Daily Active Users"
daily_data = pd.DataFrame(...) # Fetch or create this data
chart_daily = alt.Chart(daily_data).mark_line().encode(
    x='Day',
    y='Daily Active Users',
    color='Guild name'
)
st.altair_chart(chart_daily, use_container_width=True)
