from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = "用户管理"
    
    def ready(self):
        pass
        import users.signals
