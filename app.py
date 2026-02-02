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

    # Cape Town['Cape Town', 'Belmond Mount Nelson', 'Luxury', 5000, 5,
 [
  'https://crushmag-online.com/wp-content/uploads/2018/07/Belmond-mount-nelson-hotel-exterior.jpg',
  'https://tse2.mm.bing.net/th/id/OIP.XzpzNXVB87mUkq-7NRE3WAHaE8?rs=1&pid=ImgDetMain&o=7&rm=3',
  'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/01/af/ea/93/camera.jpg?w=1200&h=-1&s=1',
  'https://tse1.mm.bing.net/th/id/OIP.LqRmWsriuJurW1W7ze-h4AHaEJ?rs=1&pid=ImgDetMain&o=7&rm=3',
  'https://crushmag-online.com/wp-content/uploads/2019/06/TABLE-CARVING-CHICKEN-mount-nelson-1x6.jpg'
 ]],

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
     [
    'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0b/dd/4a/99/southern-sun-elangeni.jpg?w=1200&h=-1&s=1',
    'https://pix10.agoda.net/hotelImages/3303/0/f4bff42e1e16dcddb04085ead6d15ca2.jpeg?s=1024x768',
    'https://cloud.tui.com/pics/hotel/resize:fill/aHR0cHM6Ly9waWNzLnR1aS5jb20vcGljcy9waWNzMTYwMHgxMjAwL3R1aS83LzdjZmIxODNmLWYxMjUtNGE1My04MjIyLWUyMzQ2YjA0Zjk2ZC5qcGc=',
    'https://www.south-african-hotels.com/media/southern-sun-elangeni-and-maharani-11.jpg',
    'https://pix10.agoda.net/hotelImages/7458491/0/b4acfad7e926d07db6317ebd21bd5626.jpg?ca=8&ce=1&s=1024x768'
]],

    ['Durban', 'Protea Hotel Umhlanga Ridge', 'Mid‑range', 2400, 4,
     [
    'https://th.bing.com/th/id/R.21e04c4aeae2dfb38ccd02b3a6d84ce1?rik=gDiJesNbi9Vr6Q&riu=http%3a%2f%2fa.mktgcdn.com%2fp%2ft5PhNa_VXZN258HHsi0do6KO94-yTN546Tu49Ybe9fU%2f2048x1366.jpg&ehk=SjOQPpowgTgtD%2fkH5sBqDIfsiVSnlgQFhrtT0S%2bI%2fcw%3d&risl=&pid=ImgRaw&r=0',
    'https://images.getaroom-cdn.com/image/upload/s--tXrp1NYW--/c_limit,e_improve,fl_lossy.immutable_cache,h_940,q_auto:good,w_940/v1755802918/18408f279847d4d36b93be9e7eb2ebc435412495?_a=BACAEuEv&atc=e7cd1cfa',
    'https://protea-hotel-by-marriott-durban-umhlanga-ridge.durban-hotels-za.com/data/Photos/OriginalPhoto/9148/914845/914845768/photo-protea-hotel-by-marriott-umhlanga-ridge-durban-81.JPEG',
    'https://tse1.mm.bing.net/th/id/OIP.qYd9EdPBNdlXi_FOTdAt4wHaEK?rs=1&pid=ImgDetMain&o=7&rm=3',
    'https://tse2.mm.bing.net/th/id/OIP.9SlEUGlokjdVD-o1qOjZHwAAAA?rs=1&pid=ImgDetMain&o=7&rm=3'
]],

    ['Durban', 'Garden Court South Beach', 'Mid‑range', 2100, 4,
    [
    'https://media-cdn.holidaycheck.com/w_1280,h_720,c_fit,q_80/ugc/images/fc653542-f390-4f2e-aac5-f9de2fc92b44',
    'https://tse2.mm.bing.net/th/id/OIP.jkA0JdWqfvEfJgSDiNQKGwHaDt?rs=1&pid=ImgDetMain&o=7&rm=3',
    'https://tse1.explicit.bing.net/th/id/OIP.Xew8ZVWl1CAqwqt3sUK-QgHaE5?rs=1&pid=ImgDetMain&o=7&rm=3',
    'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1e/04/cf/da/outdoor-swimming-pool.jpg?w=1100&h=-1&s=1',
    'https://cf.bstatic.com/xdata/images/hotel/max1024x768/686575980.jpg?k=db1edba9bf6d4bc34dd37309b559780bbf31b88192a2d0e3ad3508d5b01cdf4e&o='
]],

    ['Durban', 'City Lodge Hotel Umhlanga Ridge', 'Budget', 1600, 3,
     [
    'https://citylodgeridge.durbanahotel.com/data/Photos/700x500w/12778/1277802/1277802298.JPEG',
    'https://tse2.mm.bing.net/th/id/OIP.lZRxBgaKwEQ41qbZe3VdfgHaE8?rs=1&pid=ImgDetMain&o=7&rm=3',
    'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0d/36/54/6c/city-lodge-hotel-umhlanga.jpg?w=1200&h=-1&s=1',
    'https://tse2.mm.bing.net/th/id/OIP.in284qTmR1A8ToUQdl7hQwHaE8?rs=1&pid=ImgDetMain&o=7&rm=3',
    'https://citylodgeridge.durbanahotel.com/data/Pics/700x500w/16698/1669894/1669894088/pic-city-lodge-hotel-umhlanga-ridge-durban-13.JPEG'
]],

    # Pretoria
    ['Pretoria', 'Sheraton Pretoria Hotel', 'Luxury', 3600, 5,
     [
    'https://www.south-african-hotels.com/media/sheraton-pretoria-hotel-exterior-night-main.jpg',
    'https://tse2.mm.bing.net/th/id/OIP.UysQYjG2nGnI6wDkmAYpFwHaE3?rs=1&pid=ImgDetMain&o=7&rm=3',
    'https://tse3.mm.bing.net/th/id/OIP.tmuQB0NF5N4_aVemGWp-ZQHaE8?rs=1&pid=ImgDetMain&o=7&rm=3',
    'https://tse1.mm.bing.net/th/id/OIP.8n1csOowFqBchbDAwEvKQAAAAA?rs=1&pid=ImgDetMain&o=7&rm=3',
    'https://www.south-african-hotels.com/media/sheraton-pretoria-hotel-restaurant.jpg'
]],

    ['Pretoria', 'The Capital Menlyn', 'Mid‑range', 2500, 4,
         ['Pretoria', 'The Capital Menlyn', 'Mid‑range', 2500, 4,
     [
         'https://www.centralsquare.co.za/wp-content/uploads/2017/03/central-square-blog-Capital-Hotel-1.jpg',
         'https://thecapital.co.za/wp-content/uploads/2024/10/MENLYN-MAINE-RECEPTION1-scaled.jpg',
         'https://thecapital.co.za/wp-content/uploads/2020/09/The_Capital_Menyln_Maine_PARAPLEGIC_ROOM_1.jpg',
         'https://tse2.mm.bing.net/th/id/OIP.OwIVOHYfBxl11sC_3vsfLQHaE8?rs=1&pid=ImgDetMain&o=7&rm=3',
         'https://tse3.mm.bing.net/th/id/OIP.RnAiREN2TtsH3IG8u_9jigHaE8?rs=1&pid=ImgDetMain&o=7&rm=3'
     ]],
    # next hotel row...],

    ['Pretoria', 'City Lodge Lynnwood', 'Mid‑range', 2300, 4,
     [
    'https://th.bing.com/th/id/R.d31e44c0c0c9eb3107b303ff305337ca?rik=crXAQq7Q4AOrOw&riu=http%3a%2f%2fwww.royalafrica.co.za%2fwp-content%2fuploads%2f2018%2f07%2fcity-lodge-lynnwood-royal-african-discoveries-3-600x400.jpg&ehk=39C6Uy7et8vJ5fzHGKKiwsbjqcoCSVAV6oEfskZC0iA%3d&risl=&pid=ImgRaw&r=0',
    'https://tse1.mm.bing.net/th/id/OIP.tvf_pSGak0JpsXOQFhSNbQHaF7?rs=1&pid=ImgDetMain&o=7&rm=3',
    'https://admin.clhg.com/rateimages/2019-06-07-115214amcl-single-lynwood-2jpeg.jpeg',
    'https://th.bing.com/th/id/R.d38f0a3a90e48e7767afad8c31fd053e?rik=8FRLKxQ4USdarg&pid=ImgRaw&r=0',
    'https://cf.bstatic.com/xdata/images/hotel/max1024x768/70705207.jpg?k=fb76c90715bd36d9ca18ce77c1bf7c7b678842711d27ba0d5430f36d9fcdec5c&o='
]],

    ['Pretoria', 'Protea Hatfield', 'Budget', 1800, 3,
     ['Pretoria', 'Protea Hatfield', 'Budget', 1800, 3,
 [
     'https://tse1.mm.bing.net/th/id/OIP.s3-BByG5eAJ_ghfe4Ech_gHaE5?rs=1&pid=ImgDetMain&o=7&rm=3',
     'https://cf.bstatic.com/xdata/images/hotel/max500/556292641.jpg?k=bcffaabf3da4c9caf9d0b5ec3a31d6e5b607d45b2cf2f121d1f0d9dcc23011c4&o=',
     'https://cf.bstatic.com/xdata/images/hotel/max500/573433464.jpg?k=bff106a8178ab82f242c4bfe3283e4cdd879b9fe6e181bcdeff4a292063df34e&o=&hp=1',
     'https://tse1.mm.bing.net/th/id/OIP.p0sGXNXQ_Mew7HFQdcvaUgHaE5?rs=1&pid=ImgDetMain&o=7&rm=3',
     'https://www.south-african-hotels.com/media/protea-hotel-hatfield-6.jpg'
 ]],],

    ['Pretoria', 'Apogee Boutique Hotel & Spa', 'Luxury', 3800, 5,
     [
    'https://r.profitroom.pl/apogeeboutiquehotelspa/images/gallery/thumbs/500x500/202506141216570.001_Apogee_Exterior_Views_2025.JPG?updated=2025-08-04_14-26',
    'https://tse1.mm.bing.net/th/id/OIP.OePB_sIk79sQNWRiKMefLAHaE8?rs=1&pid=ImgDetMain&o=7&rm=3',
    'https://wa-uploads.profitroom.com/apogeeboutiquehotelspa/580x460/17436817610223_room10juniorsuite1.jpg',
    'https://emirateswoman.com/wp-content/uploads/2023/12/LApogee2.jpg',
    'https://r.profitroom.pl/apogeeboutiquehotelspa/images/gallery/thumbs/500x500/202506141222310.005_Apogee_Dining_Areas.JPG?updated=2025-08-04_14-26'
]],

    # Port Elizabeth
    ['Port Elizabeth', 'No5 Boutique Hotel By Mantis', 'Luxury', 3300, 5,
     [
    'https://www.ahstatic.com/photos/b417_ho_01_p_2048x1536.jpg',
    'https://q-xx.bstatic.com/xdata/images/hotel/max1024x768/524704968.jpg?k=240ea5e5208edfa7ab1c0df2cf5fb4497761f9a5567f1eb12eaa292b67b7626e&o=',
    'https://tse3.mm.bing.net/th/id/OIP.Uq6WTMAsszseuueeUcaSrwHaE8?rs=1&pid=ImgDetMain&o=7&rm=3',
    'https://exp.cdn-hotels.com/hotels/4000000/3180000/3176600/3176524/1921e38a_z.jpg?impolicy=fcrop&w=773&h=530&q=high',
    'https://s3.amazonaws.com/static-webstudio-accorhotels-usa-1.wp-ha.fastbooking.com/wp-content/uploads/sites/12/2019/06/14072137/Mantis-No-5-Jazz-Room-Restaurant-min.jpg'
]],

    ['Port Elizabeth', 'Radisson Blu Hotel PE', 'Luxury', 3100, 5,
     [
    'https://media.radissonhotels.net/image/radisson-blu-hotel-conakry/exterior/16256-124837-f82053350_4k.jpg?impolicy=HomeHero',
    'https://media.radissonhotels.net/image/radisson-blu-scandinavia-hotel-copenhagen/lobby/16256-113960-f81080573_4k.jpg?impolicy=HomeHero',
    'https://tse2.mm.bing.net/th/id/OIP.5K5WcunMTcJpgNWVdqhstAHaE8?rs=1&pid=ImgDetMain&o=7&rm=3',
    'https://media.radissonhotels.net/image/radisson-blu-hotel-dubai-waterfront/pool--outdoor/16256-116474-f63809364_4k.jpg?impolicy=HomeHero',
    'https://tse4.mm.bing.net/th/id/OIP.soSlPHaQ7E23VMsh9_IWjQHaE8?rs=1&pid=ImgDetMain&o=7&rm=3'
]],

    ['Port Elizabeth', 'Protea PE', 'Mid‑range', 2300, 4,
     [
    'https://www.uniquest.co.za/wp-content/uploads/2015/09/4-Star-Protea-Hotel-Marine-Port-Elizabeth-1-600x343.jpg',
    'https://www.hotel.co.za/images/protea-hotel-marine-room-lounge-590x390.jpg?t=1628014941',
    'https://www.uniquest.co.za/wp-content/uploads/2015/09/4-Star-Protea-Hotel-Marine-Port-Elizabeth-2-600x343.jpg',
    'https://www.hotel.co.za/images/protea-hotel-marine-pool-view-590x390.jpg',
    'https://static-prod.dineplan.com/restaurant/restaurants/images/3343/cropped-protea-restaurant-1648220289.jpg?d=1652963189'
]],

    ['Port Elizabeth', 'The Boardwalk Hotel', 'Mid‑range', 2400, 4,
     [
    'https://freedomdestinations.co.uk/wp-content/uploads/Boardwalk-1.jpg',
    'https://tse2.mm.bing.net/th/id/OIP.8oYBSqWaEUuWnPhieTVr-AHaDt?rs=1&pid=ImgDetMain&o=7&rm=3',
    'https://static21.com-hotel.com/uploads/hotel-room/446323/photo/lg_the-boardwalk-hotel-convention-centre-spa-1-superior-luxury-family-room-1_17057371531.jpg',
    'https://howtodisney.com/wp-content/uploads/2016/11/Boardwalk_Pool.jpg',
    'https://www.south-african-hotels.com/media/the-boardwalk-hotel-7.jpg'
]],

    ['Port Elizabeth', 'Beachview Guesthouse', 'Budget', 1600, 3,
     [
    'https://st.hzcdn.com/fimgs/pictures/exteriors/beachview-brown-design-group-img~fef17e1e07d1a63a_6351-1-8394826-w320-h320-b1-p10.jpg',
    'https://travelground.imgix.net/AAEAAQAAAAAAAAAAAAAA57ec66c1a0157eb204e47911c7d0cd0b795c2902e6074ca0ace470c1edcc3c0cb222a1852daa7be3a59664c15b6b15e6b280?w=1200&h=630&fit=crop&auto=enhance,format,compress&q=80',
    'https://cf.bstatic.com/xdata/images/hotel/max1024x768/655402101.jpg?k=186c9ed6b0e38b0cca60525aadcc3dd4f51320184303557714fdcb097513cfd5&o=',
    'https://tse1.mm.bing.net/th/id/OIP.i5AwyrAib-s-SpvGIHeZHAHaFj?rs=1&pid=ImgDetMain&o=7&rm=3'
]]
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