# Generated by Django 2.2.2 on 2019-11-06 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191106_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assign_Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('agent_id', models.ManyToManyField(to='app.CreateAgent')),
                ('case_id', models.ManyToManyField(to='app.CaseCreation')),
            ],
        ),
    ]