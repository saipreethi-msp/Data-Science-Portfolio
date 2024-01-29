import streamlit as st 
import plotly.express as px
import pandas as pd 

# load data 
st.title("Exploration App")
st.tilte("sai preethi")

file = st.file_uploader("Upload a dataset", type=['csv'])
if file is not None:

    df = pd.read_csv(file)

    # streamlit app structure

    # Data Display
    if st.checkbox("Show Dataset"):
        st.write(df)

    # User inputs for plot customization
    x_axis_val = st.selectbox('Select the X axis', options=df.columns)
    y_axis_val = st.selectbox('Select the Y axis', options=df.columns)
    plot_type = st.selectbox('Select plot type', ['scatter','line','bar','asdasd'])

    #creating a plotly chart
    if plot_type == 'scatter':
        fig = px.scatter(df, x= x_axis_val, y = y_axis_val)
    elif plot_type == 'line':
        fig = px.line(df, x= x_axis_val, y = y_axis_val)
    elif plot_type == 'bar':
        fig = px.bar(df, x= x_axis_val, y = y_axis_val)
    st.plotly_chart(fig)
    # to run the code    streamlit run abcd.py