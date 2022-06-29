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
