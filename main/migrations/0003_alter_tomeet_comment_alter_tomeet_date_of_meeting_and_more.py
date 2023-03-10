# Generated by Django 4.1.2 on 2022-12-23 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tomeet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tomeet',
            name='comment',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tomeet',
            name='date_of_meeting',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tomeet',
            name='persone',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='tomeet',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
