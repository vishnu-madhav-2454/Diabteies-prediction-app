# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:24:53 2024

@author: User
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu



#loading the saved models
diabeties_model = pickle.load(open("C:/saved_models/trained_model (1).sav",'rb'))


heart_model = pickle.load(open("C:/saved_models/trained_model_2.sav",'rb'))
#side bar for navigation
with st.sidebar:
    
    selected = option_menu('disease prediction web app',
                           ['diabeties prediction','heart disease prediction']
                           ,default_index = 0)





#diabeties prediction page
if(selected == 'diabeties prediction'):
    st.title('diabeties prediction')
    
    
    pregananices = st.text_input('enter the pregnancies ')
    glucose = st.text_input('enter the glucose ')
    blood_pressure = st.text_input('enter the blood pressure ')
    skin_thickness = st.text_input('enter the skin thickness ')
    insulin = st.text_input('enter the insulin level ')
    BMI = st.text_input('enter the BMI')
    DiabetesPedigreeFunction = st.text_input('enter the diabeties pedigree function ')
    age = st.text_input('enter the age ')
    
    
    
    
    diab_diag = ''
    if st.button('diabeties test result'):
        diab_pred = diabeties_model.predict([[pregananices,glucose,blood_pressure,skin_thickness,insulin,BMI,DiabetesPedigreeFunction,age]])
        
        if(diab_pred[0] == 1):
            diab_diag = 'the person has diabeties'
        else:
            diab_diag = 'the person doesnot have diabeties'
            
    st.success(diab_diag)
    
if(selected == 'heart disease prediction'):
    st.title('heart disease prediction')
    
    




    