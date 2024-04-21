from django.shortcuts import render
from django.http import JsonResponse
from django.views import View


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
        return render(request, 'index.html')


class ObserverRegisterView(View):
    def get(self, request):
        return render(request, 'observer.html')


class APIView(View):
    def get(self, request):
        return render(request, 'api.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class DashboardView(View):
    def get(self, request):
        context = {
            'page_name': 'Dashboard'
        }
        return render(request, 'observer/dashboard.html', context)


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


class UserView(View):
    def get(self, request):
        return render(request, 'observer/user.html')
