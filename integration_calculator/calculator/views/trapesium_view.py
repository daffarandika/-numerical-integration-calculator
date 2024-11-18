from django.views import View
from django.shortcuts import render
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.io import to_html
import numpy as np
from numpy import cos
from numpy import e
from numpy import linspace
from numpy import pi
from numpy import sin
from numpy import tan
from sympy import symbols, sympify, lambdify
from sympy.utilities.autowrap import ufuncify

class TrapesiumView(View):
    context = {"result": "", "a": "", "b": "", "fx": "", "n": "", "delta_x": "", "fig": ""}
    template_file = 'trapesium.html'

    def get(self, request):
        return render(request, self.template_file, self.context)

    def post(self, request):
        try:
            a = request.POST.get("a")
            b = request.POST.get("b")
            fx = request.POST.get("fx")
            self.context.update({"a": a, "b": b, "fx": fx})

            if request.POST.get("n") and not request.POST.get("delta_x"):
                n = eval(request.POST.get("n"))
                self.context["n"] = n
                
                e_symbol = symbols("e")
                pi_symbol = symbols("pi")
                f = sympify(fx)
                fx_sym = f.subs(e_symbol, e).subs(pi_symbol, pi)
                
                self.integral_trapesium_n(eval(a), eval(b), n, fx_sym)

            elif request.POST.get("delta_x") and not request.POST.get("n"):
                delta_x = eval(request.POST.get("delta_x"))
                self.context["delta_x"] = delta_x
                
                e_symbol = symbols("e")
                pi_symbol = symbols("pi")
                f = sympify(fx)
                fx_sym = f.subs(e_symbol, e).subs(pi_symbol, pi)
                
                self.integral_trapesium_delta_x(eval(a), eval(b), delta_x, fx_sym)

            else:
                self.context["result"] = "Invalid input"
        
        except Exception as err:
            self.context["result"] = f"Error: {str(err)}"

        return render(request, 'trapesium.html', self.context)


    def integral_trapesium_n(self, a, b, n, fx, graph=True):
        def f(x):
            return fx.subs(symbols("x"), x)
        
        delta_x = (b - a)/(n)
        x_hitung = linspace(a,b,n)
        
        jumlah =  f(a) + f(b)
        for i in range(1, n-1):
            jumlah += 2 * f(x_hitung[i])

        hasil = (delta_x/2) * jumlah
        print(hasil)
        self.context["result"] = hasil

        if graph:
            y_hitung = lambdify("x", fx, modules=["numpy"])(x_hitung)
            x_real = linspace(a-1,b+1,100)
            y_real = lambdify("x", fx, modules=["numpy"])(x_real)
            print(y_real)
            df = pd.DataFrame({'x': x_real, 'y': y_real})
            fig = px.line(df, x='x', y='y')
            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=x_hitung,
                    y=y_hitung,
                    fill="tozeroy",
                    name="nilai hitung",
                    line=dict(color='red')
                ),
            )

            for i in range(0, len(x_hitung)):
                fig.add_trace(go.Scatter(
                    x=[x_hitung[i], x_hitung[i]],
                    y=[0, y_hitung[i]],
                    mode='lines',
                    line=dict(color='red'),
                    showlegend=False
                ))

            fig.add_trace(
                go.Line(
                    x=x_real,
                    y=y_real,
                    fill="tozeroy",
                    name="nilai asli",
                    line=dict(color="deepskyblue"),
                )
            )

            self.context["fig"] = to_html(fig, full_html=False, default_width="50%", 
                        include_plotlyjs="cdn", div_id="ohlc")



    def integral_trapesium_delta_x(self, a, b, delta_x, fx):
        def f(x):
            return fx.subs(symbols("x"), x)
        
        n = int((b - a)/(delta_x))
        x = linspace(a,b,n)
        
        jumlah =  f(a) + f(b)
        for i in range(1, n-1):
            jumlah += 2 * f(x[i])

        hasil = (delta_x/2) * jumlah

        return hasil