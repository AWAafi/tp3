pipeline {
    agent any

    environment {
        SONAR_TOKEN = credentials('sqa_64d3234dc7546a782600d735a2202b269784a955')
    }

    stages {
        stage('Build') {
            steps {
                bat 'docker run --rm -e PYTHONPATH=/app python-api pytest tests/'
            }
        }

        stage('Test') {
            steps {
                bat 'docker run --rm -e PYTHONPATH=/app python-api pytest tests/'
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
    }
}
