import pandas as pd
from flask import Flask, render_template
from flask_pymongo import PyMongo
import json

# create instance of Flask app
app = Flask(__name__)
mongo_uri = 'mongodb://heroku_x58zdhbn:fb7o0k7stbsk0ivbirarr2i2d3@ds139775.mlab.com:39775/heroku_x58zdhbn'
app.config['MONGO_URI'] = mongo_uri
flask_debug = False
app.config['FLASK_DEBUG'] = flask_debug
# Create db connection
mongo = PyMongo(app,uri=mongo_uri)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test')
def simulator():
  # test data for colorado one bedroom
  readDataRaw_df=pd.read_csv("https://raw.githubusercontent.com/attila5287/pr3-RegroPoly-assets-herokuAPP/master/testData.csv", encoding='ISO-8859-1')

  dictBeforeMongo = readDataRaw_df.to_dict('records')
  mongo.db.collection.drop()
  mongo.db.collection.insert_many(dictBeforeMongo)
  inventory = list(mongo.db.collection.find())

  return render_template('test.html', inventory=inventory)
  
# ===============================

@app.route('/assets')
def assets():
  assetsRaw_df=pd.read_csv("https://raw.githubusercontent.com/attila5287/pr3-RegroPoly-assets-herokuAPP/master/coloradoTestReg_bed1.csv", encoding='ISO-8859-1')
  dictAssets = assetsRaw_df.to_dict('records')
  mongo.db.collectionAssets.drop()
  mongo.db.collectionAssets.insert_many(dictAssets)
  listAssets = list(mongo.db.collectionAssets.find())

  return render_template('testAssets.html',assets=listAssets)

@app.route('/housemarket')
def houseForSale():
  forSaleRaw_df=pd.read_csv("https://raw.githubusercontent.com/attila5287/pr3-RegroPoly-assets-herokuAPP/master/testRunSimulatedNumbers.csv  ", encoding='ISO-8859-1')
  dictHouseMarket = forSaleRaw_df.to_dict('records')
  mongo.db.collectionHouseMarket.drop()
  mongo.db.collectionHouseMarket.insert_many(dictHouseMarket)
  listHouseProperties = list(mongo.db.collectionHouseMarket.find())

  return render_template('testHouseMarket.html',houseForSaleListing=listHouseProperties)


if __name__ == '__main__':
  app.run(debug=True)
