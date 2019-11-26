# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actor(models.Model):
    actor = models.CharField(max_length=255)
    movie_name = models.ForeignKey('Movie', models.DO_NOTHING, db_column='movie_name')


    class Meta:
        managed = True
        db_table = 'actor'
        unique_together=['actor','movie_name']



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class Country(models.Model):
    country = models.CharField(max_length=255)
    movie_name = models.ForeignKey('Movie', models.DO_NOTHING, db_column='movie_name')

    class Meta:
        managed = True
        db_table = 'country'
        unique_together = ['country', 'movie_name']

class Director(models.Model):
    director = models.CharField(max_length=255)
    movie_name = models.ForeignKey('Movie', models.DO_NOTHING, db_column='movie_name')

    class Meta:
        managed = True
        db_table = 'director'
        unique_together = ['director', 'movie_name']


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class Editor(models.Model):
    editor = models.CharField(max_length=255)
    movie_name = models.ForeignKey('Movie', models.DO_NOTHING, db_column='movie_name')

    class Meta:
        managed = True
        db_table = 'editor'
        unique_together = ['editor', 'movie_name']


class Kind(models.Model):
    kind = models.CharField(max_length=255)
    movie_name = models.ForeignKey('Movie', models.DO_NOTHING, db_column='movie_name')

    class Meta:
        managed = True
        db_table = 'kind'
        unique_together = ['kind', 'movie_name']


class Language(models.Model):
    language = models.CharField(max_length=255)
    movie_name = models.ForeignKey('Movie', models.DO_NOTHING, db_column='movie_name')

    class Meta:
        managed = True
        db_table = 'language'
        unique_together = ['language', 'movie_name']


class Movie(models.Model):
    movie_name = models.CharField(primary_key=True, max_length=255)
    directors = models.CharField(max_length=255, blank=True, null=True)
    editors = models.CharField(max_length=255, blank=True, null=True)
    actors = models.CharField(max_length=255, blank=True, null=True)
    kinds = models.CharField(max_length=255, blank=True, null=True)
    countrys = models.CharField(max_length=255, blank=True, null=True)
    languages = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.CharField(max_length=255, blank=True, null=True)
    runtime = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    imdb = models.CharField(db_column='IMDb', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rating_num = models.FloatField(blank=True, null=True)
    votes = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'movie'

