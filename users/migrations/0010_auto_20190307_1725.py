# Generated by Django 2.1.7 on 2019-03-07 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_customuser_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
