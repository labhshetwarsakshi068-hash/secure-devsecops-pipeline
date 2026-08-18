from flask import Flask 

app = Flask(__name__)

@app.route("/")
def home():
    return"""
    <h1>Secure DevSecOps Pipeline</h1>
    <h2>Welcome to our Secure CI/CD Application</h2>
    <p>Status: Application is Running </p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
