# Generated by Django 5.1.3 on 2024-12-01 15:58

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('asosiy', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Fan',
                'verbose_name_plural': 'Fanlar',
            },
        ),
        migrations.CreateModel(
            name='Yonalish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('aktiv', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Yonalish',
                'verbose_name_plural': 'Yonalishlar',
            },
        ),
        migrations.CreateModel(
            name='Ustoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('jins', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')], max_length=10)),
                ('yosh', models.PositiveSmallIntegerField(default=25, validators=[django.core.validators.MinValueValidator(25), django.core.validators.MaxValueValidator(60)])),
                ('daraja', models.CharField(choices=[('Bakalavr', 'Bakalavr'), ('Magistr', 'Magistr'), ('PHD', 'PHD')], max_length=50)),
                ('fan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.fan')),
            ],
            options={
                'verbose_name': 'Ustoz',
                'verbose_name_plural': 'Ustozlar',
            },
        ),
        migrations.AddField(
            model_name='fan',
            name='yonalish',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.yonalish'),
        ),
    ]
