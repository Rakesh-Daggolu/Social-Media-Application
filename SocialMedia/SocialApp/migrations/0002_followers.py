# Generated by Django 3.2.6 on 2023-01-10 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SocialApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='SocialApp.user')),
                ('following_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='SocialApp.user')),
            ],
        ),
    ]
