# Generated by Django 3.1.2 on 2022-12-28 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('ecommerceAPIsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('books', models.ManyToManyField(to='ecommerceAPIsapp.Book')),
                ('products', models.ManyToManyField(to='ecommerceAPIsapp.Product')),
            ],
            options={
                'ordering': ['cart_id', '-created_at'],
            },
        ),
    ]