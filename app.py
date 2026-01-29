import streamlit as st
import pandas as pd
from datetime import date

# Mock data for accommodations (hotels/rooms)
accommodations = pd.DataFrame({
    'Location': ['New York', 'Los Angeles', 'Chicago', 'Miami'],
    'Hotel': ['City Inn', 'Beach Resort', 'Urban Suites', 'Sun Hotel'],
    'Room Type': ['Standard', 'Deluxe', 'Suite', 'Economy'],
    'Price per Night (USD)': [150, 200, 250, 120],
    'Availability': [True, True, False, True]  # Simulate some unavailable
})

# Mock data for buses
buses = pd.DataFrame({
    'Route': ['NY to LA', 'LA to Chicago', 'Chicago to Miami', 'Miami to NY'],
    'Departure Time': ['08:00 AM', '10:00 AM', '12:00 PM', '02:00 PM'],
    'Duration (hours)': [48, 24, 30, 36],
    'Price per Seat (USD)': [100, 80, 90, 110],
    'Seats Available': [20, 15, 0, 10]  # Simulate some full
})

# App title and sidebar navigation
st.title("Booking Site for Accommodations and Buses")
page = st.sidebar.selectbox("Choose a section", ["Accommodations", "Buses"])

if page == "Accommodations":
    st.header("Book Accommodations")
    
    # Filters
    location = st.selectbox("Select Location", accommodations['Location'].unique())
    check_in = st.date_input("Check-in Date", min_value=date.today())
    check_out = st.date_input("Check-out Date", min_value=check_in)
    guests = st.number_input("Number of Guests", min_value=1, max_value=10, value=1)
    
    # Filter available accommodations
    available_accom = accommodations[(accommodations['Location'] == location) & (accommodations['Availability'])]
    
    if not available_accom.empty:
        st.subheader("Available Options")
        st.dataframe(available_accom)
        
        selected_hotel = st.selectbox("Select Hotel", available_accom['Hotel'])
        if st.button("Book Now"):
            nights = (check_out - check_in).days
            total_price = available_accom[available_accom['Hotel'] == selected_hotel]['Price per Night (USD)'].values[0] * nights
            st.success(f"Booking confirmed for {selected_hotel} in {location}! Total: ${total_price} for {nights} nights and {guests} guests.")
    else:
        st.warning("No accommodations available in this location.")

elif page == "Buses":
    st.header("Book Bus Tickets")
    
    # Filters
    route = st.selectbox("Select Route", buses['Route'].unique())
    travel_date = st.date_input("Travel Date", min_value=date.today())
    passengers = st.number_input("Number of Passengers", min_value=1, max_value=10, value=1)
    
    # Filter available buses
    available_buses = buses[(buses['Route'] == route) & (buses['Seats Available'] >= passengers)]
    
    if not available_buses.empty:
        st.subheader("Available Buses")
        st.dataframe(available_buses)
        
        selected_bus = st.selectbox("Select Bus (by Departure Time)", available_buses['Departure Time'])
        if st.button("Book Now"):
            total_price = available_buses[available_buses['Departure Time'] == selected_bus]['Price per Seat (USD)'].values[0] * passengers
            st.success(f"Booking confirmed for {route} bus at {selected_bus}! Total: ${total_price} for {passengers} passengers on {travel_date}.")
    else:
        st.warning("No buses available for this route or insufficient seats.")