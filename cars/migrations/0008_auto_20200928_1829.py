# Generated by Django 3.1.1 on 2020-09-28 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_auto_20200924_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='types',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='CarTypes',
        ),
    ]