# Generated by Django 4.0.3 on 2022-04-21 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_userprofile_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
