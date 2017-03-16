# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-16 18:33
from __future__ import unicode_literals

import datetime
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
            name='Carrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default=b'2017-03-16', max_length=200)),
                ('obert', models.BooleanField(default=True)),
                ('data', models.DateField(default=datetime.date(2017, 3, 16))),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Detall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantitat', models.FloatField()),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productes.Carrito')),
            ],
        ),
        migrations.CreateModel(
            name='Producte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('preu', models.FloatField(default=0.0)),
            ],
        ),
        migrations.AddField(
            model_name='detall',
            name='producte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productes.Producte'),
        ),
    ]
