# Generated by Django 5.0 on 2023-12-17 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_alter_feedback_unread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='visible',
            field=models.SmallIntegerField(default=0),
        ),
    ]
