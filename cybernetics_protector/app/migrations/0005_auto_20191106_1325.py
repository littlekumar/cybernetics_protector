# Generated by Django 2.2.2 on 2019-11-06 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20191106_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assign_agent',
            name='description',
            field=models.CharField(max_length=50),
        ),
    ]