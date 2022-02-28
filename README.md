The following code provides a webapp with various visualizations on a sepsis dataset from Physionet. 

The sepsis dataset can be found at the following weblink: 
https://physionet.org/content/challenge-2019/1.0.0/

The basis of the webapp comes from: 
https://github.com/PablocFonseca/streamlit-aggrid

Therefore, this needs to be installed: 
# Install
```
pip install streamlit
pip install streamlit-aggrid
```
To start the app, type the following command in the anaconda prompt: 
```shell
streamlit run example.py
```
You can found the example.py in the examples folder.

In addition, in the folders: 
1) examples/training_setA/training 
2) examples/training_setB/training

the psv files should be added to see the exact visualizations on the report. 
There are already some psv files included, but not all of the datasets. 

If done correctly, the following will be displayed:
![example image](https://github.com/s2812135/Data_Challenges_WiSe2122/webpage.png)