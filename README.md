#**About this dashboard**

This dashboard is based on a synthetic speech and language pathology dataset with data including Name of patients, Age, Type of visit, Patient Category, whether the visit was conducted remotely or not, which area of Sweden the patient was from and which is the patients forst language. I have added Months and Years, to get a temporal feature in the chart.

I have made a dashboard where there is a chart describing changes over time regarding the remote consultation rate. In this example, I suggest Kista as the are described, since the number of visits over the time period are quite few for a whole nation.

You can also view a (fictional) table describing the SLP's that work in the clinic of choice, their area of expertise as well as their rating from their most recent patient visit and an overview of their own dairy estimation of their stress level. 

In the bottom of the page you can get liks to 1177, for booking of appointments and there is also a link to an information page about Speech and Language Pathology

In the sidebar there are widgets with updates on the most proficient SLP in Sweden, their production rate, and current salary trends, as well as information of the current topic in the National Speech Pathology Magazine

Page 2 includes information about my previous project on Pokémon stats #


# PROHI Dashboard Example

**Author**: [Karin Grandin]
<!-- As main author, do not write anything in the line below.
The collaborator will edit the line below in GitHub -->
**Collaborator**: Christoffer Brändefors

_Note that this file is written in **MarkDown** language. A reference is available here: <https://www.markdownguide.org/basic-syntax/>_

_Here you can include images, like the logo from SU_

![Your dashboard](./assets/project-logo.jpg)

## Introduction

_This template project will contain a simple interactive web dashboard with Streamlit. Feel free to edit this document as desired_

## System description

### Installation of libraries

Run the commands below in a terminal to configure the project and install the package dependencies for the first time.

If you are using Mac, you may need to install Xcode. Check the official Streamlit documentation [here](https://docs.streamlit.io/get-started/installation/command-line#prerequisites).

1. Create the environment with `python -m venv env`
2. Activate the virtual environment for Python
   - If using Mac or Linux, type the command: `source env/bin/activate` 
   - If using Windows:
   - First, [set the Default Terminal Profile to CMD Terminal](https://code.visualstudio.com/docs/terminal/profiles)
   - Then, type in the CMD terminal: `.\env\Scripts\activate.bat`
3. Make sure that your terminal is in the environment (`env`) not in the global Python installation. The terminal should start with the word `env`
4. Install required packages `pip install -r ./requirements.txt`
5. Check that the installation works running `streamlit hello`
6. Stop the terminal by pressing **Ctrl+C**

### Execute custom Dashboard

First, make sure that you are running Python from the environment. Check the steps 2 and 3 above. Then, to run the custom dashboard execute the following command:

```
> streamlit run Dashboard.py
# If the command above fails, use:
> python -m streamlit run Dashboard.py
```

### Dependencies
Tested on Python 3.12.7 with the following packages:
  - Jupyter v1.1.1
  - Streamlit v1.46.1
  - Seaborn v0.13.2
  - Plotly v6.2.0
  - Scikit-Learn v1.7.0
  - shap v0.48.0

## Contributors
*Karin Grandin*. Project website: https://github.com/Wiv123/PROHI-IndividualProjectKarinGrandin.git
