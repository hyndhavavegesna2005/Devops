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

        stage('CI in Docker (tests + build)') {
            steps {
                bat '''
                  docker run --rm ^
                    -v "%cd%":/app ^
                    -w /app ^
                    python:3.12-slim sh -c "pip install --upgrade pip && pip install -r requirements.txt || true && python -m unittest -v test_main.py && mkdir -p dist && tar -czf dist/calculator-package.tar.gz main.py test_main.py"
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
