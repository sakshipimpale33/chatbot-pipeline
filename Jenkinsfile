pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/sakshipimpale33/chatbot-pipeline.git'
            }
        }

        stage('Run Chatbot') {
            steps {
        timeout(time: 2, unit: 'MINUTES') {
            bat 'python chat.py'
        }
    }
        }
    }
}