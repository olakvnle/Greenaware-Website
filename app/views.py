import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Invalid Email'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Email already exists'}, status=400)
        return JsonResponse({'email_valid': True})


class IndexView(View):
    def get(self, request):
        context={}
        return render(request, 'new/index.html')


class APIView(View):
    def get(self, request):
        context = {
            'type': 'subscriber'
        }
        return render(request, 'new/api.html',context)
    

class AboutView(View):
    def get(self, request):
        return render(request, 'new/about.html')
    
class PricingView(View):
    def get(self, request):
        return render(request, 'new/pricing.html')
    
class PricingPlanView(View):
    def get(self, request):
        return render(request, 'new/pricing_plan.html')

class ContactView(View):
    def get(self, request):
        return render(request, 'new/contact.html')


class DashboardView(LoginRequiredMixin,View):

    def get(self, request):

        context = {
            'page_name': 'Dashboard'
        }
        return render(request, 'observer/dashboard.html', context)


class ObservationRecordView(LoginRequiredMixin,View):

    def get(self, request):

        context = {
            'page_name': 'Dashboard'
        }
        return render(request, 'observer/view_observation.html', context)


class CourseView(View):
    def get(self, request):
        context = {
            'page_name': 'Course'
        }
        return render(request, 'observer/course.html', context)


class ObservationView(View):
    def get(self, request):
        context = {
            'page_name': 'Observation'
        }
        return render(request, 'observer/observation.html', context)


    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        return JsonResponse({'email_valid': True})




class UserView(View):
    def get(self, request):
        return render(request, 'observer/user.html')
