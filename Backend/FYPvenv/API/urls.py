from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UniHecViewSet, CoursesViewSet, OnlineCoursesViewSet, InstitutionsViewSet, VocationalInstitutionsViewSet,  UniCoursesViewSet


router = routers.DefaultRouter()
# router.register('users', UserViewSet)
router.register('Universities', UniHecViewSet)
router.register('Courses', CoursesViewSet)
router.register('OnlineCourses', OnlineCoursesViewSet)
router.register('Institutions', InstitutionsViewSet)
router.register('VocationalInstitutions', VocationalInstitutionsViewSet)
router.register('UniCourses', UniCoursesViewSet)
# router.register('Search', SearchViewset)

urlpatterns = [
    path('', include(router.urls))
]
