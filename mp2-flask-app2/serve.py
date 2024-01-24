from flask import Flask, request, jsonify
import subprocess
import socket
app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def serve():
   if request.method == 'POST':
      subprocess.Popen(["python3", "stress_cpu.py"])
      hostname = socket.gethostname()
      return f"stressing {socket.gethostbyname(hostname)}"
   else:
      hostname = socket.gethostname()
      return socket.gethostbyname(hostname)
      


if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000)
