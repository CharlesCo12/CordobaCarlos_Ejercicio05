import numpy as np
import matplotlib.pylab as plt
#Cadena de Ingreso
cadena='scccc'
#Cálculo de la Probabilidad
def prob(h,cadena):
    Nc=cadena.count('c')
    Ns=cadena.count('s')
    a=h**Nc
    b=(1-h)**Ns
    return a*b


h=np.linspace(0.0001,1-1e-5,100)
y=prob(h,cadena)
m=np.trapz(y,x=h)
y_new=y/m

#Valores importantes
a=np.where(y_new==np.max(y_new))
H_0=h[a[0][0]]

valor=np.log(y_new)[a[0][0]+1]-2*np.log(y_new)[a[0][0]]+np.log(y_new)[a[0][0]-1]
deriv2=valor/(H_0 - h[a[0][0]-1])**2
sigma=1/np.sqrt(-deriv2)
def aprox(h):
    A=1.0/(sigma*(np.sqrt(2*np.pi)))
    B=np.exp(-(h-H_0)**2/(2*(sigma**2)))
    return A*B

plt.plot(h,aprox(h),'--')
plt.plot(h,y_new)
plt.xlabel('H')
plt.ylabel('P(H|{datos})')
plt.title('H = {:.2f} {} {:.2f}'.format(H_0,'$\pm$',sigma))
plt.savefig('coins.png')