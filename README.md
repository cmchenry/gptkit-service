# A Flask Server that connects to OpenAI's GPT3 service
This is a simple, stateless Flask API server that parses chat requests and sends them off to
OpenAI's chat_completion API.

# Setup Environment
- pip install virtualenv (if you don't already have virtualenv installed)
- virtualenv venv to create your new environment (called 'venv' here)
- source venv/bin/activate to enter the virtual environment
- pip install -r requirements.txt 

# Configuration
Create a .env file with the following name/value pairs:
- SECRET_KEY - A secret key for signing Flask's session cookie. [Flask Documentation][https://flask.palletsprojects.com/en/3.0.x/config/#SECRET_KEY]
- CLIENT_APP_URL - Used to avoid CORS errors in development mode.  The root URL of your client app.
- OPENAI_KEY - Your Open API key.

# Execution
flask run