import streamlit as st

st.title("chai maker app")

if st.button("make chai"):
    st.success("chai is being made")

add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("Masala is added to the chai")
    
tea_type = st.radio("pick your chai base: ", ["milk", "water"])
if tea_type == "milk":
    st.write("milk chai is being made")
else:
    st.write("black chai is being made")
    
flavour = st.selectbox("Choose flavour: ", ['adrak','kesar', 'tulsi'])
st.write(f"selected Flavour {flavour}")

sugar = st.slider("sugar level",0,5,2)
st.write(f"sugar levelr {sugar}")

cups = st.number_input("how many cups", min_value=1,max_value=10,step=1)
st.write(f"cups {cups}")

name = st.text_input("Enter your Name")
st.write(f"Welcome {name}")

dob = st.date_input("select your date of birth")
st.write(f"your date of birth is {dob}")