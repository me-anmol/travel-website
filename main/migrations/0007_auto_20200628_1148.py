# Generated by Django 3.0.7 on 2020-06-28 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_news_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinations',
            name='type',
            field=models.CharField(choices=[('Beach', 'Beach'), ('HillStation', 'Hill Station'), ('safari', 'safari'), ('city', 'city'), ('International', 'International')], max_length=100),
        ),
    ]
