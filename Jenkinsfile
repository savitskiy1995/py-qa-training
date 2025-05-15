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
                sh 'python3.13 --version'  // Проверка версии
                sh 'python3.13 -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'source venv/bin/activate && python -m pytest'  // или другой командой для тестов
            }
        }
    }
}