#import libraries
from flask import Flask,render_template, request,json
import os
import time

app = Flask(__name__)


@app.route('/')

def index():
	return render_template("main.html")

@app.route('/toNLP', methods=['POST'])
def toNLP():
	#//NLP python code goes here
	
    user = request.form['link']
    
    data = """{"ProductName" : "Apple iPhone X(256 GB)","ProductDescription" : "14.73 centimeters (5.8-inch) capacitive touchscreen with 2436 x 1125 pixels resolution, iOS v11.1.1 operating system with 1.3GHz Apple A11 Bionic hexa core processor, 3GB RAM, 256GB internal memory and single SIM, 2716mAH lithium-ion battery,1 year manufacturer warranty for device and in-box accessories including batteries from the date of purchase" , "image_link" : "https://images-eu.ssl-images-amazon.com/images/I/41yHmwJxbIL._SY300_QL70_.jpg","product" : [{"category" : "phone", "percent" : "50.0%"},{"category" : "time", "percent" : "50.0%"},{"category" : "product", "percent" : "50.0%"},
    {"category" : "camera", 
    "percent" : "50.0%"},
    {
      "category" : "service", "percent" : "52.0%"
    },{
      "category" : "year", "percent" : "51.851851851851855%"
    },{
      "category" : "touch", "percent" : "53.57142857142857%"
    },{
      "category" : "complaint", "percent" : "51.724137931034484%"
    },{
      "category" : "difference", "percent" : "51.61290322580645%"
    },{
      "category" : "way", "percent" : "51.515151515151516%"
    },{
      "category" : "screen", "percent" : "51.42857142857143%"
    }],

    "tree" : [
        { "topic" : "phone","subtopic" : [{"SubtopicName" : "Nice phone"},{"SubtopicName" : "great phone"},{"SubtopicName" : "awesome phone"}]},

    { "topic" : "battery","subtopic" : [{"SubtopicName" : "good battery"}]},

    { "topic" : "experience","subtopic" : [{"SubtopicName" : "good experience"}]},

    { "topic" : "camera","subtopic" : [{"SubtopicName" : "front camera"}]},

    { "topic" : "product","subtopic" : [{"SubtopicName" : "great product"}]},

    { "topic" : "thing","subtopic" : [{"SubtopicName" : "only thing"}]},

    { "topic" : "network","subtopic" : [{"SubtopicName" : "cellular network"}]},

    { "topic" : "gamer","subtopic" : [{"SubtopicName" : "mobile gamer"}]},

    { "topic" : "hole","subtopic" : [{"SubtopicName" : "deep hole"}]},

    { "topic" : "device","subtopic" : [{"SubtopicName" : "great device"}]},

    { "topic" : "time","subtopic" : [{"SubtopicName" : "committed time"}]},

    { "topic" : "service","subtopic" : [{"SubtopicName" : "superb service"}]},
    { "topic" : "notch","subtopic" : [{"SubtopicName" : "little notch"}]},

    { "topic" : "interface","subtopic" : [{"SubtopicName" : "new interface"}]}

	]
    }"""
    
    return data

#///////////////////////////////////

#for debugging purposes
if __name__ == "__main__":
	app.run(debug=True)
#///////////////////////////////////


