# Generated by Django 3.2.9 on 2021-11-07 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20211107_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code_number',
            field=models.CharField(default='brand+năm+số TT 2 số (ex: mikrotik202101)', max_length=100),
        ),
    ]
