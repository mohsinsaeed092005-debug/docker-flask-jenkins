# MLOps Assignment 2 - Flask ML App with Jenkins CI/CD and Docker

Course: MLOPS (CS02125), University of Lahore, Fall 2026

## Project structure

    docker-flask-jenkins/
    |-- app.py            Flask application (/ and /health)
    |-- train.py          Model training (data, train, model, test, save)
    |-- tests/            pytest tests (API and ML model tests)
    |-- requirements.txt  Dependencies (flask, pytest)
    |-- Dockerfile        Container image definition
    |-- Jenkinsfile       Declarative CI/CD pipeline
    |-- README.md

## Jenkins pipeline stages

1. Checkout - pull code from GitHub
2. Create Python Environment - virtual environment .dk
3. Install Requirements - pip install -r requirements.txt
4. Test Application - pytest
5. Build Docker Image - docker-flask-app:latest

## Run locally

    python train.py
    python -m pytest -q
    docker build -t docker-flask-app:latest .
    docker run -d -p 5000:5000 --name flask-test docker-flask-app:latest
    curl http://localhost:5000/health

## Version control and rollback

Releases are tagged in Git (v1, v2, v3) and each tag has a matching Docker image.
If a release is faulty: stop the container, run the previous image
(docker run ... docker-flask-app:v1), fix with git revert, test,
tag a new version and redeploy.
