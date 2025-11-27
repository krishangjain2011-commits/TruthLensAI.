import streamlit as st

# ------------------- PAGE CONFIG -------------------
st.set_page_config(page_title="TruthLensAI", layout="wide")

# ------------------- CUSTOM CSS -------------------
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(to bottom right, #1a1a1a, #000000);
            color: white;
        }

        .glass-box {
            background: rgba(255, 255, 255, 0.15);
            padding: 25px;
            border-radius: 15px;
            margin-top: 20px;
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border: 1px solid rgba(255,255,255,0.2);
        }

        .heading {
            font-size: 45px;
            font-weight: 800;
            color: white;
            text-align: center;
        }

        .subtext {
            font-size: 20px;
            text-align: center;
            color: #dcdcdc;
        }

        .question-box {
            background: rgba(255,255,255,0.10);
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
            cursor: pointer;
            border: 1px solid rgba(255,255,255,0.2);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------- SIDEBAR -------------------
page = st.sidebar.radio("Navigation", ["Home", "Fake News Detector"])

# ------------------- HOME PAGE -------------------
if page == "Home":
    st.markdown('<div class="heading">TruthLensAI</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtext">Your companion for spotting misinformation 🔍</div>', unsafe_allow_html=True)

    st.markdown("<div class='glass-box'>", unsafe_allow_html=True)

    st.markdown(
        """
        ### ❗ How to Use

        **1️⃣ Go to the Fake News Detector screen using the menu on the left.**  
        **2️⃣ Enter the headline you want to verify.**  
        **3️⃣ Select gender & platform.**  
        **4️⃣ Hit ‘Analyze News’ to get instant insights.**
        """
    )

    st.markdown("<br><hr><br>", unsafe_allow_html=True)

    st.markdown(
        """
        ### ❓ Frequently Asked  
        Click on a question to reveal the answer.
        """
    )

    # --- FAQ Section ---
    faqs = {
        "🔎 What does this app do?": 
        "It analyzes your news headline and predicts whether it seems misleading or questionable.",

        "⚙️ How does the detector work?":
        "It uses machine learning + text analysis to understand patterns of misinformation.",

        "📊 Why do you need gender & platform?":
        "These are for academic dataset-based personalization (optional).",

        "🤖 Is this 100% accurate?":
        "Nah bestie, even AI has bad days. It gives probability-based insights."
    }

    for q, a in faqs.items():
        if st.button(q, key=q):
            st.info(a)

    st.markdown("</div>", unsafe_allow_html=True)

# ------------------- FAKE NEWS DETECTOR (unchanged) -------------------
else:
    st.title("Fake News Detector 📰")

    headline = st.text_input("Enter News Headline")
    gender = st.selectbox("Select Gender", ["Male", "Female", "Other"])
    platform = st.selectbox("Select Platform", ["Instagram", "YouTube", "Facebook"])

    if st.button("Analyze News"):
        st.success("✨ Analysis complete! (Dummy result for now)")
