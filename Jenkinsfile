pipeline {
    agent any
    stages {
         stage('Setup Python Virtual Environment'){
            steps {
                sh '''
                    sed -i -e 's/\r$//' envsetup.sh
                    chmod +x envsetup.sh
                    ./envsetup.sh
                    '''
            }
        }
        stage('Setup gunicorn service'){
            steps {
                sh '''
                    chmod +x gunicorn.sh
                    whitch 
                    ./gunicorn.sh
                    '''
            }
        }
        stage('Setup Nginx'){
            steps {
                sh '''
                    chmod +x nginx.sh
                    ./nginx.sh
                    '''
            }
        }
    }
}
