# This file contains all the text for the application, supporting multiple languages.

translations = {
    'language_map': {
        'en': 'English',
        'hi': 'हिन्दी',
        'mr': 'मराठी',
        'gu': 'ગુજરાતી',
        'pa': 'ਪੰਜਾਬੀ',
    },
    'en': {
        # --- Intent Keywords ---
        'intents': {
            'symptom_check': { 'keywords': ['fever', 'cough', 'headache', 'pain', 'ache', 'hurts', 'sick', 'ill', 'stomach', 'diarrhea', 'vomiting', 'rash', 'chills', 'fatigue'], 'handler': '_handle_symptoms' },
            'vaccine_info': { 'keywords': ['vaccine', 'schedule', 'shot', 'immunization', 'jab'], 'handler': '_handle_vaccine_info' },
            'greeting_goodbye': { 'keywords': ['bye', 'exit', 'quit', 'thank you', 'thanks', 'later'], 'handler': '_handle_goodbye' }
        },
        # --- Universal ---
        "fallback_response": "I'm sorry, I'm not equipped to handle that query. I can help with disease symptoms and vaccine information.",
        "symptom_not_recognized": "I can help with symptoms, but I didn't recognize any in your message. Please describe how you are feeling.",
        "consult_doctor_generic": "Based on your symptoms, it would be best to consult with a healthcare professional in Nagpur for an accurate diagnosis.",
        "single_symptom_fever": "A fever can be a symptom of several conditions like **Influenza, Dengue, or Malaria**. Please monitor for other symptoms like **body aches or a rash**. If your temperature is high, it is crucial to see a doctor.",
        "vaccine_schedule_info": "**Vaccination Schedule:**\n- **Polio:** Given at 2, 4, 6-18 months, and a booster at 4-6 years.\n- **MMR:** Two doses, typically at 12-15 months and 4-6 years.",
        "goodbye_message": "You're welcome! Thank you for using Swaasthya sakhi. Stay healthy!",
        # --- Login/Register UI ---
        "app_welcome": "Welcome to Swaasthya sakhi",
        "login_title": "Login to your Account",
        "register_title": "Create a New Account",
        "welcome_prompt": "Please select an option to continue.",
        "username_label": "Username:",
        "password_label": "Password:",
        "login_button": "Login",
        "register_button": "Register",
        "register_success": "Registration successful! You can now log in.",
        "register_failed_exists": "This username already exists.",
        "register_failed_short": "Password must be at least 4 characters.",
        "register_failed_empty": "Username or password cannot be empty.",
        # --- Chat UI & Logic ---
        "chat_title": "Swaasthya sakhi Chatbot",
        "chat_welcome_message": "Welcome, **{username}**! I am your medical assistant. How can I help you today? You can describe your symptoms or ask about vaccine schedules.",
    },
    'hi': {
         # --- Intent Keywords (Hindi) ---
        'intents': {
            'symptom_check': { 'keywords': ['बुखार', 'खांसी', 'सिरदर्द', 'दर्द', 'बीमार', 'पेट', 'दस्त', 'उल्टी', 'रैश', 'ठंड लगना', 'थकान'], 'handler': '_handle_symptoms' },
            'vaccine_info': { 'keywords': ['वैक्सीन', 'टीका', 'शेड्यूल', 'टीकाकरण'], 'handler': '_handle_vaccine_info' },
            'greeting_goodbye': { 'keywords': ['बाय', 'धन्यवाद', 'शुक्रिया'], 'handler': '_handle_goodbye' }
        },
        # --- Hindi Translations ---
        "fallback_response": "क्षमा करें, मैं उस प्रश्न को संभालने में सक्षम नहीं हूं।",
        "symptom_not_recognized": "मैं लक्षणों में मदद कर सकता हूं, लेकिन मुझे आपके संदेश में कोई पहचानने योग्य लक्षण नहीं मिला।",
        "consult_doctor_generic": "आपके लक्षणों के आधार पर, सटीक निदान के लिए नागपुर में एक स्वास्थ्य देखभाल पेशेवर से परामर्श करना सबसे अच्छा होगा।",
        "single_symptom_fever": "बुखार कई स्थितियों का लक्षण हो सकता है जैसे इन्फ्लूएंजा, डेंगू, या मलेरिया। कृपया शरीर में दर्द या दाने जैसे अन्य लक्षणों पर ध्यान दें।",
        "vaccine_schedule_info": "**टीकाकरण अनुसूची:**\n- **पोलियो:** 2, 4, 6-18 महीने पर दिया जाता है।\n- **एमएमआर:** दो खुराक, आमतौर पर 12-15 महीने और 4-6 साल में।",
        "goodbye_message": "आपका स्वागत है! धन्यवाद।",
        "app_welcome": "मेडिकल असिस्ट में आपका स्वागत है",
        "login_title": "अपने खाते में लॉगिन करें",
        "register_title": "नया खाता बनाएं",
        "welcome_prompt": "जारी रखने के लिए कृपया एक विकल्प चुनें।",
        "username_label": "उपयोगकर्ता नाम:",
        "password_label": "पासवर्ड:",
        "login_button": "लॉगिन करें",
        "register_button": "रजिस्टर करें",
        "register_success": "पंजीकरण सफल! अब आप लॉगिन कर सकते हैं।",
        "register_failed_exists": "यह उपयोगकर्ता नाम पहले से मौजूद है।",
        "register_failed_short": "पासवर्ड कम से कम 4 अक्षरों का होना चाहिए।",
        "register_failed_empty": "उपयोगकर्ता नाम या पासवर्ड खाली नहीं हो सकता।",
        "chat_title": "Swaasthya sakhi",
        "chat_welcome_message": "स्वागत है, **{username}**! मैं आपका मेडिकल सहायक हूं। आप अपने लक्षण बता सकते हैं।",
    },
    # Add other languages ('mr', 'gu', 'pa') here with their translated 'intents' and text.
}