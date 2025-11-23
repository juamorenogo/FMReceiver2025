# 

import sympy as sp

Ie = 2.525e-3
Ib = 25e-6
Ic = 12e-3
vcc = 8
vce = 3
vbe = 0.7

gm = Ic / 0.025
print("gm:", gm)

Av = -1*(7.5)  # Ganancia deseada
R_c = -Av/gm
r3 = R_c
print("R_c:", R_c)

# Definir símbolos
r1, r2, va = sp.symbols('r1 r2 va')

# Sistema de ecuaciones
eq1 = sp.Eq(vcc - va, r1 * Ie)
eq2 = sp.Eq(va - vce, r3 * Ic)
eq3 = sp.Eq(va - vbe, r2 * Ib)

# Resolver para r1 y r2
sol_r1_r2 = sp.solve((eq1, eq2, eq3), (r1, r2, va))
print("Solución completa:", sol_r1_r2)

# O si solo quieres r1 y r2:
r1_val = sol_r1_r2[r1]
r2_val = sol_r1_r2[r2]
va_val = sol_r1_r2[va]

print(f"r1 = {r1_val:.2f} Ω")
print(f"r2 = {r2_val:.2f} Ω") 
print(f"va = {va_val:.2f} V")