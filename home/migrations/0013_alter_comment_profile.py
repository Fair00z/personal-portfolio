# Generated by Django 5.0.2 on 2024-05-22 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_comment_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='profile',
            field=models.ImageField(default='profile_3.jpg', upload_to='profiles'),
        ),
    ]