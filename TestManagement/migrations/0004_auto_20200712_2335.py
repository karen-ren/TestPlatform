# Generated by Django 3.0.8 on 2020-07-12 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestManagement', '0003_auto_20200712_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiproject',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Time Updated'),
        ),
    ]
