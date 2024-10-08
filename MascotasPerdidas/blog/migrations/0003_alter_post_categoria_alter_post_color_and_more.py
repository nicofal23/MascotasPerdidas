# Generated by Django 5.0.7 on 2024-08-11 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_categoria_alter_post_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categoria',
            field=models.CharField(choices=[('Perro', 'Perro'), ('Gato', 'Gato')], max_length=5),
        ),
        migrations.AlterField(
            model_name='post',
            name='color',
            field=models.CharField(choices=[('Negro', 'Negro'), ('Blanco', 'Blanco'), ('Marrón', 'Marrón'), ('Gris', 'Gris')], max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(upload_to='blog_images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='zona',
            field=models.CharField(choices=[('Sur', 'Sur'), ('Centro', 'Centro'), ('Norte', 'Norte'), ('Este', 'Este'), ('Oeste', 'Oeste')], max_length=100),
        ),
    ]
