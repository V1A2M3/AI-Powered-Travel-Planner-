import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from deep_translator import GoogleTranslator

# Set up Streamlit UI
st.set_page_config(page_title="AI-Travel Planner", layout="centered", page_icon="✈️")
st.title("🌍 AI-Travel Planner")
st.write("Enter details to get estimated travel costs for various travel modes (cab, train, bus, flights).")

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
        return GoogleTranslator(source="auto", target=target_lang).translate(text)
    except:
        return text  # Return original text if translation fails

# User Input Fields
source = st.text_input(translate_text("📍 Source:", target_lang_code))
destination = st.text_input(translate_text("📍 Destination:", target_lang_code))

if st.button(translate_text("Get Travel Plan", target_lang_code)):
    if source and destination:
        with st.spinner(translate_text("Compiling all travel options ....", target_lang_code)):
            
            # AI Chat Model Prompt
            chat_template = ChatPromptTemplate(messages=[
                ("system", """
                You are an AI-powered travel assistant designed to help users find the best travel options between a given source and destination.
                Upon receiving the source and destination, generate a list of travel options, including cab, bus, train, and flight choices. 
                For each option, provide the following details: mode of transport, estimated price, travel time, and relevant details like stops or transfers in at least 50 words.
                Present the information in a clear format for easy comparison. 
                Focus on accuracy, cost-effectiveness, and convenience, ensuring that the user can make an informed decision based on their preferences.
                Keep the output concise, ensuring clarity and ease of understanding.
                Do not include any output in table format; keep all output as strings. 
                Recommend the best possible travel mode and the best time to travel at the end.
                """),
                ("human", "Find travel options from {source} to {destination} along with estimated costs.")
            ])
            
            # Google Gemini AI Model
            chat_model = ChatGoogleGenerativeAI(api_key="AIzaSyAPECPvgOQcYhZ4-Ch-mt17y4f4Xax7u4I", model="gemini-2.0-flash-exp")
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
