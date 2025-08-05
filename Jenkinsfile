pipeline {
  agent any

  stages {
    stage('Clonar proyecto') {
      steps {
        git branch: 'main', url: 'https://github.com/MiguelZod24/Ejercicios-de-automatizacion.git'
      }
    }
    stage('Instalar dependencias') {
      steps {
        sh 'pip3 install -r requirements.txt'
        sh 'python3 -m playwright install'
      }
    }
    stage('Correr tests') {
      steps {
        sh 'python3 -m pytest'
      }
    }
  }
}
