# Generated by Django 5.0.2 on 2024-05-22 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='profile',
            field=models.ImageField(default='static/images/comment.jpg', upload_to=''),
        ),
    ]
