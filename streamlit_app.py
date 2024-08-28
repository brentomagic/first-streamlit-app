import streamlit as st
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt


st.set_page_config(page_title="Brentomagic's Streamlit App", page_icon="🧙‍♂", layout="wide")

st.title("Hello everyone!")

with st.sidebar:
    st.header("About app")
    st.write("I'm *Brentomagic* :sunglasses:, this is my first streamlit app.")

st.write("My first try with streamlit app.")

st.header("My first header with a divider", divider="rainbow")

st.markdown("Markdown created by Brentomagic:sunglasses:")

#create 2 column 
col1, col2 = st.columns(2)

with col1:
    x = st.slider("choose an x value", 1, 20)
with col2:
    st.write("The value of :red[x] is:", x)

st.write("Streamlit can also take in visualizations")

# create sample data

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

#display bar chart
st.subheader("Line Chart")
st.bar_chart(chart_data)

# Display line chart
st.subheader("Line Chart")
st.line_chart(chart_data)


# Add an interactive feature
st.subheader("Interactive Feature")
selected_column = st.selectbox("Select a column to display its statistics", chart_data.columns)
st.write(f"Statistics for column {selected_column}:")
st.write(chart_data[selected_column].describe())

# Add a data editor
st.subheader("Data Editor")
st.write("You can edit the data directly in the app:")
edited_data = st.data_editor(chart_data)

# Display the edited data
st.subheader("Edited Data")
st.write(edited_data)
