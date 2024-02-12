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
}
        post {
                always {
                    // This block will be executed regardless of the build result

                    // Add post-build actions here, such as cleanup or notifications
                    echo 'Performing post-build actions...'
                    sh '''
                    cd $WORKSPACE/scripts
                    chmod +x deploy.sh
                    sudo ./deploy.sh &
                    sleep 60
                    '''
                }

                success {
                    // This block will be executed only if the build is successful
                    echo 'Build successful, additional success actions can be added here...'
                }

                failure {
                    // This block will be executed only if the build fails
                    echo 'Build failed, additional failure actions can be added here...'
                }

                unstable {
                    // This block will be executed only if the build is unstable
                    echo 'Build unstable, additional unstable actions can be added here...'
                }

                changed {
                    // This block will be executed only if the state of the pipeline has changed
                    echo 'State changed, additional actions can be added here...'
                }
            }

  }
