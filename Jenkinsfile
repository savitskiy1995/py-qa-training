pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/savitskiy1995/py-qa-training.git', branch: 'main'
            }
        }

        stage('Set up Python 3.13') {
            steps {
                sh 'python3.13 --version'
                sh 'python3.13 -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
                // Установка дополнительных пакетов для отчётов
                sh 'source venv/bin/activate && pip install pytest-html pytest-junitxml'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'source venv/bin/activate && python -m pytest --junitxml=test-results.xml --html=report.html'
            }
        }

        stage('Publish Test Results') {
            steps {
                // Публикация результатов в формате JUnit для Jenkins
                junit 'test-results.xml'
                
                // Публикация HTML отчёта (требуется установленный плагин HTML Publisher)
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '',
                    reportFiles: 'report.html',
                    reportName: 'Pytest HTML Report'
                ])
            }
        }
    }
}