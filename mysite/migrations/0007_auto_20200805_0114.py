# Generated by Django 3.0.8 on 2020-08-05 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('comment', models.TextField()),
                ('postname', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.TextField(choices=[('android', 'android'), ('test', 'test')], default='android'),
        ),
    ]
