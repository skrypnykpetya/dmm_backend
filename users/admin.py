from django.contrib import admin
from .models import *
from django import forms

class UsersAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'name',
        'status',
        'is_active',
    )

class PermissionsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug'
    )


class RolesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug'
    )

class RolesPermissionsAdmin(admin.ModelAdmin):
    list_display = (
        'role',
        'permission'
    )


class UserRolesAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'role'
    )



class UsersDataAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'name',
        'status',
    )

class UserPermissionAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'permission'
    )


admin.site.register(UsersPermissions, UserPermissionAdmin)
admin.site.register(UsersRoles, UserRolesAdmin)
admin.site.register(Permissions, PermissionsAdmin)
admin.site.register(RolesPermissions, RolesPermissionsAdmin)
admin.site.register(Roles, RolesAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(UsersData, UsersDataAdmin)