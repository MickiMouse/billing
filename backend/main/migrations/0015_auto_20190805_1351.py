# Generated by Django 2.2.3 on 2019-08-05 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20190805_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='packet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.Packet'),
        ),
    ]
