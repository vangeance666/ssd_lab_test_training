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
						sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=OWASP -Dsonar.sources=. -Dsonar.host.url=http://209.97.168.24:9000 -Dsonar.login=995427933f3517afbb3cac97afe2d63f1fd91325"
					}
				}
			}
		}

		stage('Unit Test'){
			agent {
				dockerfile {
					filename 'Dockerfile.unit_test'
					args "-it --name app-flask-unit-test --network app-test-network"
				}
			}
			steps{
				input message: "wait"
				sh 'python test.py'
			}
			post {
				success {
					junit allowEmptyResults: true, testResults: 'test-reports/*.xml'
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
					--name selnium-ui-test
					--network app-test-network
					"""
				}
			}
			steps {
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
