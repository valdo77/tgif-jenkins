pipeline {
    agent any
    stages {
        stage('BACKEND TEST') {
           steps {
                echo "Run front end test here"
            }
        }

         stage('FRONTEND TEST') {
           steps {
                echo "Run front end test here"
            }
        }

        stage('MERGE TO UAT') {
            steps{
                build job: 'MERGE TO UAT'
            }
        }

        
    }
}
