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
        sh '''
            . venv/bin/activate
            pytest --junitxml=report.xml
        '''
    }
}

    }

    post {
    always {
        junit 'report.xml'
    }
}

}
