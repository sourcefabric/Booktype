# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-18 04:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('editor', '0009_chapter_content_json'),
        ('edit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InviteCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expire_on', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.Book')),
                ('roles', models.ManyToManyField(to='core.Role', verbose_name=b'Roles to assign')),
            ],
        ),
    ]
