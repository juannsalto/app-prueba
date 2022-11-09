import calendar
 
fecha = calendar.TextCalendar(
    calendar.SUNDAY)

print(fecha.prmonth (2022, 11))


#segunda forma hecha para imprimir todo el año


#Instancia de TextCalendar
anio_entero = calendar.TextCalendar()

#Elegimos el formato del año
calendario_2022 = anio_entero.formatyear(2022)

#Mostramos el resultado
print(calendario_2022)