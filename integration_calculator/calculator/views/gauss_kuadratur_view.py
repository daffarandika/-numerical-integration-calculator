from django.views import View
from django.shortcuts import render
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import math
from scipy.interpolate import interp1d, CubicSpline
from scipy.integrate import quad
from plotly.io import to_html
from numpy import e
from numpy import linspace
from numpy import pi
from sympy import symbols, sympify, lambdify

class GaussKuadratur(View):
    context = {"error": "", "hasil": "", "a": "", "b": "", "fx": "", "n": "", "delta_x": "", "show_option": False}
    template_file = 'gauss_kuadratur.html'

    def get(self, request):
        return render(request, self.template_file, self.context)

    def post(self, request):
        try:
            a = request.POST.get("a")
            b = request.POST.get("b")
            fx = request.POST.get("fx")
            self.context.update({"a": a, "b": b, "fx": fx})

            e_symbol = symbols("e")
            pi_symbol = symbols("pi")
            f = sympify(fx)
            fx_sym = f.subs(e_symbol, e).subs(pi_symbol, pi)

            self.integral_gauss_kuadratur(eval(a),eval(b),fx_sym)

        except Exception as err:
            self.context["hasil"] = f"Error: {str(err)}"

        return render(request, self.template_file, self.context)

    def integral_gauss_kuadratur(self, a,b,fx):
        def f(x):
            return fx.subs(symbols("x"), x)

        c1 = c2 = 1

        z1 = 1/math.sqrt(3)
        z2 = -1/math.sqrt(3)
        
        x1 = ((b-a)/2) * z1 + ((b+a)/2)
        x2 = ((b-a)/2) * z2 + ((b+a)/2)
        print(f"{z1=}")
        print(f"{z2=}")

        self.context["hasil"] = 2 * (c1*f(x1) + c2*f(x2))