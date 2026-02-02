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
accommodations = pd.DataFrame(
    # Johannesburg
    ['Johannesburg', 'Hilton Sandton', 'Luxury', 4200, 5,
     ['https://s.inyourpocket.com/gallery/johannesburg/2023/05/IMG-8667%20(1).jpg',
      'https://s.inyourpocket.com/img/text/southafrica/johannesburg/hilton-sandton-jnbsa_sandton_-lobby.jpg',
      'https://pix10.agoda.net/hotelImages/791/79114/79114_13112217530017730425.jpg?s=1024x768.jpg',
      'https://www.yoninja.com/wp-content/uploads/2014/04/Hilton-Sandton-Swimming-Pool.jpg',
      'https://www.restaurants.co.za/images/gallery/full/tradewinds_restaurant_12.jpg']],

    ['Johannesburg', 'Palazzo Hotel Montecasino', 'Luxury', 3800, 5,
     ['https://www.olielo.com/wp-content/uploads/2014/01/Palazzo-Montecasino-Johannesburg.jpg', ' https://tse2.mm.bing.net/th/id/OIP.aWS4yEazVhf-Cz9v3G0CNAHaE8?rs=1&pid=ImgDetMain&o=7&rm=3', 'https://johannesburg.hotelguide.co.za/images/palazzo-montecasino-suite-786x500.jpg', 'https://edge.media.datahc.com/HI282555713.jpg',  
'https://th.bing.com/th/id/R.a6b3ee6c8dd3dda4c71b64acc510bbbc?rik=%2fMUgrtfD9fYqyA&riu=http%3a%2f%2fwww.olielo.com%2fwp-content%2fuploads%2f2014%2f01%2fPalazzo-Montecasino-Breakfast-Buffet.jpg&ehk=kKMas0mr6yxNKJ%2fTUJhvXvMAV9G0exjheZVSsptUaaM%3d&risl=&pid=ImgRaw&r=0' ]],

    ['Johannesburg', 'Southern Sun Rosebank', 'Mid‑range', 2500, 4,
     [' https://dynamic-media-cdn.tripadvisor.com/media/photo-o/28/6c/8d/23/hotel-exterior.jpg?w=1100&h=-1&s=1', 'https://drsprnoe9nnhf.cloudfront.net/southernsun-04222022/cms/cache/v2/6793a83b36f36.jpg/400x265/fit/80/efb887076f15a1ba88619af2084516cd.jpg', ' https://johannesburg.hotelguide.co.za/images/crowne-plazza-johannesburg-room-786x500.jpg?t=1688153659', ' https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/da/39/59/swimming-pool-not-heated.jpg?w=1200&h=-1&s=1', ' https://cf.bstatic.com/xdata/images/hotel/max1024x768/641404290.jpg?k=86f2563c436c3dba69e6d5f4244e7088c1c6e24d1427d29ff0f82b4d1f3512b0&o=' ]],

    ['Johannesburg', 'Radisson Blu Sandton', 'Mid‑range', 2700, 4,
     ['https://tse4.mm.bing.net/th/id/OIP.KlMNoNruOZlpi7Wsqik_pQHaLH?rs=1&pid=ImgDetMain&o=7&rm=3', 'https://www.righttravel.info/images/hotels/Radisson_Blu_Sandton_Lobby.jpg', 'https://tse4.mm.bing.net/th/id/OIP.aBoQoF8enQHJegVnbM0vfQHaE7?rs=1&pid=ImgDetMain&o=7&rm=3', 'https://media.citizen.co.za/wp-content/uploads/2022/03/the-pool-at-radisson-blu-sandton.png', 'https://tse4.mm.bing.net/th/id/OIP.F1lSmnTo2YOPgpHTXUWg0wHaD9?rs=1&pid=ImgDetMain&o=7&rm=3' ]],

    ['Johannesburg', 'Mint Hotel Rosebank', 'Budget', 1800, 3,
     ['https://tse3.mm.bing.net/th/id/OIP.QgtYPP2pPk8v25kDZV9tXwHaE8?rs=1&pid=ImgDetMain&o=7&rm=3', 'https://travelground.imgix.net/AAEAAQAAAAAAAAAAAAAA8a06b97518e8ef005634a75e58a9f1256c050dbea6f76710afcc16acf2a5af31247deab70cf8f2400b6813c8bf7a0ccd1030?fit=crop&auto=enhance,format,compress&q=80&w=720&ar=1:1', 'https://wa-uploads.profitroom.com/minthotels/1525x991/17642441805096_2025.08.12mintrosebankjesssterkweb89.jpg', 'https://tse1.mm.bing.net/th/id/OIP.UoY0IDBQJw_WCXPxG5Cn5gHaJQ?rs=1&pid=ImgDetMain&o=7&rm=3', 'https://wa-uploads.profitroom.com/minthotels/1525x991/17159455827689_hotelsmintsouthafricajohannesburgresortstheblyderestaurant02.jpg' ]],

  # Cape Town
['Cape Town', 'Belmond Mount Nelson', 'Luxury', 5000, 5,
 [
  'https://crushmag-online.com/wp-content/uploads/2018/07/Belmond-mount-nelson-hotel-exterior.jpg',
  'https://tse2.mm.bing.net/th/id/OIP.XzpzNXVB87mUkq-7NRE3WAHaE8?rs=1&pid=ImgDetMain&o=7&rm=3',
  'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/01/af/ea/93/camera.jpg?w=1200&h=-1&s=1',
  'https://tse1.mm.bing.net/th/id/OIP.LqRmWsriuJurW1W7ze-h4AHaEJ?rs=1&pid=ImgDetMain&o=7&rm=3',
  'https://crushmag-online.com/wp-content/uploads/2019/06/TABLE-CARVING-CHICKEN-mount-nelson-1x6.jpg'
 ]
],

    ['Cape Town', 'Hyatt Regency Cape Town', 'Luxury', 4700, 5,
 [
  'https://inafricaandbeyond.com/wp-content/uploads/2022/10/IMG_2162.jpg',
  'https://tse3.mm.bing.net/th/id/OIP.fmrdNmjeoNKsIs7cxz2CiAHaEK?rs=1&pid=ImgDetMain&o=7&rm=3',
  'https://assets.hyatt.com/content/dam/hyatt/hyattdam/images/2023/08/10/0440/CPTRC-P0143-Regency-Suite-Bedroom.jpg/CPTRC-P0143-Regency-Suite-Bedroom.4x3.jpg',
  'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1d/84/f3/de/pool.jpg?w=700&h=-1&s=1',
  'https://assets.hyatt.com/content/dam/hyatt/hyattdam/images/2021/01/28/0002/Hyatt-Regency-Cape-Town-P102-Pool-Night.jpg/Hyatt-Regency-Cape-Town-P102-Pool-Night.4x3.jpg?imwidth=1920'
 ]
],
   ['Cape Town', 'The Cape Milner', 'Mid-range', 2600, 4,
 [
  'https://capemilner.com/wp-content/uploads/2025/01/The-Cape-Milner-Exterior-900x604.jpg',
  'https://capemilner.com/wp-content/uploads/2021/10/capemilner-glasslounge-3.jpg',
  'https://tse4.mm.bing.net/th/id/OIP.QSBnG4ULhHgb-jIdHJNeHwHaEh?rs=1&pid=ImgDetMain&o=7&rm=3',
  'https://extraordinary.co.za/wp-content/uploads/2024/06/Extraordinary-The-Cape-Milner-pool-1536x1025.jpg',
  'https://th.bing.com/th/id/R.9e111c6d23df360417ec9a29381ff7e8?rik=yAPDfbCdliaJsg&pid=ImgRaw&r=0'
 ]
],
   ['Cape Town', 'City Lodge V&A Waterfront', 'Mid-range', 2300, 4,
 [
  'https://th.bing.com/th/id/R.e700f03c3e5ea8afc3969765d0c119ce?rik=fXYetTqkmav7UA&riu=http%3a%2f%2fmedia-cdn.tripadvisor.com%2fmedia%2fphoto-s%2f02%2f2e%2f45%2f76%2foutside-view-2.jpg&ehk=YJ%2fTyFClExNZS%2b7CXwiAxbdn2TW1ScosB0uRvHg8JbM%3d&risl=&pid=ImgRaw&r=0',
  'https://www.capetown.travel/wp-content/uploads/2022/09/City-Lodge-Hotel-VA-Entrance-CI.jpg',
  'https://city-lodge-va-waterfront.capetown-hotels-za.com/data/Photos/OriginalPhoto/12132/1213256/1213256215/cape-town-city-lodge-va-waterfront-photo-26.JPEG',
  'https://www.capetown.travel/wp-content/uploads/2022/09/Harbour-Deck-Outdoor-Pool-1-800x800.jpg',
  'https://city-lodge-va-waterfront.capetown-hotels-za.com/data/Pics/OriginalPhoto/16899/1689908/1689908590/city-lodge-hotel-v-a-waterfront-cape-town-pic-15.JPEG'
 ]
],

   ['Cape Town', 'Cloud 9 Boutique Hotel', 'Budget', 1500, 3,
 [
  'https://imgcy.trivago.com/c_fill,d_dummy.jpeg,e_sharpen:60,f_auto,h_534,q_40,w_800/partner-images/a1/e9/945baa5950028d10c2b7ce0c772b6c5f1a4ad4af0292bf0bd4043c97527a.jpeg',
  'https://www.capetownmagazine.com/media_lib/preview/cfa87866cbb4db4428233748aacd7da9.preview.jpg',
  'https://tse1.mm.bing.net/th/id/OIP.LcDdPqHDx7i1WKKcQ-d4pwHaE8?rs=1&pid=ImgDetMain&o=7&rm=3',
  'https://pix10.agoda.net/hotelImages/1771408/-1/7da0f2907653c01e9c2ffae157062de0.jpg?ca=0&ce=1&s=1024x768',
  'https://tse3.mm.bing.net/th/id/OIP.yEh94A9BVOAphdxHDrTeyAHaE8?rs=1&pid=ImgDetMain&o=7&rm=3'
 ]
],

    # Durban
   ['Durban', 'The Oyster Box', 'Luxury', 4500, 5,
 [
  'https://www.chaloafrica.com/wp-content/uploads/2018/05/The-Oyster-Box-View.jpg',
  'https://tse4.mm.bing.net/th/id/OIP.ILjDIVvyUffOT6aeTtsVUwHaE7?rs=1&pid=ImgDetMain&o=7&rm=3',
  'https://tse4.mm.bing.net/th/id/OIP.WdZdyqVrTAUhf242K858TQHaE5?rs=1&pid=ImgDetMain&o=7&rm=3',
  'https://cdn.rhinoafrica.com/tmp/image-thumbnails/objects/service-providers/the-oyster-box-hotel/_img/image-thumb__34638__background-cover/the-oyster-box-hotel-facilities-pool-09.jpg',
  'https://th.bing.com/th/id/R.0a85cf886f77a56dfcf9dff73804cf68?rik=YlJaZdAoq84a%2bg&pid=ImgRaw&r=0'
 ]
],
   ['Durban', 'Southern Sun Elangeni', 'Luxury', 3400, 5,
 [
  'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0b/dd/4a/99/southern-sun-elangeni.jpg?w=1200&h=-1&s=1',
  'https://pix10.agoda.net/hotelImages/3303/0/f4bff42e1e16dcddb04085ead6d15ca2.jpeg?s=1024x768',
  'https://cloud.tui.com/pics/hotel/resize:fill/aHR0cHM6Ly9waWNzLnR1aS5jb20vcGljcy9waWNzMTYwMHgxMjAwL3R1aS83LzdjZmIxODNmLWYxMjUtNGE1My04MjIyLWUyMzQ2YjA0Zjk2ZC5qcGc=',
  'https://www.south-african-hotels.com/media/southern-sun-elangeni-and-maharani-11.jpg',
  'https://pix10.agoda.net/hotelImages/7458491/0/b4acfad7e926d07db6317ebd21bd5626.jpg?ca=8&ce=1&s=1024x768'
 ]
],

   ['Durban', 'Protea Hotel Umhlanga Ridge', 'Mid-range', 2400, 4,
 [
  'https://th.bing.com/th/id/R.21e04c4aeae2dfb38ccd02b3a6d84ce1?rik=gDiJesNbi9Vr6Q&riu=http%3a%2f%2fa.mktgcdn.com%2fp%2ft5PhNa_VXZN258HHsi0do6KO94-yTN546Tu49Ybe9fU%2f2048x1366.jpg&ehk=SjOQPpowgTgtD%2fkH5sBqDIfsiVSnlgQFhrtT0S%2bI%2fcw%3d&risl=&pid=ImgRaw&r=0',
  'https://images.getaroom-cdn.com/image/upload/s--tXrp1NYW--/c_limit,e_improve,fl_lossy.immutable_cache,h_940,q_auto:good,w_940/v1755802918/18408f279847d4d36b93be9e7eb2ebc435412495?_a=BACAEuEv&atc=e7cd1cfa',
  'https://protea-hotel-by-marriott-durban-umhlanga-ridge.durban-hotels-za.com/data/Photos/OriginalPhoto/9148/914845/914845768/photo-protea-hotel-by-marriott-umhlanga-ridge-durban-81.JPEG',
  'https://tse1.mm.bing.net/th/id/OIP.qYd9EdPBNdlXi_FOTdAt4wHaEK?rs=1&pid=ImgDetMain&o=7&rm=3',
  'https://tse2.mm.bing.net/th/id/OIP.9SlEUGlokjdVD-o1qOjZHwAAAA?rs=1&pid=ImgDetMain&o=7&rm=3'
 ]
],

   ['Durban', 'Garden Court South Beach', 'Mid-range', 2100, 4,
 [
  'https://media-cdn.holidaycheck.com/w_1280,h_720,c_fit,q_80/ugc/images/fc653542-f390-4f2e-aac5-f9de2fc92b44',
  'https://tse2.mm.bing.net/th/id/OIP.jkA0JdWqfvEfJgSDiNQKGwHaDt?rs=1&pid=ImgDetMain&o=7&rm=3',
  'https://tse1.explicit.bing.net/th/id/OIP.Xew8ZVWl1CAqwqt3sUK-QgHaE5?rs=1&pid=ImgDetMain&o=7&rm=3',
  'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1e/04/cf/da/outdoor-swimming-pool.jpg?w=1100&h=-1&s=1',
  'https://cf.bstatic.com/xdata/images/hotel/max1024x768/686575980.jpg?k=db1edba9bf6d4bc34dd37309b559780bbf31b88192a2d0e3ad3508d5b01cdf4e&o='
 ]
],
    ['Durban', 'City Lodge Hotel Umhlanga Ridge', 'Budget', 1600, 3,
 [
  'https://citylodgeridge.durbanahotel.com/data/Photos/700x500w/12778/1277802/1277802298.JPEG',
  'https://tse2.mm.bing.net/th/id/OIP.lZRxBgaKwEQ41qbZe3VdfgHaE8?rs=1&pid=ImgDetMain&o=7&rm=3',
  'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0d/36/54/6c/city-lodge-hotel-umhlanga.jpg?w=1200&h=-1&s=1',
  'https://tse2.mm.bing.net/th/id/OIP.in284qTmR1A8ToUQdl7hQwHaE8?rs=1&pid=ImgDetMain&o=7&rm=3',
  'https://citylodgeridge.durbanahotel.com/data/Pics/700x500w/16698/1669894/1669894088/pic-city-lodge-hotel-umhlanga-ridge-durban-13.JPEG'
 ]
],
    # Pretoria
 ['Pretoria', 'Sheraton Pretoria Hotel', 'Luxury', 3600, 5,
 [
  'https://www.south-african-hotels.com/media/sheraton-pretoria-hotel-exterior-night-main.jpg',
  'https://tse2.mm.bing.net/th/id/OIP.UysQYjG2nGnI6wDkmAYpFwHaE3?rs=1&pid=ImgDetMain&o=7&rm=3',
  'https://tse3.mm.bing.net/th/id/OIP.tmuQB0NF5N4_aVemGWp-ZQHaE8?rs=1&pid=ImgDetMain&o=7&rm=3',
  'https://tse1.mm.bing.net/th/id/OIP.8n1csOowFqBchbDAwEvKQAAAAA?rs=1&pid=ImgDetMain&o=7&rm=3',
  'https://www.south-african-hotels.com/media/sheraton-pretoria-hotel-restaurant.jpg'
 ]
],

  ['Pretoria', 'The Capital Menlyn', 'Mid‑range', 2500, 4,
 [
  'https://www.centralsquare.co.za/wp-content/uploads/2017/03/central-square-blog-Capital-Hotel-1.jpg',
  'https://thecapital.co.za/wp-content/uploads/2024/10/MENLYN-MAINE-RECEPTION1-scaled.jpg',
  'https://thecapital.co.za/wp-content/uploads/2020/09/The_Capital_Menyln_Maine_PARAPLEGIC_ROOM_1.jpg',
  'https://tse2.mm.bing.net/th/id/OIP.OwIVOHYfBxl11sC_3vsfLQHaE8?rs=1&pid=ImgDetMain&o=7&rm=3',
  'https://tse3.mm.bing.net/th/id/OIP.RnAiREN2TtsH3IG8u_9jigHaE8?rs=1&pid=ImgDetMain&o=7&rm=3'
 ]
],

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
, columns=['Location','Hotel','Room Type','Price per Night (ZAR)','Rating','Image URLs'])
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
            st.markdown(f"{row['Hotel']} ({row['Room Type']}) - {row['Price per Night (ZAR)']} ZAR - {'⭐'*row['Rating']}")
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