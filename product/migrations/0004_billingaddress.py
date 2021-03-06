# Generated by Django 3.1.1 on 2020-11-10 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20201015_1728'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=20, null=True)),
                ('lname', models.CharField(blank=True, max_length=20, null=True)),
                ('Address', models.TextField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('zip', models.CharField(blank=True, max_length=7, null=True)),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
            ],
        ),
    ]
