# Generated by Django 4.1.7 on 2023-04-04 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxes', '0002_rename_carousel_image_carouselimages_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxSavingsGuide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo')),
                ('card_title', models.CharField(max_length=50)),
                ('card_description', models.CharField(max_length=200)),
            ],
        ),
    ]