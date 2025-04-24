pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Preparar entorno') {
            steps {
                sh 'python -m venv $VENV_DIR'
                sh '. $VENV_DIR/bin/activate && pip install --upgrade pip'
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh '. $VENV_DIR/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                sh '. $VENV_DIR/bin/activate && pytest'
            }
        }
    }

    post {
        always {
            junit '**/tests/results.xml' // opcional si usas `--junitxml=...`
            cleanWs()
        }
    }
}
