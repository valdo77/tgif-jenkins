pipeline {
    agent any
    stages {
        stage('BACKEND TEST') {
            agent { 
                dockerfile {
                    filename 'Dockerfile'
                    dir 'BACKEND'
                    args '-v /usr/src/app'
                    reuseNode false
                }
            }

            steps {
                sh 'cd /app; python src/test_main.py'
            }
        }

         stage('FRONTEND TEST') {
             agent { 
                dockerfile {
                    filename 'Dockerfile.test'
                    dir 'FRONTEND'
                    args '-v /usr/src/app'
                    reuseNode false
                }
            }

            steps {
                sh 'cd /app; npm run test'
            }
        }

        stage('MERGE TO UAT') {
            steps{
                build job: 'MERGE TO UAT'
            }
        }

        
    }
}
