from django.shortcuts import render
from rest_framework.routers import DefaultRouter
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .serializers import StudentSerializer,ElectiveCourseSerializer
from .models import Student,ElectiveCourse


# Create your views here.
class ElectiveCourseViewset(mixins.CreateModelMixin, mixins.ListModelMixin,\
                            mixins.UpdateModelMixin, mixins.RetrieveModelMixin,\
                                mixins.DestroyModelMixin, GenericViewSet):
    
    queryset = ElectiveCourse.objects.filter(active=True)
    serializer_class = ElectiveCourseSerializer


class StudentViewset(mixins.CreateModelMixin, mixins.ListModelMixin,\
                            mixins.UpdateModelMixin, mixins.RetrieveModelMixin,\
                                mixins.DestroyModelMixin, GenericViewSet):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

router = DefaultRouter()

router.register("electivecourse",ElectiveCourseViewset, basename="electivecourse")
router.register("student",StudentViewset, basename="student")