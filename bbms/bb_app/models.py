from django.db import models
from datetime import date
# Create your models here.


class blood_bank_details(models.Model):
    name=models.CharField(max_length=264, unique=True,primary_key=True)
    address=models.CharField(max_length=512)
    phone_no=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class donor(models.Model):
    donor_id=models.PositiveIntegerField(primary_key=True)
    name=models.CharField(max_length=264)
    address=models.CharField(max_length=512)
    gender=models.CharField(max_length=20)
    age=models.PositiveIntegerField()
    marital_status=models.CharField(max_length=30, blank=True)
    phone_no=models.CharField(max_length=20)
    blood_group=models.CharField(max_length=4)
    occupation=models.CharField(max_length=30, blank=True)
    email_id=models.EmailField(blank=True)

    def __str__(self):
        return str(self.donor_id)

class blood_bag(models.Model):
    blood_bag_id=models.PositiveIntegerField(unique=True,primary_key=True)
    donor_id=models.ForeignKey(donor,on_delete=models.CASCADE)
    blood_bank_name=models.ForeignKey(blood_bank_details,on_delete=models.CASCADE)
    status=models.BooleanField()
    collection_date=models.DateField(date.today())
    expiry_date=models.DateField()
    entered_by=models.CharField(max_length=264)
    bag_weight=models.IntegerField()

    def __str__(self):
        return str(self.blood_bag_id)

class camp_schedule(models.Model):
    code=models.PositiveIntegerField(primary_key=True)
    name=models.CharField(max_length=264)
    address=models.CharField(max_length=512)
    contact_person=models.CharField(max_length=264)
    phone_no=models.CharField(max_length=20)
    schedule_date=models.DateField()
    no_of_beds=models.PositiveIntegerField()

    def __str__(self):
        return str(self.code)

class donor_health(models.Model):
    donor_id=models.ForeignKey(donor,primary_key=True, on_delete=models.CASCADE)
    body_weight=models.PositiveIntegerField()
    temprature=models.PositiveIntegerField()
    pulse=models.PositiveIntegerField()
    blood_pressure=models.PositiveIntegerField()
    haemoglobin=models.PositiveIntegerField()
    test_vdrl=models.CharField(max_length=4)
    test_hbsag=models.CharField(max_length=4)
    test_mp=models.CharField(max_length=4)
    test_hcv=models.CharField(max_length=4)
    test_hiv=models.CharField(max_length=4)

    def __str__(self):
        return str(self.donor_id)

class employee_details(models.Model):
    employee_id=models.PositiveIntegerField(primary_key=True)
    employee_name=models.CharField(max_length=264)
    gender=models.CharField(max_length=20)
    dob=models.DateField()
    qualification=models.CharField(max_length=264)
    designation=models.CharField(max_length=264)
    address=models.CharField(max_length=512)
    phone_no=models.CharField(max_length=20)
    blood_group=models.CharField(max_length=4)
    email_id=models.EmailField()
    joining_date=models.DateField()

    def __str__(self):
        return str(self.employee_id)

class equipment_details(models.Model):
    equipment_code=models.IntegerField(primary_key=True)
    equipment_name=models.CharField(max_length=264)
    no_of_equipment=models.IntegerField()
    purchase_date=models.DateField()
    purchased_from=models.CharField(max_length=264)
    cost_per_piece=models.IntegerField()

    def __str__(self):
        return str(self.equipment_code)

class user_login(models.Model):
    username=models.CharField(max_length=264, primary_key=True)
    password=models.CharField(max_length=264)

    def __str__(self):
        return self.username

class stock_details(models.Model):
    blood_group=models.CharField(max_length=4, primary_key=True)
    no_of_bags=models.CharField(max_length=4)

    def __str__(self):
        return self.blood_group

class transaction(models.Model):
    transaction_id=models.IntegerField(primary_key=True)
    recipient_name=models.CharField(max_length=264)
    date=models.DateField()
    blood_group=models.CharField(max_length=4)
    no_of_bags=models.IntegerField()
    bill_amount=models.IntegerField()

    def __str__(self):
        return str(self.transaction_id)
