# Generated by Django 5.0 on 2023-12-17 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_alter_feedback_options_feedback_unread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='unread',
            field=models.SmallIntegerField(default=1),
        ),
    ]