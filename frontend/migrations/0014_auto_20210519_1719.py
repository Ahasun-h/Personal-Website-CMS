# Generated by Django 3.2.2 on 2021-05-19 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0013_rename_testimonials_testimonial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='site_setting',
            new_name='SiteSetting',
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_percentage',
            field=models.IntegerField(),
        ),
    ]