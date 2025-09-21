from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    data = response.json()

    dog_url = data.get("message", "no dog found")
    html_content = f"""
        <h1>Random Dog</h1>
        <img src="{dog_url}" alt="Random Dog" style="max-width:300px;"><br>
        <a href="/form">Try the form!</a>
    """
    return html_content


@app.route("/dog_by_breed")
def dog_by_breed():
    breed = request.args.get("breed", "hound")  
    url = f"https://dog.ceo/api/breed/{breed}/images/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return jsonify({"breed": breed, "image": data.get("message")})
    else:
        return jsonify({"error": "Breed not found"}), 404


@app.route("/form")
def form():
    return """
        <h2>Find a Dog by Breed</h2>
        <form action="/dog_result" method="get">
            Enter breed: <input type="text" name="breed">
            <input type="submit" value="Search">
        </form>
    """



@app.route("/dog_result")
def dog_result():
    breed = request.args.get("breed", "hound")
    url = f"https://dog.ceo/api/breed/{breed}/images/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        dog_url = data.get("message")
        return f"""
            <h1>Here is a {breed}!</h1>
            <img src="{dog_url}" alt="{breed}" style="max-width:300px;"><br>
            <a href="/form">Search again</a>
        """
    else:
        return f"<h2>Breed '{breed}' not found. Try again.</h2><a href='/form'>Back</a>"


if __name__ == "__main__":
    app.run(debug=True)
