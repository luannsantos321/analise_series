import pandas as pd
import plotly.express as px
import streamlit as st



import pandas as pd
import plotly.express as px
netflix = pd.read_csv('Netflix_Engagement_Report_2023_Jan-Jun_cleaned.csv')
net2 = netflix[['Title', 'Hours Viewed']]
globais = net2[netflix['Available Globally'] == 'Yes'].dropna(axis=1).set_index('Hours Viewed').sort_index(ascending=False)
maiores,menores = globais.head(5),globais.tail(5)


fig = px.bar(maiores, x='Title', y=maiores.index,
             title = 'Filmes ou séries mais assistidas globalmente',color='Title')
fig2 = px.bar(menores, x='Title', y=menores.index,title= 'Filmes ou séries menos assistidas globalmente')

st.title('Gráfico de filmes e séries da Netflix')
st.plotly_chart(fig)
st.plotly_chart(fig2)