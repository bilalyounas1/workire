# Generated by Django 4.1.1 on 2023-01-07 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0038_rename_search_country_jobblogfeaturedjobs_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobblog',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
