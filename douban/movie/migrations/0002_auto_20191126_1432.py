# Generated by Django 2.1.14 on 2019-11-26 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='movieinfo',
        ),
        migrations.AlterField(
            model_name='language',
            name='movie_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_language', to='movie.Movie'),
        ),
    ]