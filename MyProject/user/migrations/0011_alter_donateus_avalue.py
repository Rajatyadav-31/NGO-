# Generated by Django 3.2.4 on 2022-09-10 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_rename_donate_donateus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donateus',
            name='avalue',
            field=models.CharField(max_length=30),
        ),
    ]
