# Generated by Django 4.0.6 on 2022-09-06 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.CharField(default=12, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
