from django.contrib import admin
from .models import Appointment
from .models import Area
from .models import Hospitals

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user_display', 'booking_area', 'hospital_name', 'booking_date', 'booking_time')

    def user_display(self, obj):
        return obj.user.username  

    user_display.short_description = 'User'  

admin.site.register(Appointment, AppointmentAdmin,)

admin.site.register(Area)
admin.site.register(Hospitals)