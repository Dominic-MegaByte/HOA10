# Generated by Django 5.1.6 on 2025-04-30 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign',
            name='compatibility',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='sign',
            name='personalities',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='sign',
            name='weakness',
            field=models.CharField(max_length=300),
        ),
    ]
