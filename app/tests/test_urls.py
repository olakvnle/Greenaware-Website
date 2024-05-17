# from django.test import SimpleTestCase
# from django.urls import reverse, resolve
# from app.views import IndexView, APIView, DashboardView, ObservationView, CourseView, UserView, AboutView, PricingView, PricingPlanView, ContactView
#
# class TestUrls(SimpleTestCase):
#
#     def test_index_url_is_resolved(self):
#         url = reverse('index')
#         self.assertEquals(resolve(url).func.view_class, IndexView)
#
#     def test_about_url_is_resolved(self):
#         url = reverse('about')
#         self.assertEquals(resolve(url).func.view_class, AboutView)
#
#     def test_api_url_is_resolved(self):
#         url = reverse('api')
#         self.assertEquals(resolve(url).func.view_class, APIView)
#
#     def test_pricing_url_is_resolved(self):
#         url = reverse('pricing')
#         self.assertEquals(resolve(url).func.view_class, PricingView)
#
#     def test_pricing_plan_url_is_resolved(self):
#         url = reverse('pricing_plan')
#         self.assertEquals(resolve(url).func.view_class, PricingPlanView)
#
#     def test_contact_url_is_resolved(self):
#         url = reverse('contact')
#         self.assertEquals(resolve(url).func.view_class, ContactView)
#
#     def test_dashboard_url_is_resolved(self):
#         url = reverse('dashboard')
#         self.assertEquals(resolve(url).func.view_class, DashboardView)
#
#     def test_observation_url_is_resolved(self):
#         url = reverse('observation')
#         self.assertEquals(resolve(url).func.view_class, ObservationView)
#
#     def test_courses_url_is_resolved(self):
#         url = reverse('courses')
#         self.assertEquals(resolve(url).func.view_class, CourseView)
#
#     def test_users_profiles_url_is_resolved(self):
#         url = reverse('users')
#         self.assertEquals(resolve(url).func.view_class, UserView)
