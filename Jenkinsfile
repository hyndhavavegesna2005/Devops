pipeline {
    agent {
        docker {
            // Python image for the build environment
            image 'python:3.12-slim'
            args '-u root:root'
        }
    }

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
                sh '''
                  python --version
                  if [ -f requirements.txt ]; then
                    pip install --upgrade pip
                    pip install -r requirements.txt || true
                  fi
                '''
            }
        }

        stage('Run unit tests (CI)') {
            steps {
                sh '''
                  # Run your unittest-based tests
                  python -m unittest -v test_main.py
                '''
            }
        }

        stage('Build package') {
            steps {
                sh '''
                  mkdir -p dist
                  # Package your exact files as the build artifact
                  tar -czf dist/calculator-package.tar.gz main.py test_main.py
                '''
            }
        }

        stage('Deploy (local CD)') {
            steps {
                sh '''
                  # Simulated deployment: copy artifact to deploy folder
                  mkdir -p deploy
                  cp dist/calculator-package.tar.gz deploy/
                '''
                archiveArtifacts artifacts: 'dist/*.tar.gz', fingerprint: true
            }
        }
    }

    post {
        always {
            // If you later generate JUnit xml from unittest, you can reference it here
            // junit allowEmptyResults: true, testResults: '**/test-results.xml'
            echo 'Pipeline finished (success or failure).'
        }
    }
}
