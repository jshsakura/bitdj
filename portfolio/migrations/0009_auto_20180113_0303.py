# Generated by Django 2.0 on 2018-01-12 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20180113_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(null=True, upload_to='portfolio/%Y/%m/%d'),
        ),
    ]
