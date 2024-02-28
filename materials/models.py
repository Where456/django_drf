from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    preview = models.ImageField(upload_to='course_previews/')
    description = models.TextField()


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    preview = models.ImageField(upload_to='lesson_previews/')
    video_link = models.URLField()
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
