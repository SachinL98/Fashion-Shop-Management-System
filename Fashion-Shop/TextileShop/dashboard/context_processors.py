from dashboard.models import employee_salasry
from dashboard.models import utilitybill
from fashion.models import SupplierCancelDetails
from salesapp.models import Sales

def report1(request):
    utilir=utilitybill.objects.raw('SELECT * FROM dashboard_utilitybill where MONTH(curdate())=MONTH(date)')
    
    return {'utilir':utilir}

def report2(request):
    ordersr=SupplierCancelDetails.objects.raw('SELECT * FROM fashion_supplierCancelDetails where MONTH(curdate())=MONTH(cancelledDate)')
    
    return {'ordersr':ordersr}

def report3(request):
    salesr=Sales.objects.raw('SELECT * FROM salesapp_sales where MONTH(curdate())=MONTH(Date)')
    
    return {'salesr':salesr}

def report4(request):
    emprs=employee_salasry.objects.raw('SELECT * FROM dashboard_employee_salasry where MONTH(curdate())=MONTH(date)')

    return {'emprs':emprs}

def total1(request):
    emps=employee_salasry.objects.raw('SELECT * FROM dashboard_employee_salasry where MONTH(curdate())=MONTH(date)')
    total1=0
    for i in emps:
        total1=total1+i.netsal
    
    return {'total1':total1}

def total2(request):
    ordersr=SupplierCancelDetails.objects.raw('SELECT * FROM fashion_supplierCancelDetails where MONTH(curdate())=MONTH(cancelledDate)')
    
    total2=0
    for i in ordersr:
        total2=total2+i.total
    
    return {'total2':total2}

def total3(request):
    salesr=Sales.objects.raw('SELECT * FROM salesapp_sales where MONTH(curdate())=MONTH(Date)')
    
    total3=0
    for i in salesr:
        total3=total3+i.totalPrice
    
    return {'total3':total3}

def total4(request):
    utilir=utilitybill.objects.raw('SELECT * FROM dashboard_utilitybill where MONTH(curdate())=MONTH(date)')
    
    total4=0
    for i in utilir:
        total4=total4+i.price
    
    return {'total4':total4}

def cost(request):
    utilir=utilitybill.objects.raw('SELECT * FROM dashboard_utilitybill where MONTH(curdate())=MONTH(date)')
    t1=0
    for i in utilir:
        t1=t1+i.price

    ordersr=SupplierCancelDetails.objects.raw('SELECT * FROM fashion_supplierCancelDetails where MONTH(curdate())=MONTH(cancelledDate)')
    t2=0
    for i in ordersr:
        t2=t2+i.total
    
    emps=employee_salasry.objects.raw('SELECT * FROM dashboard_employee_salasry where MONTH(curdate())=MONTH(date)')
    t3=0
    for i in emps:
        t3=t3+i.netsal

    cost=t1+t2+t3
    return{'cost':cost}
    
def net_income(request):
    utilir=utilitybill.objects.raw('SELECT * FROM dashboard_utilitybill where MONTH(curdate())=MONTH(date)')
    t1=0
    for i in utilir:
        t1=t1+i.price

    ordersr=SupplierCancelDetails.objects.raw('SELECT * FROM fashion_supplierCancelDetails where MONTH(curdate())=MONTH(cancelledDate)')
    t2=0
    for i in ordersr:
        t2=t2+i.total
    
    emps=employee_salasry.objects.raw('SELECT * FROM dashboard_employee_salasry where MONTH(curdate())=MONTH(date)')
    t3=0
    for i in emps:
        t3=t3+i.netsal

    cost1=t1+t2+t3

    salesr=Sales.objects.raw('SELECT * FROM salesapp_sales where MONTH(curdate())=MONTH(Date)')
    
    inc=0
    for i in salesr:
        inc=inc+i.totalPrice
    
    net_income=inc-cost1
    return {'net_income':net_income}