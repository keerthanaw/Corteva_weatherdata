from django.apps import AppConfig
from django.db.models.signals import post_migrate

# Define a new AppConfig subclass for the 'api' app
class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    # Define ready function to be called when the app is loaded
    def ready(self):
        super().ready()
        post_migrate.connect(self.handle_post_migrate, sender=self)

    # Define a function to handle the post_migrate signal
    def handle_post_migrate(self, sender, **kwargs):
        pass
