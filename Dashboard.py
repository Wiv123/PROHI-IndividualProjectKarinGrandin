import streamlit as st
import numpy as np
import pandas as pd
from faker import Faker
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import altair as alt
from numpy.random import default_rng as rng

df = pd.read_csv("speech_pathology_dataset1.csv")
df['Visit_Type'] = df['Visit Type'].replace('visit', 'Assistive technology evaluation')
df['Patient Category'] = df['Patient Category'].replace('Developmental Language Disorder', 'Pediatric Speech Pathology')

import random

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

df['Month of visit'] = [random.choice(months) for _ in range(len(df))]
df['Year'] = [random.randint(2015, 2025) for _ in range(len(df))]

df['Year'] = df['Year'].astype('string')
image = Image.open('log.png') 

left, right = st.columns([0.3, 0.9])

with left:
    st.image(image, use_container_width=40)

with right:

    st.title(":grey[LOGOPEDDATA Sverige]")
    st.markdown('''
        :blue-background[_Swedish Speech and Language Pathology data for the period 2015-2025_]''')
    st.markdown("<br>", unsafe_allow_html=True)

image2 = Image.open('kista.png') 
st.sidebar.image(image2, use_container_width=True)
st.sidebar.metric("SLP of the week", "Elisabet", "+ 0.7 patients/day")
st.sidebar.metric("Average salary", "32 000 SEK", "-8% since last year")
st.sidebar.metric("Todays topic on _Logopeden Magazine_", "AI is not the solution")

chart_df = df.groupby(['Year', 'Patient Category']).agg({'Distance': 'sum'}).reset_index()
chart_df=chart_df.rename(columns={
    'Distance': 'Remote consultations'
})

chart = alt.Chart(chart_df).mark_line(point=True).encode(
    x='Year',
    y='Remote consultations',
    color='Patient Category'    
).properties(
    title='Remote consultations per year for the Kista area')


st.altair_chart(chart, use_container_width=True)

df = pd.DataFrame(
    {
        "name": ["Lisa", "Pelle", "Olle"],
        "Area of expertise": [
            "Pediatric Speech Pathology",
            "Stuttering",
            "Dyslexia",
        ],
        "stars": rng(0).integers(0, 5, size=3),
        "views_history": rng(0).integers(0, 5000, size=(3, 30)).tolist(),
    }
)

st.dataframe(
    df,
    column_config={
        "name": "SLP's (Kista)",
        "stars": st.column_config.NumberColumn(
            "Rating (last patient)",
            help="Rating by previous patients",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Estimated stress level (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)
st.subheader("_What is your problem?_")
left, middle, right = st.columns(3)
if left.button("Reading and writing"):
    left.link_button("Please book an appointment with :blue[Olle]", "https://www.1177.se/")
if middle.button("Stuttering"):
    middle.link_button("Please book an appointment with :blue[Pelle]", "https://www.1177.se/")
if right.button("Late Speech/Language Development"):
    right.link_button("Please book an appontment with :blue[Lisa]", "https://www.1177.se/")

st.subheader("Do you want to learn more about Speech Pathology?")
agree = st.checkbox("Yes")
disagree = st.checkbox("No")

if agree:
    st.link_button('Follow this link', "https://ki.se/en/clintec/divisions-at-the-department-of-clinical-science-intervention-and-technology/division-of-speech-and-language-pathology/about-speech-and-language-pathology")
if disagree:
    st.markdown("Thank you for your visit!")