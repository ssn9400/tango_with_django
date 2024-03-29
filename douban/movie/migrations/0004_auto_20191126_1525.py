# Generated by Django 2.1.14 on 2019-11-26 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20191126_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='movie_name',
            field=models.ForeignKey(db_column='movie_name', on_delete=django.db.models.deletion.DO_NOTHING, related_name='FK_actor_movie', to='movie.Movie'),
        ),
        migrations.AlterField(
            model_name='country',
            name='movie_name',
            field=models.ForeignKey(db_column='movie_name', on_delete=django.db.models.deletion.DO_NOTHING, related_name='FK_country_movie', to='movie.Movie'),
        ),
        migrations.AlterField(
            model_name='director',
            name='movie_name',
            field=models.ForeignKey(db_column='movie_name', on_delete=django.db.models.deletion.DO_NOTHING, related_name='FK_director_movie', to='movie.Movie'),
        ),
        migrations.AlterField(
            model_name='editor',
            name='movie_name',
            field=models.ForeignKey(db_column='movie_name', on_delete=django.db.models.deletion.DO_NOTHING, related_name='FK_editor_movie', to='movie.Movie'),
        ),
        migrations.AlterField(
            model_name='kind',
            name='movie_name',
            field=models.ForeignKey(db_column='movie_name', on_delete=django.db.models.deletion.DO_NOTHING, related_name='FK_kind_movie', to='movie.Movie'),
        ),
        migrations.AlterField(
            model_name='language',
            name='movie_name',
            field=models.ForeignKey(db_column='movie_name', on_delete=django.db.models.deletion.DO_NOTHING, related_name='FK_language_movie', to='movie.Movie'),
        ),
    ]
