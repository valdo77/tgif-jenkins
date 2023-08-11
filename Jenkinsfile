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
            steps {
                echo "Run front end test here"
            }
        }

        stage('Merge to UAT') {
            steps {
                build job: 'merge_branch'
            }
        }
    }
}
