# Generated by Django 2.2.3 on 2019-08-05 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20190805_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='card',
            name='status',
            field=models.BooleanField(default=False, verbose_name='status'),
        ),
    ]
