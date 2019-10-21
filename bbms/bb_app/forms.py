from django import forms
from .models import blood_bag,blood_bank_details,camp_schedule,donor,donor_health,employee_details,equipment_details,stock_details,transaction,user_login

class new_blood_bag(forms.ModelForm):
    class Meta:
        model= blood_bag
        fields='__all__'

class new_blood_bank_details(forms.ModelForm):
    class Meta:
        model= blood_bank_details
        fields='__all__'

class new_camp_schedule(forms.ModelForm):
    class Meta:
        model= camp_schedule
        fields='__all__'

class new_donor(forms.ModelForm):
    class Meta:
        model= donor
        fields='__all__'

class new_donor_health(forms.ModelForm):
    class Meta:
        model= donor_health
        fields='__all__'

class new_employee_details(forms.ModelForm):
    class Meta:
        model= employee_details
        fields='__all__'

class new_equipment_details(forms.ModelForm):
    class Meta:
        model= equipment_details
        fields='__all__'

class new_stock_details(forms.ModelForm):
    class Meta:
        model= stock_details
        fields='__all__'

class new_transaction(forms.ModelForm):
    class Meta:
        model= transaction
        fields='__all__'

class new_user_login(forms.ModelForm):
    class Meta:
        model= user_login
        fields='__all__'
