from django.db import models

# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    user_type = models.CharField(max_length=100)

class doctor(models.Model):
    login_id = models.ForeignKey(login,default=1,on_delete=models.CASCADE)
    d_name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)




class patient(models.Model):
    login_id = models.ForeignKey(login,default=1,on_delete=models.CASCADE)
    p_name = models.CharField(max_length=200)
    dob = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    pin = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)


class schedule(models.Model):
    date = models.CharField(max_length=200)
    doctor = models.ForeignKey(doctor,default=1,on_delete=models.CASCADE)
    starting_time = models.CharField(max_length=200)
    ending_time = models.CharField(max_length=200)
    total_token = models.CharField(max_length=200)

class doctor_rating(models.Model):
    patient_id = models.ForeignKey(patient,default=1,on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(doctor,default=1,on_delete=models.CASCADE)
    rating = models.CharField(max_length=200)
    date = models.CharField(max_length=200)

class appointment(models.Model):
    patient = models.ForeignKey(patient,default=1,on_delete=models.CASCADE)
    Schedule = models.ForeignKey(schedule,default=1,on_delete=models.CASCADE)
    date = models.CharField(max_length=200)
    token = models.IntegerField()

class prescription(models.Model):
    appointment = models.ForeignKey(appointment,default=1,on_delete=models.CASCADE)
    drug_name = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    dosage = models.CharField(max_length=200)
    route = models.CharField(max_length=200)
    instruction = models.CharField(max_length=200)

class chat(models.Model):
    sender_id = models.IntegerField()
    receiver_id = models.IntegerField()
    chat = models.CharField(max_length=500)
    date = models.CharField(max_length=200)
    type = models.CharField(max_length=200)






