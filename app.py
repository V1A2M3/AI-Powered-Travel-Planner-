import streamlit as st
import google.generativeai as genai
from langchain.llms import OpenAI
from googletrans import Translator

# Configure Google GenAI
GOOGLE_GENAI_API_KEY = "AIzaSyBp9HTFCVniu253dllKqReHaPzE_BvjSDU"
genai.configure(api_key=GOOGLE_GENAI_API_KEY)

# Initialize Translator
translator = Translator()

# Supported Indian Languages
INDIAN_LANGUAGES = {
    "English": "en",
    "Hindi (हिन्दी)": "hi",
    "Tamil (தமிழ்)": "ta",
    "Telugu (తెలుగు)": "te",
    "Bengali (বাংলা)": "bn",
    "Marathi (मराठी)": "mr",
    "Kannada (ಕನ್ನಡ)": "kn",
    "Malayalam (മലയാളം)": "ml",
    "Gujarati (ગુજરાતી)": "gu",
    "Punjabi (ਪੰਜਾਬੀ)": "pa"
}

# Translation Function
def translate_text(text, target_lang):
    try:
        return translator.translate(text, dest=target_lang).text
    except:
        return text  # If translation fails, return original text

# --- Step 1: Language Selection ---
st.title("🌍 Select Your Language | अपनी भाषा चुनें | உங்கள் மொழியைத் தேர்ந்தெடுக்கவும்")

selected_lang = st.selectbox("Choose Language", options=list(INDIAN_LANGUAGES.keys()))

if selected_lang:
    target_lang_code = INDIAN_LANGUAGES[selected_lang]
    st.success(translate_text("Language Selected Successfully!", target_lang_code))

    # --- Step 2: Travel Planner UI ---
    st.title(translate_text("🛫 AI-Powered Travel Planner", target_lang_code))

    source = st.text_input(translate_text("Enter Source Location", target_lang_code), placeholder="Chennai")
    destination = st.text_input(translate_text("Enter Destination", target_lang_code), placeholder="Mumbai")

    if st.button(translate_text("Get Travel Options", target_lang_code)):
        if source and destination:
            # Dummy travel options (Replace with real API calls)
            travel_options = {
                "Flight": {"price": "₹20,000", "duration": "2h 30m"},
                "Train": {"price": "₹1,200", "duration": "5h"},
                "Bus": {"price": "₹800", "duration": "7h"},
                "Cab": {"price": "₹3,000", "duration": "3h"}
            }

            # Display Travel Options (Translated)
            st.subheader(translate_text("🚀 Available Travel Options", target_lang_code))
            for mode, details in travel_options.items():
                mode_translated = translate_text(mode, target_lang_code)
                price_translated = translate_text("Price", target_lang_code)
                duration_translated = translate_text("Duration", target_lang_code)
                st.write(f"**{mode_translated}** - {price_translated}: {details['price']}, {duration_translated}: {details['duration']}")

            # AI Recommendation (Translated)
            st.subheader(translate_text("🤖 AI Recommendation", target_lang_code))
            ai_recommendation = "Based on cost and convenience, Flight is the best option."
            ai_recommendation_translated = translate_text(ai_recommendation, target_lang_code)
            st.write(ai_recommendation_translated)
        else:
            st.warning(translate_text("Please enter both source and destination.", target_lang_code))
