from django.contrib import admin

# Register your models here.
from .models import UniHec, Courses, OnlineCourses, Institutions, VocationalInstitutions,UniCourses

class UniHecAdmin(admin.ModelAdmin):
    list_display = ('uni_name', 'sector','email', 'website')
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('institute', 'city','duration','field')
class OnlineCoursesAdmin(admin.ModelAdmin):
    list_display = ('course_name','difficulty', 'field')
class InstitutionsAdmin(admin.ModelAdmin):
    list_display = ('inst_name', 'adress', 'phone')
class VocationalInstitutionsAdmin(admin.ModelAdmin):
    list_display = ('inst_name','type','gender','province')

class UniCoursesAdmin(admin.ModelAdmin):
    list_display = ('institute','city','duration','course','field')

admin.site.register(UniHec, UniHecAdmin)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(OnlineCourses, OnlineCoursesAdmin)
admin.site.register(Institutions, InstitutionsAdmin)
admin.site.register(VocationalInstitutions, VocationalInstitutionsAdmin)
admin.site.register(UniCourses, UniCoursesAdmin)