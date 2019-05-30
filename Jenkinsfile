pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                label 'test3'
            }
            steps {
                sh 'printenv'
            }
        }
        stage('Test') {
            agent {
                label 'test'
            }
            steps {
                sh 'ipconfig'
            }
        }
        stage('Deploy') {
            agent {
                label 'test2'
            }
            steps {
                sh 'docker image ls -a'
            }
        }
    }
}
