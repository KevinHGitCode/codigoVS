def f():
    while True:
        a = r.randint(0,10)
        b = r.randint(0,10)
        c = r.randint(0,10)
        d = r.randint(0,10)
        print(f'''
             {a}     {b}
            --- + ---
             {c}     {d}

        cual es la respuesta?''')

        x=int(input('arriba: '))
        y=int(input('abajo: '))

        R= (x==(d*a) + (c*b)) and y==c * d

        print(f'''
           Respuesta: {'Correcta' if R else 'Incorrecta'}
              {(d*a) + (c*b)}
           = ---
              {c * d}
        ''')
        break