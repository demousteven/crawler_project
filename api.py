# api.py
from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient('your_mongo_uri_here')
db = client['your_mongo_database_name_here']

@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword')
    articles = list(db['news'].find({"$text": {"$search": keyword}}))
    for article in articles:
        article['_id'] = str(article['_id'])
    return jsonify(articles)

if __name__ == "__main__":
    app.run(debug=True)
