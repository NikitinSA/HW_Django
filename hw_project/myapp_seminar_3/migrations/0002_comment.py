# Generated by Django 4.2.4 on 2023-09-03 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_sem3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('public_date', models.DateTimeField(auto_now=True)),
                ('change_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp_sem3.author')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp_sem3.post')),
            ],
        ),
    ]