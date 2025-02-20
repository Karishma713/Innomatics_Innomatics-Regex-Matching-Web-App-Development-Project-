from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    test_string = request.form["test_string"]
    regex_pattern = request.form["regex"]
    matches = re.findall(regex_pattern, test_string)
    return render_template("index.html", matches=matches, test_string=test_string, regex=regex_pattern)

@app.route("/validate-email", methods=["POST"])
def validate_email():
    email = request.form["email"]
    regex_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    is_valid = bool(re.match(regex_pattern, email))
    return render_template("index.html", email=email, is_valid=is_valid)

if __name__ == "__main__":
    app.run(debug=True)