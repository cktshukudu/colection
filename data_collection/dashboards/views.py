from django.shortcuts import render
from . models import main_erp
from . models import planning_erp

# Create your views here.


def index(request):
    return render(request, 'dashboards/index.html',{})

def main_erp(request):
    if request.method == 'POST':
        inspection_yes=request.POST.get('inspection_yes')
        inspection_no=request.POST.get('inspection_no')
        Preventitive_yes=request.POST.get('Preventitive_yes')
        Preventitive_no=request.POST.get('Preventitive_no')
        repairs_yes=request.POST.get('repairs_yes')
        repairs_no=request.POST.get('repairs_no')
        current_yes=request.POST.get('current_yes')
        current_no=request.POST.get('current_no')
        print(inspection_yes,inspection_no,Preventitive_yes,Preventitive_no,repairs_yes,current_yes,current_no,repairs_no)

        content= {'inspection_yes':inspection_yes,'inspection_no':inspection_no,'Preventitive_yes':Preventitive_yes,'Preventitive_no':Preventitive_no,'repairs_yes':repairs_yes,'repairs_no':repairs_no,'current_yes':current_yes,'current_no':current_no}

    return render(request, 'dashboards/main_erp.html',{})

def planning_erp(request):
    if request.method == 'POST':
        response_yes=request.POST.get('response_yes')
        response_no=request.POST.get('response_no')
        plan_yes=request.POST.get('plan_yes')
        plan_no=request.POST.get('plan_no')
        integrated_yes=request.POST.get('integrated_yes')
        integrated_no=request.POST.get('integrated_no')
        current_yes=request.POST.get('current_yes')
        current_no=request.POST.get('current_no')
        print(response_yes,response_no,plan_yes,plan_no,integrated_yes,integrated_no, current_yes,current_no)

        content= {'response_yes':response_yes,'response_no':response_no,'plan_yes':plan_yes,'plan_no':plan_no,'integrated_yes':integrated_yes,'integrated_no':integrated_no,'current_yes':current_no}
    return render(request, 'dashboards/planning_erp.html',{})

def hr_erp(request):
    if request.method == 'POST':
        response_yes=request.POST.get('response_yes')
        response_no=request.POST.get('response_no')
        plan_yes=request.POST.get('plan_yes')
        plan_no=request.POST.get('plan_no')
        integrated_yes=request.POST.get('integrated_yes')
        integrated_no=request.POST.get('integrated_no')
        current_yes=request.POST.get('current_yes')
        current_no=request.POST.get('current_no')
        print(response_yes,response_no,plan_yes,plan_no,integrated_yes,integrated_no, current_yes,current_no)

        content= {'response_yes':response_yes,'response_no':response_no,'plan_yes':plan_yes,'plan_no':plan_no,'integrated_yes':integrated_yes,'integrated_no':integrated_no,'current_yes':current_no}
    return render(request, 'dashboards/hr_erp.html',{})