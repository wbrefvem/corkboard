pipeline {
	node {
		stage('Build') {
			sh 'pip install -r requirements.txt'
			sh 'python manage.py test'
		}
	}
}