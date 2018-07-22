from django.shortcuts import render
from django.views import View

from .forms import Submit_ifsc
from .models import IFSC

import requests
import json


class ifsc_view(View):
    def get(self, request, *args, **kwargs):
        the_ifsc = Submit_ifsc()
        my_context = {
            "title": "IFSC Finder",
            "ifsc_form": the_ifsc
        }
        return render(request, "ifsc.html", my_context)

    def post(self, request, *args, **kwargs):
        the_ifsc = Submit_ifsc(request.POST)
        if the_ifsc.is_valid():
            ifsc_code = the_ifsc.cleaned_data.get("ifsc")
            print(ifsc_code)
            obj, created = IFSC.objects.get_or_create(ifsc=ifsc_code)
            print(obj.ifsc)
            url = "https://ifsc.razorpay.com/" + str(obj.ifsc)
            print(url)
            r = requests.get(url)
            data = json.loads(r.content)
            print(data)
            if data == "Not Found":
                return render(request, "not_exists.html")
            else:
                return render(request, "details.html", data)
