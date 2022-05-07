# Generated by Django 3.2.2 on 2021-05-30 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0029_rename_postcomment_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('keywords', models.TextField()),
                ('Website_title', models.CharField(max_length=20)),
                ('favicon', models.ImageField(upload_to='site_image/')),
                ('copyright', models.CharField(max_length=200)),
            ],
        ),
    ]
