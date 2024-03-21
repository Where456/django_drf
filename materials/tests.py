from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from materials.models import Course, Lesson
from users.models import User, Subscriptions


class CourseLessonSubscriptionTests(TestCase):
    def setUp(self):
        # Создание пользователей
        self.user1 = User.objects.create_user('user1', 'user1@example.com', 'user1password')
        self.user2 = User.objects.create_user('user2', 'user2@example.com', 'user2password')

        # Создание курса
        self.course = Course.objects.create(title='Test Course', description='Test Description')

        # Создание урока
        self.lesson = Lesson.objects.create(title='Test Lesson', description='Test Lesson Description',
                                            course=self.course, video_link='https://www.youtube.com/')

        # Клиент для API запросов
        self.client = APIClient()
        self.client.force_authenticate(user=self.user1)

    def test_lesson_create(self):
        # Формирование данных для запроса
        data = {
            'title': 'New Lesson',
            'description': 'New Description',
            'course': self.course.id,
            'video_link': 'https://www.youtube.com/new'
        }

        # Выполнение запроса на создание урока
        response = self.client.post('/materials/lessons/create/', data)

        # Проверка успешного создания урока
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Lesson.objects.count(), 2, "Lesson was not created")

    def test_list_lessons(self):
        response = self.client.get('/materials/lessons/list/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) >= 1)  # Предполагается, что в базе данных есть хотя бы 1 урок


class SubscriptionTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Создание тестовых пользователей
        self.user1 = User.objects.create_user(username='user21', email='user1@example.com', password='pass123')
        self.user2 = User.objects.create_user(username='user32', email='user2@example.com', password='pass123')

        # Создание тестового курса
        self.course = Course.objects.create(title='Test1 Course', description='Test Description')

        # Аутентификация первого пользователя
        self.client.force_authenticate(user=self.user1)

    def test_create_subscription(self):
        # Подписка пользователя на курс
        response = self.client.post('/materials/subscription_create/', {
            'user': self.user1.id,
            'course': self.course.id,
            'status': True
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Subscriptions.objects.filter(user=self.user1, course=self.course).exists())

    def test_delete_subscription(self):
        # Создание подписки
        subscription = Subscriptions.objects.create(user=self.user1, course=self.course, status=True)

        # Удаление подписки
        response = self.client.delete(f'/materials/subscription_destroy/{subscription.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Subscriptions.objects.filter(id=subscription.id).exists())
