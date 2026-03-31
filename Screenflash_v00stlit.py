#v00: 30/03/26
#-------------------------------
import streamlit as st
import pandas as pd
import time

#start--------------------------------------------------------
#st.subheader("Screenflash (local version)", divider="grey")
st.set_page_config(layout='wide')
Sel_00 = [' ' for i in range(25)]
tones = {0:'white', 1:'black', 2:'blue', 3:'red', 4:'yellow', 5:'green', 6:'orange',
         7:'lime', 8:'magenta'}

flash, ton0, ton1 = False, tones[0], tones[0]  #only intializing
col01, col02, col03, col04, col05 = st.columns(5)
with col01:
    if st.button("Mixed", type="primary", key="seleccion"):   
        flash, ton0, ton1 = True, tones[7], tones[8]
with col02:
    if st.button("Blue"):
        flash, ton0, ton1 = True, tones[2], tones[0]
with col03:
    if st.button("Red"):
        flash, ton0, ton1 = True, tones[3], tones[0]
with col04:
    if st.button("Yellow"):
        flash, ton0, ton1 = True, tones[4], tones[0]
with col05:
    if st.button("Green"):
        flash, ton0, ton1 = True, tones[5], tones[0]        
if flash:
    c = 0    
    while c < 10:
        vaciar = st.empty()
        if c%2 == 0:
            with vaciar.container():
                Sel_00df = pd.DataFrame(Sel_00)
                Sel_01df = Sel_00df.style.set_properties(**{'background-color': ton0})
                st.dataframe(Sel_01df, width="stretch", hide_index=True, height=800)
        else:
            with vaciar.container():
                Sel_00df = pd.DataFrame(Sel_00)
                Sel_01df = Sel_00df.style.set_properties(**{'background-color': ton1})
                st.dataframe(Sel_01df, width="stretch", hide_index=True, height=800)
        time.sleep(0.1)
        c += 1
        vaciar.empty()
