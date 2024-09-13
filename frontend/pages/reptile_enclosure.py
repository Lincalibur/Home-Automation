import streamlit as st

st.title("Reptile Enclosure Monitoring")
st.write("Monitor temperature, humidity, lighting, and live feed for your reptile pet.")

# Mock data for enclosure
temperature = 28.5  # degrees Celsius
humidity = 65  # percentage
heat_lamp_status = st.session_state.get("heat_lamp_status", "Off")  # Heat lamp toggle status

st.metric("Temperature (°C)", temperature)
st.metric("Humidity (%)", humidity)

# Heat lamp toggle button
if st.button(f"Turn Heat Lamp {('Off' if heat_lamp_status == 'On' else 'On')}"):
    if heat_lamp_status == "On":
        st.session_state["heat_lamp_status"] = "Off"
        st.success("Heat lamp turned off!")
    else:
        st.session_state["heat_lamp_status"] = "On"
        st.success("Heat lamp turned on!")

# Live Camera Feed for enclosure
st.subheader("Live Camera Feed")
camera_feed_url = "https://www.youtube.com/embed/live_stream?channel=YOUR_REPTILE_ENCLOSURE_CHANNEL"
if camera_feed_url:
    st.video(camera_feed_url)
else:
    st.write("No live feed available.")
