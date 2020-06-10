from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CourseSerializer,LessonSerializer,CourseCreateSerializer
from .models import Course,Lesson
from membership.models import UserMembership
class CourseLessonAPI(APIView):
    serializer_class = CourseSerializer

    def get(self,request,*args,**kwargs):
        print(self.request['id'])
        return Response({"hey"})

class CourseAPI(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
class CourseCreateAPI(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer

    def perform_create(self, serializer):
        return serializer.save(slug = self.request.data['title'])
class CourseDetailsAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, pk, *args, **kwargs):
        print(pk)
        user = 1
        user_membership = UserMembership.objects.filter(user=user).first()
        user_membership_type = user_membership.membership.membership_type
        print(user_membership_type)
        course = Course.objects.filter(pk=pk).first()
        courses = Course.objects.filter(pk=pk)
        course_allowed_mem_types = course.allowed_membership.all()
        if course_allowed_mem_types.filter(membership_type=user_membership_type):
            print("allowed")
            return Response(CourseSerializer(course).data)
        else:
            return Response({"You have finished your free articles for this week. Kindlu upgrade your acount"})
        # print(course)
        return Response({"je"})
class LessonAPI(generics.ListCreateAPIView):
    queryset = Lesson.objects.all().order_by('position')
    serializer_class = LessonSerializer
class LessonDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all().order_by('position')
    serializer_class = LessonSerializer

    def get(self,request,pk,*args,**kwargs):
        print(pk)
        lesson = Lesson.objects.filter(pk=pk).first()
        if lesson:
            z = lesson.course
            user = 1
            user_membership = UserMembership.objects.filter(user=user).first()
            user_membership_type = user_membership.membership.membership_type
            course = Course.objects.filter(title=z).first()
            if course:
                print(course)
                course_allowed_mem_types = course.allowed_membership.all()
                if course_allowed_mem_types.filter(membership_type=user_membership_type):
                    print("allowed")
                    return Response(LessonSerializer(lesson).data)
                else:
                    return Response({"You have finished your free articles for this week. Kindlu upgrade your acount"})
            else:
                return Response({"This has either been deleted or moved"})
        else:
            return Response({"This has either been deleted or moved"})