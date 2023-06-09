pipeline {
    agent {
        docker { image 'openjdk:17.0.2' }
    }
    stages {
        stage("verify tooling") {
            steps {withEnv(['PATH+EXTRA=/usr/sbin:/usr/bin:/sbin:/bin']) {
                sh '''
                  docker version
                  docker info
                  docker-compose version
                '''
                }
            }
        }
        stage('Cloning Git Project') {
            steps {
                git branch: 'main', url: "$GIT_HUB_URL"
            }
        }
        stage('Build Docker Images') {  
            steps {withEnv(['PATH+EXTRA=/usr/sbin:/usr/bin:/sbin:/bin']) {
                sh 'docker-compose build'
                echo 'Docker-compose-build Build Image Completed'
                }
            }                     
        }
        stage("Tag Docker Images") {
            steps {withEnv(['PATH+EXTRA=/usr/sbin:/usr/bin:/sbin:/bin']) {
                sh "docker tag try_easyp2-project $DOCKERHUB_USR/try_easyp2-project:$BUILD_NUMBER"
                sh "docker tag try_easyp2-frontend $DOCKERHUB_USR/try_easyp2-frontend:$BUILD_NUMBER"
                }
            }
        }
        stage('Testing Project') {
            steps {withEnv(['PATH+EXTRA=/usr/sbin:/usr/bin:/sbin:/bin']) {
                    sh '''
                    docker rm -f backend || echo 'nothing to remove'
                    docker run --rm --name=backend -p 8000:8000 -d dockercgvd/try_easyp2-project:$BUILD_NUMBER
                    docker exec backend sh -c "python -m unittest discover -s api/tests"
                    docker rm -f backend || echo 'nothing to remove'
                    '''
                    echo "Testing completed"
                }
            }
        }
        stage('Push Images to Docker Hub') {         
            steps {withEnv(['PATH+EXTRA=/usr/sbin:/usr/bin:/sbin:/bin']) {
                withCredentials([usernamePassword(credentialsId: 'docker_hub_credentials', passwordVariable: 'DOCKERHUB_PSW', usernameVariable: 'DOCKERHUB_USR')]) {
                    sh 'echo $DOCKERHUB_PSW | docker login -u $DOCKERHUB_USR --password-stdin'                     
                    echo 'Login Completed'
                    sh 'docker push $DOCKERHUB_USR/try_easyp2-project:$BUILD_NUMBER'
                    sh 'docker push $DOCKERHUB_USR/try_easyp2-frontend:$BUILD_NUMBER'
                    echo 'Push Images Completed'
                    }
                }
            }
        }
        stage('Clean server') {  
            steps {withEnv(['PATH+EXTRA=/usr/sbin:/usr/bin:/sbin:/bin']) {
                sh '''
                docker rmi try_easyp2-project
                docker rmi $DOCKERHUB_USR/try_easyp2-project:$BUILD_NUMBER
                docker rmi try_easyp2-frontend
                docker rmi $DOCKERHUB_USR/try_easyp2-frontend:$BUILD_NUMBER
                '''
                echo 'Docker Images Removal Completed'
                }
            }                     
        }
        // stage('Deploy') {  
        //     steps {withEnv(['PATH+EXTRA=/usr/sbin:/usr/bin:/sbin:/bin']) {
        //         withCredentials([file(credentialsId: 'server_key', variable: 'KEY_PAIR')]) {
		// 	        script {
        //         		sh """
        //        	 	    #!/bin/bash
        //         		ssh -i $KEY_PAIR ec2-user@3.38.230.38 << EOF
        //         		docker pull $DOCKERHUB_USR/try_easyp2-frontend:$BUILD_NUMBER
        //         		docker pull $DOCKERHUB_USR/try_easyp2-project:$BUILD_NUMBER
        //                 docker rm -f frontend
		// 	            docker run --network="mynet" --name=frontend -p 7000:7000 -d $DOCKERHUB_USR/try_easyp2-frontend:$BUILD_NUMBER
        //         		docker rm -f backend
        //                 docker run --network="mynet" --name=backend -p 8000:8000 -d $DOCKERHUB_USR/try_easyp2-project:$BUILD_NUMBER
		// 	            docker system prune -f
		//             	<< EOF
        //         		"""
        //         	    }
                   
        //             }
        //         }
        //     }                     
        // }
    }
    post {
        success {
            office365ConnectorSend color: '#86BC25', 
            status: currentBuild.result, 
            webhookUrl: "${EASYP_WEBHOOK}",
            message: "Images have been uploaded to Docker Hub. - ${currentBuild.displayName}<br>Pipeline duration: ${currentBuild.durationString.replace(' and counting', '')}"
        }
        unstable {
            office365ConnectorSend color: '#FFE933', 
            status: currentBuild.result, 
            webhookUrl: "${EASYP_WEBHOOK}",
            message: "Successfully Build but Unstable. Unstable means test failure, code violation, push to remote failed etc. : ${JOB_NAME} - ${currentBuild.displayName}<br>Pipeline duration: ${currentBuild.durationString.replace(' and counting', '')}"
        }
        failure {
            office365ConnectorSend color: '#ff0000', 
            status: currentBuild.result, 
            webhookUrl: "${EASYP_WEBHOOK}",
            message: "Build Failed. - ${currentBuild.displayName}<br>Pipeline duration: ${currentBuild.durationString.replace(' and counting', '')}"
        }
        always {
            echo "Build completed with status: ${currentBuild.result}"
        }
    }
}