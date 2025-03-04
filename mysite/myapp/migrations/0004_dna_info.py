# Generated by Django 5.0.7 on 2024-11-09 07:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_dna_sequence_seq_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='dna_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq_info', models.CharField(max_length=10000000)),
                ('clean_sequence1', models.CharField(max_length=10000000)),
                ('reverse_comp', models.CharField(max_length=10000000)),
                ('comp', models.CharField(max_length=10000000)),
                ('trans', models.CharField(max_length=1000000)),
                ('translat_protein', models.CharField(max_length=100000)),
                ('translat_protein_stop', models.CharField(max_length=100000)),
                ('gc', models.FloatField()),
                ('dna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='myapp.dna_sequence')),
            ],
        ),
    ]
