import streamlit as st
import os

root = os.path.join(os.path.dirname(__file__))



#dashboard2 = {
#        "Main Page": os.path.join(root, "main.py")
#    }
dashboards = {
    # Richtige: "Exercise 1": os.path.join(root, "main_example.py"),
    #Bearbeitete 
    "Home": os.path.join(root, "mainPage.py"),
    #"Exersice 1": os.path.join(root, "exersice1.py"),
    "Visualizations on the entire dataset": os.path.join(root, "exersice1.py"),
    "Visualizations on Sepsis-Subgroup-Relation": os.path.join(root, "exersice2.py"),
    #"Dimensionality Reduction & Data Imputation": os.path.join(root, "DimReductImput.py"),
    #"Exersice 2": os.path.join(root, "exersice2.py"),
    #"Exersice 2": os.path.join(root, "exersice2old.py"),
    #"Exersice 2": os.path.join(root, "fixed_key_example.py"),
    #"Exersice 3": os.path.join(root, "licensing_example.py"),
    #"Exersice 3": os.path.join(root, "exersice3.py"),
    #"Exersice 4": os.path.join(root, "two_grids_example.py"),
    #"Exersice 5": os.path.join(root, "virtual_columns.py"),
    "Visualization Component": os.path.join(root, "exersice6.py"),
    #"Exersice 6": os.path.join(root, "exersice6.py"),
    #"Test Ex 6": os.path.join(root, "main_example.py"),
    #"Exersice 6": os.path.join(root, "exersice6.py"),
    #"Exersice 6": os.path.join(root, "example_highlight_change.py"),
    #"Inside st.form": os.path.join(root, "forms.py"),
    #"Pinned Row": os.path.join(root, "pinned_rows.py"),
    #"Theming & Pre-Selection": os.path.join(root, "themes_and_pre_selection.py")
}

#choice2 = st.sidebar.radio("Pages", list(dashboard2.keys()))

choice = st.sidebar.radio("Vizualizations on the Exercises", list(dashboards.keys()))

#path2 = dashboard2[choice2]
path = dashboards[choice]

with open(path, encoding="utf-8") as code:
    exec(code.read(), globals())
