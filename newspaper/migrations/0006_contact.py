# Generated by Django 5.1.7 on 2025-04-17 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0005_advertisement_description_category_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('message', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
