pipeline {
  agent any

  stages {
    stage('Clonar proyecto') {
      steps {
        git url: 'https://github.com/MiguelZod24/Ejercicios-de-automatizacion'
      }
    }
    stage('Instalar dependencias') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'python -m playwright install'
      }
    }
    stage('Correr tests') {
      steps {
        sh 'pytest'
      }
    }
  }
}
