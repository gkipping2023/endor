from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
Certif_Medico_Class = (
    ('primera','PRIMERA CLASE'),
    ('segunda','SEGUNDA CLASE')
)

class User(AbstractUser):
    email = models.EmailField(unique=True,null=True,max_length=150)
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gov_id = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    pob = models.CharField(max_length=50)
    dob = models.DateField(null=True, blank=False, default='1900-01-01')
    phone = models.CharField(max_length=50, null=True, blank=False, default=0)
    medical = models.CharField(max_length=50,choices=Certif_Medico_Class,default='1')
    medical_date = models.DateField(default='1900-01-01')
    is_paid = models.BooleanField(default=False)
    USERNAME_FIELD  =   'email'
    REQUIRED_FIELDS =   ['name','last_name']

    def __str__(self):
        return self.email

class Logbook(models.Model):
    date = models.DateField()
    equip = models.CharField(max_length=250, null=True, blank=True, default=0) #null = False
    registration = models.CharField(max_length=10, null=True, blank=True, default=0)
    origin = models.CharField(max_length=80, null=True, blank=True, default=0)
    destination = models.CharField(max_length=80, null=True, blank=True, default=0)
    airplane_sel = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    airplane_mel = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    airplane_cfi = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    x_country = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    night = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    act_ifr = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    sim_ifr = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    gnd_trainer = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    pic = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    sic = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    dual = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    totalt = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    remarks = models.CharField(max_length=250, default=0, null=True, blank=True)
    synth_trainer = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)

    def __str__(self):
        return str(self.date)

class Airports(models.Model):
    oaci_id = models.CharField(max_length=4)
    iata_id = models.CharField(max_length=3)
    airport_name = models.CharField(max_length=80)
    display_name = models.CharField(max_length=80)

    def __str__(self):
        return str(self.oaci_id)