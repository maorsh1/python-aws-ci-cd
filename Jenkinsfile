pipeline {
    agent any

    environment {
        AWS_REGION = 'eu-north-1'
        S3_BUCKET = 'project22.7'
        EB_APP_NAME = 'project22.7'
        EB_ENV_NAME = 'Project227-env'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/maorsh1/python-aws-ci-cd.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python -m unittest discover -s tests'
            }
        }
        stage('Package Application') {
            steps {
                sh 'zip -r application.zip .'
            }
        }
        stage('Upload to S3') {
            steps {
                withAWS(region: "${env.AWS_REGION}", credentials: 'aws-credentials') {
                    s3Upload(bucket: "${env.S3_BUCKET}", file: 'application.zip')
                }
            }
        }
        stage('Deploy to Elastic Beanstalk') {
            steps {
                withAWS(region: "${env.AWS_REGION}", credentials: 'aws-credentials') {
                    elasticBeanstalkUpdateApplication(
                        applicationName: "${env.EB_APP_NAME}",
                        environmentName: "${env.EB_ENV_NAME}",
                        versionLabel: "v${env.BUILD_NUMBER}",
                        s3Bucket: "${env.S3_BUCKET}",
                        s3Key: 'application.zip'
                    )
                }
            }
        }
    }
}
