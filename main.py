from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from chatbot_logic import Chatbot
from Localization import translations # Import the translations

app = Flask(__name__)
CORS(app)

user_sessions = {}

@app.route('/')
def index():
    """Serves the main HTML file and injects the translations into it."""
    # This now passes the entire translations dictionary to the frontend.
    return render_template('index.html', translations=translations)

@app.route('/api/register', methods=['POST'])
def register():
    """API endpoint for user registration, now language-aware."""
    data = request.json
    username = data.get('username')
    password = data.get('password')
    language = data.get('language', 'en') # Get language from frontend, default to 'en'

    bot = Chatbot()
    bot.set_language(language) # Set the language before processing
    
    message = bot.register_user(username, password)
    
    if "successful" in message or "सफल" in message:
        return jsonify({"success": True, "message": message})
    else:
        return jsonify({"success": False, "message": message}), 400

@app.route('/api/login', methods=['POST'])
def login():
    """API endpoint for user login, now language-aware."""
    data = request.json
    username = data.get('username')
    password = data.get('password')
    language = data.get('language', 'en') # Get language from frontend
    
    session_id = request.headers.get('Session-ID') 
    if not session_id:
        return jsonify({"success": False, "message": "Session ID is missing."}), 400

    bot = Chatbot()
    bot.set_language(language) # Set the language for this session
    
    if bot.login_user(username, password):
        user_sessions[session_id] = bot 
        initial_message = bot.get_initial_chat_message()
        return jsonify({
            "success": True, 
            "message": "Login successful!",
            "initial_bot_message": initial_message
        })
    else:
        # Use the bot's trans() method to send back a translated error message
        return jsonify({"success": False, "message": bot.trans("login_failed")}), 401

@app.route('/api/chat', methods=['POST'])
def chat():
    """API endpoint for chat messages (remains unchanged)."""
    data = request.json
    user_message = data.get('message')
    
    session_id = request.headers.get('Session-ID')
    bot = user_sessions.get(session_id) 
    
    if not bot:
        # It's good practice to provide a default language for error messages
        error_message = translations.get('en', {}).get('session_expired_error', "User not authenticated or session expired.")
        return jsonify({"error": error_message}), 403
        
    bot_response = bot.get_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)