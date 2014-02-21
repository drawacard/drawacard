from flask import Flask, request, render_template
from elasticsearch import Elasticsearch

app = Flask(__name__)
elastic = Elasticsearch()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    body = {
        "query": {
            "term": {"name": request.args.get('query')}
         }
    }
    hits = elastic.search('m14', body=body, size=25)['hits']
    
    cards = []
    total = hits['total']
    
    for hit in hits['hits']:
        cards.append(hit['_source'])
    
    return render_template("search.html", total=total, cards=cards)


if __name__ == "__main__":
    app.run(debug=True)
