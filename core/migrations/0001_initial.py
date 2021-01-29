# Generated by Django 3.0.5 on 2020-04-07 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TempImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(upload_to='temp/')),
                ('result_file', models.ImageField(blank=True, null=True, upload_to='results/')),
            ],
        ),
    ]