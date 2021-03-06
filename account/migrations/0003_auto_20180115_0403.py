# Generated by Django 2.0 on 2018-01-14 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180115_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='about',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='About'),
        ),
        migrations.AlterField(
            model_name='user',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Facebook link'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gogle_plus_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Gogle plus link'),
        ),
        migrations.AlterField(
            model_name='user',
            name='pinterest_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Pinterest link'),
        ),
        migrations.AlterField(
            model_name='user',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Twitter link'),
        ),
    ]
