# import modules
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

# Header of App defined
st.header('st.write')

st.write('The following can be displayed with the st.write function')
# Example 1

st.write('What, *Incredible!* :shots:')

# Example 2

st.write(45678)

# Example 3

df = pd.DataFrame({
     'john_bill': [1, 2, 3, 4],
     'favour_bill': [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Here is a DataFrame:', df, 'Wait, did you miss the one above.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(300, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)