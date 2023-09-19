import plotly.express as px #visualize library
import streamlit as st #create a web app
import seaborn as sns #load datasets
import matplotlib.pyplot as plt #visualize library

#Iris
df_iris = sns.load_dataset("iris")


fig1 = px.scatter_3d(    #2D: px.scatter
    df_iris,
    x="sepal_length",
    y="sepal_width",
    z="petal_width",
    size="petal_length",
    color="species",
    log_x=True,
    size_max=60,
)


#mpg
df_mpg = sns.load_dataset("mpg")

fig2 = px.scatter_3d(    #2D: px.scatter
    df_mpg,
    x="horsepower",
    y="weight",
    z="displacement",
    size="cylinders",
    color="model_year",
    log_x=True,
    size_max=60,
)

#planets
df_pla = sns.load_dataset("planets")
chart= {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'distance', 'type': 'quantitative'},
        'y': {'field': 'orbital_period', 'type': 'quantitative'},
        'size': {'field': 'method', 'type': "nominal"},
        'color': {'field': 'method', 'type': "nominal"},
    },
}

#Titanic
df_tita = sns.load_dataset("titanic")

tab1, tab2, tab3, tab4= st.tabs(["Iris Dataset", "pmg Dataset", "Planets Dataset","Titanic Dataset"])

with tab1:
    st.write("""
    # Iris Dataset
    The relationship among sepal_length, sepal_width, petal_length and species of Iris.
    """)

    st.plotly_chart(fig1, theme=None, use_container_width=True)

with tab2:
    st.write("""
    # mpg Dataset
    The development of cars in different years.
    """)

    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)

with tab3:
    st.write("""
    # planets Dataset
    How different method influence the parameters of planets. 
    """)

    st.vega_lite_chart(
        df_pla, chart, theme=None, use_container_width=True)

with tab4:
    st.write("""
    # Titanic Dataset
    The age distribution of Titanic.
    """)

    fig = plt.figure()
    plt.plot(df_tita["age"])
    plt.ylabel('Age') 
    st.pyplot(fig)
