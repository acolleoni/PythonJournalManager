# Generated by Django 4.1.7 on 2023-03-17 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalissues', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img_url',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
