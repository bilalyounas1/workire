# Generated by Django 3.2.3 on 2021-05-17 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0006_auto_20210517_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='TeamSize',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
