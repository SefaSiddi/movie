# Generated by Django 4.1.4 on 2022-12-21 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='dddddfs', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
