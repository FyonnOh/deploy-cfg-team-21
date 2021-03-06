# Generated by Django 3.2.8 on 2021-10-08 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_auto_20211008_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationLevel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='school',
            name='attendanceRate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='dropoutRate',
            field=models.FloatField(null=True),
        ),
    ]
