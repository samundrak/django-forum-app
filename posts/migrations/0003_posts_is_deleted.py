# Generated by Django 3.0.2 on 2020-01-20 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_posts_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]