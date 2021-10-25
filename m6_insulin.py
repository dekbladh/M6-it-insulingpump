import matplotlib.pyplot as plt
import math

Isc = 5
Ip = 4
tau1 = 49 
tau2 = 47
IDt = 1
Cl = 2010
P = 1.06 * 10**-2
Ieff = 1
S = 8.11 * 10**-4
Ip = 1
Gezi = 2.20 * 10**-3
G = 1
EGP = 1.33
Ra =0
Vg1 = 253
E=math.e
tau_m=47
time_step = 100
t_min=60

def isc_delta (Isc, tau1, IDt, Cl):
    return (((-1/tau1)*Isc)+((1/tau1)*(IDt/Cl)))

def Ip_delta(Ip, tau2, Isc):
   return (((-1/tau2)*Ip)+((1/tau2)*Isc))

def Ieff_delta(P, Ieff, S, Ip):
    return ((-P*Ieff)+(P*S*Ip))

def G_delta(Gezi, Ieff, G, EGP, Ra):
    return ((-(Gezi+Ieff)*G)+EGP+Ra)
    
def Ra_delta(Ch, Vg, Taum, t):
    return ((Ch/(Vg*(Taum**2))) * t * (E**(-(t/Taum)))) 
    
def Ra1(t,t_food=0,food=1000):
    if t <= t_food:
        return 0
    else: 
         return Ra_delta(food,Vg1,tau_m,t-t_food)
    
def euler (current_value, delta_value, time):
    return (current_value + delta_value*time)

def projected_value (val1, val2, val3, val4, t = t_min, t_step = time_step):
    Isc_list = [val1]
    Ip_list = [val2]
    Ieff_list = [val3]
    G_list = [val4]
    ra_list = [1.5]
    for x in range(t*t_step):
        Isc_list.append(euler(Isc_list[-1], isc_delta(Isc_list[-1], tau1, IDt, Cl), 1/t_step))
        
        Ip_list.append(euler(Ip_list[-1], Ip_delta(Ip_list[-1], tau2, Isc_list[-1] ), 1/t_step))
        
        Ieff_list.append(euler(Ieff_list[-1], Ieff_delta(P, Ieff_list[-1], S, Ip_list[-1]), 1/t_step))
        
        G_list.append(euler(G_list[-1], G_delta(Gezi, Ieff_list[-1], G_list[-1], EGP, ra_list[-1]), 1/t_step))
        
        ra_list.append(euler(ra_list[-1], Ra1(x/t_step), 1/t_step))
        
    return ( Isc_list, Ip_list, Ieff_list, G_list, ra_list)
   
result = (projected_value(5,25,0.9,4))
x=[]
for i in range(t_min*time_step+1):
    x.append(i/time_step)
plt.plot(x,result[0], "r--", x, result[1], "rs", x, result[2], "b*", x,result[3],'gs',x,result[4],'g--')

"""print (result[0])
print (result[1])
print (result[2])
print (result[3])"""

plt.show()
