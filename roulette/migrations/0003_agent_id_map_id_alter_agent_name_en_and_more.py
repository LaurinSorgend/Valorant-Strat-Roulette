# Generated by Django 5.0.6 on 2024-06-20 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roulette', '0002_remove_agent_id_remove_map_id_alter_agent_name_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='id',
            field=models.BigAutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='map',
            name='id',
            field=models.BigAutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agent',
            name='name_en',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='map',
            name='name_en',
            field=models.CharField(max_length=30),
        ),
    ]
