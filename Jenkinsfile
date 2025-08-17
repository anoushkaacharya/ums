pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Aryo15/University-Management-System.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t uni_app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker rm -f uni_app || true'
                sh 'docker run -d --name uni_app -p 5000:5000 uni_app'
            }
        }
    }
}
