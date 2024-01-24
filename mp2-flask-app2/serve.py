from flask import Flask, request, jsonify
import subprocess
import socket
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#    return 'Hello World'



seed = 0

@app.route('/',methods = ['POST', 'GET'])
def seeds():
   global seed
   if request.method == 'POST':
        p = subprocess.Popen(["python", "stress_cpu.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = p.communicate()
   else:
      return socket.gethostname()
      


if __name__ == '__main__':
   app.run(port="0.0.0.0")