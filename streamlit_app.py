import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Page title
st.set_page_config(page_title='Interactive Data Explorer', page_icon='📊')
st.title('📊 Interactive Data Explorer')

st.title("this is the app title")
st.header("this")
st.markdown("this")
st.subheader("this")
st.caption("this is")
st.code("x=2021")
st.latex(r'''a+ar^1+ar^2+ar^3''')

st.checkbox('yes')
st.button('Click')
gender = st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter','Mars','neptune'])
st.select_slider('Pick a mark',['Bad','Good','Excellent'])
st.slider('Pick a number',0,50)

st.write('gender',gender)