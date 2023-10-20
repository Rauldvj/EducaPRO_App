from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile

@receiver(post_save, sender=Profile)
def add_user_to_students_group(sender, instance, created, **kwargs):
    if created:
        try:
            funcionarios = Group.objects.get(name='Funcionarios')
        except Group.DoesNotExist:
            funcionarios = Group.objects.create(name='Administradores')
            funcionarios = Group.objects.create(name='Funcionarios')
            funcionarios = Group.objects.create(name='Coordinador')
            funcionarios = Group.objects.create(name='Psicopedagógo')
            funcionarios = Group.objects.create(name='Psicólogo')
            funcionarios = Group.objects.create(name='Terapeuta Ocupacional')
            funcionarios = Group.objects.create(name='Fonoaudiologo')
        instance.user.groups.add(funcionarios)