# Generated by Django 2.1.4 on 2018-12-19 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.TextField(default='this is product'),
            preserve_default=False,
        ),
    ]
