import streamlit as st
import math
from rupantaran.land import terai
from rupantaran.land import hilly
https://github.com/biraj094/rupantaran/blob/main/example-streamlit-app/static/baseball.jpeg?raw=true
###############################################################################
# Constants
###############################################################################
# Reference areas with name, area in square meters, and image URLs
REFERENCE_AREAS = {
    "Football Field": {"area": 7140, "image": "https://raw.githubusercontent.com/biraj094/rupantaran/main/example-streamlit-app/static/football-field.jpeg?raw=true"},
    "Cricket Ground": {"area": 15000, "image": "https://raw.githubusercontent.com/biraj094/rupantaran/main/example-streamlit-app/static/cricket.jpeg?raw=true"},
    "Basketball Court": {"area": 420, "image": "https://raw.githubusercontent.com/biraj094/rupantaran/main/example-streamlit-app/static/basketball-court.jpeg?raw=true"},
    "Tennis Court": {"area": 260, "image": "https://raw.githubusercontent.com/biraj094/rupantaran/main/example-streamlit-app/static/tennis-court.jpeg?raw=true"},
    "Olympic Swimming Pool": {"area": 1250, "image": "https://raw.githubusercontent.com/biraj094/rupantaran/main/example-streamlit-app/static/swimming-pool.jpeg?raw=true"},
    "Baseball Field": {"area": 10000, "image": "https://raw.githubusercontent.com/biraj094/rupantaran/main/example-streamlit-app/static/baseball.jpeg?raw=true"},  
    "Volleyball Court": {"area": 162, "image": "https://raw.githubusercontent.com/biraj094/rupantaran/main/example-streamlit-app/static/volleyball.jpeg?raw=true"},
    "Taj Mahal (entire complex)": {"area": 170000, "image": "https://raw.githubusercontent.com/biraj094/rupantaran/main/example-streamlit-app/static/taj-mahal.jpeg?raw=true"},
    "Eiffel Tower (base footprint)": {"area": 15625, "image": "https://raw.githubusercontent.com/biraj094/rupantaran/main/example-streamlit-app/static/eiffel-tower.jpeg?raw=true"},
    "Central Park (NYC)": {"area": 3410000, "image": "https://raw.githubusercontent.com/biraj094/rupantaran/main/example-streamlit-app/static/central-park.jpeg?raw=true"},
    "Great Pyramid of Giza (base)": {"area": 53000, "image": "https://raw.githubusercontent.com/biraj094/rupantaran/main/example-streamlit-app/static/pyramid.jpeg?raw=true"},
    "Boeing 747 (bounding rectangle)": {"area": 5168, "image": "https://raw.githubusercontent.com/biraj094/rupantaran/main/example-streamlit-app/static/boeing.jpeg?raw=true"}
}
###############################################################################
# Streamlit Page Configuration
###############################################################################
st.set_page_config(page_title="Nepali Land Converter", layout="wide")

# Custom CSS for background color and multiselect styling
st.markdown(
    """
    <style>
    /* Adjust sidebar width */
    [data-testid="stSidebar"][aria-expanded="true"]{
        min-width: 450px;
        max-width: 450px;
    }
    /* Customize multiselect */
    .stMultiSelect div[data-baseweb="select"] span {
        font-size: 11px;  /* Slightly smaller font */
        max-height: 16px; /* Reduce item height */
        line-height: 18px;
    }
    .stMultiSelect div[data-baseweb="select"] {
        max-height: 160px; /* Adjust dropdown height */
    }
    .stMultiSelect div[data-baseweb="tag"] {
        background-color: #1f77b4 !important; /* Keep selected item background color */
        color: white !important; /* Maintain text color */
        font-size: 11px; /* Maintain proportional font size */
        padding: 2px 6px !important; /* Keep padding balanced */
        border-radius: 4px; /* Slight rounding for a cleaner look */
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.sidebar.title("Bigha Busters 🏡⚡")

st.sidebar.markdown(
    """
    Ever looked at a plot of land and thought, *"How many basketball courts could fit in here?"* 🏀 Or *"Is my backyard larger than the base of the Great Pyramid?"* 🦋⃤♡⃤🌈⃤   
    
    This quirky tool lets you **convert Nepali land units** into **real-world reference objects**.Whether it's football fields, Olympic pools, or the Eiffel Tower's base 🗼 , we give your land a fun, relatable comparison—because raw numbers are boring! 📏✨  
    """
)
st.sidebar.markdown("---")

st.sidebar.subheader("ℹ️ About This Project")
st.sidebar.markdown(
    """
    **Bigha Busters** is a **fun demonstration project** showcasing the power of [**rupantaran**](https://github.com/biraj094/rupantaran), an opensource package built to **convert Nepali measurements** with ease. 
    """
)

st.sidebar.markdown("---")

st.sidebar.subheader("🔗 Relevant Links")
st.sidebar.markdown(
    """
    - 📖 [**Rupantaran Docs**](https://rupantaran.readthedocs.io/en/latest/index.html)  
    - 💻 [**Rupantaran Repo**](https://github.com/biraj094/rupantaran)  
    """
)
###############################################################################
# Main Container for Input and Output
###############################################################################
left_col, right_col = st.columns(2)

with left_col:
    st.markdown("### Step 1: Land Measurement")
    measurement_type = st.radio(
        "**Select Land Measurement Type:**", 
        ("Terai", "Hilly"),
        horizontal=True
    )

    if measurement_type == "Terai":
        st.markdown("**Terai Units (Bigha, Kattha, Dhur)**")
        t_col1, t_col2, t_col3 = st.columns(3)
        with t_col1:
            bigha_val = st.number_input("Bigha:", min_value=0.0, value=0.0, key="bigha", label_visibility="visible")
        with t_col2:
            kattha_val = st.number_input("Kattha:", min_value=0.0, value=0.0, key="kattha", label_visibility="visible")
        with t_col3:
            dhur_val = st.number_input("Dhur:", min_value=0.0, value=0.0, key="dhur", label_visibility="visible")
        ropani_val = aana_val = paisa_val = dam_val = 0.0
    else:
        st.markdown("**Hilly Units (Ropani, Aana, Paisa, Dam)**")
        h_col1, h_col2, h_col3, h_col4 = st.columns(4)
        with h_col1:
            ropani_val = st.number_input("Ropani:", min_value=0.0, value=0.0, key="ropani", label_visibility="visible")
        with h_col2:
            aana_val = st.number_input("Aana:", min_value=0.0, value=0.0, key="aana", label_visibility="visible")
        with h_col3:
            paisa_val = st.number_input("Paisa:", min_value=0.0, value=0.0, key="paisa", label_visibility="visible")
        with h_col4:
            dam_val = st.number_input("Dam:", min_value=0.0, value=0.0, key="dam", label_visibility="visible")
        bigha_val = kattha_val = dhur_val = 0.0

with right_col:
    st.markdown("### Step 2: Reference Areas")
    selected_areas = st.multiselect(
        "Select areas to compare your land with:",
        options=list(REFERENCE_AREAS.keys()),
        default=list(REFERENCE_AREAS.keys())
    )

# Add check equivalent button centered after both columns
_, center_col, _ = st.columns([1, 2, 1])
with center_col:
    check_equivalent = st.button("Check Equivalent", type="primary")

# Calculate and display results only when button is clicked
if check_equivalent:
    total_sq_m = 0.0
    
    # Convert Terai units → m²
    if bigha_val > 0:
        total_sq_m += terai.terai_to_sq_meters(value=bigha_val, from_unit="bigha")
    if kattha_val > 0:
        total_sq_m += terai.terai_to_sq_meters(value=kattha_val, from_unit="kattha")
    if dhur_val > 0:
        total_sq_m += terai.terai_to_sq_meters(value=dhur_val, from_unit="dhur")

    # Convert Hilly units → m²
    if ropani_val > 0:
        total_sq_m += hilly.hilly_to_sq_meters(value=ropani_val, from_unit="ropani")
    if aana_val > 0:
        total_sq_m += hilly.hilly_to_sq_meters(value=aana_val, from_unit="aana")
    if paisa_val > 0:
        total_sq_m += hilly.hilly_to_sq_meters(value=paisa_val, from_unit="paisa")
    if dam_val > 0:
        total_sq_m += hilly.hilly_to_sq_meters(value=dam_val, from_unit="dam")

    # Display the comparisons
    st.subheader("Equivalent Areas")
    cols = st.columns(3)
    for idx, area_name in enumerate(selected_areas):
        area_data = REFERENCE_AREAS[area_name]
        equivalent_count = total_sq_m / area_data["area"]
        
        with cols[idx % 3]:
            st.markdown(f"≈ **{equivalent_count:.2f} {area_name}(s)** ")
            st.image(area_data["image"], width=200, use_container_width=False)
