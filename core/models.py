from accounts.models import CustomUser
from django.db import models


class Devices(models.Model):
    name = models.CharField(verbose_name="Nome do dispositivo", null=False, blank=False, max_length=255)
    owner = models.ForeignKey(CustomUser, verbose_name="Usuário/Dono", on_delete=models.PROTECT)

    class Meta:
        ordering = ["id"]
        verbose_name = "Dispositivo"
        verbose_name_plural = "Dispositivos"

    def __str__(self):
        return f"{self.name}"


class Commands(models.Model):
    name = models.CharField(verbose_name="Nome do comando", null=False, blank=False, max_length=255)
    plataform = models.CharField(verbose_name="Plataforma de Execução", null=False, blank=False, max_length=255)
    script = models.TextField(verbose_name="Script de execução", null=False, blank=False, max_length=512)

    class Meta:
        ordering = ["id"]
        verbose_name = "Comando"
        verbose_name_plural = "Comandos"

    def __str__(self):
        return f"{self.name}"


class Intents(models.Model):
    name = models.CharField(verbose_name="Nome da intenção", null=False, blank=False, max_length=255)
    command = models.ForeignKey(Commands, verbose_name="Comando", on_delete=models.PROTECT)
    device = models.ForeignKey(Devices, verbose_name="Dispositivos", on_delete=models.PROTECT)

    class Meta:
        ordering = ["id"]
        verbose_name = "Intenção"
        verbose_name_plural = "Intenções"

    def __str__(self):
        return f"{self.name}"


class ExecutionIntentsLogs(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    intent = models.ForeignKey(Intents, verbose_name="Intent", on_delete=models.PROTECT)

    class Meta:
        ordering = ["id"]
        verbose_name = "Log de execução"
        verbose_name_plural = "Logs de execução"

    def __str__(self):
        return f"{self.intent.name}"
