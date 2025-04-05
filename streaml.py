import streamlit as st
import pandas as pd
import numpy as np

# Title of the application
st.title("Hello Streamlit")
st.header("This is a Streamlit app")
st.write("This is a simple text")

# Creating a simple DataFrame
df = pd.DataFrame({'firstcol': [1, 2, 3, 4],
                   'Secondcol': [1, 4, 9, 16]})

# Display the DataFrame with a description
st.write("Here is a sample DataFrame:")
st.write(df)

# Creating a line chart from random data
st.subheader("Random Data Line Chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])  # Added column names
st.line_chart(chart_data)

# Creating a line chart from the DataFrame
st.subheader("DataFrame Line Chart")
st.line_chart(df)