# Generated by Django 4.1.1 on 2022-11-03 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('type', models.CharField(choices=[('Trousers', 'Trousers'), ('Saree', 'Saree'), ('Lungi', 'Lungi'), ('Frocks', 'Frocks'), ('Jeans', 'Jeans'), ('Shirts', 'Shirts')], max_length=20, null=True)),
            ],
        ),
    ]