pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "todo-app:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Shuvra-458/To-Do_List_CI-CD.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python3 -m venv env'
                sh '. env/bin/activate && python -m pip install --upgrade pip'
                sh '. env/bin/activate && pip install -r requirements.txt flake8 pytest'
            }
        }

        stage('Lint') {
            steps {
                sh '. env/bin/activate && flake8 app/ tests/ || true'
            }
        }

        stage('Test') {
            steps {
                sh '. env/bin/activate && cd $WORKSPACE && python -m pytest --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Build Docker') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Push Docker') {
            when {
                branch 'main'
            }
            steps {
                script {
                    docker.withRegistry('', 'shuvra458'){
                        sh "docker tag ${DOCKER_IMAGE} shuvra458/todo-app:latest"
                        sh "docker push shuvra458/todo-app:latest"
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
    }
}
