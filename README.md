🛫 AI-Powered Travel Planner (Multi-Language & AI Recommendations)

🌍 Find the best travel options between any two locations using AI-powered recommendations and real-time travel information.

✨ Supports multiple Indian & global languages and integrates Google Places API for real-time city/place details.

🚀 Features
✅ Multi-Language Support: Hindi, Tamil, Telugu, Bengali, Marathi, Kannada, Malayalam, Gujarati, Punjabi & more!
✅ Real-Time Travel Options: Flight ✈️, Train 🚆, Bus 🚌, Cab 🚖 (Replace with actual APIs)
✅ AI-Powered Recommendations: Smart suggestions based on cost, convenience, and travel time.
✅ Google Places API Integration: Get ratings, addresses, and types of locations.
✅ User-Friendly Interface: Clean & simple Streamlit web application.

📌 Demo
🔗 Live App: AI Travel Planner
🔗 GitHub Repo: V1A2M3/AI-Powered-Travel-Planner

📥 Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/V1A2M3/AI-Powered-Travel-Planner-.git
cd AI-Powered-Travel-Planner-
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Set Up API Keys
This app requires:

Google Generative AI API Key (for AI responses)
Google Places API Key (for real-time place information)
👉 Create a .env file and add:

ini
Copy
Edit
GOOGLE_GENAI_API_KEY=your_google_genai_api_key
GOOGLE_PLACES_API_KEY=your_google_places_api_key
4️⃣ Run the App Locally
bash
Copy
Edit
streamlit run app.py
✔️ Your app will be live on http://localhost:8501/

🔗 Deployment on Streamlit Cloud
1️⃣ Push Your Code to GitHub
bash
Copy
Edit
git add .
git commit -m "Initial commit: AI Travel Planner"
git push origin main
2️⃣ Deploy on Streamlit
Go to Streamlit Cloud
Click New App
Select your GitHub Repository
Set the Main File Path → app.py
Click Deploy 🚀
✅ Your AI-powered travel planner is now live! 🎉

🌍 Supported Languages
This app supports multiple Indian & global languages, including:

English
Hindi (हिन्दी)
Tamil (தமிழ்)
Telugu (తెలుగు)
Bengali (বাংলা)
Marathi (मराठी)
Kannada (ಕನ್ನಡ)
Malayalam (മലയാളം)
Gujarati (ગુજરાતી)
Punjabi (ਪੰਜਾਬੀ)
🔹 You can easily add more languages by modifying INDIAN_LANGUAGES in app.py.

🛠 Tech Stack
Frontend: Streamlit 🎨
AI Engine: Google Generative AI 🧠
Backend Framework: LangChain 🔗
Translation API: Google Translate 🌎
Real-time Data: Google Places API 📍
🔗 API Configuration
1️⃣ Get Google Generative AI API Key
Go to Google AI Console
Generate an API Key
Add it to .env file:
ini
Copy
Edit
GOOGLE_GENAI_API_KEY=your_google_genai_api_key
2️⃣ Get Google Places API Key
Go to Google Cloud Console
Enable Google Places API
Generate an API Key
Add it to .env file:
ini
Copy
Edit
GOOGLE_PLACES_API_KEY=your_google_places_api_key

🚀 How It Works
✅ Step 1: Select your language from the dropdown menu.
✅ Step 2: Enter source & destination locations.
✅ Step 3: The app fetches:

📍 Real-time place details (Ratings, Address, etc.)
✈️ Flight, Train, Bus, Cab options (Price & Duration)
🤖 AI-Powered travel recommendation
✅ Step 4: View translated results in your selected language.

🔮 Future Enhancements
🚀 Integrate Real-Time Travel APIs
💬 Add Voice Input (Speech-to-Text)
📍 Show Map View for Travel Routes
🧑‍💻 Mobile App Version (React Native)

📝 Contributing
Want to improve this project? Contributions are welcome!

Fork the repository
Create a new branch (feature-branch)
Commit changes (git commit -m "Added feature")
Push to GitHub (git push origin feature-branch)
Open a Pull Request
📩 Contact me at your-email@example.com for any suggestions or issues.

📜 License
This project is open-source and available under the MIT License.

🔗 GitHub Repository: V1A2M3/AI-Powered-Travel-Planner
🚀 Enjoy hassle-free travel planning with AI! 😊
