# Generated by Django 3.2 on 2021-06-27 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_friend_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
