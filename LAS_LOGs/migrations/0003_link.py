# Generated by Django 4.2.3 on 2023-08-10 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LAS_LOGs', '0002_entry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
