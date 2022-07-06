from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, view, request, obj):
        return (view.method in permissions.SAFE_METHODS
                or obj.author == view.user)
