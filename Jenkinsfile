pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Цей крок автоматично стягує код з GitHub
                checkout scm
            }
        }

        stage('Docker Down') {
            steps {
                echo 'Зупиняємо старі контейнери...'
                sh 'docker compose down'
            }
        }

        stage('Docker Deploy') {
            steps {
                echo 'Збираємо образи та запускаємо FastAPI...'
                sh 'docker compose up --build -d'
            }
        }

        stage('Cleanup') {
            steps {
                echo 'Очищаємо застарілі шари Docker, щоб не забивати диск...'
                sh 'docker image prune -f'
            }
        }
    }

    post {
        success {
            echo 'Ура! Збірка та деплой пройшли успішно! 🎉'
        }
        failure {
            echo 'Щось пішло не так. Перевіряй логи контейнерів! ❌'
        }
    }
}
