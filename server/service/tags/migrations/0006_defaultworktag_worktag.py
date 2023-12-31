# Generated by Django 4.2.3 on 2023-11-24 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LAS_LOGs', '0004_work'),
        ('tags', '0005_defaulttopictag_defaultusertag_rename_tag_topictag_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultWorkTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WorkTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LAS_LOGs.work')),
            ],
        ),
    ]
