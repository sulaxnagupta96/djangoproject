from django.contrib import admin
from .models import blood_bag,blood_bank_details,camp_schedule,donor,donor_health,employee_details,equipment_details,stock_details,transaction,user_login
# Register your models here.

admin.site.register(blood_bag)
admin.site.register(blood_bank_details)
admin.site.register(camp_schedule)
admin.site.register(donor)
admin.site.register(donor_health)
admin.site.register(employee_details)
admin.site.register(equipment_details)
admin.site.register(stock_details)
admin.site.register(transaction)
admin.site.register(user_login)
