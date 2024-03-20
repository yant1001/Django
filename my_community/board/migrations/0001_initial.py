# Generated by Django 2.1.7 on 2024-03-20 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_auto_20240320_0058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성시간')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='작성자')),
            ],
            options={
                'db_table': 'tb_board',
            },
        ),
    ]
