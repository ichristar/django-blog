# Generated by Django 5.0.4 on 2025-04-05 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_blog_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.TextField(choices=[('Draft', 'Draft'), ('published', 'published')], default='Draft', max_length=20),
        ),
    ]
