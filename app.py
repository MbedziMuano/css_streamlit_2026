import streamlit as st
import pandas as pd
from datetime import date

# ------------------ CSS Styling ------------------
st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #e3f2fd, #fce4ec); }
h1 { color: #0d47a1; text-align: center; }
h2, h3 { color: #1a237e; }
[data-testid="stSidebar"] { background-color: #263238; }
[data-testid="stSidebar"] * { color: white; }
.card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0px 4px 15px rgba(0,0,0,0.15); margin-bottom: 20px; }
.stButton>button { background-color: #1976d2; color: white; border-radius: 10px; height: 3em; font-size: 16px; font-weight: bold; }
.stButton>button:hover { background-color: #0d47a1; color: #ffffff; }
.stAlert.success { background-color: #e8f5e9; color: #1b5e20; }
.stAlert.warning { background-color: #fff3e0; color: #e65100; }
</style>
""", unsafe_allow_html=True)

# ------------------ Hotels Data ------------------
accommodations = pd.DataFrame([
    # Johannesburg
    ['Johannesburg', 'Hilton Sandton', 'Luxury', 4200, 5,
     ['https://www.hilton.com/imageresizer?imageUrl=https://assets.hilton.com/hilton_exterior.jpg',
      'https://www.hilton.com/imageresizer?imageUrl=https://assets.hilton.com/hilton_lobby.jpg',
      'https://www.hilton.com/imageresizer?imageUrl=https://assets.hilton.com/hilton_room.jpg',
      'https://www.hilton.com/imageresizer?imageUrl=https://assets.hilton.com/hilton_pool.jpg',
      'https://www.hilton.com/imageresizer?imageUrl=https://assets.hilton.com/hilton_restaurant.jpg']],
    ['Johannesburg', 'Palazzo Hotel Montecasino', 'Luxury', 3800, 5,
     ['https://www.tsogosun.com/media/2970/palazzo-exterior-2.jpg',
      'https://www.tsogosun.com/media/2971/palazzo-lobby.jpg',
      'https://www.tsogosun.com/media/2972/palazzo-room.jpg',
      'https://www.tsogosun.com/media/2973/palazzo-pool.jpg',
      'https://www.tsogosun.com/media/2974/palazzo-restaurant.jpg']],
    ['Johannesburg', 'Southern Sun Rosebank', 'Mid‑range', 2500, 4,
     ['https://www.tsogosun.com/media/2849/southern-sun-rosebank.jpg',
      'https://www.tsogosun.com/media/2850/southern-sun-lobby.jpg',
      'https://www.tsogosun.com/media/2851/southern-sun-room.jpg',
      'https://www.tsogosun.com/media/2852/southern-sun-pool.jpg',
      'https://www.tsogosun.com/media/2853/southern-sun-restaurant.jpg']],
    ['Johannesburg', 'Radisson Blu Sandton', 'Mid‑range', 2700, 4,
     ['https://www.radissonhotels.com/en-us/images/sandton-radisson-blu.jpg',
      'https://www.radissonhotels.com/en-us/images/sandton-lobby.jpg',
      'https://www.radissonhotels.com/en-us/images/sandton-room.jpg',
      'https://www.radissonhotels.com/en-us/images/sandton-pool.jpg',
      'https://www.radissonhotels.com/en-us/images/sandton-restaurant.jpg']],
    ['Johannesburg', 'Mint Hotel Rosebank', 'Budget', 1800, 3,
     ['https://www.mintrosebank.co.za/assets/images/mint-hotel.jpg',
      'https://www.mintrosebank.co.za/assets/images/lobby.jpg',
      'https://www.mintrosebank.co.za/assets/images/room.jpg',
      'https://www.mintrosebank.co.za/assets/images/pool.jpg',
      'https://www.mintrosebank.co.za/assets/images/restaurant.jpg']],

    # Cape Town
    ['Cape Town', 'Belmond Mount Nelson', 'Luxury', 5000, 5,
     ['https://www.belmond.com/images/hotels/africa/cape-town/belmond-mount-nelson-hotel/exterior.jpg',
      'https://www.belmond.com/images/hotels/africa/cape-town/belmond-mount-nelson-hotel/lobby.jpg',
      'https://www.belmond.com/images/hotels/africa/cape-town/belmond-mount-nelson-hotel/room.jpg',
      'https://www.belmond.com/images/hotels/africa/cape-town/belmond-mount-nelson-hotel/pool.jpg',
      'https://www.belmond.com/images/hotels/africa/cape-town/belmond-mount-nelson-hotel/restaurant.jpg']],
    ['Cape Town', 'Hyatt Regency Cape Town', 'Luxury', 4700, 5,
     ['https://www.hyatt.com/content/dam/hyatt/hyattdam/images/2019/08/02/1028/Hyatt-Cape-Town.jpg',
      'https://www.hyatt.com/content/dam/hyatt/hyatt-lobby.jpg',
      'https://www.hyatt.com/content/dam/hyatt/hyatt-room.jpg',
      'https://www.hyatt.com/content/dam/hyatt/hyatt-pool.jpg',
      'https://www.hyatt.com/content/dam/hyatt/hyatt-restaurant.jpg']],
    ['Cape Town', 'The Cape Milner', 'Mid‑range', 2600, 4,
     ['https://www.thecapemilner.co.za/images/hotel.jpg',
      'https://www.thecapemilner.co.za/images/lobby.jpg',
      'https://www.thecapemilner.co.za/images/room.jpg',
      'https://www.thecapemilner.co.za/images/pool.jpg',
      'https://www.thecapemilner.co.za/images/restaurant.jpg']],
    ['Cape Town', 'City Lodge V&A Waterfront', 'Mid‑range', 2300, 4,
     ['https://www.citylodge.co.za/images/vawaterfront.jpg',
      'https://www.citylodge.co.za/images/lobby.jpg',
      'https://www.citylodge.co.za/images/room.jpg',
      'https://www.citylodge.co.za/images/pool.jpg',
      'https://www.citylodge.co.za/images/restaurant.jpg']],
    ['Cape Town', 'Cloud 9 Boutique Hotel', 'Budget', 1500, 3,
     ['https://cloud9hotel.co.za/images/cloud9.jpg',
      'https://cloud9hotel.co.za/images/lobby.jpg',
      'https://cloud9hotel.co.za/images/room.jpg',
      'https://cloud9hotel.co.za/images/pool.jpg',
      'https://cloud9hotel.co.za/images/restaurant.jpg']]
], columns=['Location','Hotel','Room Type','Price per Night (ZAR)','Rating','Image URLs'])

# ------------------ Bus Routes ------------------
buses = pd.DataFrame([
    ['Johannesburg to Cape Town', '08:00', 16, 800, 20],
    ['Cape Town to Durban', '09:30', 20, 950, 15],
    ['Durban to Pretoria', '12:00', 12, 700, 0],
    ['Pretoria to Port Elizabeth', '14:00', 14, 850, 10]
], columns=['Route','Departure Time','Duration (hours)','Price per Seat (ZAR)','Seats Available'])

# ------------------ Booking Section ------------------
st.title("🚌🏨 South Africa Booking System")
page = st.sidebar.selectbox("Choose a section", ["Accommodations", "Buses", "Cancel Booking"])

# For simplicity, we store current bookings in session state
if 'accom_booking' not in st.session_state: st.session_state.accom_booking = None
if 'bus_booking' not in st.session_state: st.session_state.bus_booking = None

# ------------------ Accommodation Booking ------------------
if page == "Accommodations":
    st.header("Book Accommodations")
    location = st.selectbox("Select City", accommodations['Location'].unique())
    check_in = st.date_input("Check-in Date", min_value=date.today())
    check_out = st.date_input("Check-out Date", min_value=check_in)
    guests = st.number_input("Number of Guests", min_value=1, max_value=10, value=1)
    
    available_accom = accommodations[accommodations['Location'] == location]
    
    if not available_accom.empty:
        st.subheader("Available Hotels")
        for idx, hotel in available_accom.iterrows():
            with st.container():
                st.markdown(f"### {hotel['Hotel']} ({hotel['Room Type']})")
                st.markdown(f"**Rating:** {'⭐'*hotel['Rating']}  | **Price/Night:** R{hotel['Price per Night (ZAR)']}")
                cols = st.columns(5)
                for i, col in enumerate(cols):
                    col.image(hotel['Image URLs'][i], use_column_width=True)
                if st.button(f"Book {hotel['Hotel']}"):
                    nights = (check_out - check_in).days
                    total_price = hotel['Price per Night (ZAR)'] * nights
                    st.session_state.accom_booking = {
                        'Hotel': hotel['Hotel'], 'City': location, 'Nights': nights, 'Guests': guests, 'Total': total_price
                    }
                    st.success(f"Booked {hotel['Hotel']} in {location} for {nights} nights. Total: R{total_price}")
    else:
        st.warning("No hotels available in this city.")

# ------------------ Bus Booking ------------------
elif page == "Buses":
    st.header("Book Bus Tickets")
    route = st.selectbox("Select Route", buses['Route'].unique())
    travel_date = st.date_input("Travel Date", min_value=date.today())
    passengers = st.number_input("Number of Passengers", min_value=1, max_value=10, value=1)
    
    available_buses = buses[(buses['Route'] == route) & (buses['Seats Available'] >= passengers)]
    
    if not available_buses.empty:
        st.subheader("Available Buses")
        for idx, bus in available_buses.iterrows():
            st.markdown(f"**Route:** {bus['Route']} | **Departure:** {bus['Departure Time']} | **Duration:** {bus['Duration (hours)']}h | **Price/Seat:** R{bus['Price per Seat (ZAR)']} | Seats: {bus['Seats Available']}")
            if st.button(f"Book {bus['Route']} at {bus['Departure Time']}"):
                total_price = bus['Price per Seat (ZAR)'] * passengers
                st.session_state.bus_booking = {'Route': bus['Route'], 'Departure': bus['Departure Time'], 'Passengers': passengers, 'Total': total_price, 'Date': travel_date}
                st.success(f"Booked {passengers} seat(s) on {bus['Route']} at {bus['Departure Time']}. Total: R{total_price}")
    else:
        st.warning("No buses available for this route or insufficient seats.")

# ------------------ Cancel Booking ------------------
elif page == "Cancel Booking":
    st.header("❌ Cancel Booking")
    if st.session_state.accom_booking or st.session_state.bus_booking:
        if st.session_state.accom_booking:
            st.markdown(f"**Hotel Booking:** {st.session_state.accom_booking['Hotel']} in {st.session_state.accom_booking['City']} | Total: R{st.session_state.accom_booking['Total']}")
            if st.button("Cancel Accommodation Booking"):
                st.session_state.accom_booking = None
                st.success("Accommodation booking cancelled!")
        if st.session_state.bus_booking:
            st.markdown(f"**Bus Booking:** {st.session_state.bus_booking['Route']} at {st.session_state.bus_booking['Departure']} | Seats: {st.session_state.bus_booking['Passengers']} | Total: R{st.session_state.bus_booking['Total']}")
            if st.button("Cancel Bus Booking"):
                st.session_state.bus_booking = None
                st.success("Bus booking cancelled!")
    else:
        st.warning("No bookings to cancel.")
            st.warning("No bus bookings file found.")