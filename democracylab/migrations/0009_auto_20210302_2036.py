# Generated by Django 3.1.4 on 2021-03-02 20:36

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('democracylab', '0008_contributor_qiqo_signup_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='user_technologies',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', related_name='technology_users', through='democracylab.UserTaggedTechnologies', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
