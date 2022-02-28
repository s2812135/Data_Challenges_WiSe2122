import streamlit as st
import os

root = os.path.join(os.path.dirname(__file__))

dashboards = {
    "Home": os.path.join(root, "mainPage.py"),
    #"Exersice 1": os.path.join(root, "exersice1.py"),
    "Visualizations on the entire dataset": os.path.join(root, "exersice1.py"),
    "Visualizations on Sepsis-Subgroup-Relation": os.path.join(root, "exersice2.py"),
    #"Dimensionality Reduction & Data Imputation": os.path.join(root, "DimReductImput.py"),

    "Visualization Component": os.path.join(root, "exersice6.py"),
}

#choice2 = st.sidebar.radio("Pages", list(dashboard2.keys()))

choice = st.sidebar.radio("Vizualizations on the Exercises", list(dashboards.keys()))

#path2 = dashboard2[choice2]
path = dashboards[choice]

with open(path, encoding="utf-8") as code:
    exec(code.read(), globals())
