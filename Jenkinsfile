pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/savitskiy1995/py-qa-training.git'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt || true'
                sh 'pip install pytest pytest-html'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest test/ --html=report.html --self-contained-html'
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Test Report'
                ])
            }
        }
    }
}
