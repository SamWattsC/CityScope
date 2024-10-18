import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="CityScope",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar menu options
st.sidebar.title("CityScope Menu")
st.sidebar.header("Explore Your City")
menu_options = ["Home", "Weather", "Crime", "Top Restaurants", "Public Transport", "Events", "Healthcare", "Education"]
menu_choice = st.sidebar.radio("Select a category:", menu_options)

# Main page layout
st.title("Welcome to CityScope! 🏙️")
st.subheader("Your one-stop portal for all city information")

# Display different sections based on menu selection
if menu_choice == "Home":
    st.write("""
    ### What can you find here?
    CityScope brings you the most important information about your city, including:
    
    - Current weather and forecasts
    - Crime statistics and safety alerts
    - Top restaurants to try
    - Public transportation updates
    - Local events and festivals
    - Healthcare facilities and services
    - Education and schools information
    
    Explore the categories on the left to get started!
    """)
elif menu_choice == "Weather":
    st.write("### Weather Information")
    st.info("Weather data will be shown here.")
elif menu_choice == "Crime":
    st.write("### Crime Statistics")
    st.info("Crime reports and data will be shown here.")
elif menu_choice == "Top Restaurants":
    st.write("### Top Restaurants in Your City")
    st.info("Restaurant recommendations will be shown here.")
elif menu_choice == "Public Transport":
    st.write("### Public Transport Information")
    st.info("Updates on buses, trains, and traffic will be shown here.")
elif menu_choice == "Events":
    st.write("### Upcoming Events")
    st.info("List of upcoming city events will be shown here.")
elif menu_choice == "Healthcare":
    st.write("### Healthcare Facilities")
    st.info("Information on hospitals and clinics will be shown here.")
elif menu_choice == "Education":
    st.write("### Education and Schools")
    st.info("Details about schools and universities will be shown here.")

# Footer
st.markdown("---")
st.markdown("📍 *CityScope – Your window into city life!*")
