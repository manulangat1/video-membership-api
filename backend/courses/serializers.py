from rest_framework import serializers
from .models import Course,Lesson


class CourseSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = (
            'id',
            'slug',
            'title',
            'description',
            'lessons',
            'allowed_membership',
        )
    def get_lessons(self,obj):
        return LessonsSerializer(obj.lesson.all().order_by('position'),many=True).data
class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'description',
            'allowed_membership',
        )

class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'id',
            'slug',
            # 'course',
            'position',
            'video'
        )
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'id',
            'slug',
            'course',
            'position',
            'video'
        )