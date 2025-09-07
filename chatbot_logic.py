from database import Database
from Localization import translations
from disease_data import DISEASES 

class Chatbot:
    """
    The core logic for the chatbot. This version corrects the disease name recognition logic.
    """
    
    def __init__(self):
        """Initializes the chatbot and pre-loads known disease names from the data."""
        self.db = Database()
        self.language = 'en'
        self.user = None
        self.state = "AWAITING_LOGIN"
        
        self.known_disease_names = []
        if 'en' in DISEASES:
            self.known_disease_names = [data.get('name', '').lower() for key, data in DISEASES.get('en', {}).items()]

    def trans(self, key):
        lang_dict = translations.get(self.language, translations.get('en', {}))
        return lang_dict.get(key, f"<{key}>")

    def set_language(self, lang_code):
        if lang_code in translations.get('language_map', {}):
            self.language = lang_code
            return True
        return False

    def register_user(self, username, password):
        if len(password) < 4:
            return translations.get('en', {}).get('register_failed_short')
        if self.db.add_user(username, password):
            return self.trans('register_success')
        else:
            return self.trans('register_failed_exists')

    def login_user(self, username, password):
        if self.db.check_user(username, password):
            self.user = username
            self.state = "LOGGED_IN"
            return True
        return False

    def get_initial_chat_message(self):
        return self.trans('chat_welcome_message').replace('{username}', self.user)

    def get_response(self, user_input):
        if self.state != "LOGGED_IN":
            return "Error: User not properly logged in."
        
        user_input = user_input.lower().strip()
        
        # --- THIS IS THE CORRECTED LOGIC ---
        # It now checks if the USER'S TEXT is IN any of the known disease names.
        # e.g., is "dengue" in "dengue fever"? YES.
        if any(user_input in disease_name for disease_name in self.known_disease_names if disease_name and user_input):
            return self._handle_disease_query(user_input)

        # The old intent-checking logic for symptoms, etc.
        current_intents = self.trans('intents')
        if isinstance(current_intents, dict):
            for intent_name, intent_data in current_intents.items():
                if any(keyword in user_input for keyword in intent_data.get('keywords', [])):
                    handler_method = getattr(self, intent_data.get('handler'), None)
                    if handler_method:
                        return handler_method(user_input)

        return self.trans('fallback_response')
    
    def _handle_disease_query(self, text):
        """
        When a user mentions a disease name, this finds the advice.
        """
        disease_data_en = DISEASES.get('en', {})
        for disease_key, disease_data in disease_data_en.items():
            # Find which disease name the user's text matched
            disease_name = disease_data.get('name', '').lower()
            if disease_name and text in disease_name:
                return disease_data.get('advice', self.trans('fallback_response'))
        return self.trans('fallback_response') # Failsafe

    def _handle_symptoms(self, text):
        """Analyzes a description of symptoms to find the most likely disease."""
        current_disease_data = DISEASES.get(self.language, DISEASES.get('en', {}))
        scores = {}
        mentioned_symptoms = set()

        for disease, data in current_disease_data.items():
            for keyword in data.get('keywords', []):
                if keyword in text:
                    mentioned_symptoms.add(keyword)

        if not mentioned_symptoms:
            return self.trans('symptom_not_recognized')

        # Logic for single symptoms
        if len(mentioned_symptoms) == 1:
            symptom = list(mentioned_symptoms)[0]
            if any(k in symptom for k in ['fever', 'बुखार']): return self.trans('single_symptom_fever')
            if any(k in symptom for k in ['headache', 'सिरदर्द']): return current_disease_data.get('migraine', {}).get('advice', self.trans('consult_doctor_generic'))
            if any(k in symptom for k in ['cough', 'खांसी']): return current_disease_data.get('common_cold', {}).get('advice', self.trans('consult_doctor_generic'))
        
        # Scoring logic for multiple symptoms
        for disease, data in current_disease_data.items():
            match_count = sum(1 for keyword in data.get('keywords', []) if keyword in mentioned_symptoms)
            if match_count > 0:
                keywords_len = len(data.get('keywords', []))
                if keywords_len > 0:
                    scores[disease] = match_count / keywords_len

        if not scores:
            return self.trans('consult_doctor_generic')

        best_match_disease = max(scores, key=scores.get)
        
        if scores[best_match_disease] >= 0.20:
            return current_disease_data.get(best_match_disease, {}).get('advice', self.trans('consult_doctor_generic'))
        else:
            return self.trans('consult_doctor_generic')

    def _handle_vaccine_info(self, text):
        return self.trans('vaccine_schedule_info')

    def _handle_goodbye(self, text):
        return self.trans('goodbye_message')

