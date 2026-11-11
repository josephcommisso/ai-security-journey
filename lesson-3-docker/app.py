from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from my first container!"

if __name__ == "__main__":
    # Accepted risk: the app runs inside a Docker container, so it must listen on
    # 0.0.0.0 for the -p port mapping to work. Exposure is controlled by Docker, not the app.
    app.run(host="0.0.0.0", port=5000)  # nosemgrep: python.flask.security.audit.app-run-param-config.avoid_app_run_with_bad_host
