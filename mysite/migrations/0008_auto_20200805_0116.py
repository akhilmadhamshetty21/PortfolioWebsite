# Generated by Django 3.0.8 on 2020-08-05 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_auto_20200805_0114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='comments',
        ),
    ]
