# Generated by Django 3.2.2 on 2021-05-19 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkProcces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='work_procces/')),
                ('procces_name', models.CharField(max_length=400)),
            ],
        ),
    ]
