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
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate.bat
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pytest tests/
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQubeServer') {
                    bat """
                        sonar-scanner ^
                        -Dsonar.projectKey=tp3-use-case ^
                        -Dsonar.sources=. ^
                        -Dsonar.host.url=%SONAR_HOST_URL% ^
                        -Dsonar.login=%SONAR_TOKEN%
                    """
                }
            }
        }

        // Tu peux ajouter ici une étape 'Quality Gate' si nécessaire
        /*
        stage('Quality Gate') {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
        */
    }
}
