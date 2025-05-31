import streamlit as st

st.title("hello1")
st.subheader("hello2")
st.text("hello3")
st.write("hello4")


hello = st.selectbox("your fav hello: ",["hello1","hello2","hello3"])

st.write(f"Your choose {hello}. Excellent choose")

st.success("your hello has been brewed")