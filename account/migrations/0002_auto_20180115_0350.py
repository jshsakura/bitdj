# Generated by Django 2.0 on 2018-01-14 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='about'),
        ),
        migrations.AddField(
            model_name='user',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='facebook link'),
        ),
        migrations.AddField(
            model_name='user',
            name='gogle_plus_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='gogle-plus link'),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_image/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='user',
            name='pinterest_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='pinterest link'),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='twitter link'),
        ),
    ]
