# Generated by Django 3.1.3 on 2022-11-03 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='singer',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
