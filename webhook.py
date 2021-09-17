# app.py
import json
import os
#import request

from flask import Flask
from flask import request
from flask import make_response


app = Flask(__name__)             # create an app instance

#@app.route("/")                   # at the end point /
#def hello():                      # call method hello
#    return "Hello World ZT!"         # which returns "hello world"
#@app.route('/projects/')
#def projects():
#   return 'The project page'

#@app.route('/about')
#def about():
#    return 'The about page'
if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app



@app.route('/webhook',methods=['POST'])

def webhook():
    req = request.get_json(silemt=True,force=True)
    print(json.dumps(req,indent=4))
    res = makeResponse(req)
    res  = json.dumps(res, indent = 4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeRespomse(req):
    result = req.get("queryResult")
    parameters = result.get("parameters")
    city = parameters.get("geo_city")
#    r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=6969565fadecbd630d53a3a3551894c6')
#     condition=weather['weather'][0]['description']
    r = get_data()
    return r    

 


def get_data():  
#    speech = "the forecast value for "+city+" is "+condition
     return{
     "speech":"shailaja Jha",
     "fulfillmentText":speech
#    "source": "apiai_checkweather_webhook"
    }
   

 
#if __name__ =='__main__':
#port = int(os.getenv('port',5000))
#print("starting app on port %d"%port)
#app.run(debug=False, port=port,host='0.0.0.0')
