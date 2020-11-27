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
│   └── sidecar-worker
│       ├── Dockerfiles
│       │   ├── Dockerfile
│       │   ├── __init__.py
│       │   ├── app
│       │   │   ├── __init__.py
│       │   │   ├── connect.py
│       │   │   ├── proxy.py
│       │   │   └── requirements.txt
│       │   ├── docker_run.sh
│       │   └── entry.sh
│       ├── __init__.py
│       └── app
│           ├── __init__.py
│           ├── proxy.py
│           └── requirements.txt
├── demo
│   ├── Deployment
│   │   ├── IKontact-example.yaml
│   │   ├── ffmpeg-conv.yaml
│   │   ├── flask-calc.yaml
│   │   ├── flask-gateway.yaml
│   │   ├── haproxy-lb.yaml
│   │   └── nginx-gateway.yaml
│   └── Evaluation
│       └── eval.py
└── readme.md

```
