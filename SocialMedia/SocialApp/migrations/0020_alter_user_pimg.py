# Generated by Django 3.2.6 on 2023-01-12 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialApp', '0019_alter_user_pimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pimg',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
    ]
