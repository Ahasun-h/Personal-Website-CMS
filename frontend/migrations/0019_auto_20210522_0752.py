# Generated by Django 3.2.2 on 2021-05-22 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0018_auto_20210522_0729'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('category_class', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='portfolio_item/')),
                ('link', models.CharField(max_length=400)),
                ('category_class', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='frontend.portfoliocategory', verbose_name='Category')),
            ],
        ),
        migrations.DeleteModel(
            name='PortfolioMenu',
        ),
    ]