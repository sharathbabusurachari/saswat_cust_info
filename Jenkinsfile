pipeline{
    agent any
    stages {
    
        stage('Setup Python Virtual ENV for dependencies'){
       
      steps  {
            sh '''
            sudo apt-get install python3.8-venv
            cd $WORKSPACE/scripts
            chmod +x envsetup.sh
            ./envsetup.sh
            '''}
        }
        stage('Setup Gunicorn Setup'){
            steps {
                sh '''
                cd $WORKSPACE/scripts
                chmod +x gunicorn.sh
                ./gunicorn.sh
                '''
            }
        }
        stage('setup NGINX'){
            steps {
                sh '''
                cd $WORKSPACE/scripts
                chmod +x nginx.sh
                ./nginx.sh
                '''
            }
        }

        stage('BUILD'){
                    steps {
                        sh '''
                        cd $WORKSPACE/scripts
                        chmod +x nginx.sh
                        ./nginx.sh
                        '''
                    }
                }
    }

  }
