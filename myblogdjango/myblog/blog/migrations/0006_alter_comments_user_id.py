# Generated by Django 4.2.5 on 2023-09-28 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.user'),
        ),
    ]
