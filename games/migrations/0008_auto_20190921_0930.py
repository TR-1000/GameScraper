# Generated by Django 2.2.5 on 2019-09-21 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_auto_20190921_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
