# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Basket1Tbl(models.Model):
    department = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    score = models.SmallIntegerField()
    professor = models.CharField(max_length=10)
    time = models.CharField(max_length=30)
    place = models.CharField(max_length=10)
    nowmember = models.SmallIntegerField()
    total = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'basket1tbl'


class Basket2Tbl(models.Model):
    department = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    score = models.SmallIntegerField()
    professor = models.CharField(max_length=10)
    time = models.CharField(max_length=30)
    place = models.CharField(max_length=10)
    nowmember = models.SmallIntegerField()
    total = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'basket2tbl'


class Culturesubjecttbl(models.Model):
    culturesubjectcode = models.CharField(max_length=5)
    subjecttimecode = models.CharField(max_length=20)
    place = models.CharField(max_length=10)
    professorname = models.CharField(max_length=10)
    nowmember = models.SmallIntegerField()
    totalmax = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'culturesubjecttbl'


class Departmenttbl(models.Model):
    departmentcode = models.CharField(unique=True, max_length=3)
    departmentname = models.CharField(max_length=20)
    totalnum = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'departmenttbl'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Fixculturesubjecttbl(models.Model):
    fixculturesubjectcode = models.CharField(unique=True, max_length=5)
    culturesubjectname = models.CharField(max_length=20)
    completescore = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'fixculturesubjecttbl'


class Fixmajorsubjecttbl(models.Model):
    fixmajorsubjectcode = models.CharField(unique=True, max_length=5)
    majorsubjectname = models.CharField(max_length=20)
    completescore = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'fixmajorsubjecttbl'


class Logintbl(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=15)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logintbl'


class Majorsubjecttbl(models.Model):
    majorsubjectcode = models.CharField(max_length=5)
    subjecttimecode = models.CharField(max_length=20)
    place = models.CharField(max_length=10)
    professorname = models.CharField(max_length=10)
    nowmember = models.SmallIntegerField()
    totalmax = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'majorsubjecttbl'


class Professorinfotbl(models.Model):
    professor = models.ForeignKey(Logintbl, models.DO_NOTHING, db_column='professor')
    department_code = models.CharField(max_length=3)
    username = models.CharField(db_column='userName', max_length=10)  # Field name made lowercase.
    address = models.CharField(max_length=30)
    social_security_num = models.CharField(max_length=15)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone_num = models.CharField(max_length=11)
    subject_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'professorinfotbl'


class Score1Tbl(models.Model):
    yearsemester = models.CharField(max_length=4)
    subjectcode = models.CharField(max_length=5)
    subjectname = models.CharField(max_length=20)
    rating = models.CharField(max_length=2)
    numrating = models.FloatField()

    class Meta:
        managed = False
        db_table = 'score1tbl'


class Score2Tbl(models.Model):
    yearsemester = models.CharField(max_length=4)
    subjectcode = models.CharField(max_length=5)
    subjectname = models.CharField(max_length=20)
    rating = models.CharField(max_length=2)
    numrating = models.FloatField()

    class Meta:
        managed = False
        db_table = 'score2tbl'


class Studentinfotbl(models.Model):
    student = models.ForeignKey(Logintbl, models.DO_NOTHING, db_column='student')
    departmentcode = models.CharField(max_length=3)
    username = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    socialsecuritynum = models.CharField(max_length=15)
    email = models.CharField(max_length=255, blank=True, null=True)
    academic = models.CharField(max_length=5)
    phone_num = models.CharField(max_length=11)
    grade = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'studentinfotbl'


class Subjectgroup1Tbl(models.Model):
    subjectgroup1id = models.ForeignKey(Logintbl, models.DO_NOTHING, db_column='subjectgroup1id')
    studentname = models.CharField(max_length=10)
    assignmentscore = models.SmallIntegerField()
    attendancescore = models.SmallIntegerField()
    midtermexamscore = models.SmallIntegerField()
    finalexamscore = models.SmallIntegerField()
    rating = models.CharField(max_length=2)
    numrating = models.FloatField()

    class Meta:
        managed = False
        db_table = 'subjectgroup1tbl'


class Subjectgroup2Tbl(models.Model):
    subjectgroup2id = models.ForeignKey(Logintbl, models.DO_NOTHING, db_column='subjectgroup2id')
    studentname = models.CharField(max_length=10)
    assignmentscore = models.SmallIntegerField()
    attendancescore = models.SmallIntegerField()
    midtermexamscore = models.SmallIntegerField()
    finalexam_score = models.SmallIntegerField()
    rating = models.CharField(max_length=2)
    numrating = models.FloatField()

    class Meta:
        managed = False
        db_table = 'subjectgroup2tbl'
