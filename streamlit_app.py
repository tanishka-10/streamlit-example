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


r=ro.r
r.source("./utils.R")
p=r.my_function()




process1 = subprocess.Popen(["Rscript", "PortFolio_Recom.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result1 = process1.communicate()
st.write(result1)

print("Hello")
