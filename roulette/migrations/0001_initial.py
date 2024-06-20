# Generated by Django 5.0.6 on 2024-06-18 18:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AgentSpecificText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roulette.agent')),
            ],
        ),
        migrations.CreateModel(
            name='MapSpecificText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roulette.map')),
            ],
        ),
    ]