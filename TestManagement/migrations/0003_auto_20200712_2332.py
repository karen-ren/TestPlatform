# Generated by Django 3.0.8 on 2020-07-12 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestManagement', '0002_apimodule'),
    ]

    operations = [
        migrations.AddField(
            model_name='apiproject',
            name='update_time',
            field=models.DateTimeField(default='2020-07-12 12:32:09.749745', verbose_name='Time Updated'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='apimodule',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Time Created'),
        ),
        migrations.AlterField(
            model_name='apimodule',
            name='describe',
            field=models.TextField(default='', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='apimodule',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Module Name'),
        ),
        migrations.AlterField(
            model_name='apiproject',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Time Created'),
        ),
        migrations.AlterField(
            model_name='apiproject',
            name='describe',
            field=models.TextField(default='', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='apiproject',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Project Name'),
        ),
        migrations.AlterField(
            model_name='apiproject',
            name='status',
            field=models.BooleanField(default=1, verbose_name='Status'),
        ),
    ]