from django.http import HttpResponse
from django.shortcuts import render
from numpy import cos
from numpy import e
from numpy import linspace
from numpy import pi
from numpy import sin
from numpy import tan
from sympy import symbols, sympify
from sympy.core.sympify import SympifyError


# Create your views here.
def index(request):
    return render(request, 'base_sidebar.html')

def trapesium(request):
    if request.method == "POST":
        try:
            n = eval(request.POST.get("n"))
            a = eval(request.POST.get("a"))
            b = eval(request.POST.get("b"))

            f_str = str(request.POST.get("fx"))
            e_symbol = symbols("e")
            pi_symbol = symbols("pi")

            f = sympify(f_str)
            fx = f.subs(e_symbol, e).subs(pi_symbol, pi)

            result = integral_trapesium(a,b,n,fx)
            return HttpResponse(f"Hasilnya: {result}")
            

        except Exception as err:
            return HttpResponse(f"Error: {str(err)}", status=400)

    return render(request, 'trapesium.html')

def integral_trapesium(a, b, n, f):
    def fx(x):
        return f.subs(symbols("x"), x)
    
    delta_x = (b - a)/(n)
    x = linspace(a,b,n)
    
    jumlah =  fx(a) + fx(b)
    for i in range(1, n-1):
        jumlah += 2 * fx(x[i])

    hasil = (delta_x/2) * jumlah

    return hasil

