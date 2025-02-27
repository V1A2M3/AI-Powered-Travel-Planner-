import streamlit as st
import google.generativeai as genai
import requests
from langchain.llms import OpenAI
from googletrans import Translator

# Configure Google GenAI (Replace with your API key)
GOOGLE_GENAI_API_KEY = "AIzaSyBp9HTFCVniu253dllKqReHaPzE_BvjSDU"
genai.configure(api_key=GOOGLE_GENAI_API_KEY)

# Google Places API (For place info, replace with your key)
GOOGLE_PLACES_API_KEY = "AIzaSyBp9HTFCVniu253dllKqReHaPzE_BvjSDU"

# Initialize Translator
translator = Translator()

# Supported Languages
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

# Function to fetch place information using Google Places API
def get_place_info(place):
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={place}&key={GOOGLE_PLACES_API_KEY}"
    response = requests.get(url).json()
    if response.get("results"):
        place_info = response["results"][0]
        return {
            "name": place_info.get("name"),
            "address": place_info.get("formatted_address"),
            "rating": place_info.get("rating", "N/A"),
            "types": ", ".join(place_info.get("types", []))
        }
    return None

# Dummy function for travel options (Replace with API calls)
def fetch_travel_options(source, destination):
    return {
        "Flight": {"price": "₹20,000", "duration": "2h 30m"},
        "Train": {"price": "₹1,200", "duration": "5h"},
        "Bus": {"price": "₹800", "duration": "7h"},
        "Cab": {"price": "₹3,000", "duration": "3h"}
    }

# AI Travel Recommendation (LangChain)
def generate_travel_recommendations(source, destination):
    prompt = f"Suggest best travel options from {source} to {destination}, considering cost and convenience in India."
    model = OpenAI(temperature=0.7)
    return model(prompt)

# Translation Function
def translate_text(text, target_lang):
    try:
        return translator.translate(text, dest=target_lang).text
    except:
        return text  # Return original text if translation fails

# Step 1: Language Selection
st.title("🌍 AI-Powered Travel Planner")
selected_lang = st.selectbox("Choose Language", options=list(INDIAN_LANGUAGES.keys()))
target_lang_code = INDIAN_LANGUAGES[selected_lang]

if selected_lang:
    st.success(translate_text("Language Selected Successfully!", target_lang_code))

    # Step 2: Travel Planner UI
    st.title(translate_text("🛫 Travel Options", target_lang_code))

    source = st.text_input(translate_text("Enter Source Location", target_lang_code), placeholder="Chennai")
    destination = st.text_input(translate_text("Enter Destination", target_lang_code), placeholder="Mumbai")

    if st.button(translate_text("Get Travel Options", target_lang_code)):
        if source and destination:
            travel_options = fetch_travel_options(source, destination)

            # Place Information
            st.subheader(translate_text("📍 Place Information", target_lang_code))
            source_info = get_place_info(source)
            destination_info = get_place_info(destination)
            if source_info:
                st.write(f"**{translate_text('Source:', target_lang_code)}** {source_info['name']} ({source_info['address']}) - ⭐ {source_info['rating']}")
            if destination_info:
                st.write(f"**{translate_text('Destination:', target_lang_code)}** {destination_info['name']} ({destination_info['address']}) - ⭐ {destination_info['rating']}")

            # Display Travel Options
            st.subheader(translate_text("🚀 Available Travel Options", target_lang_code))
            for mode, details in travel_options.items():
                mode_translated = translate_text(mode, target_lang_code)
                price_translated = translate_text("Price", target_lang_code)
                duration_translated = translate_text("Duration", target_lang_code)
                st.write(f"**{mode_translated}** - {price_translated}: {details['price']}, {duration_translated}: {details['duration']}")

            # AI Recommendation
            st.subheader(translate_text("🤖 AI Recommendation", target_lang_code))
            ai_recommendation = generate_travel_recommendations(source, destination)
            ai_recommendation_translated = translate_text(ai_recommendation, target_lang_code)
            st.write(ai_recommendation_translated)
        else:
            st.warning(translate_text("Please enter both source and destination.", target_lang_code))
