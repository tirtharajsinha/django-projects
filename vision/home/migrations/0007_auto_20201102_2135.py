# Generated by Django 3.1 on 2020-11-02 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20201102_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='action',
            field=models.CharField(choices=[('NO_FILTER', 'NO_FILTER'), ('COLORIZED', 'colorized'), ('GRAYSCALE', 'grayscale'), ('BLURRED', 'blurred'), ('BINARY', 'binary'), ('INVERT', 'invert'), ('FACE_DETECTION', 'face_detection'), ('CLASSIFICATION', 'classification'), ('SKETCHED', 'sketched'), ('SHAPE', 'shape')], max_length=50),
        ),
    ]
