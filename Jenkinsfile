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
						sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=OWASP -Dsonar.sources=. -Dsonar.host.url=http://18.191.251.0:9000 -Dsonar.login=24ead8f93033fc73d9f1157faff96b4fcb3973ab"
					}
				}
			}
		}


		stage("Build UI-Testing Container") {
			steps {
			// Build the ui-test container and runs it for headless testing
				sh 'docker-compose -f docker-compose.ui-test.yaml up -d --build'
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
				sh 'docker-compose -f docker-compose.ui-test.yaml down -v'              
			}

		}

		stage("Deploy") {
			steps {
				echo "Put here incase need deploy for test"
			}
		}

	}    
}
