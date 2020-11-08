# Generated by Django 3.1 on 2020-11-02 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_upload_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='action',
            field=models.CharField(choices=[('NO_FILTER', 'NO_FILTER'), ('COLORIZED', 'colorized'), ('GRAYSCALE', 'grayscale'), ('BLURRED', 'blurred'), ('BINARY', 'binary'), ('INVERT', 'invert'), ('FACE_DETECTION', 'face_detection'), ('CLASSIFICATION', 'classification'), ('SKETCHED', 'sketched')], max_length=50),
        ),
    ]
