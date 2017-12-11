

class PermissionsByActionMixin(object):
    """
    Mixed permission base model allowing for action level permission control.
    """
    permission_classes_by_action = {}

    def get_permissions(self):
        try:
            permissions = [permission() for permission in self.permission_classes_by_action[self.action]]
            return permissions
        except KeyError:
            permissions = [permission() for permission in self.permission_classes]
            return permissions
