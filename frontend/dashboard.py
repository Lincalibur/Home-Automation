import streamlit as st
from utils.camera_feed import get_camera_feed
from utils.server_events import get_upcoming_events

st.set_page_config(page_title="Home Automation Dashboard", layout="wide")

st.title("Home Automation Dashboard")
st.subheader("Upcoming Events")

# Fetch upcoming events from the server (you can replace this with real data)
events = get_upcoming_events()

if events:
    for event in events:
        st.write(f"Event: {event['name']} | Time: {event['time']}")
else:
    st.write("No upcoming events.")

# Display live camera feed from a predefined source
st.subheader("Live Camera Feed")
camera_feed_url = get_camera_feed()
if camera_feed_url:
    st.video(camera_feed_url)
else:
    st.write("No live feed available.")
