# Generated by Django 4.0.1 on 2022-01-31 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proizvodi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='novi',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]