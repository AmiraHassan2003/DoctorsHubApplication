from django.db import models

class Specialization(models.Model):
    special_id = models.AutoField(primary_key=True)
    special_name = models.CharField(max_length=50)
    area_name = models.CharField(max_length=150, default="none")

    def __str__(self):
        return self.special_name

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctor_name = models.CharField(max_length=50)
    doctor_phone = models.CharField(max_length=50)
    doctor_address = models.CharField(max_length=50)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)

    def __str__(self):
        return self.doctor_name
