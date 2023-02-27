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
                    sed -i -e 's/\r$//' gunicorn.sh
                    chmod +x gunicorn.sh
                    ./gunicorn.sh
                    '''
            }
        }
        stage('Setup Nginx'){
            steps {
                sh '''
                    sed -i -e 's/\r$//' nginx.sh
                    chmod +x nginx.sh
                    ./nginx.sh
                    '''
            }
        }
    }
}
