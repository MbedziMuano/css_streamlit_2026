import streamlit as st
import pandas as pd
from datetime import date

# ------------------ CSS FOR COLORS AND STYLING ------------------
st.markdown("""
<style>
/* Main background gradient */
.stApp {
    background: linear-gradient(135deg, #e3f2fd, #fce4ec);
}

/* Titles */
h1 {
    color: #0d47a1;
    text-align: center;
}
h2, h3 {
    color: #1a237e;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #263238;
}
[data-testid="stSidebar"] * {
    color: white;
}

/* Card style */
.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.15);
    margin-bottom: 20px;
}

/* Buttons */
.stButton>button {
    background-color: #1976d2;
    color: white;
    border-radius: 10px;
    height: 3em;
    font-size: 16px;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #0d47a1;
    color: #ffffff;
}

/* Success message */
.stAlert.success {
    background-color: #e8f5e9;
    color: #1b5e20;
}

/* Warning message */
.stAlert.warning {
    background-color: #fff3e0;
    color: #e65100;
}
</style>
""", unsafe_allow_html=True)

# ------------------ MOCK DATA (SOUTH AFRICA HOTELS) ------------------
accommodations = pd.DataFrame([
    # Johannesburg
    ['Johannesburg', 'Hilton Sandton', 'Luxury', 4200, 5],
    ['Johannesburg', 'Palazzo Hotel Montecasino', 'Luxury', 3800, 5],
    ['Johannesburg', 'Southern Sun Rosebank', 'Mid‑range', 2500, 4],
    ['Johannesburg', 'Radisson Blu Sandton', 'Mid‑range', 2700, 4],
    ['Johannesburg', 'Mint Hotel Rosebank', 'Budget', 1800, 3],

    # Cape Town
    ['Cape Town', 'Belmond Mount Nelson', 'Luxury', 5000, 5],
    ['Cape Town', 'Hyatt Regency Cape Town', 'Luxury', 4700, 5],
    ['Cape Town', 'The Cape Milner', 'Mid‑range', 2600, 4],
    ['Cape Town', 'City Lodge V&A Waterfront', 'Mid‑range', 2300, 4],
    ['Cape Town', 'Cloud 9 Boutique Hotel', 'Budget', 1500, 3],

    # Durban
    ['Durban', 'Southern Sun Elangeni & Maharani', 'Luxury', 3400, 5],
    ['Durban', 'The Oyster Box (Umhlanga)', 'Luxury', 4500, 5],
    ['Durban', 'Protea Hotel Umhlanga Ridge', 'Mid‑range', 2400, 4],
    ['Durban', 'Garden Court South Beach', 'Mid‑range', 2100, 4],
    ['Durban', 'City Lodge Hotel Umhlanga Ridge', 'Budget', 1600, 3],

    # Pretoria
    ['Pretoria', 'Sheraton Pretoria Hotel', 'Luxury', 3600, 5],
    ['Pretoria', 'The Capital Menlyn Maine', 'Mid‑range', 2500, 4],
    ['Pretoria', 'City Lodge Hotel Lynnwood', 'Mid‑range', 2300, 4],
    ['Pretoria', 'Protea Hotel Hatfield', 'Budget', 1800, 3],
    ['Pretoria', 'Apogee Boutique Hotel & Spa', 'Luxury', 3800, 5],

    # Port Elizabeth
    ['Port Elizabeth', 'No5 Boutique Hotel By Mantis', 'Luxury', 3300, 5],
    ['Port Elizabeth', 'Radisson Blu Hotel PE', 'Luxury', 3100, 5],
    ['Port Elizabeth', 'Protea Hotel Port Elizabeth', 'Mid‑range', 2300, 4],
    ['Port Elizabeth', 'The Boardwalk Hotel', 'Mid‑range', 2400, 4],
    ['Port Elizabeth', 'Beachview Guesthouse', 'Budget', 1600, 3],
],
columns=['Location', 'Hotel', 'Room Type', 'Price per Night (ZAR)', 'Rating'])

# ------------------ MOCK DATA (Buses) ------------------
buses = pd.DataFrame([
    ['Johannesburg to Cape Town', '08:00', 16, 800, 20],
    ['Cape Town to Durban', '09:30', 20, 950, 15],
    ['Durban to Pretoria', '12:00', 12, 700, 0],
    ['Pretoria to Port Elizabeth', '14:00', 14, 850, 10],
],
columns=['Route', 'Departure Time', 'Duration (hours)', 'Price per Seat (ZAR)', 'Seats Available'])

# ------------------ TITLE AND NAVIGATION ------------------
st.title("🚌🏨 South Africa Booking System")
page = st.sidebar.selectbox("Choose a section", ["Accommodations", "Buses"])

# ------------------ ACCOMMODATION BOOKING ------------------
if page == "Accommodations":
    st.header("🏨 Book Accommodation in South Africa")
    st.markdown('<div class="card">', unsafe_allow_html=True)

    # User input
    name = st.text_input("Full Name")
    location = st.selectbox("Select City", accommodations['Location'].unique())
    check_in = st.date_input("Check-in Date", min_value=date.today())
    check_out = st.date_input("Check-out Date", min_value=check_in)
    guests = st.number_input("Number of Guests", min_value=1, max_value=10, value=1)

    # Filter available accommodations
    available_accom = accommodations[
        (accommodations['Location'] == location)
    ]

    if not available_accom.empty:
        # Display hotels with ratings
        available_accom_display = available_accom.copy()
        available_accom_display['Rating'] = available_accom_display['Rating'].apply(lambda x: '⭐'*x)
        st.subheader("Available Hotels")
        st.dataframe(available_accom_display, use_container_width=True)

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
                ]['Price per Night (ZAR)'].values[0]

                total_price = price * nights

                booking = pd.DataFrame([{
                    "Name": name,
                    "Hotel": selected_hotel,
                    "City": location,
                    "Guests": guests,
                    "Check-in": check_in,
                    "Check-out": check_out,
                    "Total Price (ZAR)": total_price
                }])

                # Save to CSV
                booking.to_csv(
                    "accommodation_bookings.csv",
                    mode="a",
                    header=not pd.io.common.file_exists("accommodation_bookings.csv"),
                    index=False
                )

                st.success("✅ Accommodation booking confirmed!")
                st.write(booking)
    else:
        st.warning("No hotels available in this city.")

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ BUS BOOKING ------------------
elif page == "Buses":
    st.header("🚌 Book Bus Tickets in South Africa")
    st.markdown('<div class="card">', unsafe_allow_html=True)

    # User input
    name = st.text_input("Full Name")
    route = st.selectbox("Select Route", buses['Route'].unique())
    travel_date = st.date_input("Travel Date", min_value=date.today())
    passengers = st.number_input("Number of Passengers", min_value=1, max_value=10, value=1)

    # Filter available buses
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
                ]['Price per Seat (ZAR)'].values[0]

                total_price = price * passengers

                booking = pd.DataFrame([{
                    "Name": name,
                    "Route": route,
                    "Departure Time": selected_time,
                    "Travel Date": travel_date,
                    "Passengers": passengers,
                    "Total Price (ZAR)": total_price
                }])

                # Save to CSV
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

    st.markdown('</div>', unsafe_allow_html=True)
