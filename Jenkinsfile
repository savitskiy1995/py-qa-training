pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/savitskiy1995/py-qa-training.git', branch: 'main'
            }
        }

        stage('Set up Python') {
            steps {
                bat 'python --version'
                bat 'python -m venv venv'
                bat 'call venv\\Scripts\\activate && pip install -r requirements.txt'
                bat 'call venv\\Scripts\\activate && pip install pytest pytest-html pytest-junitxml'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'call venv\\Scripts\\activate && python -m pytest --junitxml=test-results.xml --html=report.html'
            }
        }

        stage('Publish Reports') {
            steps {
                junit 'test-results.xml'
                publishHTML(target: [
                    reportDir: '',
                    reportFiles: 'report.html',
                    reportName: 'Pytest Report'
                ])
            }
        }
    }
}