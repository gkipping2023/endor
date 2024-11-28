from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Logbook,Airports, User
from django.db.models import Sum
from datetime import datetime, timedelta
import calendar
from django.http import HttpResponse
from django.conf import settings
from django.template.loader import get_template
#from xhtml2pdf import pisa
from .forms import new_entry_form, newUser_form
from django.core.paginator import Paginator

# Create your views here.
# george@george.com/george/panama2024


def home(request):
    last_90 = datetime.now() - timedelta(days=90)
    last_30 = datetime.now() - timedelta(days=30)
    last_365 = datetime.now() - timedelta(days=365)
    now_m = datetime.now().month
    mar_2025= 16 #Marzo 2025
    rem_mo = mar_2025 - int(now_m)
    now_y = datetime.now().year
    #si no hay entries, no puede redondear y da error, xq seria NoneType
    try:
        last_90_days = round(Logbook.objects.filter(date__gte=last_90).aggregate(Sum('totalt'))['totalt__sum'],2)
    except:
        last_90_days = 0.00
    try:
        last_365_days = round(Logbook.objects.filter(date__gte=last_365).aggregate(Sum('totalt'))['totalt__sum'],2)
    except:
        last_365_days = 0.00
    try :
        last_30_days = round(Logbook.objects.filter(date__gte=last_30).aggregate(Sum('totalt'))['totalt__sum'],2)
    except:
        last_30_days = 0.00
    log_30_days = Logbook.objects.all().order_by('-date')[0:10]
    total_flight = round(Logbook.objects.aggregate(Sum('totalt'))['totalt__sum'],2)
    total_737 = round(Logbook.objects.filter(equip__startswith='7').aggregate(Sum('totalt'))['totalt__sum'],2)
    total_pa28 = round(Logbook.objects.filter(equip__startswith='PA28').aggregate(Sum('totalt'))['totalt__sum'],2)
    total_sic = round(Logbook.objects.aggregate(Sum('sic'))['sic__sum'],2)
    total_pic = round(Logbook.objects.aggregate(Sum('pic'))['pic__sum'],2)
    total_cfi = round(Logbook.objects.aggregate(Sum('airplane_cfi'))['airplane_cfi__sum'],2)
    total_sim = round(Logbook.objects.aggregate(Sum('synth_trainer'))['synth_trainer__sum'],2)
    try:
        homet_asel= round(Logbook.objects.filter(date__gte=last_30).aggregate(Sum('airplane_sel'))['airplane_sel__sum'],2)
    except:
        homet_asel = 0.00
    try:
        homet_amel = round(Logbook.objects.filter(date__gte=last_30).aggregate(Sum('airplane_mel'))['airplane_mel__sum'],2)
    except:
        homet_amel = 0.00
    try:
        homet_cfi = round(Logbook.objects.filter(date__gte=last_30).aggregate(Sum('airplane_cfi'))['airplane_cfi__sum'],2)
    except:
        homet_cfi = 0.00
    try:
        homet_xc = round(Logbook.objects.filter(date__gte=last_30).aggregate(Sum('x_country'))['x_country__sum'],2)
    except:
        homet_xc = 0.00
    try:
        homet_night = round(Logbook.objects.filter(date__gte=last_30).aggregate(Sum('night'))['night__sum'],2)
    except:
        homet_night = 0.00
    try:
        homet_act_ifr = round(Logbook.objects.filter(date__gte=last_30).aggregate(Sum('act_ifr'))['act_ifr__sum'],2)
    except:
        homet_act_ifr = 0.00
    try:
        homet_sim_ifr = round(Logbook.objects.filter(date__gte=last_30).aggregate(Sum('sim_ifr'))['sim_ifr__sum'],2)
    except:
        homet_sim_ifr = 0.00
    try:
        homet_gnd_trainer = round(Logbook.objects.filter(date__gte=last_30).aggregate(Sum('gnd_trainer'))['gnd_trainer__sum'],2)
    except:
        homet_gnd_trainer = 0.00
    try:
        homet_pic = round(Logbook.objects.filter(date__gte=last_30).aggregate(Sum('pic'))['pic__sum'],2)
    except:
        homet_pic = 0.00
    try:
        homet_sic = round(Logbook.objects.filter(date__gte=last_30).aggregate(Sum('sic'))['sic__sum'],2)
    except:
        homet_sic = 0.00
    try:
        homet_dual = round(Logbook.objects.filter(date__gte=last_30).aggregate(Sum('dual'))['dual__sum'],2)
    except:
        homet_dual = 0.00
    try:
        homet_synth_trainer = round(Logbook.objects.filter(date__gte=last_30).aggregate(Sum('synth_trainer'))['synth_trainer__sum'],2)
    except:
        homet_synth_trainer = 0.00
    #Chart
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    months_data = []
    for x in months:
        dataset = Logbook.objects.filter(date__year=now_y).filter(date__month=x).aggregate(Sum('totalt'))['totalt__sum']
        if dataset is None:
            dataset = 0
            months_data.append(dataset)
        else:
            months_data.append(int(dataset)) # use int b/c SQLite does not support Float

    up_totales = 4000
    up_b737 = 3000
    up_cm = 2000
    # 176 Credito de horas de SIM hasta el 13 de abril.
    # 500 Credito por FTD-A
    rem_total = up_totales - total_flight
    rem_total_cr = up_totales - total_flight - 500 - total_sim
    rem_b737 = up_b737 - total_737
    if up_cm - total_737 < 0 :
        rem_cm = 0
    else:
        rem_cm = up_cm - total_737

    min_mo_avr = round(rem_total_cr/rem_mo,2)

    return render(request, 'hoth/home.html',{
        'dataset': dataset,
        'months_data':months_data,
        'months' : months,
        'homet_synth_trainer':homet_synth_trainer,
        'homet_dual':homet_dual,
        'homet_sic':homet_sic,
        'homet_pic':homet_pic,
        'homet_gnd_trainer':homet_gnd_trainer,
        'homet_sim_ifr':homet_sim_ifr,
        'homet_act_ifr':homet_act_ifr,
        'homet_night':homet_night,
        'homet_xc':homet_xc,
        'homet_cfi':homet_cfi,
        'homet_amel':homet_amel,
        'homet_asel':homet_asel,
        'total_sim':total_sim,
        'rem_total_cr':rem_total_cr,
        'up_totales':up_totales,
        'up_b737': up_b737,
        'up_cm':up_cm,
        'rem_total': rem_total,
        'rem_b737':rem_b737,
        'rem_cm':rem_cm,
        'last_30_days':last_30_days,
        'last_365_days':last_365_days,
        'log_30_days':log_30_days,
        'last_90_days':last_90_days,
        'total_flight':total_flight,
        'total_737':total_737,
        'total_pa28':total_pa28,
        'total_sic':total_sic,
        'total_pic':total_pic,
        'total_cfi':total_cfi,
        'now_m':now_m,
        'rem_mo':rem_mo,
        'min_mo_avr':min_mo_avr,
    })

def new_entry(request):
    airport_datalist = Airports.objects.all()
    new_entry = new_entry_form()
    if request.method == 'POST':
        save_entry = new_entry_form(request.POST)
        if save_entry.is_valid():
            save_entry.save()
            print('Success!')
            #messages.success(request,'Entry recorded Successfully!')
            return redirect('home')
    return render(request,'hoth/new_entry.html',{
    'new_entry': new_entry,
    'airport_datalist':airport_datalist
    })

def logbook(request):
    date_from = request.GET.get('from')
    date_to = request.GET.get('to')
    logbook_search = Logbook.objects.filter(date__range=[date_from,date_to]).order_by('date')
    log_test = Logbook.objects.all().order_by('date')
    p = Paginator(log_test,20)
    page = request.GET.get('page')
    xyz = p.get_page(page)
    return render(request,'hoth/logbook.html',{
        'xyz':xyz,
        'log_test':log_test,
        'logbook_search':logbook_search,
        'date_from':date_from,
        'date_to':date_to,
        })

# def render_pdf_view(request):
#     last_30 = datetime.now() - timedelta(days=30)
#     template_path = 'hoth/pdf1.html'
#     context = {'myvar': Logbook.objects.filter(date__gte=last_30)}
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'filename="report.pdf"'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context)

#     # create a pdf
#     pisa_status = pisa.CreatePDF(
#        html, dest=response)
#     # if error then show some funny view
#     if pisa_status.err:
#        return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response

def time_calc(request):
    return render(request,'hoth/time_calc.html')

# def login(request):

def logoutUser(request):
    logout(request)
    return redirect('home')

def register_user(request):
    user_form = newUser_form
    if request.method == 'POST':
        user_form = newUser_form(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.name = user.name.capitalize()
            user.last_name = user.last_name.capitalize()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            pass
    return render (request,'hoth/register_user.html',{'user_form':user_form})
