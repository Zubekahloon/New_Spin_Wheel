# Generated by Django 5.1.7 on 2025-04-04 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spinapp', '0004_house_delete_uploadedcsv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignedhouse',
            name='house_number',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
