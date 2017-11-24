# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-22 08:38
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('userperm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('qq', models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(message='\u8bf7\u8f93\u5165\u6b63\u786e\u7684QQ\u53f7', regex='^[^0]\\d{4,15}$')], verbose_name='QQ')),
                ('mobile', models.CharField(blank=True, error_messages={'required': '\u8054\u7cfb\u7535\u8bdd\u4e0d\u80fd\u4e3a\u7a7a'}, max_length=30, validators=[django.core.validators.RegexValidator(code='\u53f7\u7801\u9519\u8bef', message='\u8bf7\u8f93\u5165\u6b63\u786e\u7684\u7535\u8bdd\u6216\u624b\u673a\u53f7\u7801', regex='^[^0]\\d{6,7}$|^[1]\\d{10}$')], verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('position', models.CharField(blank=True, max_length=20, verbose_name='\u804c\u4f4d')),
                ('role', models.CharField(choices=[('SU', '\u8d85\u7ea7\u7ba1\u7406\u5458'), ('GA', '\u7ec4\u7ba1\u7406\u5458'), ('CU', '\u666e\u901a\u7528\u6237')], default='CU', max_length=2)),
            ],
            options={
                'default_permissions': (),
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237\u7ba1\u7406',
                'permissions': (('view_user', '\u67e5\u770b\u7528\u6237'), ('edit_user', '\u7ba1\u7406\u7528\u6237')),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AdminGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'default_permissions': (),
                'verbose_name': '\u7ba1\u7406\u5458\u7ec4',
                'verbose_name_plural': '\u7ba1\u7406\u5458\u7ec4\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('deptname', models.CharField(max_length=20, verbose_name='\u90e8\u95e8')),
                ('level', models.PositiveIntegerField(default=1, verbose_name='\u90e8\u95e8\u7ea7\u522b')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_children', to='userauth.Department', verbose_name='\u4e0a\u7ea7\u90e8\u95e8')),
            ],
            options={
                'default_permissions': (),
                'verbose_name': '\u90e8\u95e8',
                'verbose_name_plural': '\u90e8\u95e8\u7ba1\u7406',
                'permissions': (('view_department', '\u67e5\u770b\u90e8\u95e8'), ('edit_department', '\u7ba1\u7406\u90e8\u95e8')),
            },
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('group_name', models.CharField(max_length=80, unique=True, verbose_name='\u7528\u6237\u7ec4')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
                ('command', models.ManyToManyField(related_name='group_command_set', to='userperm.UserCommand', verbose_name='\u7528\u6237\u7ec4\u547d\u4ee4')),
                ('directory', models.ManyToManyField(related_name='group_directory_set', to='userperm.UserDirectory', verbose_name='\u7528\u6237\u7ec4\u76ee\u5f55')),
            ],
            options={
                'default_permissions': (),
                'verbose_name': '\u7528\u6237\u7ec4',
                'verbose_name_plural': '\u7528\u6237\u7ec4\u7ba1\u7406',
            },
            bases=('auth.group',),
        ),
        migrations.AddField(
            model_name='admingroup',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userauth.UserGroup'),
        ),
        migrations.AddField(
            model_name='admingroup',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ManyToManyField(related_name='user_group_set', to='userauth.UserGroup', verbose_name='\u7528\u6237\u5c5e\u7ec4'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
