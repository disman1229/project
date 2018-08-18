# Generated by Django 2.0.5 on 2018-08-18 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0002_auto_20180818_0834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mustbuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=20)),
                ('trackid', models.CharField(max_length=20)),
                ('isDelete', models.NullBooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='nav',
            name='trackid',
            field=models.CharField(max_length=20),
        ),
    ]