# Generated by Django 4.1.7 on 2023-04-09 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_utilisateur_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='gère',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='category',
            field=models.CharField(choices=[('Responsable_vente_et_achat', 'Responsable_vente_et_achat'), ('analyste_achat', 'analyste_achat'), ('analyste_vente', 'analyste_vente')], max_length=190, null=True),
        ),
    ]
