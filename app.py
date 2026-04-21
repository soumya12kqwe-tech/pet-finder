import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from datetime import datetime

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="PetFinder: Local Lost & Found",
    page_icon="🐕",
    layout="wide"
)

# 2. ATTENTION-CATCHING CUSTOM CSS
st.markdown("""
    <style>
    /* Change background color */
    .stApp {
        background-color: #f0f2f6;
    }
    /* Style the main header */
    .main-title {
        font-size: 50px;
        color: #FF4B4B; /* Emergency Red/Orange */
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    /* Style subheaders */
    .section-header {
        color: #1c3d5a;
        border-bottom: 2px solid #FF4B4B;
        padding-bottom: 5px;
    }
    /* Success/Found banner */
    .found-banner {
        background-color: #D4EDDA;
        color: #155724;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #C3E6CB;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER SECTION
st.markdown('<p class="main-title">🐕 PetFinder: Bring Them Home</p>', unsafe_allow_html=True)
st.write("<h4 style='text-align: center; color: #555;'>Helping local communities reconnect lost pets with their families.</h4>", unsafe_allow_html=True)

# 4. SIDEBAR FOR NAVIGATION
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/194/194279.png", width=100)
    st.header("Search Filters")
    pet_type = st.multiselect("Filter by Type", ["Dog", "Cat", "Other"], default=["Dog", "Cat"])
    status = st.radio("Show:", ["All", "Lost", "Found"])

# 5. MAIN CONTENT TABS
tab1, tab2, tab3 = st.tabs(["📍 View Live Map", "📢 Report a Pet", "📋 Recent Listings"])

with tab1:
    st.markdown('<h2 class="section-header">Live Incidents Nearby</h2>', unsafe_allow_html=True)
    
    # Mock Data for Pins
    map_data = [
        {"name": "Buddy", "lat": 40.7128, "lon": -74.0060, "status": "Lost", "color": "red"},
        {"name": "Unknown Husky", "lat": 40.7300, "lon": -74.0100, "status": "Found", "color": "green"}
    ]

    # Create Map
    m = folium.Map(location=[40.7128, -74.0060], zoom_start=13)
    for pet in map_data:
        folium.Marker(
            [pet['lat'], pet['lon']], 
            popup=f"{pet['status']}: {pet['name']}",
            icon=folium.Icon(color=pet['color'], icon='info-sign')
        ).add_to(m)

    st_folium(m, width="100%", height=400)

with tab2:
    st.markdown('<h2 class="section-header">Submit a New Report</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        report_type = st.selectbox("Report Type", ["Lost (I missed my pet)", "Found (I saw a stray)"])
        pet_name = st.text_input("Pet Name (if known)")
        breed = st.text_input("Breed/Description")
    
    with col2:
        date = st.date_input("Date Noticed", datetime.now())
        photo = st.file_uploader("Upload Clear Photo", type=["jpg", "png", "jpeg"])
    
    if st.button("🚨 Broadcast to Neighborhood"):
        st.balloons()
        st.success("Your report has been pinned to the map and broadcasted to local users!")

with tab3:
    st.markdown('<h2 class="section-header">Active Alerts</h2>', unsafe_allow_html=True)
    
    # Example Listing Card
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        st.image("https://placedog.net/300/200", caption="Last seen near 5th Ave")
    with col_txt:
        st.error("**URGENT: LOST DOG - BUDDY**")
        st.write("**Breed:** Golden Retriever Mix")
        st.write("**Last Seen:** 2 hours ago")
        st.button("I have seen this pet", key="buddy_btn")

# 6. FOOTER
st.divider()
st.caption("PetFinder 2026 - Keeping our furry friends safe.")
