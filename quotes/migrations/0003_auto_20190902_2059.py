# Generated by Django 2.2.5 on 2019-09-02 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_auto_20190902_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='key',
            field=models.CharField(max_length=100),
        ),
    ]
