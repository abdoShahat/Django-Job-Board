# Generated by Django 3.1.6 on 2021-07-08 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_auto_20210708_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
    ]
