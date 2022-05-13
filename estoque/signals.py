from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

from .models import Arma, Municao


@receiver(post_delete, sender=Arma)
def delete_arma_objeto(sender, **kwargs):
    try:
        if kwargs['instance'].id:
            kwargs['instance'].id.delete()
    except:
        pass


@receiver(post_delete, sender=Municao)
def delete_municao_objeto(sender, **kwargs):
    try:
        if kwargs['instance'].id:
            kwargs['instance'].id.delete()
    except:
        pass