# Generated by Django 3.2 on 2025-07-26 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype',
            name='is_active',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
