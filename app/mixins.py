# mixins.py
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect

class AdminCoordinatorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.is_superuser or self.request.user.groups.filter(name__in=['Coordinadores', 'Administradores']).exists()
        )

    def handle_no_permission(self):
        # Redirigir al usuario a una página específica
        return redirect('error')
