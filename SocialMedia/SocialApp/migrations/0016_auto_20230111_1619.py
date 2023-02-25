# Generated by Django 3.2.6 on 2023-01-11 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialApp', '0015_followers_base_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nfollowers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='nfollowing',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='nposts',
            field=models.IntegerField(default=0),
        ),
    ]
