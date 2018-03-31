from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from SelectGame.models import Location


class LocationsView(View):
    def locations(self, request):
        try:
            self.locations = Location.objects.filter(owner=self.user)
        except ObjectDoesNotExist:
            self.locations = {}

    def get(self, request):
        self.user = request.user
        self.locations(request)
        return render(request,
                      'SelectGame/locations.html',
                      {'locations': self.locations, })

    def post(self, request):
        self.user = request.user
        # TODO check if adress is empty, if it is empty return error message
        address = request.POST.get("location")
        new_location = Location(owner=self.user, address=address)
        new_location.save()
        self.locations(request)
        return render(request,
                      'SelectGame/locations.html',
                      {'locations': self.locations})
