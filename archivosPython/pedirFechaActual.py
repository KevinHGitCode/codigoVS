#funcion para obtener la fecha actual
def pedirFechaActual():
    import datetime
    fechaActual = datetime.datetime.now()
    return fechaActual

#llaamamos a la funcion
#fechaActual = pedirFechaActual()
#print(fechaActual)

#funcion para obtener la fecha actual dia/mes/año
def pedirFechaActualDiaMesAnio():
    import datetime
    fechaActual = datetime.datetime.now()
    return fechaActual.strftime("%d/%m/%Y")

#llamamos a la funcion
fechaActualDiaMesAnio = pedirFechaActualDiaMesAnio()
print(fechaActualDiaMesAnio)

#funcion para obtener la fecha actual hora:minutos:segundos
def pedirHoraMinutosSegundosActual():
    import datetime
    fechaActual = datetime.datetime.now()
    return fechaActual.strftime("%H:%M:%S")

#llamamos a la funcion
#fechaActualHoraMinutosSegundos = pedirHoraMinutosSegundosActual()
#print(fechaActualHoraMinutosSegundos)

#funcion para obtener la fecha actual dia de la semana
def pedirDiaSemanaActual():
    import datetime
    fechaActual = datetime.datetime.now()
    return fechaActual.strftime("%A")

#llamamos a la funcion
#fechaActualDiaSemana = pedirDiaSemanaActual()
#print(fechaActualDiaSemana)

#funcion que me dice que la fecha dentro de n dias
def fechaDentroNDias(dias):
    import datetime
    fechaActual = datetime.datetime.now()
    fechaDentroNDias = fechaActual + datetime.timedelta(days=dias)
    return fechaDentroNDias.strftime("%d/%m/%Y")

#llamamos a la funcion
#fechaDentroNDias = fechaDentroNDias(5)
#print(fechaDentroNDias)

# funcion que calcula cuantos dias faltan para que se cumpla una fecha
def calcularDiasFaltantes(fecha):
    import datetime
    fechaActual = datetime.datetime.now()
    fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y")
    dias = (fecha - fechaActual).days
    return dias

#llamamos a la funcion
dias=calcularDiasFaltantes("09/07/2022")
print("faltan",dias,"dias para que se cumpla la fecha")


#funcion que me dice si un año x es bisiesto
def esBisiesto(año):
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

#llamamos a la funcion
#esBisiesto = esBisiesto(2020)
#print(esBisiesto)

#calcular edad
def calcularEdad(fechaNacimiento):
    import datetime
    fechaActual = datetime.datetime.now()
    fechaNacimiento = datetime.datetime.strptime(fechaNacimiento, "%d/%m/%Y")
    edad = fechaActual.year - fechaNacimiento.year
    if fechaActual.month < fechaNacimiento.month:
        edad = edad - 1
    elif fechaActual.month == fechaNacimiento.month:
        if fechaActual.day < fechaNacimiento.day:
            edad = edad - 1
    return edad

#llamamos a la funcion
#edad = calcularEdad("04/09/2003")
#print(edad)

#calcular edad en años meses y dias
def calcularEdadEnAnosMesesDias(fechaNacimiento):
    #calculamos la edad en años llanamos la funcion
    años=calcularEdad(fechaNacimiento)
    #llamamos a la funcion
    fehaActual=str(pedirFechaActualDiaMesAnio())
    mesActual=fehaActual[3:5]
    mesNacimiento=fechaNacimiento[3:5]
    #si el mes de nacimiento es mayor que el mes actual
    if int(mesNacimiento)>int(mesActual):
        meses = int(mesActual)+12-int(mesNacimiento)
    #si el mes de nacimiento es menor que el mes actual
    elif int(mesNacimiento)<int(mesActual):
        meses = int(mesActual)-int(mesNacimiento)

    diaActual=fehaActual[0:2]
    diaNacimiento=fechaNacimiento[0:2]

    #si el dia de nacimiento es mayor que el dia actual
    if int(diaNacimiento)>int(diaActual):
        dias = (int(diaActual)+30-int(diaNacimiento))
        dias += 2
        meses -= 1
    #si el dia de nacimiento es menor que el dia actual
    elif int(diaNacimiento)<int(diaActual):
        dias = 1+(int(diaActual)-int(diaNacimiento))
    return años,meses,dias

#llamamos a la funcion
#años,meses,dias = calcularEdadEnAnosMesesDias("01/10/2009")
#print("Has vivido:",años,"años,",meses,"meses y",dias,"dias")

#funcion para calcular los dias entre dos fechas
def calcularDiasEntreFechas(fechaInicio,fechaFin):
    import datetime
    fechaInicio = datetime.datetime.strptime(fechaInicio, "%d/%m/%Y")
    fechaFin = datetime.datetime.strptime(fechaFin, "%d/%m/%Y")
    dias = (fechaFin - fechaInicio).days
    return dias

#llamamos a la funcion
#dias = calcularDiasEntreFechas("01/10/2009","01/10/2017")
#print("Han pasado",dias,"dias entre las dos fechas")
