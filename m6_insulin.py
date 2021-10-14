import matplotlib.pyplot as plt


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
Vg = 253


def isc_delta (Isc, tau1, IDt, Cl):
    return (((-1/tau1)*Isc)+((1/tau1)*(IDt/Cl)))

def Ip_delta(Ip, tau2, Isc):
   return (((-1/tau2)*Ip)+((1/tau2)*Isc))

def Ieff_delta(P, Ieff, S, Ip):
    return ((-P*Ieff)+(P*S*Ip))

def G_delta(Gezi, Ieff, G, EGP, Ra):
    return ((-(Gezi+Ieff)*G)+EGP+Ra)
    
def Ra_delta(Gh, Vg, Taum, T, E):
    ((Gh/(Vg*(Taum**2))) * T * (E**(-(t/Taum))))
    
def euler (current_value, delta_value, time):
    return (current_value + delta_value*time)

def projected_value (val1, val2, val3, val4, t = 100):
    list1 = [val1]
    list2 = [val2]
    list3 = [val3]
    list4 = [val4]
    
    for x in range(t):
        list1.append(euler(list1[-1], isc_delta(list1[-1], tau1, IDt, Cl), 1))
        list2.append(euler(list2[-1], Ip_delta(list2[-1], tau2, list1[-1] ), 1))
        list3.append(euler(list3[-1], Ieff_delta(list3[-1], Ieff, S, list2[-1]), 1))
        list4.append(euler(list4[-1], G_delta(Gezi, list3[-1], G, EGP, Ra), 1))
    return (list1, list2, list3, list4)
   
result = (projected_value(5,2.3,5,4))
x = list(range(101))
plt.plot(x,result[0], "r--", x, result[1], "bs", x, result[2], "go", x,result[3],'rs')

"""print (result[0])
print (result[1])
print (result[2])
print (result[3])"""

plt.show()


    

   