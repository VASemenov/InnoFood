# Generated by Django 2.2.6 on 2019-11-14 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=400)),
                ('visible', models.BooleanField(default=True)),
                ('manager', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0)),
                ('visible', models.BooleanField(default=True)),
                ('in_menu', models.BooleanField(default=True)),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cafe')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=400)),
                ('confirmed', models.BooleanField(default=False)),
                ('visible', models.BooleanField(default=True)),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cafe')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('dishes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Dish')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visible', models.BooleanField(default=True)),
                ('cafe', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Cafe')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500)),
                ('complaint_resolved', models.BooleanField(default=False)),
                ('visible', models.BooleanField(default=True)),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cafe')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Order')),
            ],
        ),
    ]
