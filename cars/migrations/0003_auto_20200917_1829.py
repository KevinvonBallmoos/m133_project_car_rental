# Generated by Django 3.1.1 on 2020-09-17 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20200917_0850'),
        ('cars', '0002_auto_20200912_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='map.map'),
        ),
    ]
