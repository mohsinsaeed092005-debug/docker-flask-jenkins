pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/mohsinsaeed092005-debug/docker-flask-jenkins.git'
            }
        }

        stage('Create Python Environment') {
            steps {
                sh 'python3 -m venv .dk'
            }
        }

        stage('Install Requirements') {
            steps {
                sh '. .dk/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Test Application') {
            steps {
                sh '. .dk/bin/activate && python -m pytest -q'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t docker-flask-app:latest .'
            }
        }
    }
}
