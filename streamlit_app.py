'''import altair as alt
import numpy as np
import pandas as pd
import rpy2.robjects as ro
import streamlit as st


r=ro.r
r.source("./utils.R")
p=r.my_function()'''


import streamlit as st
import subprocess


'''r=ro.r
r.source("./utils.R")
p=r.my_function()'''


st.subheader('1. Printing text in R')
with st.expander('See code'):
  code1 = '''print("Hello world ...")
  '''
  st.code(code1, language='R')
process1 = subprocess.Popen(["Rscript", "PortFolio_Recom.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result1 = process1.communicate()
st.write(result1)

print("Hello")
