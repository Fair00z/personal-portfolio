# Generated by Django 5.0.2 on 2024-05-22 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_comment_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='profile',
        ),
    ]
