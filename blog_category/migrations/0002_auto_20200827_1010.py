# Generated by Django 3.1 on 2020-08-27 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcategory',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
