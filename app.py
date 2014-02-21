from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    results = [{
        'name': "Sen Triplets",
        'colors': ["White", "Blue", "Black"],
        'supertypes': ["Legendary"],
        'types': ["Artifact", "Creature"],
        'subtypes': ["Human", "Wizard"],
        'rarity': "Mythic Rare",
        'power': "3",
        'toughness': "3",
        'layout': "normal"
    }]

    return render_template("search.html", results=results)


if __name__ == "__main__":
    app.run()
