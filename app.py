import streamlit as st
import pandas as pd
from datetime import date

# ------------------ CSS ------------------
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

# ------------------ Hotels ------------------
accommodations = pd.DataFrame([
    # Johannesburg
    ['Johannesburg', 'Hilton Sandton', 'Luxury', 4200, 5, 'https://tse2.mm.bing.net/th/id/OIP.IhjfnDBzTIlzSxvxvZ1LpQHaER?rs=1&pid=ImgDetMain&o=7&rm=3'],
    ['Johannesburg', 'Palazzo Hotel Montecasino', 'Luxury', 3800, 5, 'https://www.olielo.com/wp-content/uploads/2014/01/Palazzo-Montecasino-Johannesburg.jpg'],
    ['Johannesburg', 'Southern Sun Rosebank', 'Mid‑range', 2500, 4, 'https://cf.bstatic.com/xdata/images/hotel/max1024x768/434263028.jpg?k=6e4dbf1eebcf9c2b22a01f0e2b360d390fdabe06105de31a8da5814228cc3387&o=&hp=1'],
    ['Johannesburg', 'Radisson Blu Sandton', 'Mid‑range', 2700, 4, 'https://whatson.gauteng.net/wp-content/uploads/2025/06/radisson-blu-hotel-sandton-johannesburg-review-luxury-and-comfort-in-the-heart-of-sandton-1750709939-1024x576.png'],
    ['Johannesburg', 'Mint Hotel Rosebank', 'Budget', 1800, 3, 'https://profitroom-uploads.fra1.digitaloceanspaces.com/minthotels/500x500/1709203419979_mintexpressmelroseviewexterior.jpg'],

    # Cape Town
    ['Cape Town', 'Belmond Mount Nelson', 'Luxury', 5000, 5, 'https://www.belmond.com/images/hotels/africa/cape-town/belmond-mount-nelson-hotel/exterior.jpg'],
    ['Cape Town', 'Hyatt Regency Cape Town', 'Luxury', 4700, 5, 'https://www.hyatt.com/content/dam/hyatt/hyattdam/images/2019/08/02/1028/Hyatt-Cape-Town.jpg'],
    ['Cape Town', 'The Cape Milner', 'Mid‑range', 2600, 4, 'https://www.thecapemilner.co.za/images/hotel.jpg'],
    ['Cape Town', 'City Lodge V&A Waterfront', 'Mid‑range', 2300, 4, 'https://www.citylodge.co.za/images/vawaterfront.jpg'],
    ['Cape Town', 'Cloud 9 Boutique Hotel', 'Budget', 1500, 3, 'https://cloud9hotel.co.za/images/cloud9.jpg'],

    # Durban
    ['Durban', 'Southern Sun Elangeni & Maharani', 'Luxury', 3400, 5, 'https://www.tsogosun.com/media/2850/southern-sun-elangeni.jpg'],
    ['Durban', 'The Oyster Box (Umhlanga)', 'Luxury', 4500, 5, 'https://www.oysterbox.co.za/images/hotel.jpg'],
    ['Durban', 'Protea Hotel Umhlanga Ridge', 'Mid‑range', 2400, 4, 'https://www.marriott.com/protea-umhlanga.jpg'],
    ['Durban', 'Garden Court South Beach', 'Mid‑range', 2100, 4, 'https://www.tsogosun.com/media/2810/garden-court-south-beach.jpg'],
    ['Durban', 'City Lodge Hotel Umhlanga Ridge', 'Budget', 1600, 3, 'https://www.citylodge.co.za/images/umhlanga.jpg'],

    # Pretoria
    ['Pretoria', 'Sheraton Pretoria Hotel', 'Luxury', 3600, 5, 'https://www.marriott.com/sheraton-pretoria.jpg'],
    ['Pretoria', 'The Capital Menlyn Maine', 'Mid‑range', 2500, 4, 'https://www.capitalhotels.co.za/images/menlyn.jpg'],
    ['Pretoria', 'City Lodge Hotel Lynnwood', 'Mid‑range', 2300, 4, 'https://www.citylodge.co.za/images/lynnwood.jpg'],
    ['Pretoria', 'Protea Hotel Hatfield', 'Budget', 1800, 3, 'https://www.marriott.com/protea-hatfield.jpg'],
    ['Pretoria', 'Apogee Boutique Hotel & Spa', 'Luxury', 3800, 5, 'https://www.apogeehotel.co.za/images/hotel.jpg'],

    # Port Elizabeth
    ['Port Elizabeth', 'No5 Boutique Hotel By Mantis', 'Luxury', 3300, 5, 'https://www.mantiscollection.com/no5-boutique-hotel.jpg'],
    ['Port Elizabeth', 'Radisson Blu Hotel PE', 'Luxury', 3100, 5, 'https://www.radissonhotels.com/pe-radisson.jpg'],
    ['Port Elizabeth', 'Protea Hotel Port Elizabeth', 'Mid‑range', 2300, 4, 'https://www.marriott.com/protea-pe.jpg'],
    ['Port Elizabeth', 'The Boardwalk Hotel', 'Mid‑range', 2400, 4, 'https://www.theboardwalk.co.za/images/hotel.jpg'],
    ['Port Elizabeth', 'Beachview Guesthouse', 'Budget', 1600, 3, 'https://www.beachviewguesthouse.co.za/images/guesthouse.jpg']
], columns=['Location','Hotel','Room Type','Price per Night (ZAR)','Rating','Image URL'])

# ------------------ Buses ------------------
buses = pd.DataFrame([
    ['Johannesburg to Cape Town', '08:00', 16, 800, 20],
    ['Cape Town to Durban', '09:30', 20, 950, 15],
    ['Durban to Pretoria', '12:00', 12, 700, 0],
    ['Pretoria to Port Elizabeth', '14:00', 14, 850, 10]
], columns=['Route','Departure Time','Duration (hours)','Price per Seat (ZAR)','Seats Available'])

# ------------------ App ------------------
st.title("🚌🏨 South Africa Booking System")
page = st.sidebar.selectbox("Choose a section", ["Accommodations", "Buses", "Cancel Booking"])

# ------------------ ACCOMMODATION ------------------
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
            st.image(row['Image URL'], width=300)
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
                name_list = df["Name"].unique().tolist()
                selected_name = st.selectbox("Select Your Name", name_list)
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
                name_list = df["Name"].unique().tolist()
                selected_name = st.selectbox("Select Your Name", name_list)
                user_bookings = df[df["Name"]==selected_name]
                st.write(user_bookings)
                to_cancel = st.selectbox("Select Route to Cancel", user_bookings["Route"])
                if st.button("Cancel Bus Booking"):
                    df = df.drop(user_bookings[user_bookings["Route"]==to_cancel].index)
                    df.to_csv("bus_bookings.csv", index=False)
                    st.success(f"✅ Booking for {to_cancel} cancelled successfully!")
        except FileNotFoundError:
            st.warning("No bus bookings file found.")
