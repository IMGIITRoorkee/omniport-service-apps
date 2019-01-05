from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from discovery.available import available_apps
from configuration.serializers.app.app import AppSerializer


class AppViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Return the information on various apps on Omniport
    """

    permission_classes = [IsAuthenticated, ]
    serializer_class = AppSerializer
    pagination_class = None
    lookup_field = 'name'

    def get_object(self):
        search_term = self.kwargs.get(self.lookup_field)
        all_apps = available_apps(self.request, search_term=search_term)

        if len(all_apps) == 1:
            app_tuple = all_apps[0]
            _, app_configuration = app_tuple
            return app_configuration
        else:
            return super().get_object()

    def get_queryset(self):
        return [
            app_configuration
            for (app, app_configuration)
            in available_apps(self.request)
        ]
