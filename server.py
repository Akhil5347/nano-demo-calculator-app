from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello World!"

@app.route("/calculator/add", methods=['POST'])
def add():
    try:
        data = request.json
        num1 = data['first']
        num2 = data['second']
        
        result = num1 + num2
        
        return jsonify({"result": result})
    except KeyError:
        return jsonify({"error": "Invalid input"}), 400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    
    data = request.json
    num1 = data['first']
    num2 = data['second']
        
    result = num1 - num2
        
    return jsonify({"result": result})
    

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')