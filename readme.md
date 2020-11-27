C0116023
Takamasa Iijima

# IKontact
This is proxy working on kubernetes systems.

## Features
- Add UniqueID to each requests over the container.

## Files
```
.
├── app
│   ├── __init__.py
│   └── sidecar-worker #main conponents
│       ├── connect.py #api which connect control plane's db
│       ├── Dockerfiles
│       │   ├── entry.sh
│       │   ├── IKontact.Dockerfile
│       │   └── __init__.py
│       ├── __init__.py
│       ├── proxy.py
│       └── requirements.txt
├── demo
│   ├── Deployment
│   │   ├── ffmpeg-conv.yaml
│   │   ├── flask-calc.yaml
│   │   ├── flask-gateway.yaml
│   │   ├── haproxy-lb.yaml
│   │   ├── IKontact-example.yaml
│   │   └── nginx-gateway.yaml
│   └── Evaluation
│       └── eval.py
└── readme.md
```
