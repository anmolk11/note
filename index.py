from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route('/addText',methods = ['POST'])
def addText():
    data = request.json
    text = data['text']
    

if __name__ == '__main__':
    app.run(debug=True)