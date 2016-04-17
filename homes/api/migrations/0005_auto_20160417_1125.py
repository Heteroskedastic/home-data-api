# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-17 11:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_delete_simpleproperty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag_type', models.CharField(choices=[('E', 'exact duplicate'), ('S', 'merge candidate')], max_length=1)),
                ('is_open', models.BooleanField(default=True)),
                ('date_submitted', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_resolved', models.DateTimeField(auto_now=True)),
                ('note', models.CharField(blank=True, max_length=512, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='submitter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='property',
            name='valid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='resolution',
            name='final_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Property'),
        ),
        migrations.AddField(
            model_name='resolution',
            name='flag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Flag'),
        ),
        migrations.AddField(
            model_name='resolution',
            name='resolver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='flag',
            name='first_object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first', to='api.Property'),
        ),
        migrations.AddField(
            model_name='flag',
            name='second_object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second', to='api.Property'),
        ),
        migrations.AddField(
            model_name='flag',
            name='submitter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
