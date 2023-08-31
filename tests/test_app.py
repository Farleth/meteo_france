import streamlit as st
from app import get_map_data  # Import the function you want to test
import pandas as pd

data = pd.read_csv("communes-departement-region.csv", sep=',')
data = data[["nom_commune_postal", "latitude", "longitude"]].dropna()

def test_get_map_data():
    # Test the get_map_data function
    selected_location = "MONSOLS"
    expected_result = data[data["nom_commune_postal"] == selected_location]

    actual_result = get_map_data(selected_location)

    assert len(actual_result) == len(expected_result)
    # Add more assertions as needed

# Add more test cases as needed
