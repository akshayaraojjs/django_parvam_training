from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Blog
from django.dispatch import receiver

@receiver(post_migrate)
def create_roles_and_permissions(sender, **kwargs):
    try:
        content_type = ContentType.objects.get_for_model(Blog)
        # creating the necessary permissions for the blog app (add_blog, view_blog, change_blog, delete_blog)
        # This block will add the permissions in the auth_permission table
        permissions = {
            'add_blog': Permission.objects.get_or_create(
                codename='add_blog',  # permission name
                content_type=content_type,
                name='Can add blog')[0], # permission description
            'view_blog': Permission.objects.get_or_create(
                codename='view_blog',
                content_type=content_type,
                name='Can view blog')[0],
            'change_blog': Permission.objects.get_or_create(
                codename='change_blog',
                content_type=content_type,
                name='Can change blog')[0],
            'delete_blog': Permission.objects.get_or_create(
                codename='delete_blog',
                content_type=content_type,
                name='Can delete blog')[0],
        }

        # While creating the group, the groups will be added in the auth_group table
        # While assigning the permissions to the group, the permissions will be added in the auth_group_permissions table
        # Creating 3 different groups (roles): admin, writer & user
        # Admin Group
        admin_group, _ = Group.objects.get_or_create(name='admin')  # admin group has been created
        admin_group.permissions.set(permissions.values()) # assigning all permissions to the admin group

        # Writer Group
        writer_group, _ = Group.objects.get_or_create(name='writer') # writer group has been created
        writer_group.permissions.set([
            permissions['add_blog'], # assigning only 2 permissions to the writer group : add_blog, view_blog
            permissions['view_blog']
        ])

        # User Group
        user_group, _ = Group.objects.get_or_create(name='user') # user group has been created
        user_group.permissions.set([
            permissions['view_blog'] # user group has only one permission: view_blog
        ])

        print("✅ Roles and permissions created successfully.")

    except Exception as e:
        print("⚠️ Error in creating permissions:", e)