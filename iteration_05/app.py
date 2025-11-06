from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html", name="Mia", interest="AI")

@app.route("/contact")
def contact():
    contact = {"email": "mguo26@nmhschool.org", "github": "mguo26/my_work", "phone": None}
    return render_template("contact.html", contact=contact)

if __name__ == "__main__":
    app.run(debug=True)
