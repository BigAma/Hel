# Generated by Django 4.0.2 on 2022-02-23 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_demande_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_img',
            field=models.ImageField(default='cat.svg', null=True, upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='professionnel',
            name='pro_img',
            field=models.ImageField(default='avatar.svg', null=True, upload_to='upload/'),
        ),
    ]
