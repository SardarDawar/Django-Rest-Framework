# Generated by Django 2.1.5 on 2019-03-24 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190324_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='finder',
            name='status',
            field=models.CharField(choices=[('Active', 'active'), ('IN_Active', 'inactive')], default=0, max_length=25),
            preserve_default=False,
        ),
    ]
