import math

class Complejo:

    def __init__(self,real,img):        
        self.com_img = img
        self.com_real = real

def suma(A,B):
    suma_real = A.com_real + B.com_real
    suma_img = A.com_img + B.com_img
    if suma_img > 0:
        signo = '+'
    else:
        signo=''
    print("A + B = {0}{1}{2}i".format(suma_real,signo,suma_img))

def resta(A,B):
    resta_real = A.com_real - B.com_real
    resta_img = A.com_img - B.com_img
    if resta_img > 0:
        signo = '+'
    else:
        signo=''
    print("A - B = {0}{1}{2}i".format(resta_real,signo,resta_img))

def multiplicacion(A,B):
    mul_real = (A.com_real * B.com_real) - (A.com_img * B.com_img)
    mul_img = (A.com_real*B.com_img) + (B.com_real * A.com_img)
    if mul_img > 0:
        signo = '+'
    else:
        signo=''
    print("A * B = {0}{1}{2}i".format(mul_real,signo,mul_img))

def division(A,B):
    div_real = ((A.com_real * B.com_real) + (A.com_img * B.com_img))/(pow(B.com_real,2)+ pow(B.com_img,2))
    div_img = ((B.com_real * A.com_img)-(A.com_real*B.com_img))/(pow(B.com_real,2)+ pow(B.com_img,2))
    if div_img > 0:
        signo = '+'
    else:
        signo=''
    print("A / B = {0}{1}{2}i".format(round(div_real,2),signo,round(div_img,2)))

def mod(A,label):
    mod_real = pow(pow(A.com_real,2)+pow(A.com_img,2),0.5)
    print('mod({0}) = {1} + 0i'.format(label,round(mod_real,2)))

A = Complejo(2,1)
print('Numero Complejo A: {0} + {1}i'.format(A.com_real, A.com_img))
B = Complejo(5,6)
print('Numero Complejo B: {0} + {1}i'.format(B.com_real, B.com_img))
suma(A,B)
resta(A,B)
multiplicacion(A,B)
division(A,B)
mod(A,'A')
mod(B,'B')