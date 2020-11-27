import uuid
import socket
from flask import Flask, request, redirect, url_for
from kubernetes import client, config
import os

global cuid
cuid = uuid.uuid4()

global nextip

global servicePort
servicePort = 6000
global nextPort
nextPort = 80

config.load_kube_config(
    os.path.join(os.environ["HOME"], '.kube/config'))

v1 = client.CoreV1Api()

pod_list = v1.list_namespaced_pod("default")
for pod in pod_list.items:
    print("%s\t%s\t%s" % (pod.metadata.name,
                          pod.status.phase,
                          pod.status.pod_ip))

app = Flask(__name__)

#  uid
# def generateId():
#     uid = uuid.uuid4()
#     return uid


def judge_in_or_out(header):
    ip = socket.gethostbyname(socket.gethostname())

    # 同一cuidじゃなかったらingressだからin, 同一cuidならサービスからなのでOUT
    if header["cuid"] is not cuid:
        # IN
        header[cuid] = cuid
        return header

    if header["cuid"] is cuid:
        # OUT
        return header


@app.route("/", methods=['GET'])
def proxy():
    if request.headers["cuid"] is cuid:
        request.headers = judge_in_or_out(request.headers)
        return redirect("http://localhost:" + servicePort)
    else:
        return redirect(nextip+ + nextPort)

@app.route("/", methods=['POST'])
def proxy(uid):
    request.headers = judge_in_or_out(request.headers)
    return redirect("http://localhost:" + servicePort)


app.run("localhost", port=80, debug=True)
