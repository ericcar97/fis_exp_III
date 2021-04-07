from sympy import *

v_0, L, C, R, sv_0, s_L, s_C, s_R = symbols('\nu_{0} L C R s_{v_0} s_L s_C s_R')
v_0 = 1/(2*pi*sqrt(L*C))
#sv_0 = (diff(v_0,L)*s_L)**2
#sv_0 += (diff(v_0,C)*s_C)**2
#sv_0 = sqrt(sv_0)

#print(sv_0)


V_f, V_R, sV_f, sV_R, G, sG, Q, s_Q = symbols('V_f V_R s_{V_f} s_{V_R} G s_G Q s_Q')

#G = V_R/V_f
#s_G = (diff(G,V_R)*sV_R)**2
#s_G += (diff(G,V_f)*sV_f)**2
#s_G = sqrt(s_G)

#print(s_G)
#print(latex(s_G))

#Q = sqrt(L/C)/R
#s_Q = (diff(Q,R)*s_R)**2
#s_Q += (diff(Q,L)*s_L)**2
#s_Q += (diff(Q,C)*s_C)**2
#s_Q = sqrt(s_Q)


print(simplify(s_Q))
print(latex(s_Q))


