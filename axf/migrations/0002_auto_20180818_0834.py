# Generated by Django 2.0.5 on 2018-08-18 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=20)),
                ('trackid', models.CharField(max_length=10)),
                ('isDelete', models.NullBooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='wheel',
            name='trackid',
            field=models.CharField(max_length=20),
        ),
    ]
