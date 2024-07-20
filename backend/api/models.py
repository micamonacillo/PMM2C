from django.db import models

class Item(models.Model):
    first_name = models.CharField(max_length=100, default="")
    middle_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    contact_number = models.CharField(max_length=15, default="")
    email = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=255, default="")
    sex = models.CharField(max_length=10, default="")
    date_of_birth = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=100, default="")   
    citizenship = models.CharField(max_length=100, default="")
    zip_code = models.CharField(max_length=10, default="")
    height = models.FloatField(default=0.0)
    weight = models.FloatField(default=0.0)
    elementary = models.CharField(max_length=100, default="")
    secondary = models.CharField(max_length=100, default="")
    college = models.CharField(max_length=100, default="")
    mother_first_name = models.CharField(max_length=100, default="")
    mother_middle_name = models.CharField(max_length=100, default="")
    mother_surname = models.CharField(max_length=100, default="")
    father_first_name = models.CharField(max_length=100, default="")
    father_middle_name = models.CharField(max_length=100, default="")
    father_surname = models.CharField(max_length=100, default="")
    tin_number = models.CharField(max_length=20, default="")
    sss_number = models.CharField(max_length=20, default="")
    civil_status = models.CharField(max_length=20, default="")
    agency_employee_number = models.CharField(max_length=20, default="")
    
    def __str__(self):
        return (
            f"{self.first_name} {self.middle_name} {self.last_name} {self.email} "
            f"{self.address} {self.sex} {self.date_of_birth} {self.place_of_birth} "
            f"{self.citizenship} {self.height} {self.weight} {self.elementary} "
            f"{self.secondary} {self.college} {self.zip_code} "
            f"{self.mother_first_name} {self.mother_middle_name} {self.mother_surname} "
            f"{self.father_first_name} {self.father_middle_name} {self.father_surname} "
            f"{self.tin_number} {self.sss_number} {self.civil_status}  {self.agency_employee_number}" 
        )
