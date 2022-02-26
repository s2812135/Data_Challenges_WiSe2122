# %%
import numpy as np
import pandas as pd
import os
from tqdm import tqdm
import dataframe_image as dfi
import streamlit as st
import altair as alt
from itertools import cycle
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode


###### begin function

@st.cache(allow_output_mutation=True)
def fetch_data(samples):

    #SepsisArray
    filenamearray = []
    genderarray = []
    agearray  = []
    sepsisarray = []
    datasetarray = []

    for i in range(len(samples)):
        filenamearray.append(samples[i][0])
        genderarray.append(samples[i][1])
        agearray.append(samples[i][2])
        sepsisarray.append(samples[i][3])
        datasetarray.append(samples[i][4])

    #for()

    dummy_data = {
        "Filename":np.array(filenamearray),
        "Gender":np.array(genderarray),
        "Age":np.array(agearray),
        "Sepsis":np.array(sepsisarray),
        "Dataset ":np.array(datasetarray)
    }

    print(dummy_data)
    return pd.DataFrame(dummy_data)


###### End function



#Zum Anzeigen des Grids
#@st.cache(suppress_st_warning=True)
def getGridImplementierung(personArray):

    #enterprise modules
    enable_enterprise_modules = True
    #enable_enterprise_modules = st.sidebar.checkbox("Enable Enterprise Modules")
    #if enable_enterprise_modules:
    #    enable_sidebar =st.sidebar.checkbox("Enable grid sidebar", value=False)
    #else:
    #    enable_sidebar = False
    enable_sidebar = False

    #features
    #fit_columns_on_grid_load = st.sidebar.checkbox("Fit Grid Columns on Load")
    #fit_columns_on_grid_load = st.sidebar.checkbox("Fit Grid Columns on Load")

    enable_selection= True
    if enable_selection:
        #st.sidebar.subheader("Selection options")
        #selection_mode = st.sidebar.radio("Selection Mode", ['single'])
        selection_mode = True
    
        #use_checkbox = st.sidebar.checkbox("Use check box for selection")
        #if use_checkbox:
        #    groupSelectsChildren = st.sidebar.checkbox("Group checkbox select children", value=True)
        #    groupSelectsFiltered = st.sidebar.checkbox("Group checkbox includes filtered", value=True)

        #if ((selection_mode == 'multiple') & (not use_checkbox)):
        #    rowMultiSelectWithClick = st.sidebar.checkbox("Multiselect with click (instead of holding CTRL)", value=False)
        #    if not rowMultiSelectWithClick:
        #        suppressRowDeselection = st.sidebar.checkbox("Suppress deselection (while holding CTRL)", value=False)
        #else:
        suppressRowDeselection=False
        #st.sidebar.text("___")


    #enable_selection=st.sidebar.checkbox("Enable row selection", value=True)
    #if enable_selection:
    #    st.sidebar.subheader("Selection options")
    #    selection_mode = st.sidebar.radio("Selection Mode", ['single','multiple'])
    
    #use_checkbox = st.sidebar.checkbox("Use check box for selection")
    #if use_checkbox:
    #    groupSelectsChildren = st.sidebar.checkbox("Group checkbox select children", value=True)
    #    groupSelectsFiltered = st.sidebar.checkbox("Group checkbox includes filtered", value=True)

    #if ((selection_mode == 'multiple') & (not use_checkbox)):
    #    rowMultiSelectWithClick = st.sidebar.checkbox("Multiselect with click (instead of holding CTRL)", value=False)
    #    if not rowMultiSelectWithClick:
    #        suppressRowDeselection = st.sidebar.checkbox("Suppress deselection (while holding CTRL)", value=False)
    #    else:
    #        suppressRowDeselection=False


    #Funktionsaufruf
    #sample_size = st.sidebar.number_input("rows", min_value=10, value=10)
    #grid_height = st.sidebar.number_input("Grid height", min_value=200, max_value=800, value=200)
    #return_mode = st.sidebar.selectbox("Return Mode", list(DataReturnMode.__members__), index=1)
    #return_mode_value = DataReturnMode.__members__[return_mode]

    #update_mode = st.sidebar.selectbox("Update Mode", list(GridUpdateMode.__members__), index=6)
    update_modelist = list(GridUpdateMode.__members__)
    update_mode = update_modelist[6]
    print("Das ist update mode")
    print(update_mode)
    update_mode_value = GridUpdateMode.__members__[update_mode]
    
    df = fetch_data(personArray)

    #Infer basic colDefs from dataframe types
    gb = GridOptionsBuilder.from_dataframe(df)

    #customize gridOptions
    #gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)

    #gb.configure_column("date_tz_aware", type=["dateColumnFilter","customDateTimeFormat"], custom_format_string='yyyy-MM-dd HH:mm zzz', pivot=True)

    #gb.configure_column("apple", type=["numericColumn","numberColumnFilter","customNumericFormat"], precision=2, aggFunc='sum')
    #gb.configure_column("banana", type=["numericColumn", "numberColumnFilter", "customNumericFormat"], precision=1, aggFunc='avg')
    #gb.configure_column("chocolate", type=["numericColumn", "numberColumnFilter", "customCurrencyFormat"], custom_currency_symbol="R$", aggFunc='max')

    #configures last row to use custom styles based on cell's value, injecting JsCode on components front end
    cellsytle_jscode = JsCode("""
    function(params) {
        if (params.value == 'A') {
            return {
                'color': 'white',
                'backgroundColor': 'darkred'
            }
        } else {
            return {
                'color': 'black',
                'backgroundColor': 'white'
            }
        }
    };
    """)
    #gb.configure_column("group", cellStyle=cellsytle_jscode)

    #if enable_sidebar:
    gb.configure_side_bar()

    if enable_selection:
        gb.configure_selection(selection_mode)
        #if use_checkbox:
            #gb.configure_selection(selection_mode, use_checkbox=True, groupSelectsChildren=groupSelectsChildren, groupSelectsFiltered=groupSelectsFiltered)
        #if ((selection_mode == 'multiple') & (not use_checkbox)):
        #    gb.configure_selection(selection_mode, use_checkbox=False, rowMultiSelectWithClick=rowMultiSelectWithClick, suppressRowDeselection=suppressRowDeselection)

    #show grid
    gb.configure_selection(selection_mode)
    gb.configure_grid_options(domLayout='normal')
    gridOptions = gb.build()

    #Display the grid
    st.header("Result of the person search")
    st.markdown("""
    The grid lists the people found based on entering values to the sidebar with the appropriate criteria. 
    """)

    grid_response = AgGrid(
        df, 
        gridOptions=gridOptions,
        height=200, 
        width='100%',
        #data_return_mode=return_mode_value, 
        update_mode=update_mode_value,
        #fit_columns_on_grid_load=fit_columns_on_grid_load,
        allow_unsafe_jscode=True, #Set it to True to allow jsfunction to be injected
        enable_enterprise_modules=enable_enterprise_modules,
        )

    
    df = grid_response['data']
    selected = grid_response['selected_rows']
    selected_df = pd.DataFrame(selected)

    with st.spinner("Displaying results..."):
        chart_data = df.loc[:,['Filename','Gender','Age','Sepsis']].assign(source='total')

        
        #if not selected_df.empty:
            #print("hier reingegangen beim auswählen und selected ist nicht leer")
            #selected_data = selected_df.loc[:,['Filename','Gender','Age','Sepsis']].assign(source='selection')
            #chart_data = pd.concat([chart_data, selected_data])
            #displays the chart
            #chart_data = df.loc[:,['date_time_naive','apple','banana','chocolate']].assign(source='total')
  


