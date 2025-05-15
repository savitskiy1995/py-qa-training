pipeline {
    agent any

    stages {

        stage('Install dependencies') {
            steps {
                bat 'pip install -r requirements.txt || exit 0'
                bat 'pip install pytest pytest-html'
            }
        }

        stage('Run tests') {
            steps {
                bat 'pytest test/ --html=report.html --self-contained-html'
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
