# Generated by Django 2.2.12 on 2021-05-28 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='作者姓名')),
            ],
        ),
        migrations.CreateModel(
            name='Wife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='妻子姓名')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='oto.Author')),
            ],
        ),
    ]
