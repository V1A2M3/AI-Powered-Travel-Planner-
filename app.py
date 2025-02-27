import os
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from googletrans import Translator
from dotenv import load_dotenv

# Load API Keys
load_dotenv()
GOOGLE_GENAI_API_KEY = os.getenv("AIzaSyBp9HTFCVniu253dllKqReHaPzE_BvjSDU")

# Set up Streamlit UI
st.set_page_config(page_title="AI-Travel Planner", layout="centered", page_icon="✈️")
st.title("🌍 AI-Travel Planner")
st.write("Enter details to get estimated travel costs for various travel modes (cab, train, bus, flights).")

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

# Select Language
selected_lang = st.selectbox("🌐 Choose Your Language", list(INDIAN_LANGUAGES.keys()))
target_lang_code = INDIAN_LANGUAGES[selected_lang]

# Function to Translate Text
def translate_text(text, target_lang):
    try:
        return translator.translate(text, dest=target_lang).text
    except:
        return text  # Return original text if translation fails

# User Input Fields
source = st.text_input(translate_text("📍 Source:", target_lang_code))
destination = st.text_input(translate_text("📍 Destination:", target_lang_code))

if st.button(translate_text("Get Travel Plan", target_lang_code)):
    if source and destination:
        with st.spinner(translate_text("Compiling all travel options ....", target_lang_code)):
            
            # AI Chat Model Prompt
            chat_template = ChatPromptTemplate.from_messages([
                SystemMessagePromptTemplate.from_template("""
                You are an AI-powered travel assistant that provides the best travel options between two locations.
                Include cab, bus, train, and flight options. For each option, provide:
                - Mode of transport
                - Estimated price
                - Travel time
                - Additional details (stops, layovers, etc.)
                - Best recommended travel mode & time
                """),
                HumanMessagePromptTemplate.from_template("Find travel options from {source} to {destination} with estimated costs.")
            ])
            
            # Google Gemini AI Model
            chat_model = ChatGoogleGenerativeAI(api_key=GOOGLE_GENAI_API_KEY, model="gemini-2.0-pro")
            parser = StrOutputParser()
            
            # AI Chat Chain
            chain = chat_template | chat_model | parser
            
            # Process User Input
            raw_input = {"source": source, "destination": destination}
            response = chain.invoke(raw_input)
            
            # Translate Response
            translated_response = translate_text(response, target_lang_code)
            
            # Display Travel Options
            st.success(translate_text("✅ Estimated Travel Options and Costs:", target_lang_code))
            travel_modes = translated_response.split("\n")
            for mode in travel_modes:
                st.markdown(mode)
    else:
        st.error(translate_text("❌ Error! Please enter both source and destination", target_lang_code))
