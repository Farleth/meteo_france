import streamlit as st
import requests
import folium
from streamlit_folium import folium_static
from back import get_coordonner, get_weather_data

def main():
    st.header("Find the Weather 🌥️")
    city = st.text_input("Enter the city").lower()
    if st.button('Find'):
        longitude, latitude = get_coordonner(city)
        general, temperature, max_temperature, feels_temp, humidity, icon = get_weather_data(longitude, latitude)
        # Display map with city location
        st.header("City Location on Map 🗺️")
        map_center = [latitude, longitude]
        m = folium.Map(location=map_center, zoom_start=10)
        folium.Marker(map_center, popup=city.capitalize()).add_to(m)
        folium_static(m)  # Display the map in Streamlit

        st.header("The weather of your city:", city)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric('Temperature', str(temperature)+'℃', str(max_temperature-temperature)+'℃')
            #st.metric('Feels Like', str(feels_temp)+'℃')
        with col2:
            st.metric('Humidity', str(humidity)+'%')
        with col3:
            st.write(general)
            st.image(icon)

        st.header("WEATHAPP weather-location")

if __name__ == '__main__':
    main()