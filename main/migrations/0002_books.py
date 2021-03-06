# Generated by Django 3.1.3 on 2021-01-18 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('title', models.CharField(max_length=180)),
                ('subtitle', models.CharField(max_length=180)),
                ('description', models.CharField(max_length=180)),
                ('price', models.CharField(max_length=150)),
                ('genre', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('year', models.DateField(auto_created=True)),
                ('date', models.CharField(auto_created=True)),
            ],
        ),
    ]
