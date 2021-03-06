import streamlit as st

st.title("This is a TITLE")
st.header("This is a header")
st.subheader("This is a subheader")

st.write("""
# This is a level 1 header
## level 2
## level 3
This is normal text.
""")

st.write("#### this is a code block:")
st.code("import pandas as pd")

st.image("https://raw.githubusercontent.com/aaa-yanbin/myfirstapp/main/AAA%20(a)%20Logo%20Reverse.png")

placeholder1 = st.empty()
placeholder1.write("whatever....")
