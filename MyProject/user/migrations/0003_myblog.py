# Generated by Django 3.2.4 on 2022-09-03 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_igallery_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='myblog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=40)),
                ('bdes', models.TextField()),
                ('bpic', models.ImageField(null=True, upload_to='static/blogs')),
                ('bdate', models.DateField()),
            ],
        ),
    ]
