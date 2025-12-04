pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                bat '''
                  python --version
                  if exist requirements.txt (
                    pip install --upgrade pip
                    pip install -r requirements.txt
                  )
                '''
            }
        }

        stage('Run unit tests (CI)') {
            steps {
                bat '''
                  python -m unittest -v test_main.py
                '''
            }
        }

        stage('Build package') {
            steps {
                bat '''
                  if not exist dist mkdir dist
                  tar -czf dist\\calculator-package.tar.gz main.py test_main.py
                '''
            }
        }

        stage('Deploy (local CD)') {
            steps {
                bat '''
                  if not exist deploy mkdir deploy
                  copy /Y dist\\calculator-package.tar.gz deploy\\
                '''
                archiveArtifacts artifacts: 'dist/*.tar.gz', fingerprint: true
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished (success or failure).'
        }
    }
}
