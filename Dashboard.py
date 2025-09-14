import streamlit as st
import numpy as np
import pandas as pd
from faker import Faker
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

df = pd.read_csv("speech_pathology_dataset1.csv")
df['Visit_Type'] = df['Visit Type'].replace('visit', 'Assistive technology evaluation')

import random

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

df['Month of visit'] = [random.choice(months) for _ in range(len(df))]
df['Year'] = [random.randint(2015, 2025) for _ in range(len(df))]

st.title(":blue[LOGOPEDDATA Sverige]")
st.markdown('''
    :blue-background[_Swedish Speech and Language Pathology data for the years 2015-2025_]''')

image = Image.open('logopedbild.jpg') 

st.sidebar.image(image, use_container_width=True)
st.page_link("Dashboard.py", label="Page 1", icon="1️⃣")

st.snow()
