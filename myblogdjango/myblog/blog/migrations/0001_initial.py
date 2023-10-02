# Generated by Django 4.2.5 on 2023-09-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='default title', max_length=200)),
                ('heading', models.CharField(max_length=200, unique=True)),
                ('content', models.TextField(verbose_name='Content')),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateField(verbose_name='Date of publication')),
            ],
            options={
                'verbose_name': 'Write',
                'verbose_name_plural': 'Writes',
            },
        ),
    ]