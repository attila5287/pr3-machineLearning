import pandas as pd
from flask import Flask, render_template
from flask_pymongo import PyMongo
from dataImport import testURLS

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
  inventoryDemo=pd.read_csv("https://raw.githubusercontent.com/attila5287/pr3-RegroPoly-assets-herokuAPP/master/testData.csv", encoding='ISO-8859-1')

  invenDemo = inventoryDemo.copy()

  print(type(invenDemo))

  return render_template('test.html', inventoryDemo=invenDemo)
  


if __name__ == '__main__':
  app.run(debug=True)
