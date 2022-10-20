from django.contrib import admin

# Register your models here.

from .models import Departments,Doctors,Booking


admin.site.register(Departments)
admin.site.register(Doctors)

class BookingAdmin(admin.ModelAdmin):
    list_display =  ('id', 'patient_name', 'patient_phone', 'patient_mail', 'doc_name','booking_date', 'booked_on' )

admin.site.register(Booking, BookingAdmin)

