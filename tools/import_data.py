import json
from urllib2 import urlopen
from elasticsearch import Elasticsearch

elastic = Elasticsearch()


def fetch(url):
    return json.loads(urlopen(url).read())


if __name__ == '__main__':
    data = fetch("http://mtgjson.com/json/M14.json")
    index = 'm14'
    
    elastic.indices.delete(index)
    
    for card in data['cards']:
        elastic.index(index, doc_type='card', body=card)

    elastic.indices.refresh(index)

