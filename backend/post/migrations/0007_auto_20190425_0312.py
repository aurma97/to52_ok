# Generated by Django 2.1.3 on 2019-04-25 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20190425_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumb',
            field=models.TextField(default=None, max_length=1000),
        ),
    ]
