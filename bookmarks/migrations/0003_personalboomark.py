# Generated by Django 2.0.5 on 2018-05-24 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookmarks', '0002_auto_20180523_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalBoomark',
            fields=[
                ('bookmark_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bookmarks.Bookmark')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('bookmarks.bookmark',),
        ),
    ]
