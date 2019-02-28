import pandas as pd
from flask import Flask, render_template
from flask_pymongo import PyMongo
import json
import jinja2
app = Flask(__name__)
app.jinja_env.filters['zip'] = zip
# create instance of Flask app
mongo_uri = 'mongodb://heroku_x58zdhbn:fb7o0k7stbsk0ivbirarr2i2d3@ds139775.mlab.com:39775/heroku_x58zdhbn'
app.config['MONGO_URI'] = mongo_uri
flask_debug = False
app.config['FLASK_DEBUG'] = flask_debug
# Create db connection
mongo = PyMongo(app,uri=mongo_uri)


@app.route('/')
def index():
  pass
  figureL2st=list()
  figureL1st = ['plotColorado.png',
  'plotCalifornia.png',
  'plotNebraska.png',
  'custPriceIndex.png',
  'medianHHI.png',
  'unempRate.png',
  'mortgage15.png',
  'mortgage30.png',
  'rentCustIndex.png'
  ]
  preFigureSrc = 'https://raw.githubusercontent.com/attila5287/pr3-RegroPoly-assets-herokuAPP/master/plot/'
  figureL2st=[]
  for file in figureL1st:
    file = preFigureSrc + file
    figureL2st.append(file) 

  figureL3st = ['Colorado all homes zillow actual prices, stars are Round Dates:Game Checkpoints',
  'California all homes zillow actual prices, stars are Round Dates:Game Checkpoints', 
  'Nebraska all homes zillow actual prices, stars are Round Dates:Game Checkpoints', 
  'Macro-econ: Pair Plot for House Prices vs Customer Price Index',
  'Macro-econ: Pair Plot for House Prices vs Median HouseHold Income',
  'Macro-econ: Pair Plot for House Prices vs Unemployment Rate',
  'Macro-econ: Pair Plot for House Prices vs Mortgage 15 yrs rate',
  'Macro-econ: Pair Plot for House Prices vs Mortgage 30 yrs rate',
  'Macro-econ: Pair Plot for House Prices vs Customer Rent Index'
  ]



  return render_template('index.html',figureList =figureL2st, descList = figureL3st)


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


