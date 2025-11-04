from flask import Flask, render_template, request
import jinja2

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contact")
def contact():
    contact = {"email": "mguo26@nmhschool.org", "phone": None, "github": "mguo26/my_work"}
    return render_template("contact.html", contact=contact)

@app.route("/about")
def about():
    return render_template("about.html", name="Mia", interest="AI")

if __name__ == "__main__":
    app.run(debug=True)
