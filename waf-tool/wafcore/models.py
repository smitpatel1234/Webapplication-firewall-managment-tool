from django.db import models
# Create your models 
class Configuration(models.Model):
    name  = models.CharField(max_length=100)
    port = models.IntegerField()
    ip = models.GenericIPAddressField()
    class Meta: 
        constraints = [
            models.UniqueConstraint(fields=['port', 'ip'], name='unique_port_ip')
        ]
