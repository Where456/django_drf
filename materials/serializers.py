from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from users.models import User, Payment
from .models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.IntegerField(source='lesson_set.count', read_only=True)
    lessons = serializers.SerializerMethodField()
    owner = SlugRelatedField(slug_field='first_name', queryset=User.objects.all(), required=False)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons(self, course):
        return LessonListSerializer(Lesson.objects.filter(course=course), many=True).data


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'preview', 'video_link']


class PaymentSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())
    lesson = SlugRelatedField(slug_field='title', queryset=Lesson.objects.all())
    user = SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Payment
        fields = '__all__'


class PaymentsForOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'amount', 'payment_date', 'payment_method']
