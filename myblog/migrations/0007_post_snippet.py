# Generated by Django 3.2.4 on 2021-06-26 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_post_header_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Clink Link Above to Read Blog Post', max_length=255),
        ),
    ]
