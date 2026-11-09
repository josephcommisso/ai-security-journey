import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    if os.environ.get("SECRET_CODE"):
        return "Secret code loaded: YES"
    return "Secret code loaded: NO"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
