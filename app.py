import streamlit as st
import plotly.express as px

# --- Page Config ---
st.set_page_config(page_title="TruthLensAI", layout="wide", page_icon="📰")

# --- Custom CSS for dark theme and styling ---
st.markdown("""
    <style>
    /* Dark background */
    body, .main {
        background-color: #0d0d0d;
        color: #ffffff;
        font-family: 'Arial', sans-serif;
    }
    
    /* Header style */
    .stButton>button {
        background-color: #ff6f3c;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1.2em;
        border: none;
    }

    .stButton>button:hover {
        background-color: #ff4500;
        color: white;
    }

    /* Input boxes */
    div.stTextInput>div>input {
        background-color: #1a1a1a;
        color: white;
        border: 1px solid #ff6f3c;
        border-radius: 6px;
        padding: 0.5em;
    }

    /* Hide Streamlit footer */
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- Title & description ---
st.title("TruthLensAI")
st.subheader("Fake News Detection & Analytics")
st.markdown("Enter the platform and your gender to visualize content trends.")

# --- User Inputs ---
col1, col2 = st.columns(2)
with col1:
    platform = st.selectbox("Select Platform", ["Instagram", "YouTube", "Facebook"])
with col2:
    gender = st.selectbox("Select Gender", ["Male", "Female", "Other"])

# --- Pie chart ---
data = {
    "Platform": ["Instagram", "YouTube", "Facebook"],
    "Percentage": [10, 50, 40]
}

fig = px.pie(data, names="Platform", values="Percentage",
             color_discrete_sequence=["#ff6f3c", "#ffa94d", "#ffffff"])
fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  font_color='white')

st.plotly_chart(fig, use_container_width=True)

# --- Optional floating-like design element ---
st.markdown("""
<div style="position:absolute; top:200px; right:50px; width:100px; height:100px; 
background: linear-gradient(135deg, #ff6f3c, #ffa94d); border-radius:50%; opacity:0.7;">
</div>
""", unsafe_allow_html=True)

