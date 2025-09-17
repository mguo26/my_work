import requests

# https://catfact.ninja/

url = "https://catfact.ninja/fact"
response = requests.get(url)
data = response.json()

print("Random Cat Fact:", data["fact"])


# second route to get fact

@app.route("/catbreeds")
def cat_breed():
    limit = int(request.args.get("limit,1"))
    url = 'https://catfact.ninja/breeds?limit={limit}'
    response = requests.get(url)
    response = response.json()
    breeds_list = []
    for breed in response('data'):
        breeds_list.append(f"Breed:['breed]") Country:{breed['country']}")"
        breed_html = "<br></br>".join(breeds_list)
        html_content=f"<h1>Cat Breeds<h1><p>{breed_html}</p>"
        return html_content 
