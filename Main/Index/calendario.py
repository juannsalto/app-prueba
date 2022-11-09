import calendar
 
fecha = calendar.TextCalendar(
    calendar.SUNDAY)

print(fecha.prmonth (2022, 11))


#segunda forma hecha para imprimir todo el año


#Instancia de TextCalendar
cl = calendar.TextCalendar()

#Elegimos el formato del año
calendario_2022 = cl.formatyear(2022)

#Mostramos el resultado
print(calendario_2022)