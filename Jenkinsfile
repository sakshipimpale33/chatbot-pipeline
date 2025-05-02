pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/sakshipimpale33/chatbot-pipeline.git'
            }
        }

        stage('Run Chatbot') {
            steps {
                sh 'python chatbot.py'
            }
        }
    }
}
