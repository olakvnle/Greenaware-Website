# from django.test import TestCase
# from django.utils import timezone
# from users.models import UserAccount as User
# from ..models import Payment
# import uuid

# class PaymentModelTests(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         # Create a user for the foreign key relationship
#         cls.user = User.objects.create(username='testuser', email='user@example.com', password='testpass123')

#     def test_payment_creation(self):
#         # Create a Payment instance to ensure it can be created properly
#         payment_id = uuid.uuid4()
#         payment = Payment.objects.create(
#             id=payment_id,
#             user=self.user,
#             subscription_type='Monthly',
#             amount=29.99,
#             currency='USD'
#         )

#         # Fetch the created payment from the database
#         fetched_payment = Payment.objects.get(id=payment_id)

#         # Check that the fetched payment matches the created one
#         self.assertEqual(fetched_payment.user, self.user)
#         self.assertEqual(fetched_payment.subscription_type, 'Monthly')
#         self.assertEqual(fetched_payment.amount, 29.99)
#         self.assertEqual(fetched_payment.currency, 'USD')
#         self.assertEqual(str(fetched_payment), str(payment_id))

#     def test_payment_str_method(self):
#         # Create a Payment instance
#         payment = Payment.objects.create(
#             user=self.user,
#             subscription_type='Yearly',
#             amount=99.99,
#             currency='EUR'
#         )

#         # Check __str__ method
#         self.assertEqual(str(payment), str(payment.id))

#     def test_default_values(self):
#         # Create a payment with default values
#         payment = Payment.objects.create(
#             user=self.user,
#             subscription_type='Annual',
#             amount=150.00  # Currency defaults to 'USD'
#         )

#         # Check that defaults are set correctly
#         self.assertEqual(payment.currency, 'USD')
