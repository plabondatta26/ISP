from django.db import models


# Create your models here.
class ServiceModel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, help_text="Service name")
    price = models.PositiveIntegerField(blank=True, null=True, help_text="Service price")
    details = models.JSONField(blank=True, null=True, help_text="Service details")
    view_order = models.PositiveIntegerField(blank=True, null=True, help_text="Order of this service")
    status = models.BooleanField(default=True, help_text="Is service is active")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Package creation time")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "services"


class PackageModel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, help_text="Package name")
    price = models.PositiveIntegerField(blank=True, null=True, help_text="Package price")
    details = models.JSONField(blank=True, null=True, help_text="Package details")
    service = models.ManyToManyField(ServiceModel, related_name='package_service')
    status = models.BooleanField(default=True, help_text="Is package is active")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Package creation time")

    # def __str__(self):
    #     return self.name
    #
    # def services(self):
    #     return ",".join(str(s.name) for s in self.service.all())

    class Meta:
        db_table = "packages"
