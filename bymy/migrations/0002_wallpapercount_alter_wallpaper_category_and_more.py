# Generated by Django 4.2.7 on 2023-11-11 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bymy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WallpaperCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.IntegerField()),
                ('likes', models.IntegerField()),
                ('views', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='wallpaper',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='WallpaperComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('likes', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
