# Generated by Django 3.2 on 2025-07-27 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_mood'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': [('has_comment_permission', 'User Has Comment Permission')], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='mood',
            field=models.PositiveSmallIntegerField(choices=[(3, 'Fear'), (1, 'Sad'), (2, 'Happy')]),
        ),
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='blog.comment'),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_attribute', to='blog.producttype'),
        ),
    ]
