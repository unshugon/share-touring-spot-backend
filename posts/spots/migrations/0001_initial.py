# Generated by Django 4.0 on 2021-12-31 11:47

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='タイトル')),
                ('image', models.ImageField(upload_to='images', verbose_name='イメージ画像')),
                ('content', models.TextField(max_length=500, verbose_name='本文')),
                ('location', django.contrib.gis.db.models.fields.GeometryField(null=True, srid=4326, verbose_name='位置情報')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='削除判定')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.useraccount', verbose_name='作成者')),
            ],
        ),
    ]
