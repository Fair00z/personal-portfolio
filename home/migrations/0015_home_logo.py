# Generated by Django 5.0.2 on 2024-05-23 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_comment_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='logo',
            field=models.ImageField(default='logo.png', upload_to='logo'),
        ),
    ]