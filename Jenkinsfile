pipeline {

	agent any

	environment { 
		CI = 'true'
		DOCKER_BUILDKIT='1'  // For Multistage build for Dockerfile
	}

	stages {
		stage('init') {
			steps{
				sh 'apt install docker-compose -y'
				sh 'apt update'
				sh 'apt install python3-pip'
				sh 'pip install --upgrade pip'				
			}
		}	

		stage('OWASP DependencyCheck') {
		    steps {
		        sh 'echo $JAVA_HOME'
		        echo "[!] OWASP DependencyCheck"
		        dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'Default'
		    }
		    post {
		        success {
		            dependencyCheckPublisher pattern: 'dependency-check-report.xml'
		        }
		    }
		}

		stage('Code Quality Check via SonarQube') {
            steps {
                script {
                    def scannerHome = tool 'SonarQube';
                    withSonarQubeEnv() {
                        sh """${scannerHome}/bin/sonar-scanner 
                        -Dsonar.projectKey=OWASP -Dsonar.sources=. 
                        -Dsonar.host.url=http://172.20.0.3:9000 
                        -Dsonar.login=5b3bd86020f55c3d6440b9ac849dc09afc6f552b"""
                    }
                }
            }
        }

        stage('Unit Test'){
        	agent {
        		dockerfile {
					filename 'Dockerfile.unit_test'
					args """
						 --name app-flask-unit-test
						 --network app-test-network
						 -v /root/.m2:/root/.m2
					"""
        		}
        	}
            steps{
            	sh 'python test.py'
                // sh 'pytest test.py'
                // sh 'pytest ./Flask/tests/unit/test_models.py'
            }
            post {
				always {
					 // sh 'touch test-reports/*.xml'
					 junit allowEmptyResults: true, testResults: 'test-reports/*.xml'
				}
			}

        }

        stage("Integration Testing") {
        	parallel {
        		stage("Deploy Test Server for ui test") {
		        	agent {
		        		dockerfile {
							filename 'Dockerfile.ui_test'
							args """
								 --name app-flask-ui-test
								 --network app-test-network
								 -v /root/.m2:/root/.m2
							"""
		        		}
		        	}
		        	steps {
		        		sh "python app.py"
		        		input message: "Kill UI-Testing test server?"		        		
		        	}
		        }

		        stage("Headless Browser Testing") {
		        	agent {
		        		dockerfile {
		        			filename 'Dockerfile.'
		        			args """
		        			--name selnium-ui-test
		        			--network app-test-network
		        			"""
		        		}
		        	}
		        	steps {
		 				sh 'pytest ui_tests/test.py -v --junitxml="results.xml"'
		        	}
		        	post {
		        		success {
 							junit allowEmptyResults: true, testResults: 'results.xml'
		        		}
		        	}
		        }
        	}

        }

////////////////////////////////

	}    
}
