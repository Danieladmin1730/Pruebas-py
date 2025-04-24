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
