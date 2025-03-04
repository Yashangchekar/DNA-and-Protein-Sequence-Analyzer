# Generated by Django 5.0.7 on 2024-11-09 06:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprotein', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProteinProperties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('molecular_weight', models.FloatField()),
                ('isoelectric_point', models.FloatField()),
                ('extinction_coefficient', models.FloatField()),
                ('instability_index', models.FloatField()),
                ('gravy', models.FloatField()),
                ('aliphatic_index', models.FloatField()),
                ('aromatic_ratio', models.FloatField()),
                ('hydrophobic_polarity', models.FloatField()),
                ('protein', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='myprotein.protein_sequence')),
            ],
        ),
    ]
