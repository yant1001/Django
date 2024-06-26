# Generated by Django 2.1.7 on 2024-04-10 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_qty', models.IntegerField(verbose_name='수량')),
                ('ordered_date', models.DateTimeField(auto_now_add=True, verbose_name='주문일자')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='상품')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='사용자')),
            ],
            options={
                'verbose_name': '주문',
                'verbose_name_plural': '주문',
                'db_table': 'tb_order',
            },
        ),
    ]
