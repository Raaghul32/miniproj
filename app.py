# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 15:01:24 2020

@author: raagh
"""
def something(x):
    if x== 'ICSE':
        return 0
    elif x=='TN state board':
        return 1
    elif x=='CBSE':
        return 2
    elif x=='Andhra State Board':
        return 3
    elif x=='NRI':
        return 4
    else:
        return 5

def streamugh(z):
    if z == 'Computer Science':
        return 1
    elif z == 'Biology':
        return 0
    else :
        return 3
    
    
import streamlit as st
import pandas as pd
import numpy as np
import xgboost
import joblib
df = pd.read_excel('Mini Excel.xlsx')



model = joblib.load('model.pkl')
sc = joblib.load('sc.pkl')
try :
    st.title('Course Recommender')
    st.subheader('Developed by: \n Raaghul Viswanath and Snigdha Desiraju')
    st.subheader('Sliding is changing dept at the end of first year and getting what you need based on CGPA')
    st.subheader('SOCE = School of Computer Science Engeering\t SEEE =School of Electronics \t SOME = School of Mechanical \t SCBT = School of Chemistry and Biotech')
    JEE = st.number_input('JEE MARKS, (Enter zero if not appeared)', step=10.0, min_value=0.0)
    twelvep = st.number_input('12th percentage', step=10.0, min_value=0.0)
    tenthpe = st.number_input('10th percentage(wrt 100)', step=10.0, min_value=0.0)
    twestr = st.selectbox('12 th medium of study',('ICSE','TN state board','CBSE','Andhra State Board','NRI','Others'))
    twestr1 = something(twestr)
    stream12 = st.selectbox('12th stream of study',('Computer Science','Biology','Others that has neither CS nor BIO'))
    stream12 = streamugh(stream12)
    sliding = st.radio('Are you okay with sliding, see above for ref(1 for yes,0 for no)',options = [0,1])
    fiftykm = st.radio('Is your 50km from the campus(1 for yes,0 for no)',options = [0,1])
    hostelwill = st.slider('Willingness to stay in hostel',
                   min_value=0.0, max_value=5.0, step=0.1)
    mark = [[JEE,twelvep,tenthpe,twestr1,sliding,stream12,fiftykm,hostelwill]]
    if st.button('Predict'):
        
        final_features = sc.transform(mark)
        prediction = model.predict_proba(final_features)
        prediction = np.array(prediction*100)
        Converted = pd.DataFrame(prediction,columns=['SEEE','SOCE','SCBT','SOME','Civil'])
        st.dataframe(data= Converted)
        st.write("Dept recommendation based on our dataset is given in the above table in terms of percentage")
except:
    st.write("Ooops something is wrong")
      
    


