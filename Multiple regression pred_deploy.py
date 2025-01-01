# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 22:26:06 2024

@author: rsing
"""

import pandas as pd
import numpy as np
import sklearn
import pickle
import streamlit as st
from streamlit_option_menu import option_menu




# Loading the saved models

diabetes_model=pickle.load(open("C:/Users/rsing/OneDrive/Desktop/Multiple regression prediction/saved model/Diabetes2.sav", 'rb'))

Heart_model= pickle.load(open("C:/Users/rsing/OneDrive/Desktop/Multiple regression prediction/saved model/Heart2.sav", 'rb'))

prkinson_model= pickle.load(open("C:/Users/rsing/OneDrive/Desktop/Multiple regression prediction/saved model/Parkinsons1.sav", 'rb'))


# sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple disease prediction system by using ML',
                           
                           ['Diabetes Predicion',
                            'Heart disease Prediction',
                            'Parkinson Prediction'],
                           
                           icons = ['activity', 'heart', 'person'],
                           
                           default_index=0)
    
    
##  Diabetes prediction page

if(selected == 'Diabetes Predicion'):
    
    # page title
    st.title('Diabetes Predicion using ML')
    
    Pregnancies = st.text_input('Number of pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the person')
    
    
    
    # code for prediction
    diab_diagnosis=''
    
    # creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        
        if(diab_prediction[0]==1):
            diab_diagnosis = 'The Person is Diabetic'
            
        else:
            diab_diagnosis = 'The Person is not Diabetic'
            
            
    st.success(diab_diagnosis)



if(selected == 'Heart disease Prediction'):
    
    st.title('Heart Disease Predicion using ML')
    
    
    
    age = st.text_input('Age of the person')
    sex = st.text_input('Sex')
    cp = st.text_input('Chest Pain type')
    trestbps = st.text_input('Resting blood Pressure')
    chol = st.text_input('Serum Cholestoral in mg/dl')
    fbs = st.text_input('Fasting Blood Sugar in mg/dl')
    restecg = st.text_input('Resting Electrocardiographic')
    thalach = st.text_input('Maximum Heart Rate Achieved')
    exang = st.text_input('Exercise Induced Angina')
    oldpeak = st.text_input('ST depression induced by exercise')
    slope = st.text_input('Slope of the peak exercise ST segment')
    ca = st.text_input('Major vessels colored by flourosopy')
    thal =st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    heart_diag = ''
    
    if st.button('Heart Disease Test Result'):
        heart_prediction =Heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if heart_prediction[0] == 1:
            heart_diag = 'The person is having heart disease'
        else:
            heart_diag = 'The person does not have any heart disease'
            
            
    st.success(heart_diag)
        
    
    
if selected == 'Parkinson Prediction':
    st.title('Parkinson Prediction using ML')

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = prkinson_model.predict([user_input])  # Replace .predict with model.predict

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    
    










        