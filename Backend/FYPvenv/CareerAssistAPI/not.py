# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Courses(models.Model):
    institute = models.TextField(db_column='Institute', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    duration = models.CharField(db_column='Duration', max_length=50, blank=True, null=True)  # Field name made lowercase.
    field = models.TextField(db_column='Field', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'courses'


class Institutions(models.Model):
    inst_name = models.TextField(db_column='Inst_Name', blank=True, null=True)  # Field name made lowercase.
    adress = models.CharField(db_column='Adress', max_length=200, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'institutions'


class OnlineCourses(models.Model):
    course_name = models.TextField(db_column='Course_Name', blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=250, blank=True, null=True)  # Field name made lowercase.
    difficulty = models.TextField(db_column='Difficulty', blank=True, null=True)  # Field name made lowercase.
    field = models.TextField(db_column='Field', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'online_courses'


class UniCourses(models.Model):
    institute = models.TextField(db_column='Institute', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    duration = models.CharField(db_column='Duration', max_length=60, blank=True, null=True)  # Field name made lowercase.
    course = models.TextField(db_column='Course', blank=True, null=True)  # Field name made lowercase.
    field = models.TextField(db_column='Field', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'uni_courses'


class UniHec(models.Model):
    uni_name = models.TextField(db_column='Uni_Name', blank=True, null=True)  # Field name made lowercase.
    sector = models.TextField(db_column='Sector', blank=True, null=True)  # Field name made lowercase.
    adress = models.CharField(db_column='Adress', max_length=200, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=512, db_collation='ascii_general_ci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'uni_hec'


class VocationalInstitutions(models.Model):
    inst_name = models.TextField(db_column='Inst_Name', blank=True, null=True)  # Field name made lowercase.
    ownership = models.TextField(db_column='Ownership', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    gender = models.TextField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    province = models.TextField(db_column='Province', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vocational_institutions'
