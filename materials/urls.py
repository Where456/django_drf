from django.urls import path, include
from rest_framework import routers

from materials.views import CourseViewSet, LessonListCreateAPIView, LessonRetrieveUpdateDestroyAPIView, \
    LessonListAPIView, LessonCreateAPIView, LessonUpdateAPIView, LessonRetrieveAPIView, LessonDestroyAPIView, \
    PaymentListAPIView, SubscriptionDestroyAPIView, SubscriptionCreateAPIView
from users.views import UserViewSet

router = routers.DefaultRouter()

router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('lessons/', LessonListCreateAPIView.as_view(), name='lesson-list-create'),
    path('lessons/list/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDestroyAPIView.as_view(), name='lesson-detail'),
    path('lessons/<int:pk>/retrieve/', LessonRetrieveAPIView.as_view(), name='lesson-retrieve'),
    path('lessons/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lessons/<int:pk>/destroy/', LessonDestroyAPIView.as_view(), name='lesson-destroy'),
    path('lessons/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson-delete'),

    path('subscription_create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscription_destroy/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscription_destroy'),

    path('payments/', PaymentListAPIView.as_view(), name='payments-list'),
]

