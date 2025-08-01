# Generated by Django 3.2 on 2025-07-27 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20250727_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='mood',
            field=models.PositiveSmallIntegerField(choices=[(2, 'Happy'), (1, 'Sad'), (3, 'Fear')]),
        ),
    ]
