# Generated by Django 4.2.1 on 2023-06-04 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recipe_storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=50)),
                ('recipe_description', models.TextField()),
                ('recipe_image', models.ImageField(upload_to='recipe_images')),
            ],
        ),
    ]
