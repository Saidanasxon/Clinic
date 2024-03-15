from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Doktor,QabulVaqti,Davolash
from django.http import JsonResponse

def index(request):
    doktors = Doktor.objects.all()
    davolash = Davolash.objects.all()
    davolash1 = [davo.qabul_vaqt.id for davo in davolash]
    doctor_time = {}

    for doktor in doktors:
        qabul = QabulVaqti.objects.filter(doktor=doktor).order_by('vaqt')
        qabul_time = []
        for qab in qabul:
            if qab.id not in davolash1:
                qabul_time.append(qab)
        doctor_time[doktor] = qabul_time
    
    data = {
        'doctor_time': doctor_time,
        'doktors': doktors,
    }

    return render(request, 'my_app/index.html', context=data)



def vaqt_add(request):
    a=[]
    vaqtlar=[]
    if request.method == 'POST':
        vaqt_id = request.POST.get('vaqt_id')
        
        user=request.user
 
        davo1 = Davolash.objects.filter(foydalanuvchi=user)
        for davo in davo1:
            a.append(davo.foydalanuvchi)
            vaqtlar.append(davo.qabul_vaqt.vaqt)
        if vaqt_id:
            vaqt = QabulVaqti.objects.get(id=vaqt_id)
            if user  not in  a:
                davolash = Davolash(foydalanuvchi=request.user, qabul_vaqt=vaqt)
                davolash.save()
                
      

            elif vaqt.vaqt not in vaqtlar: 
                davolash = Davolash(foydalanuvchi=request.user, qabul_vaqt=vaqt)
                davolash.save()
                
                
            else:
 
                return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'Alo'})
    
            










def error_404(request):
    return render(request,'my_app/404.html')

def about(request):
    return render(request,'my_app/about.html')

def contact(request):
    return render(request,'my_app/contact.html')

def appointment(request):
    return render(request,'my_app/appointment.html')

def feature(request):
    return render(request,'my_app/feature.html')

def service(request):
    davolash = Davolash.objects.all()

    data={
        'davolash': davolash,
  
    }
    return render(request,'my_app/service.html',context=data)

def team(request):
    return render(request,'my_app/team.html')

def testimonial(request):
    return render(request,'my_app/testimonial.html')