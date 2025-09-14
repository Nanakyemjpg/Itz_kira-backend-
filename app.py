from flask import Flask
from routes.auth import auth_bp
from routes.kyc import kyc_bp
from routes.chatbot import chatbot_bp
from routes.payments import payments_bp

app = Flask(__name__)

# Register blueprints (modular routes)
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(kyc_bp, url_prefix="/api/kyc")
app.register_blueprint(chatbot_bp, url_prefix="/api/chatbot")
app.register_blueprint(payments_bp, url_prefix="/api/payments")

@app.route("/")
def home():
    return {"status": "Itz Kira Backend Running ✅"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
