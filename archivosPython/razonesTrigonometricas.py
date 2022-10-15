''' si: 
    a es el catetoOpuesto
    b es el catetoAdyacente
    h es la hipotenusa
    Crear funciones con las razones trigonometricas
'''
from math import *
# seno = catetoOpuesto/hipotenusa
def seno(a, h):
    return a/h

# coseno = catetoAdyacente/hipotenusa
def coseno(b, h):
    return b/h

# tangente = catetoOpuesto/catetoAdyacente
def tangente(a, b):
    return a/b

# crear un triangulo rectangulo aleatorio
def trianguloRectangulo():
    import random
    catetoOpuesto = random.randint(1, 100)
    catetoAdyacente = random.randint(1, 100)
    hipotenusa = (catetoOpuesto**2 + catetoAdyacente**2)**0.5
    return catetoOpuesto, catetoAdyacente, hipotenusa

# pasar grados a radianes
def pasarGrados(grados):
    return grados*pi/180
    


if __name__ == '__main__':
    # main
    def main():
        
     while True:
        '''
        catetoOpuesto, catetoAdyacente, hipotenusa = trianguloRectangulo()
        print(f'a = {catetoOpuesto}')
        print(f'b = {catetoAdyacente}')
        print(f'h = {hipotenusa}')

        # mostrar las razones trigonometricas
        # seno
        print(f'seno = {seno(catetoOpuesto, hipotenusa)}')
        # coseno
        print(f'coseno = {coseno(catetoAdyacente, hipotenusa)}')
        # tangente
        print(f'tangente = {tangente(catetoOpuesto, catetoAdyacente)}')
        # aleatorio
        if input() == 'n':
            break
        '''
        grados = float(input('grados: '))
        print(f'radianes = {pasarGrados(grados)/pi} {chr(960)}')

    main()