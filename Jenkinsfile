pipeline {

    agent any
	tools {
    jfrog 'jfrog-cli'
}
stages {
	
	stage ('Artifactory configuration') {
            steps {
           rtServer (
                    id: "artifactory-tlv",
                    url: "https://artifactorytlv.jfrog.io/",
                )
            }
        }


        stage('Build') {
		agent{
		dockerfile {
      		filename 'Dockerfile'
      		label 'zip-job-docker'
		additionalBuildArgs  '--build-arg version=1.2.0'
  	        args '--privileged'
		args '-v /tmp:/tmp'
	  
	
    }
	
}
            steps {
        echo 'Building..'
	sh 'rm src/*.zip'
	sh 'python3 src/zip_job.py'
	sh 'cp src/*.zip /tmp/'
	sh 'ls /tmp'

            }
        }


         stage('Deploy') {
            when {
              expression {
                currentBuild.result == null || currentBuild.result == 'SUCCESS' 
              }
            }
		 
            steps {    
//                sh 'make publish'
		  jf "rt u /tmp/*.zip binary-storage/"
            }
    }
    }
	
    post {
        always {
           
            echo 'sending an Email...'

            mail to: "romyyy1812@gmail.com",
            subject: "Build status Email",
            body: "${currentBuild.currentResult}: Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n More info at: ${env.BUILD_URL}"

	
            cleanWs(cleanWhenNotBuilt: false,
                    deleteDirs: true,
                    disableDeferredWipeout: true,
                    notFailBuild: true,
                    patterns: [[pattern: '.gitignore', type: 'INCLUDE'],
                               [pattern: '.propsfile', type: 'EXCLUDE']])
       		 
		}

	    }

}
