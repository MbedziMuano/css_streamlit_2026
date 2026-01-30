import streamlit as st
import pandas as pd
from datetime import date

# ------------------ HELPER FUNCTION ------------------
def clean_image_urls(urls):
    """Remove whitespace and keep only valid image URLs"""
    clean_urls = []
    for url in urls:
        if isinstance(url, str):
            url = url.strip()
            if url.startswith("http"):
                clean_urls.append(url)
    return clean_urls


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

# ------------------ ACCOMMODATION DATA ------------------
accommodations = pd.DataFrame([
    ['Johannesburg', 'Hilton Sandton', 'Luxury', 4200, 5,
     [
      'https://s.inyourpocket.com/gallery/johannesburg/2023/05/IMG-8667%20(1).jpg',
      'https://s.inyourpocket.com/img/text/southafrica/johannesburg/hilton-sandton-jnbsa_sandton_-lobby.jpg',
      'https://pix10.agoda.net/hotelImages/791/79114/79114_13112217530017730425.jpg?s=1024x768.jpg',
      'https://www.yoninja.com/wp-content/uploads/2014/04/Hilton-Sandton-Swimming-Pool.jpg',
      'https://www.restaurants.co.za/images/gallery/full/tradewinds_restaurant_12.jpg'
     ]],
], columns=['Location','Hotel','Room Type','Price per Night (ZAR)','Rating','Image URLs'])

# ------------------ BUS ROUTES ------------------
buses = pd.DataFrame([
    ['Johannesburg to Cape Town', '08:00', 16, 800, 20],
    ['Cape Town to Durban', '09:30', 20, 950, 15],
    ['Durban to Pretoria', '12:00', 12, 700, 0],
    ['Pretoria to Port Elizabeth', '14:00', 14, 850, 10]
], columns=['Route','Departure Time','Duration (hours)','Price per Seat (ZAR)','Seats Available'])

# ------------------ APP ------------------
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

        for _, row in available_accom.iterrows():
            st.markdown(
                f"**{row['Hotel']} ({row['Room Type']})** — "
                f"{row['Price per Night (ZAR)']} ZAR — {'⭐'*row['Rating']}"
            )

            clean_urls = clean_image_urls(row['Image URLs'])

            if clean_urls:
                st.image(
                    clean_urls,
                    width=250,
                    caption=["Exterior", "Lobby", "Room", "Pool", "Restaurant"][:len(clean_urls)]
                )
            else:
                st.warning("Images unavailable for this hotel.")

            st.markdown("---")

        selected_hotel = st.selectbox("Select Hotel", available_accom['Hotel'])

        if st.button("Confirm Accommodation Booking"):
            nights = (check_out - check_in).days

            if not name:
                st.error("Please enter your name.")
            elif nights <= 0:
                st.error("Check-out must be after check-in.")
            else:
                price = available_accom.loc[
                    available_accom['Hotel'] == selected_hotel,
                    'Price per Night (ZAR)'
                ].values[0]

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

                booking.to_csv(
                    "accommodation_bookings.csv",
                    mode="a",
                    index=False,
                    header=not pd.io.common.file_exists("accommodation_bookings.csv")
                )

                st.success("✅ Accommodation booking confirmed!")
                st.write(booking)

    else:
        st.warning("No hotels available in this city.")

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ BUS BOOKING ------------------
elif page == "Buses":
    st.header("🚌 Book Bus Tickets")
    st.markdown('<div class="card">', unsafe_allow_html=True)

    name = st.text_input("Full Name")
    route = st.selectbox("Select Route", buses['Route'].unique())
    travel_date = st.date_input("Travel Date", min_value=date.today())
    passengers = st.number_input("Number of Passengers", min_value=1, max_value=10, value=1)

    available_buses = buses[
        (buses['Route'] == route) &
        (buses['Seats Available'] >= passengers)
    ]

    if not available_buses.empty:
        st.dataframe(available_buses, use_container_width=True)
        selected_time = st.selectbox("Select Departure Time", available_buses['Departure Time'])

        if st.button("Confirm Bus Booking"):
            if not name:
                st.error("Please enter your name.")
            else:
                price = available_buses.loc[
                    available_buses['Departure Time'] == selected_time,
                    'Price per Seat (ZAR)'
                ].values[0]

                total_price = price * passengers

                booking = pd.DataFrame([{
                    "Name": name,
                    "Route": route,
                    "Departure Time": selected_time,
                    "Travel Date": travel_date,
                    "Passengers": passengers,
                    "Total Price (ZAR)": total_price
                }])

                booking.to_csv(
                    "bus_bookings.csv",
                    mode="a",
                    index=False,
                    header=not pd.io.common.file_exists("bus_bookings.csv")
                )

                st.success("✅ Bus booking confirmed!")
                st.write(booking)
    else:
        st.warning("No buses available or insufficient seats.")

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ CANCEL BOOKING ------------------
elif page == "Cancel Booking":
    st.header("❌ Cancel Booking")
    booking_type = st.radio("Select Booking Type", ["Accommodation", "Bus"])

    try:
        if booking_type == "Accommodation":
            df = pd.read_csv("accommodation_bookings.csv")
            selected_name = st.selectbox("Select Your Name", df["Name"].unique())
            user_bookings = df[df["Name"] == selected_name]
            st.write(user_bookings)

            to_cancel = st.selectbox("Select Hotel to Cancel", user_bookings["Hotel"])
            if st.button("Cancel Accommodation Booking"):
                df = df.drop(user_bookings[user_bookings["Hotel"] == to_cancel].index)
                df.to_csv("accommodation_bookings.csv", index=False)
                st.success("✅ Booking cancelled successfully!")

        else:
            df = pd.read_csv("bus_bookings.csv")
            selected_name = st.selectbox("Select Your Name", df["Name"].unique())
            user_bookings = df[df["Name"] == selected_name]
            st.write(user_bookings)

            to_cancel = st.selectbox("Select Route to Cancel", user_bookings["Route"])
            if st.button("Cancel Bus Booking"):
                df = df.drop(user_bookings[user_bookings["Route"] == to_cancel].index)
                df.to_csv("bus_bookings.csv", index=False)
                st.success("✅ Booking cancelled successfully!")

    except FileNotFoundError:
        st.warning("No bookings found.")