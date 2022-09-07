from django.shortcuts import render
from rest_framework import viewsets
from .models import UniHec, Courses ,OnlineCourses , Institutions, VocationalInstitutions,UniCourses
from .serializers import UniHecSerializer, CoursesSerializer, OnlineCoursesSerializer, InstitutionsSerializer, VocationalInstitutionsSerializer, UniCoursesSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication

# Create your views here.

# class SearchViewSet(viewsets.ModelViewSet):


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (AllowAny,)
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)


class UniCoursesViewSet(viewsets.ModelViewSet):
    queryset = UniCourses.objects.all()
    serializer_class = UniCoursesSerializer
    permission_classes = (AllowAny,)

class UniHecViewSet(viewsets.ModelViewSet):
    queryset = UniHec.objects.all()
    serializer_class = UniHecSerializer
    permission_classes = (AllowAny,)
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = (AllowAny,)
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

class OnlineCoursesViewSet(viewsets.ModelViewSet):
    queryset = OnlineCourses.objects.all()
    serializer_class = OnlineCoursesSerializer
    permission_classes = (AllowAny,)
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

class InstitutionsViewSet(viewsets.ModelViewSet):
    queryset = Institutions.objects.all()
    serializer_class = InstitutionsSerializer
    permission_classes = (AllowAny,)
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

class VocationalInstitutionsViewSet(viewsets.ModelViewSet):
    queryset = VocationalInstitutions.objects.all()
    serializer_class = VocationalInstitutionsSerializer
    permission_classes = (AllowAny,)
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)