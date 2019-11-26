# Generated by Django 2.1.14 on 2019-11-26 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20191126_1525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='actor',
            new_name='actors',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='country',
            new_name='countrys',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='director',
            new_name='directors',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='editor',
            new_name='editors',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='kind',
            new_name='kinds',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='language',
            new_name='languages',
        ),
        migrations.AlterField(
            model_name='actor',
            name='movie_name',
            field=models.ForeignKey(db_column='movie_name', on_delete=django.db.models.deletion.DO_NOTHING, to='movie.Movie'),
        ),
        migrations.AlterField(
            model_name='country',
            name='movie_name',
            field=models.ForeignKey(db_column='movie_name', on_delete=django.db.models.deletion.DO_NOTHING, to='movie.Movie'),
        ),
        migrations.AlterField(
            model_name='director',
            name='movie_name',
            field=models.ForeignKey(db_column='movie_name', on_delete=django.db.models.deletion.DO_NOTHING, to='movie.Movie'),
        ),
        migrations.AlterField(
            model_name='editor',
            name='movie_name',
            field=models.ForeignKey(db_column='movie_name', on_delete=django.db.models.deletion.DO_NOTHING, to='movie.Movie'),
        ),
        migrations.AlterField(
            model_name='kind',
            name='movie_name',
            field=models.ForeignKey(db_column='movie_name', on_delete=django.db.models.deletion.DO_NOTHING, to='movie.Movie'),
        ),
        migrations.AlterField(
            model_name='language',
            name='movie_name',
            field=models.ForeignKey(db_column='movie_name', on_delete=django.db.models.deletion.DO_NOTHING, to='movie.Movie'),
        ),
        migrations.AlterUniqueTogether(
            name='actor',
            unique_together={('actor', 'movie_name')},
        ),
    ]