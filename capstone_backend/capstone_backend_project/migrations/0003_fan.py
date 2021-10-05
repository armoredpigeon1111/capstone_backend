# Generated by Django 3.2.8 on 2021-10-05 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone_backend_project', '0002_auto_20211005_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('genre1', models.CharField(max_length=50)),
                ('genre2', models.CharField(max_length=50)),
                ('genre3', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
            ],
        ),
    ]