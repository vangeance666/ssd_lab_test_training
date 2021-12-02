pipeline {

	agent any

	environment { 
		CI = 'true'
	}

	stages {
		stage('init') {
			steps{
				sh 'apt install docker-compose -y'
			}
		}
		stage('Code Quality Check via SonarQube') {
			steps {
				script {
					def scannerHome = tool 'SonarQube';
					withSonarQubeEnv() {
						sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=OWASP2 -Dsonar.sources=. -Dsonar.host.url=http://18.221.176.167:9000 -Dsonar.login=d1cad2e7f4705027587c1f4f6822481952dae824"
					}
				}
			}
		}


		stage("Build UI-Testing Container") {
			steps {
			// Build the ui-test container and runs it for headless testing
				sh 'docker-compose -f docker-compose.ui-test-server.yaml down -v'
				

				sh 'docker-compose -f docker-compose.ui-test-server.yaml up -d --build'
			}
		}
		stage("Headless Browser Testing") {
			agent {
				dockerfile {
					filename 'Dockerfile.ui_test'
					args """
					--name selenium-ui-test
					--network app-test-network
					"""
				}
			}
			steps {
				input message: "wait"
				// sh 'pytest ui_tests/tests/test_login.py -v --junitxml="results.xml"'
				sh 'pytest ui_tests/ui_test.py -v --junitxml="results.xml"'
			}
			post {
				success {
					junit allowEmptyResults: true, testResults: 'results.xml'
				}
			}
		}

		stage("Teardown of Test Containers") {
			steps {
				sh 'docker-compose -f docker-compose.ui-test-server.yaml down -v'           
			}

		}

		stage("Deploy") {
			steps {
				echo "Put here incase need deploy for test"
			}
		}

	}    
}
