from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Appointment, Area, Hospitals
from datetime import datetime, timedelta

class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user', email='test@example.com', password='test_password')
        self.area = Area.objects.create(name='Test City')
        self.hospital = Hospitals.objects.create(area=self.area, text='Test Hospital')
       
        booking_date = datetime.now().date() + timedelta(days=1)  
        booking_time = datetime.now().time().replace(second=0, microsecond=0) 
        self.appointment = Appointment.objects.create(
            user=self.user,
            booking_area=self.area.name,
            hospital_name=self.hospital.text,
            booking_date=booking_date,
            booking_time=booking_time
        )

    def test_appointment_details_view(self):
        response = self.client.get(reverse('appointment_details', args=[self.appointment.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appointment_details.html')

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_book_appointment_view(self):
        self.client.login(username='test_user', password='test_password')
        response = self.client.get(reverse('book_appointment'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_appointment.html')

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_logout_view(self):
       
        try:
            reverse('logout')
        except:
            return 

       
        self.client.login(username='test_user', password='test_password')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

