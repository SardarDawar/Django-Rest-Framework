# Generated by Django 2.1.5 on 2019-03-24 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190324_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finder',
            name='image3',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='finder',
            name='image4',
            field=models.ImageField(blank='True', upload_to=''),
        ),
    ]