# Generated by Django 3.1.7 on 2021-03-07 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0002_auto_20210305_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='target_distance',
            field=models.IntegerField(default=0),
        ),
    ]
