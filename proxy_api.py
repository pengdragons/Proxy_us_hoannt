from flask import Flask
from flask import request
import json
import os

app = Flask(__name__)
@app.route("/")
def hello_world():
   return "Hello World!"
@app.route("/proxy/<number_gen>",methods=["GET"])
def excute_data(number_gen):
    mydata =[]
    f = open("port.txt", "r")
    PORT = f.read()

    for i in range(int(number_gen)): 
        mydata.append({
            'ip' : '103.75.184.246',
            'port': PORT
            })
        PORT = int(PORT) + 1
        print(PORT)
    jsonstring = json.dumps(mydata)
    f = open("port.txt", "w")
    f.write(str(PORT))
    os.system('python3 run_cmd')
    return(jsonstring) 
if __name__ == "__main__":
   app.run()
