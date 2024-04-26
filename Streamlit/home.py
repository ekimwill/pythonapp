import streamlit as st
import pandas as pd
import plotly.express as px



st.set_page_config(page_title="WEB Page",
                    page_icon="bar_chart:",
                    layout="wide"
                    )




@st.cache_data
def load_data(path:str):
    data = pd.read_csv(path)
    return data


with st.sidebar:
    uploadfile= st.file_uploader("Choose a file", type=["csv","xlsx"])

    if uploadfile is None:
        st.info("upload file through config")
        st.stop()

with st.sidebar:
    uploadfile2 = st.file_uploader("Choose another file", type=["csv","xlsx"])

    if uploadfile is None:
        st.info("upload file through config")
        st.stop()

sales_data=load_data(uploadfile)  
another_data =load_data(uploadfile2)   
# st.dataframe(sales_data)

c1,c2,c3=st.columns([1,1,1])

with c1.expander("Env Data"):
    st.write(sales_data)

with c2.expander("another Data"):
    st.write(another_data)



with c1.expander("data"):
    st.dataframe(
        df,
        column_config={
            "Year": st.column_config.NumberColumn(format="%d")
        }
    )