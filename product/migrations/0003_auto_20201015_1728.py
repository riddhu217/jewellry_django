# Generated by Django 3.1.1 on 2020-10-15 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200914_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='contact_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
