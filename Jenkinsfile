pipeline {
    agent any

    environment {
        SONAR_TOKEN = credentials('sqa_64d3234dc7546a782600d735a2202b269784a955')
    }

    stages {
        stage('Build') {
            steps {
                bat 'docker build -t python-api .'
            }
        }

        stage('Test') {
            steps {
                bat 'docker run --rm -e PYTHONPATH=/app python-api pytest tests/'
            }
        }

        stage('Lint') {
            steps {
                // Installe pylint et génère un rapport
                bat 'docker run --rm python:3.10-slim pip install pylint && pylint ton_script.py > pylint-report.txt || exit 0'
            }
            post {
                always {
                    // Enregistre les issues pour Jenkins (plugin Warnings Next Generation)
                    recordIssues tools: [pmd(pattern: 'pylint-report.txt')]
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQubeServer') {
                    bat """
                        "C:\\Users\\yombe\\Desktop\\sonar-scanner-7.1.0.4889-windows-x64\\bin\\sonar-scanner.bat" ^
                        -Dsonar.projectKey=tp3-use-case ^
                        -Dsonar.sources=. ^
                        -Dsonar.host.url=%SONAR_HOST_URL% ^
                        -Dsonar.login=%SONAR_TOKEN%
                    """
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                    docker stop python-api || echo "No container to stop"
                    docker rm python-api || echo "No container to remove"
                    docker run -d --name python-api -p 5000:5000 python-api
                '''
            }
        }
    }
}
