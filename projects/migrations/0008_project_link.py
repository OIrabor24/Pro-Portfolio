# Generated by Django 4.0.3 on 2022-03-24 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_project_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]
