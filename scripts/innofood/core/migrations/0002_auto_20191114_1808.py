# Generated by Django 2.2.6 on 2019-11-14 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='complaint_order_number',
            field=models.TextField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='complaint',
            name='complaint_title',
            field=models.TextField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='description',
            field=models.TextField(default=None, max_length=500),
        ),
    ]