# Generated by Django 5.2.1 on 2025-05-12 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('age', models.IntegerField()),
                ('mois_grossesse', models.IntegerField()),
                ('poids_kg', models.FloatField()),
                ('taille_cm', models.FloatField()),
                ('activite', models.CharField(max_length=20)),
                ('regime', models.CharField(max_length=20)),
                ('antecedents', models.CharField(max_length=20)),
                ('symptome', models.CharField(max_length=20)),
                ('profil_risque', models.CharField(choices=[('normal', 'Normal'), ('modéré', 'Modéré'), ('élevé', 'Élevé')], max_length=10)),
                ('conseil', models.TextField()),
            ],
        ),
    ]
