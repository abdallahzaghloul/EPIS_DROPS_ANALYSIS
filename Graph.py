import numpy as np #1
import pandas as pd #2
import plotly.graph_objects as go  #6
import plotly.express as px  #7
from plotly.subplots import make_subplots  #8
import plotly.figure_factory as ff #21
from PIL import Image
import streamlit as st

pd.set_option('mode.chained_assignment',None)

im = Image.open("EPIS.png")
image = np.array(im)
st.image(image)


st.markdown(" <center>  <h1> KPC (DRLG/WO) Drops Analysis </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)
 

#####
df = pd.read_excel("Book2.xlsx")
df.columns  = [i.replace(' ','_') for i in df.columns]
df.columns  = [i.upper() for i in df.columns]

X1=['PASS Vs. 1ST_CAMPAIGN','1ST_CAMPAIGN']
Y1=pd.Series([[df.PASS.sum(),df['1ST_CAMPAIGN'].sum()]])
fig1 = px.bar(x= X1, y= Y1)



X2=['PASS Vs. 1ST_CAMPAIGN','PASS Vs. 2ND_CAMPAIGN','2ND_CAMPAIGN']
Y2=pd.Series([[df.PASS.sum(),df.PASS.sum()+(df['1ST_CAMPAIGN'].sum()-df['2ND_CAMPAIGN'].sum()),df['2ND_CAMPAIGN'].sum() ]])
fig2=px.bar(x= X2, y= Y2)

X3=['PASS Vs. 1ST_CAMPAIGN','PASS Vs. 2ND_CAMPAIGN','PASS Vs. 3RD_CAMPAIGN','3RD_CAMPAIGN']
Y3=pd.Series([[df.PASS.sum(),df.PASS.sum()+(df['1ST_CAMPAIGN'].sum()-df['2ND_CAMPAIGN'].sum()),df.PASS.sum()+(df['1ST_CAMPAIGN'].sum()-df['3RD_CAMPAIGN'].sum()),df['3RD_CAMPAIGN'].sum() ]])
fig3=px.bar(x= X3, y= Y3)

X4=['PASS Vs. 1ST_CAMPAIGN','PASS Vs. 2ND_CAMPAIGN','PASS Vs. 3RD_CAMPAIGN','PASS Vs. 4TH_CAMPAIGN','4TH_CAMPAIGN']
Y4=pd.Series([[df.PASS.sum(),df.PASS.sum()+(df['1ST_CAMPAIGN'].sum()-df['2ND_CAMPAIGN'].sum()),df.PASS.sum()+(df['1ST_CAMPAIGN'].sum()-df['3RD_CAMPAIGN'].sum()),df.PASS.sum()+(df['1ST_CAMPAIGN'].sum()-df['4TH_CAMPAIGN'].sum()),df['4TH_CAMPAIGN'].sum() ]])
fig4 = px.bar(x= X4, y= Y4)




#####
st.plotly_chart(fig1, use_container_width=True)
st.write("This graph is showing Bla Bla Bla Bla Bla ")

st.plotly_chart(fig2, use_container_width=True)
st.write("This graph is showing Bla Bla Bla Bla Bla ")

st.plotly_chart(fig3, use_container_width=True)
st.write("This graph is showing Bla Bla Bla Bla Bla ")

st.plotly_chart(fig4, use_container_width=True)
st.write("This graph is showing Bla Bla Bla Bla Bla ")

# streamlit run "C:\\Users\\hp\\Desktop\\EPIS\\EDC_87\\EPIS_HOME.py" 


















