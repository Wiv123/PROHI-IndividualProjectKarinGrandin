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


st.title("Karin Grandin")

st.markdown("The project I conducted using the Pokémon stats dataset was divided into three parts. First I, analyzed and visualized relationships between different stats, such as the relationship between Defense Points and Attack Points across different Pokémon types and the difference in Total Points between legendary and non-legendary Pokémon, across the first 6 Pokémon generations. Next, I used clustering to investigate if patterns could emerge from the Hit Point and Attack Point stats. Two somewhat clear clusters were identified. The third part included a predictive analysis, using supervised learning, where I tried to predict legendary status from a set of battle stats. The most successful model was a decision tree model with only 2 splits, having a recall score of 0.62, meaning that 62 % of the (quite few) legendary Pokémon were successfully identified.")