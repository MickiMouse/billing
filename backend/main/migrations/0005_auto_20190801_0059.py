# Generated by Django 2.2.3 on 2019-08-01 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190801_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reseller',
            name='telephone',
            field=models.CharField(blank=True, max_length=30, verbose_name='telephone'),
        ),
    ]
