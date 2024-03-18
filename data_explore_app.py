import streamlit as st 
import pandas_profiling
import plotly.express as px
import pandas as pd 


from streamlit_pandas_profiling import st_profile_report

# load data 
st.title("Exploration App")
# menu
options = st.sidebar.selectbox('Menu',("Profile Report","Prediction"))
if options == "Profile Report":
    file = st.file_uploader("Upload a dataset", type=['csv'])
    st.subheader("Profile Report")
    if file is not None:

        df = pd.read_csv(file)
        
        # Data Display
        st.write(df)

        pr = df.profile_report()
        st_profile_report(pr)

        # User inputs for plot customization
        x_axis_val = st.selectbox('Select the X axis', options=df.columns)
        y_axis_val = st.selectbox('Select the Y axis', options=df.columns)
        plot_type = st.selectbox('Select plot type', ['scatter','line','bar',])


        #creating a plotly chart
        if plot_type == 'scatter':
            fig = px.scatter(df, x= x_axis_val, y = y_axis_val)
        elif plot_type == 'line':
            fig = px.line(df, x= x_axis_val, y = y_axis_val)
        elif plot_type == 'bar':
            fig = px.bar(df, x= x_axis_val, y = y_axis_val)
        st.plotly_chart(fig)
        # to run the code    streamlit run abcd.py
