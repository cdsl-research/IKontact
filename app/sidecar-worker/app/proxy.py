import uuid
import socket
from flask import Flask, request, redirect, url_for
from kubernetes import client, config
import os
config.load_kube_config(
    os.path.join(os.environ["HOME"], '.kube/config'))

v1 = client.CoreV1Api()

pod_list = v1.list_namespaced_pod("default")
for pod in pod_list.items:
    print("%s\t%s\t%s" % (pod.metadata.name,
                          pod.status.phase,
                          pod.status.pod_ip))

app = Flask(__name__)


def generateId():
    uid = uuid.uuid4()
    return uid


def judge_in_or_out():
    ip = socket.gethostbyname(socket.gethostname())
    # 同一ipじゃなかったらingressだからin, 同一ipならサービスからなのでOUT
    if request.remote_addr is not ip:
        return "IN"
    if request.remote_addr is ip:
        return "OUT"


@app.route("/", methods=['GET'])
def proxy():
    uid = generateId()
    servicePort = 6000

    return redirect("http://localhost:" + servicePort)


@app.route("/", methods=['POST'])
def proxy(uid):
    servicePort = 6000
    return redirect("http://localhost:" + servicePort)


app.run("localhost", port=80, debug=True)
