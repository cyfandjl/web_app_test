import streamlit as st #create a web app
import seaborn as sns #load datasets
import pandas as pd

#Breast Cancer Wisconsin (Diagnostic) Data Set
wi_can_df = pd.read_csv('WI cancer dataset.csv') 


tab1, tab2, tab3, tab4= st.tabs(["plot1", "plot2", "plot3", "plot4"])

with tab1:
    

    plot1=sns.displot(wi_can_df, x="radius_mean", y="texture_mean", kind="kde", rug=True)
    st.pyplot(plot1)

    st.button("Reset", type="primary")
    if st.button('test'):
        st.write('hello')
    else:
        st.write('Goodbye')

with tab2:
    

    plot2=sns.jointplot(data=wi_can_df, x='texture_worst', y='perimeter_worst', color="#eccd13")
    st.pyplot(plot2)

    t = st.time_input('Set an alarm for', datetime.time(2, 30))
    st.write('Alarm is set for', t)

with tab3:
    

    plot3=sns.displot(wi_can_df, x="symmetry_mean", binwidth=0.02)
    st.pyplot(plot3)

with tab4:
    
    plot4=sns.relplot(data=wi_can_df,
    x="smoothness_mean", y="compactness_mean", hue="diagnosis", style="diagnosis")
    st.pyplot(plot4)
