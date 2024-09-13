import streamlit as st

st.title("Order Coffee from Multiple Machines")
st.write("Manage multiple coffee machines and order from your favorite one.")

# Add coffee machines to a list
if "coffee_machines" not in st.session_state:
    st.session_state["coffee_machines"] = ["Office Coffee Machine", "Kitchen Coffee Machine"]

# Show list of available coffee machines
st.subheader("Available Coffee Machines")
for machine in st.session_state["coffee_machines"]:
    st.write(f"- {machine}")

# Add new coffee machines
new_machine = st.text_input("Add a new coffee machine")
if st.button("Add Coffee Machine"):
    if new_machine:
        st.session_state["coffee_machines"].append(new_machine)
        st.success(f"Added new coffee machine: {new_machine}")
    else:
        st.warning("Please enter a valid coffee machine name.")

# Select coffee machine and type of coffee
selected_machine = st.selectbox("Select Coffee Machine", st.session_state["coffee_machines"])
coffee_options = ["Espresso", "Latte", "Cappuccino"]
selected_coffee = st.selectbox("Choose your coffee", coffee_options)

# Order coffee
if st.button(f"Order {selected_coffee} from {selected_machine}"):
    st.success(f"Ordered {selected_coffee} from {selected_machine} successfully!")
