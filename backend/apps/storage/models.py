from django.db import models

class StorageScan(models.Model):
    device = models.foreingnkey(
        'devices.Device',
        on_delete=models.CASCADE,
        related_name='storage_scans'
    )
    total_space = models.BigIntegerField()
    used_space = models.BigIntegerField()
    free_space = models.BigIntegerField()
    scanned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Storage Scan - {self.scanned_at}"
