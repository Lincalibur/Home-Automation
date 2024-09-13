import streamlit as st

st.title("Control Devices")
st.write("Turn devices on or off within your home.")

# Example device controls
st.checkbox("Living Room Lights", value=True)  # True indicates ON state
st.checkbox("Kitchen Lights", value=False)  # False indicates OFF state
st.button("Turn All Off")
