# Generated by Django 3.1.4 on 2020-12-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20201211_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborativelist',
            name='name',
            field=models.CharField(default='none', max_length=128),
        ),
    ]
