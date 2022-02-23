# Generated by Django 4.0.2 on 2022-02-23 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wouldyourather',
            name='option_one',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wouldyourather',
            name='option_one_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='wouldyourather',
            name='option_two',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wouldyourather',
            name='option_two_count',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
