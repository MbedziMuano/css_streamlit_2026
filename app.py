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
      'https://cloud9hotel.co.za/images/restaurant.jpg']],

    # Durban
    ['Durban', 'The Oyster Box', 'Luxury', 4500, 5,
     [
    'https://www.chaloafrica.com/wp-content/uploads/2018/05/The-Oyster-Box-View.jpg',
    'https://tse4.mm.bing.net/th/id/OIP.ILjDIVvyUffOT6aeTtsVUwHaE7?rs=1&pid=ImgDetMain&o=7&rm=3',
    'https://tse4.mm.bing.net/th/id/OIP.WdZdyqVrTAUhf242K858TQHaE5?rs=1&pid=ImgDetMain&o=7&rm=3',
    'https://cdn.rhinoafrica.com/tmp/image-thumbnails/objects/service-providers/the-oyster-box-hotel/_img/image-thumb__34638__background-cover/the-oyster-box-hotel-facilities-pool-09.jpg',
    'https://th.bing.com/th/id/R.0a85cf886f77a56dfcf9dff73804cf68?rik=YlJaZdAoq84a%2bg&pid=ImgRaw&r=0'
]],

    ['Durban', 'Southern Sun Elangeni', 'Luxury', 3400, 5,
     ['https://www.tsogosun.com/media/2850/southern-sun-elangeni.jpg',
      'https://www.tsogosun.com/media/2851/southern-sun-lobby.jpg',
      'https://www.tsogosun.com/media/2852/southern-sun-room.jpg',
      'https://www.tsogosun.com/media/2853/southern-sun-pool.jpg',
      'https://www.tsogosun.com/media/2854/southern-sun-restaurant.jpg']],

    ['Durban', 'Protea Hotel Umhlanga Ridge', 'Mid‑range', 2400, 4,
     ['https://www.marriott.com/protea-umhlanga.jpg',
      'https://www.marriott.com/protea-umhlanga-lobby.jpg',
      'https://www.marriott.com/protea-umhlanga-room.jpg',
      'https://www.marriott.com/protea-umhlanga-pool.jpg',
      'https://www.marriott.com/protea-umhlanga-restaurant.jpg']],

    ['Durban', 'Garden Court South Beach', 'Mid‑range', 2100, 4,
     ['https://www.tsogosun.com/media/2810/garden-court-south-beach.jpg',
      'https://www.tsogosun.com/media/2811/lobby.jpg',
      'https://www.tsogosun.com/media/2812/room.jpg',
      'https://www.tsogosun.com/media/2813/pool.jpg',
      'https://www.tsogosun.com/media/2814/restaurant.jpg']],

    ['Durban', 'City Lodge Hotel Umhlanga Ridge', 'Budget', 1600, 3,
     ['https://www.citylodge.co.za/images/umhlanga.jpg',
      'https://www.citylodge.co.za/images/lobby.jpg',
      'https://www.citylodge.co.za/images/room.jpg',
      'https://www.citylodge.co.za/images/pool.jpg',
      'https://www.citylodge.co.za/images/restaurant.jpg']],

    # Pretoria
    ['Pretoria', 'Sheraton Pretoria Hotel', 'Luxury', 3600, 5,
     ['https://www.marriott.com/sheraton-pretoria.jpg',
      'https://www.marriott.com/sheraton-pretoria-lobby.jpg',
      'https://www.marriott.com/sheraton-pretoria-room.jpg',
      'https://www.marriott.com/sheraton-pretoria-pool.jpg',
      'https://www.marriott.com/sheraton-pretoria-restaurant.jpg']],

    ['Pretoria', 'The Capital Menlyn', 'Mid‑range', 2500, 4,
     ['https://www.capitalhotels.co.za/images/menlyn.jpg',
      'https://www.capitalhotels.co.za/images/lobby.jpg',
      'https://www.capitalhotels.co.za/images/room.jpg',
      'https://www.capitalhotels.co.za/images/pool.jpg',
      'https://www.capitalhotels.co.za/images/restaurant.jpg']],

    ['Pretoria', 'City Lodge Lynnwood', 'Mid‑range', 2300, 4,
     ['https://www.citylodge.co.za/images/lynnwood.jpg',
      'https://www.citylodge.co.za/images/lobby.jpg',
      'https://www.citylodge.co.za/images/room.jpg',
      'https://www.citylodge.co.za/images/pool.jpg',
      'https://www.citylodge.co.za/images/restaurant.jpg']],

    ['Pretoria', 'Protea Hatfield', 'Budget', 1800, 3,
     ['https://www.marriott.com/protea-hatfield.jpg',
      'https://www.marriott.com/protea-hatfield-lobby.jpg',
      'https://www.marriott.com/protea-hatfield-room.jpg',
      'https://www.marriott.com/protea-hatfield-pool.jpg',
      'https://www.marriott.com/protea-hatfield-restaurant.jpg']],

    ['Pretoria', 'Apogee Boutique Hotel & Spa', 'Luxury', 3800, 5,
     ['https://www.apogeehotel.co.za/images/hotel.jpg',
      'https://www.apogeehotel.co.za/images/lobby.jpg',
      'https://www.apogeehotel.co.za/images/room.jpg',
      'https://www.apogeehotel.co.za/images/pool.jpg',
      'https://www.apogeehotel.co.za/images/restaurant.jpg']],

    # Port Elizabeth
    ['Port Elizabeth', 'No5 Boutique Hotel By Mantis', 'Luxury', 3300, 5,
     ['https://www.mantiscollection.com/no5-boutique-hotel.jpg',
      'https://www.mantiscollection.com/no5-lobby.jpg',
      'https://www.mantiscollection.com/no5-room.jpg',
      'https://www.mantiscollection.com/no5-pool.jpg',
      'https://www.mantiscollection.com/no5-restaurant.jpg']],

    ['Port Elizabeth', 'Radisson Blu Hotel PE', 'Luxury', 3100, 5,
     ['https://www.radissonhotels.com/pe-radisson.jpg',
      'https://www.radissonhotels.com/pe-lobby.jpg',
      'https://www.radissonhotels.com/pe-room.jpg',
      'https://www.radissonhotels.com/pe-pool.jpg',
      'https://www.radissonhotels.com/pe-restaurant.jpg']],

    ['Port Elizabeth', 'Protea PE', 'Mid‑range', 2300, 4,
     ['https://www.marriott.com/protea-pe.jpg',
      'https://www.marriott.com/protea-pe-lobby.jpg',
      'https://www.marriott.com/protea-pe-room.jpg',
      'https://www.marriott.com/protea-pe-pool.jpg',
      'https://www.marriott.com/protea-pe-restaurant.jpg']],

    ['Port Elizabeth', 'The Boardwalk Hotel', 'Mid‑range', 2400, 4,
     ['https://www.theboardwalk.co.za/images/hotel.jpg',
      'https://www.theboardwalk.co.za/images/lobby.jpg',
      'https://www.theboardwalk.co.za/images/room.jpg',
      'https://www.theboardwalk.co.za/images/pool.jpg',
      'https://www.theboardwalk.co.za/images/restaurant.jpg']],

    ['Port Elizabeth', 'Beachview Guesthouse', 'Budget', 1600, 3,
     ['https://www.beachviewguesthouse.co.za/images/guesthouse.jpg',
      'https://www.beachviewguesthouse.co.za/images/lobby.jpg',
      'https://www.beachviewguesthouse.co.za/images/room.jpg',
      'https://www.beachviewguesthouse.co.za/images/pool.jpg',
      'https://www.beachviewguesthouse.co.za/images/restaurant.jpg']]
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

    available_accom = accommodations[accommodations['Location']==location]
    if not available_accom.empty:
        st.subheader("Available Hotels")
        for idx, row in available_accom.iterrows():
            st.markdown(f"**{row['Hotel']} ({row['Room Type']})** - {row['Price per Night (ZAR)']} ZAR - {'⭐'*row['Rating']}")
            st.image(row['Image URLs'], width=250, caption=['Exterior','Lobby','Room','Pool','Restaurant'])
            st.markdown("---")

        selected_hotel = st.selectbox("Select Hotel", available_accom['Hotel'])

        if st.button("Confirm Accommodation Booking"):
            nights = (check_out - check_in).days
            if not name: st.error("Please enter your name.")
            elif nights <= 0: st.error("Check-out must be after check-in.")
            else:
                price = available_accom[available_accom['Hotel']==selected_hotel]['Price per Night (ZAR)'].values[0]
                total_price = price * nights
                booking = pd.DataFrame([{
                    "Name": name, "Hotel": selected_hotel, "City": location,
                    "Guests": guests, "Check-in": check_in, "Check-out": check_out,
                    "Total Price (ZAR)": total_price
                }])
                booking.to_csv("accommodation_bookings.csv", mode="a", index=False, header=not pd.io.common.file_exists("accommodation_bookings.csv"))
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

    available_buses = buses[(buses['Route']==route) & (buses['Seats Available']>=passengers)]
    if not available_buses.empty:
        st.subheader("Available Buses")
        st.dataframe(available_buses, use_container_width=True)
        selected_time = st.selectbox("Select Departure Time", available_buses['Departure Time'])
        if st.button("Confirm Bus Booking"):
            if not name: st.error("Please enter your name.")
            else:
                price = available_buses[available_buses['Departure Time']==selected_time]['Price per Seat (ZAR)'].values[0]
                total_price = price * passengers
                booking = pd.DataFrame([{
                    "Name": name, "Route": route, "Departure Time": selected_time,
                    "Travel Date": travel_date, "Passengers": passengers, "Total Price (ZAR)": total_price
                }])
                booking.to_csv("bus_bookings.csv", mode="a", index=False, header=not pd.io.common.file_exists("bus_bookings.csv"))
                st.success("✅ Bus booking confirmed!")
                st.write(booking)
    else:
        st.warning("No buses available or insufficient seats.")
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ CANCEL BOOKING ------------------
elif page == "Cancel Booking":
    st.header("❌ Cancel Booking")
    booking_type = st.radio("Select Booking Type", ["Accommodation", "Bus"])

    if booking_type == "Accommodation":
        try:
            df = pd.read_csv("accommodation_bookings.csv")
            if df.empty: st.warning("No accommodation bookings found.")
            else:
                selected_name = st.selectbox("Select Your Name", df["Name"].unique())
                user_bookings = df[df["Name"]==selected_name]
                st.write(user_bookings)
                to_cancel = st.selectbox("Select Hotel to Cancel", user_bookings["Hotel"])
                if st.button("Cancel Accommodation Booking"):
                    df = df.drop(user_bookings[user_bookings["Hotel"]==to_cancel].index)
                    df.to_csv("accommodation_bookings.csv", index=False)
                    st.success(f"✅ Booking for {to_cancel} cancelled successfully!")
        except FileNotFoundError:
            st.warning("No accommodation bookings file found.")

    else:
        try:
            df = pd.read_csv("bus_bookings.csv")
            if df.empty: st.warning("No bus bookings found.")
            else:
                selected_name = st.selectbox("Select Your Name", df["Name"].unique())
                user_bookings = df[df["Name"]==selected_name]
                st.write(user_bookings)
                to_cancel = st.selectbox("Select Route to Cancel", user_bookings["Route"])
                if st.button("Cancel Bus Booking"):
                    df = df.drop(user_bookings[user_bookings["Route"]==to_cancel].index)
                    df.to_csv("bus_bookings.csv", index=False)
                    st.success(f"✅ Booking for {to_cancel} cancelled successfully!")
        except FileNotFoundError:
            st.warning("No bus bookings file found.")