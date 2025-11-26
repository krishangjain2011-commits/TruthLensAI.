import streamlit as st

# ---------------- UI Styling ----------------
st.set_page_config(page_title="TruthLensAI", layout="centered")

st.markdown("""
    <h1 style="text-align:center; color:#2E86C1; font-family:Arial;">
        TruthLensAI
    </h1>
    <p style="text-align:center; font-size:18px; color:#555;">
        Analyse headlines with clarity and precision.
    </p>
    <hr>
""", unsafe_allow_html=True)

# ---------------- Input Section ----------------
st.subheader("Enter the required details")

headline = st.text_input("Headline received:")
gender = st.selectbox("Your gender:", ["Male", "Female", "Other"])
platform = st.selectbox("Platform where you found this headline:", 
                        ["Instagram", "YouTube", "Facebook", "X (Twitter)", "Others"])

submit = st.button("Analyse")

if submit:
    st.success("Inputs received successfully.")
    st.write("**Headline:**", headline)
    st.write("**Gender:**", gender)
    st.write("**Platform:**", platform)
