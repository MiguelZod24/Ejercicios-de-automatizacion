pipeline {
  agent any

  stages {
    stage('Clonar proyecto') {
      steps {
        git branch: 'main', url: 'https://github.com/MiguelZod24/Ejercicios-de-automatizacion.git'
      }
    }
    stage('Preparar entorno') {
      steps {
        // Crear virtualenv, activarlo, instalar paquetes y playwright
        sh '''
          python3 -m venv venv
          . venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
          python3 -m playwright install
        '''
      }
    }
    stage('Correr tests') {
      steps {
        // Correr pytest dentro del virtualenv
        sh '''
          . venv/bin/activate
          python3 -m pytest
        '''
      }
    }
  }
}
