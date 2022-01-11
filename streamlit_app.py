from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit, Ali :heart:!

## Multiplier:
"""

x = st.slider("Number of points in spiral", 1, 100, 2)
y = st.slider("Number of turns in spiral", 1, 100, 3)

text = "Product is {0}"
st.text(text.format(x * y))

"""
Version: 2
"""