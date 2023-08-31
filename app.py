import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2, col3 = st.columns(3)

data = pd.read_csv("communes-departement-region.csv", sep=',')
data = data[["nom_commune_postal", "latitude", "longitude"]].dropna()

with col3:
    st.title("")
    st.title("")
    st.title("")
    st.title("")
    st.title("")
    st.title("")
    st.title("")
    st.title("")
    dropdown = st.selectbox("Choose your location", data["nom_commune_postal"].unique())


with col2:
    # Title
    st.title("Météo app")

    # Reactive block using @st.cache
    @st.cache_data(hash_funcs={pd.DataFrame: id})
    def get_map_data(selected_location):
        return data[data["nom_commune_postal"] == selected_location]

    map_data = get_map_data(dropdown)
    st.map(data=map_data)

    st.markdown(f"<h1 style='text-align: center;'>{dropdown}</h1>", unsafe_allow_html=True)
    col2_1, col2_2, col2_3 = st.columns(3)

    with col2_1:
        st.metric("Temp", value=999, delta=3)

    with col2_2:
        st.metric("Wind", value=999)

    with col2_3:
        st.metric("Humidity", value=999)
