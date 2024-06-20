# Generated by Django 5.0.6 on 2024-06-20 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roulette', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentspecifictext',
            name='attacking',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='agentspecifictext',
            name='defending',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='agentspecifictext',
            name='random_player',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mapspecifictext',
            name='attacking',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mapspecifictext',
            name='defending',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mapspecifictext',
            name='random_player',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='text',
            name='attacking',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='text',
            name='defending',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='text',
            name='random_player',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='agent',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='map',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]