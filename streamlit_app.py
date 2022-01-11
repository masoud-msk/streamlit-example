from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to your app, Ali :heart:!
"""

x = st.slider("First number", 1, 100, 2)
y = st.slider("Second number", 1, 100, 3)

prod = x * y

text = "Product of {0} and {1} equals: {2}"
st.text(text.format(x, y, prod))
