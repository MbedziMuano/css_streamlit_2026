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

# ------------------ Hotels with 5 Images ------------------
accommodations = pd.DataFrame([
    # Example hotel entry (repeat for all your hotels)
    ['Johannesburg', 'Hilton Sandton', 'Luxury', 4200, 5,
     ['https://www.hilton.com/imageresizer?imageUrl=https://assets.hilton.com/hilton_exterior.jpg',
      'https://www.hilton.com/imageresizer?imageUrl=https://assets.hilton.com/hilton_lobby.jpg',
      'https://www.hilton.com/imageresizer?imageUrl=https://assets.hilton.com/hilton_room.jpg',
      'https://www.hilton.com/imageresizer?imageUrl=https://assets.hilton.com/hilton_pool.jpg',
      'https://www.hilton.com/imageresizer?imageUrl=https://assets.hilton.com/hilton_restaurant.jpg']]
], columns=['Location','Hotel','Room Type','Price per Night (ZAR)','Rating','Image URLs'])

# ------------------ Bus Routes ------------------
buses = pd.DataFrame([
    ['Johannesburg to Cape Town', '08:00', 16, 800, 20],
    ['Cape Town to Durban', '09:30', 20, 950, 15],
    ['Durban to Pretoria', '12:00', 12, 700, 0],
    ['Pretoria to Port Elizabeth', '14:00', 14, 850, 10]
], columns=['Route','Departure Time','Duration (hours)','Price per Seat (ZAR)','Seats Available'])

# ------------------ App ------------------
st.title("🚌🏨 South Africa Booking System")
page = st.sidebar.selectbox("Choose a section", ["Accommodations", "Buses", "Cancel Booking"])

# ------------------ ACCOMMODATION BOOKING ------------------
if page == "Accommodations":
    st.header("🏨 Book Accommodation")
    st.markdown('<div class="card">', unsafe_allow_html=True)

    name = st.text_input("Full Name")
    location = st.selectbox("Select City", accommodations['Location'].unique())
    check_in = st.date_input("Check-in Date", min_value=date.today())
    check_out = st.date_input("Check-out Date", min_value=check_in)
    guests = st.number_input("Number of Guests", min_value=1, max_value=10, value=1)

    available_accom = accommodations[accommodations['Location'] == location]
    if not available_accom.empty:
        st.subheader("Available Hotels")

        for idx, row in available_accom.iterrows():
            st.markdown(f"**{row['Hotel']} ({row['Room Type']})** - {row['Price per Night (ZAR)']} ZAR - {'⭐'*row['Rating']}")

            # Initialize session state for image index if not exists
            if f"img_idx_{idx}" not in st.session_state:
                st.session_state[f"img_idx_{idx}"] = 0

            # Display the current image
            captions = ['Exterior','Lobby','Room','Pool','Restaurant']
            st.image(row['Image URLs'][st.session_state[f"img_idx_{idx}"]], width=400,
                     caption=captions[st.session_state[f"img_idx_{idx}"]])

            # Previous/Next buttons
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Previous", key=f"prev_{idx}"):
                    if st.session_state[f"img_idx_{idx}"] > 0:
                        st.session_state[f"img_idx_{idx}"] -= 1
            with col2:
                if st.button("Next", key=f"next_{idx}"):
                    if st.session_state[f"img_idx_{idx}"] < len(row['Image URLs']) - 1:
                        st.session_state[f"img_idx_{idx}"] += 1

            st.markdown("---")

        selected_hotel = st.selectbox("Select Hotel", available_accom['Hotel'])

        if st.button("Confirm Accommodation Booking"):
            nights = (check_out - check_in).days
            if not name:
                st.error("Please enter your name.")
            elif nights <= 0:
                st.error("Check-out must be after check-in.")
            else:
                price = available_accom[available_accom['Hotel'] == selected_hotel]['Price per Night (ZAR)'].values[0]
                total_price = price * nights
                booking = pd.DataFrame([{
                    "Name": name, "Hotel": selected_hotel, "City": location,
                    "Guests": guests, "Check-in": check_in, "Check-out": check_out,
                    "Total Price (ZAR)": total_price
                }])
                booking.to_csv("accommodation_bookings.csv", mode="a", index=False,
                               header=not pd.io.common.file_exists("accommodation_bookings.csv"))
                st.success("✅ Accommodation booking confirmed!")
                st.write(booking)
    else:
        st.warning("No hotels available in this city.")
    st.markdown('</div>', unsafe_allow_html=True)