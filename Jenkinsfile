pipeline{
        agent any
            stage('Build Images'){
                steps{
                    sh "./scripts/build.sh"
                }
            }
            stage('Run Ansible'){
                steps{
                    sh "./scripts/ansible.sh"
                }
            }
            stage('Push'){
                steps{
                    sh "./scripts/push.sh"
                }
            }
            stage('Deploy'){
                steps{
                    sh "./scripts/deploy.sh"
                }
            }
        }
}