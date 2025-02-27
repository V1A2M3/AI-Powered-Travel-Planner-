
import os
import streamlit as st
import google.generativeai as genai
import requests
from langchain.chat_models import ChatOpenAI
from googletrans import Translator
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
GOOGLE_GENAI_API_KEY = os.getenv("GOOGLE_GENAI_API_KEY")
GOOGLE_PLACES_API_KEY = os.getenv("GOOGLE_PLACES_API_KEY")
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
SKYSCANNER_API_KEY = os.getenv("SKYSCANNER_API_KEY")
IRCTC_API_KEY = os.getenv("IRCTC_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configure Google Generative AI
if GOOGLE_GENAI_API_KEY:
    genai.configure(api_key=GOOGLE_GENAI_API_KEY)

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
    if not GOOGLE_PLACES_API_KEY:
        return None

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

# Function to fetch real-time travel options
def fetch_travel_options(source, destination):
    travel_data = {}

    # Google Maps API (Cab Distance & Estimated Fare)
    maps_url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={source}&destinations={destination}&key={GOOGLE_MAPS_API_KEY}"
    maps_response = requests.get(maps_url).json()

    if "rows" in maps_response and maps_response["rows"]:
        elements = maps_response["rows"][0]["elements"][0]
        if elements.get("status") == "OK":
            travel_data["Cab"] = {
                "price": "₹" + str(int(elements["distance"]["value"] / 1000 * 10)),  # Approx ₹10/km
                "duration": elements["duration"]["text"]
            }

    # Skyscanner API (Flights)
    flights_url = f"https://partners.api.skyscanner.net/apiservices/browseroutes/v1.0/IN/INR/en-US/{source}/{destination}/anytime?apikey={SKYSCANNER_API_KEY}"
    flights_response = requests.get(flights_url).json()

    if "Quotes" in flights_response and flights_response["Quotes"]:
        cheapest_flight = flights_response["Quotes"][0]
        travel_data["Flight"] = {
            "price": "₹" + str(cheapest_flight["MinPrice"]),
            "duration": "Approx 2h"
        }

    # IRCTC API (Trains)
    irctc_url = f"https://api.railwayapi.com/v2/between/source/{source}/dest/{destination}/apikey/{IRCTC_API_KEY}/"
    irctc_response = requests.get(irctc_url).json()

    if "trains" in irctc_response and irctc_response["trains"]:
        first_train = irctc_response["trains"][0]
        travel_data["Train"] = {
            "price": "₹" + str(int(first_train["fare"])),
            "duration": first_train["travel_time"]
        }

    return travel_data

# AI Travel Recommendation
def generate_travel_recommendations(source, destination):
    if not OPENAI_API_KEY:
        return "⚠ OpenAI API Key is missing. Please set it in your environment."

    prompt = f"Suggest best travel options from {source} to {destination}, considering cost, convenience, and safety."

    try:
        model = ChatOpenAI(temperature=0.7, openai_api_key=OPENAI_API_KEY)
        response = model.predict(prompt)
        return response
    except Exception as e:
        return f"⚠ Error generating AI recommendations: {str(e)}"

# Translation Function
def translate_text(text, target_lang):
    try:
        return translator.translate(text, dest=target_lang).text
    except:
        return text

# --- Step 1: Language Selection ---
st.title("🌍 AI-Powered Travel Planner")
selected_lang = st.selectbox("Choose Language", options=list(INDIAN_LANGUAGES.keys()))
target_lang_code = INDIAN_LANGUAGES[selected_lang]

if selected_lang:
    st.success(translate_text("Language Selected Successfully!", target_lang_code))

    # --- Step 2: Travel Planner UI ---
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
                st.write(f"{translate_text('Source:', target_lang_code)}** {source_info['name']} ({source_info['address']}) - ⭐ {source_info['rating']}")
            if destination_info:
                st.write(f"{translate_text('Destination:', target_lang_code)}** {destination_info['name']} ({destination_info['address']}) - ⭐ {destination_info['rating']}")

            # Display Travel Options
            st.subheader(translate_text("🚀 Available Travel Options", target_lang_code))
            for mode, details in travel_options.items():
                mode_translated = translate_text(mode, target_lang_code)
                price_translated = translate_text("Price", target_lang_code)
                duration_translated = translate_text("Duration", target_lang_code)
                st.write(f"{mode_translated}** - {price_translated}: {details['price']}, {duration_translated}: {details['duration']}")

            # AI Recommendation
            st.subheader(translate_text("🤖 AI Recommendation", target_lang_code))
            ai_recommendation = generate_travel_recommendations(source, destination)
            ai_recommendation_translated = translate_text(ai_recommendation, target_lang_code)
            st.write(ai_recommendation_translated)
        else:
            st.warning(translate_text("Please enter both source and destination.", target_lang_code))
