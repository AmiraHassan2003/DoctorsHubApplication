from django.shortcuts import render, redirect
from .models import Doctor
from .models import Specialization
from django.urls import reverse


def specialization(request):
    if request.method == 'POST':
        specialization = request.POST.get('specialization')
        area = request.POST.get('area')

        if specialization and area:
            specialization = specialization.lower().split(' ')
            area = area.lower().split(' ')
            # print("specialization: " , specialization)
            # print("area: " , area)
            for special in specialization:
                specializationIsValid = Specialization.objects.filter(special_name=special)
                if specializationIsValid.exists():
                    # specialValid = Specialization.objects.filter(special_name=special)
                    print("specializationIsValid:  ", specializationIsValid)
                    break

            for a in area:
                areaIsValid = Specialization.objects.filter(area_name=a)
                if areaIsValid.exists():
                    # specialArea = Specialization.objects.filter(area_name=a)
                    print("areaIsValid:  ", areaIsValid[0].special_id)
                    break
            
            if areaIsValid and areaIsValid.exists():
                print("specialInfo : ", areaIsValid[0].special_id)     
                special_id = areaIsValid[0].special_id
                url = reverse('show_Doctors') + f'?special_id={special_id}'
                # print("urlllllllll", url)
                return redirect(url)
            else:
                context = {'error': "Not Found"}
                print("Doctors/index.htmlllllllllllll")
                return render(request,"Doctors/index.html", context)
        else:
            # print("return redirect('specialization')")
            return redirect('specialization')
    # print("rDoctors/index.html'lloutside")
    return render(request, 'Doctors/index.html')

def show_Doctors(request):
    special_id = request.GET.get('special_id')
    if special_id:
        doctors = Doctor.objects.filter(specialization_id=special_id)
        context = {'doctors': doctors}
        # print("context: ", special_id)
        return render(request, 'Doctors/index.html', context)
    return render(request, 'Doctors/index.html')



def show_doctor_info(request, doctor_id):
    print("idddddd: ", doctor_id)
    context = {
        'doctor' : Doctor.objects.get(doctor_id = doctor_id)
    }
    return render(request,'Doctors/doctorInfo.html',context) 

# Create your views here.
