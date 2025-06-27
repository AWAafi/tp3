pipeline {
    agent any

    environment {
        SONAR_TOKEN = credentials('sqa_64d3234dc7546a782600d735a2202b269784a955')
    }

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t python-api .'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pytest tests/
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQubeServer') {
                    sh '''
                        sonar-scanner \
                        -Dsonar.projectKey=tp3-use-case \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://localhost:9000 \
                        -Dsonar.login=$SONAR_TOKEN
                    '''
                }
            }
        }

        stage('PMD Static Analysis') {
            steps {
                recordIssues tools: [pmd(pattern: '**/pmd-report.xml')]
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker stop python-api || true
                    docker rm python-api || true
                    docker run -d -p 5000:5000 --name python-api python-api
                '''
            }
        }

        stage('UI Test with Selenium') {
            steps {
                sh '''
                    . venv/bin/activate
                    pip install selenium
                    python selenium_test.py
                '''
            }
        }
    }
}
