# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ArticleUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('fb_id', models.CharField(max_length=200, null=True, blank=True)),
                ('google_id', models.CharField(max_length=200, null=True, blank=True)),
                ('linkedin_id', models.CharField(max_length=200, null=True, blank=True)),
                ('device_token', models.TextField(null=True, blank=True)),
                ('device_type', models.IntegerField(default=1)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('change_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(to='app.ArticleUser'),
        ),
    ]
