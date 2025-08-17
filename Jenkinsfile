pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Aryo15/ums.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ums-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                  docker rm -f ums-app || true
                  docker run -d -p 80:5000 --name ums-app ums-app
                '''
            }
        }
    }
}
