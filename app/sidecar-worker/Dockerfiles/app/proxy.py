import uuid
import socket
from flask import Flask, request, redirect,url_for

app = Flask(__name__)


def generateId():
    uid = uuid.uuid4()
    return uid

def judge_in_or_out():
    ip = socket.gethostbyname(socket.gethostname())
    #同一ipじゃなかったらingressだからin, 同一ipならサービスからなのでOUT
    if request.remote_addr is not ip:
        return "IN"
    if request.remote_addr is ip:
        return "OUT"


@app.route("/", methods=['GET'])
def proxy():
    uid = generateId()
    servicePort=6000

    return redirect("http://localhost:"+servicePort)

@app.route("/", methods=['POST'])
def proxy(uid):
    servicePort = 6000
    return redirect("http://localhost:"+servicePort)

app.run("localhost",port=80, debug=True)