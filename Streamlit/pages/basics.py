import streamlit as st

st.set_page_config(page_title="WEB Page",
                    page_icon="bar_chart:",
                    layout="wide"
                    )
st.title("EDA analysis result")
val=st.slider("Select a value",0,100,50,step=1)

st.write(val)