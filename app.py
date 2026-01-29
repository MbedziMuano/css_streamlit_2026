import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Booking System", page_icon="🚌")

# ---------------- MOCK DATA ----------------
accommodations = pd.DataFrame({
    'Location': ['New York', 'Los Angeles', 'Chicago', 'Miami'],
    'Hotel': ['City Inn', 'Beach Resort', 'Urban Suites', 'Sun Hotel'],
    'Room Type': ['Standard', 'Deluxe', 'Suite', 'Economy'],
    'Price per Night (USD)': [150, 200, 250, 120],
    'Availability': [True, True, False, True]
})

buses = pd.DataFrame({
    'Route': ['NY to LA', 'LA to Chicago', 'Chicago to Miami', 'Miami to NY'],
    'Departure Time': ['08:00 AM', '10:00 AM', '12:00 PM', '02:00 PM'],
    'Duration (hours)': [48, 24, 30, 36],
    'Price per Seat (USD)': [100, 80, 90, 110],
    'Seats Available': [20, 15, 0, 10]
})

# ---------------- TITLE ----------------
st.title("🚌🏠 Booking Site for Accommodations and Buses")
page = st.sidebar.selectbox("Choose a section", ["Accommodations", "Buses"])

# ---------------- ACCOMMODATION BOOKING ----------------
if page == "Accommodations":
    st.header("🏠 Book Accommodation")

    name = st.text_input("Full Name")
    location = st.selectbox("Select Location", accommodations['Location'].unique())
    check_in = st.date_input("Check-in Date", min_value=date.today())
    check_out = st.date_input("Check-out Date", min_value=check_in)
    guests = st.number_input("Number of Guests", min_value=1, max_value=10, value=1)

    available_accom = accommodations[
        (accommodations['Location'] == location) &
        (accommodations['Availability'])
    ]

    if not available_accom.empty:
        st.subheader("Available Options")
        st.dataframe(available_accom, use_container_width=True)

        selected_hotel = st.selectbox("Select Hotel", available_accom['Hotel'])

        if st.button("Confirm Accommodation Booking"):
            nights = (check_out - check_in).days

            if not name:
                st.error("Please enter your name.")
            elif nights <= 0:
                st.error("Check-out date must be after check-in date.")
            else:
                price = available_accom[
                    available_accom['Hotel'] == selected_hotel
                ]['Price per Night (USD)'].values[0]

                total_price = price * nights

                booking = pd.DataFrame([{
                    "Name": name,
                    "Hotel": selected_hotel,
                    "Location": location,
                    "Guests": guests,
                    "Check-in": check_in,
                    "Check-out": check_out,
                    "Total Price (USD)": total_price
                }])

                booking.to_csv(
                    "accommodation_bookings.csv",
                    mode="a",
                    header=not pd.io.common.file_exists("accommodation_bookings.csv"),
                    index=False
                )

                st.success("✅ Accommodation booking confirmed!")
                st.write(booking)

    else:
        st.warning("No accommodations available in this location.")

# ---------------- BUS BOOKING ----------------
elif page == "Buses":
    st.header("🚌 Book Bus Tickets")

    name = st.text_input("Full Name")
    route = st.selectbox("Select Route", buses['Route'].unique())
    travel_date = st.date_input("Travel Date", min_value=date.today())
    passengers = st.number_input("Number of Passengers", min_value=1, max_value=10, value=1)

    available_buses = buses[
        (buses['Route'] == route) &
        (buses['Seats Available'] >= passengers)
    ]

    if not available_buses.empty:
        st.subheader("Available Buses")
        st.dataframe(available_buses, use_container_width=True)

        selected_time = st.selectbox(
            "Select Departure Time",
            available_buses['Departure Time']
        )

        if st.button("Confirm Bus Booking"):
            if not name:
                st.error("Please enter your name.")
            else:
                price = available_buses[
                    available_buses['Departure Time'] == selected_time
                ]['Price per Seat (USD)'].values[0]

                total_price = price * passengers

                booking = pd.DataFrame([{
                    "Name": name,
                    "Route": route,
                    "Departure Time": selected_time,
                    "Travel Date": travel_date,
                    "Passengers": passengers,
                    "Total Price (USD)": total_price
                }])

                booking.to_csv(
                    "bus_bookings.csv",
                    mode="a",
                    header=not pd.io.common.file_exists("bus_bookings.csv"),
                    index=False
                )

                st.success("✅ Bus booking confirmed!")
                st.write(booking)

    else:
        st.warning("No buses available or insufficient seats.")
