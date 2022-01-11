from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to your app, Ali :heart:!
"""

x = st.slider("Number of points in spiral", 1, 100, 2)
y = st.slider("Number of turns in spiral", 1, 100, 3)

prod = x * y

text = "Product of {0} and {1} equals: {2}"
st.text(text.format(x, y, prod))
