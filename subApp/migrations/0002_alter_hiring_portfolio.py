# Generated by Django 4.1.6 on 2023-03-18 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiring',
            name='portfolio',
            field=models.FileField(max_length=300, upload_to='resume/'),
        ),
    ]