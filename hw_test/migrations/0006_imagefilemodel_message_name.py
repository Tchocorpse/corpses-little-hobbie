# Generated by Django 3.0.7 on 2020-10-16 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw_test', '0005_auto_20201002_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagefilemodel',
            name='message_name',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
