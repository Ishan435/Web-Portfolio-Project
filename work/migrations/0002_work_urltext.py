# Generated by Django 2.1.3 on 2019-06-09 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='urltext',
            field=models.CharField(default='', max_length=100),
        ),
    ]
