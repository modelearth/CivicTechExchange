# Generated by Django 3.1.4 on 2021-03-03 00:16

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('democracylab', '0009_auto_20210302_2036'),
        ('civictechprojects', '0041_namerecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_legacy_organization',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', related_name='org_events', through='civictechprojects.TaggedEventOrganization', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_projects', to='democracylab.contributor'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_issue_area',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', related_name='issue_projects', through='civictechprojects.TaggedIssueAreas', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_organization',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', related_name='org_projects', through='civictechprojects.TaggedOrganization', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_organization_type',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', related_name='org_type_projects', through='civictechprojects.TaggedOrganizationType', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_stage',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', related_name='stage_projects', through='civictechprojects.TaggedStage', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_technologies',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', related_name='technology_projects', through='civictechprojects.TaggedTechnologies', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='volunteerrelation',
            name='role',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', related_name='+', through='civictechprojects.TaggedVolunteerRole', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
