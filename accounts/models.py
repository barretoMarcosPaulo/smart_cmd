from django.contrib.auth.models import User


class CustomUser(User):
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return f"Adm - {self.get_full_name()}"
