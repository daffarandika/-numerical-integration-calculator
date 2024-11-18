from django.http import HttpResponse
from django.shortcuts import render
from numpy import cos
from numpy import e
from numpy import linspace
from numpy import pi
from numpy import sin
from numpy import tan
from sympy import symbols, sympify


# Create your views here.
def index(request):
    return render(request, 'base_sidebar.html')

def trapesium(request):
    context = {"result": "", "a": "", "b": "", "fx": "", "n": "", "delta_x": ""}
    
    if request.method == "POST":
        try:
            a = request.POST.get("a")
            b = request.POST.get("b")
            fx = request.POST.get("fx")
            context.update({"a": a, "b": b, "fx": fx})

            if request.POST.get("n") and not request.POST.get("delta_x"):
                n = eval(request.POST.get("n"))
                context["n"] = n
                
                e_symbol = symbols("e")
                pi_symbol = symbols("pi")
                f = sympify(fx)
                fx_sym = f.subs(e_symbol, e).subs(pi_symbol, pi)
                
                result = integral_trapesium_n(eval(a), eval(b), n, fx_sym)
                context["result"] = result

            elif request.POST.get("delta_x") and not request.POST.get("n"):
                delta_x = eval(request.POST.get("delta_x"))
                context["delta_x"] = delta_x
                
                e_symbol = symbols("e")
                pi_symbol = symbols("pi")
                f = sympify(fx)
                fx_sym = f.subs(e_symbol, e).subs(pi_symbol, pi)
                
                result = integral_trapesium_delta_x(eval(a), eval(b), delta_x, fx_sym)
                context["result"] = result

            else:
                context["result"] = "Invalid input"
        
        except Exception as err:
            context["result"] = f"Error: {str(err)}"

    print(context)
    return render(request, 'trapesium.html', context)

def integral_trapesium_n(a, b, n, fx):
    def f(x):
        return fx.subs(symbols("x"), x)
    
    delta_x = (b - a)/(n)
    x = linspace(a,b,n)
    
    jumlah =  f(a) + f(b)
    for i in range(1, n-1):
        jumlah += 2 * f(x[i])

    hasil = (delta_x/2) * jumlah

    return hasil

def integral_trapesium_delta_x(a, b, delta_x, fx):
    def f(x):
        return fx.subs(symbols("x"), x)
    
    n = int((b - a)/(delta_x))
    x = linspace(a,b,n)
    
    jumlah =  f(a) + f(b)
    for i in range(1, n-1):
        jumlah += 2 * f(x[i])

    hasil = (delta_x/2) * jumlah

    return hasil