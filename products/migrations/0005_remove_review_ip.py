# Generated by Django 3.2.25 on 2024-03-22 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_review_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='ip',
        ),
    ]