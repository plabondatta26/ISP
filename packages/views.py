from django.db.models import Q, Count
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, View
from .models import ServiceModel, PackageModel


class HomeView(TemplateView):
    template_name = 'packages/home.html'

    def get(self, request, *args, **kwargs):
        service_qs = ServiceModel.objects.filter(status=True).order_by('view_order')
        data_list = []
        for service in service_qs:
            if 'is_service' in service.details:
                if service.details['is_service']:
                    data_list.append(service)

        return render(request, self.template_name, context={"data": data_list})


class PackagesView(View):
    template_name = 'packages/packges.html'

    def post(self, request, *args, **kwargs):
        package_qs = []
        services = request.POST.getlist('service', None)
        service_ids = [eval(i) for i in services]
        if services:
            package_qs = PackageModel.objects.filter(service__in=service_ids, status=True).distinct()
        return render(request, self.template_name, context={"data": package_qs})


class BillingView(View):
    template_name = 'packages/billing.html'

    def post(self, request, *args, **kwargs):
        package_id = request.POST.get('package', None)
        package_obj = PackageModel.objects.filter(id=package_id, status=True).first()
        data = {}
        service_list = []
        total = 0
        if package_obj:
            data["package"] = package_obj
            for item in package_obj.service.filter(status=True):
                 if "is_addon" in item.details.keys():
                    if item.details["is_addon"]:
                        service_list.append(item)
                        total += item.price
            data["service"] = service_list
            data["total"] = total + package_obj.price
        return render(request, self.template_name, context=data)
