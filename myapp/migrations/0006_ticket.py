# Generated by Django 3.1.5 on 2021-01-17 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_concert'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone', models.CharField(default='none', max_length=128)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('concert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.concert')),
            ],
        ),
    ]
