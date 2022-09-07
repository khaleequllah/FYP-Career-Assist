from rest_framework import serializers
from .models import UniHec, Institutions,VocationalInstitutions, OnlineCourses ,Courses
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class UniHecSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniHec
        fields = ('id', 'uni_name', 'sector', 'adress', 'phone', 'email', 'website')


class InstitutionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institutions
        fields = ('id', 'inst_name', 'adress', 'phone')

class VocationalInstitutionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VocationalInstitutions
        fields = ('id', 'inst_name', 'ownership', 'type', 'gender', 'province')


class OnlineCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineCourses
        fields = ('id','course_name','url','difficulty', 'field')



class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('id','institute', 'city','duration','field')

