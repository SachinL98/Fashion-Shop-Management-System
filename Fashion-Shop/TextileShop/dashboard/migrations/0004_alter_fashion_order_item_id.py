# Generated by Django 4.1.1 on 2022-11-02 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_fashion_order_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fashion_order',
            name='item_Id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]