# Generated by Django 4.0.4 on 2022-05-30 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='icono_SinImagen.jpg', upload_to=''),
        ),
    ]
