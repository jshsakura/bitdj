# Generated by Django 2.0 on 2018-01-10 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20180111_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='filtered_image',
            field=models.ImageField(null=True, upload_to='assets/images/portfolio/%Y/%m/%d/filtered'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(null=True, upload_to='assets/images/portfolio/%Y/%m/%d/origin'),
        ),
    ]
