1. Set Up the Environment:
pip install scrapy readability-lxml pymongo flask
2. pip install scrapy readability-lxml pymongo flask
Create a Scrapy Spider:

Let's begin with creating a spider for www.bbc.com.
3.Define the Item:

Items are simple containers used by Scrapy to collect the scraped data.

4.Pipeline to Save to MongoDB:

Once you scrape the data, you want to save it to MongoDB.

5 . Add this to settings.py:
ITEM_PIPELINES = {
    'pipelines.MongoDBPipeline': 300,
}
MONGO_URI = 'your_mongo_uri_here'
MONGO_DATABASE = 'your_mongo_database_name_here'


6. Flask API:

Use Flask to create a simple API to search the articles.

7. Make sure you have created a text index in MongoDB to allow the search. In MongoDB shell:

db.news.createIndex({content: "text", headline: "text"})

8. run .

First, run the Scrapy spider to collect data.
scrapy runspider bbc_spider.py

Then run the Flask API.
python api.py
