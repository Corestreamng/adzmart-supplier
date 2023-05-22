from django.contrib.auth.decorators import login_required
from django.utils.deprecation import MiddlewareMixin
from django.urls import resolve
from django.conf import settings

class RejectAnonymousUsersMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path.startswith('/admin/'):
            return None
        current_route_name = resolve(request.path_info).url_name

        if current_route_name in settings.AUTH_EXEMPT_ROUTES:
            return

        if  request.user.is_authenticated:
            return

        return login_required(view_func)(request, *view_args, **view_kwargs)
