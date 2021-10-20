from django.shortcuts import render, get_object_or_404

# Create your views here.

# table
from .models import Travel
def info_demo(request):
    t1 = Travel.objects.get(pk=1)
    t_demo = {'info': t1}
    return render(request, 'table_info.html', t_demo)

def table_info(request, pk):
    travel = get_object_or_404(Travel, pk=pk)
    t_info = {'info': travel}
    return render(request, 'table_info.html', t_info)

def table_list(request):
    travel = Travel.objects.all()
    t_list = {'travels': travel}
    return render(request, 'table_list.html', t_list)