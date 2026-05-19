from django.db import migrations


def create_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    common_group, _ = Group.objects.get_or_create(name='common')
    authors_group, _ = Group.objects.get_or_create(name='authors')

    permissions = Permission.objects.filter(
        content_type__app_label='news',
        codename__in=['add_post', 'change_post'],
    )
    authors_group.permissions.add(*permissions)


def delete_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name__in=['common', 'authors']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RunPython(create_groups, delete_groups),
    ]
