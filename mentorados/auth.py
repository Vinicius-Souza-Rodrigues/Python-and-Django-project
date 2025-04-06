from .models import Mentorados

def valida_token(token):
  return Mentorados.objects.filter(token=token).first()
