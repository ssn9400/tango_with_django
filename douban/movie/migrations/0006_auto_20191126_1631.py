# Generated by Django 2.1.14 on 2019-11-26 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20191126_1601'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='country',
            unique_together={('country', 'movie_name')},
        ),
        migrations.AlterUniqueTogether(
            name='director',
            unique_together={('director', 'movie_name')},
        ),
        migrations.AlterUniqueTogether(
            name='editor',
            unique_together={('editor', 'movie_name')},
        ),
        migrations.AlterUniqueTogether(
            name='kind',
            unique_together={('kind', 'movie_name')},
        ),
        migrations.AlterUniqueTogether(
            name='language',
            unique_together={('language', 'movie_name')},
        ),
    ]