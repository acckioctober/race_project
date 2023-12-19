# Generated by Django 4.2.6 on 2023-12-19 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('race', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='review',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='race.event', verbose_name='Мероприятие'),
        ),
        migrations.AddField(
            model_name='organizer',
            name='event',
            field=models.ManyToManyField(related_name='organizers', to='race.event', verbose_name='Событие'),
        ),
        migrations.AddField(
            model_name='organizer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Организатор'),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='race.event', verbose_name='Событие'),
        ),
        migrations.AddField(
            model_name='eventschedule',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='race.event', verbose_name='Мероприятие'),
        ),
        migrations.AddField(
            model_name='eventregistration',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='race.event', verbose_name='Мероприятие'),
        ),
        migrations.AddField(
            model_name='eventregistration',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='race.racetype', verbose_name='Участвующие группы'),
        ),
        migrations.AddField(
            model_name='eventregistration',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='race.location', verbose_name='Место проведения мероприятия'),
        ),
        migrations.AddField(
            model_name='event',
            name='race_types',
            field=models.ManyToManyField(to='race.racetype', verbose_name='Участвующие группы'),
        ),
    ]
