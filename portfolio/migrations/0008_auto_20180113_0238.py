# Generated by Django 2.0 on 2018-01-12 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20180112_2241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='author',
            new_name='email',
        ),
    ]
