# Generated by Django 3.1 on 2020-08-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_category', '0001_initial'),
        ('blog_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, to='blog_category.PostCategory'),
        ),
    ]
