# Generated by Django 5.0 on 2023-12-17 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'ordering': ['-sent_date']},
        ),
        migrations.AddField(
            model_name='feedback',
            name='unread',
            field=models.SmallIntegerField(default=1, max_length=1),
        ),
    ]
