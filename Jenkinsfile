pipeline{
    agent any
    stages {
    
        stage('Setup Python Virtual ENV'){
       
      steps  {
            sh '''
            chmod +x envsetup.sh
            ./mesotheliomalegalhelpcenter/envsetup.sh
            '''}
        }
        stage('Setup Gunicorn Setup'){
            steps {
                sh '''
                chmod +x gunicorn.sh
                ./mesotheliomalegalhelpcenter/gunicorn.sh
                '''
            }
        }
        stage('setup NGINX'){
            steps {
                sh '''
                chmod +x nginx.sh
                ./mesotheliomalegalhelpcenter/nginx.sh
                '''
            }
        }
    }
}
