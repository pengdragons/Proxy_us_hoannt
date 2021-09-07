from flask import Flask
from flask import request
import json
import os
from threading import Thread

app = Flask(__name__)
@app.route("/")
def hello_world():
   return "Hello World!"
@app.route("/proxy/<number_gen>",methods=["GET"])
def excute_data(number_gen):
    os.system('killall proxybroker')
    mydata =[]
    f = open("port.txt", "r")
    PORT = f.read()

    for i in range(int(number_gen)):
        mydata.append({
            'ip' : '8.6.8.208',
            'port': PORT
            })
        PORT = int(PORT) + 1
        print(PORT)
    jsonstring = json.dumps(mydata)
    f = open("port.txt", "w")
    f.write(str(PORT))
    f.close()
    def do_work(number_gen):
        os.system('python3 run_cmd.py '+number_gen)
    thread = Thread(target=do_work, args=(number_gen,))
    thread.start()
    return(jsonstring)
if __name__ == "__main__":
   app.run(host='8.6.8.208', debug=True)
