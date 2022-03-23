tipo_trabajador=["DOCENTE"]
tipo_trabajador2=["GUARDA", "CONSERJE", "AUXILIAR", "DIRECCION", "COCINERO", "ORIENTADOR"]
correcto=False;
while(not correcto):
   print("Cual es su puesto de trabajo¿?")
   puesto=input()
   if puesto.upper() in tipo_trabajador:
       print("Cual es su docencia, de primaria o de secundaria¿?")
       docencia=input()
       primaria="PRIMARIA"
       secundaria="SECUNDARIA"
       if docencia.upper()==primaria:
           print("Cual es su pago por leccion¿?")
           pago_por_leccion=int(input())
           print("Cuantas lecciones tiene los lunes¿?")
           lecciones_lunes=int(input())
           print("Cuantas lecciones tiene los martes¿?")
           lecciones_martes=int(input())
           print("Cuantas lecciones tiene los miercoles¿?")
           lecciones_miercoles=int(input())
           print("Cuantas lecciones tiene los jueves¿?")
           lecciones_jueves=int(input())
           print("Cuantas lecciones tiene los viernes¿?")
           lecciones_viernes=int(input())
           total_de_lecciones= lecciones_lunes+lecciones_martes+lecciones_miercoles+lecciones_jueves+lecciones_viernes
           pago_lunes=lecciones_lunes*pago_por_leccion
           pago_martes=lecciones_martes*pago_por_leccion
           pago_miercoles=lecciones_miercoles*pago_por_leccion
           pago_jueves=lecciones_jueves*pago_por_leccion
           pago_viernes=lecciones_viernes*pago_por_leccion
           pago_semanal_docencia=total_de_lecciones*pago_por_leccion
           pago_por_quincena_docencia=pago_semanal_docencia*2
           pago_por_mes=pago_por_quincena_docencia*2
           pago_por_año= pago_por_mes*12    
           print("Usted trabaja un total de ", total_de_lecciones, " lecciones por semana")     
           print("Su pago del lunes es de: ",pago_lunes, "colones")
           print("Su pago de los martes es: ",pago_martes, "colones") 
           print("su pago de los miercoles es: ",pago_miercoles, "colones") 
           print("su pago de los jueves: ",pago_jueves, "colones") 
           print("su pago de los viernes es: ",pago_viernes, "colones")
           print("Su pago por semana es de:", pago_semanal_docencia,"colones")
           print("Su pago por quincena es de:",pago_por_quincena_docencia, "colones")
           print("Su pago por mes es de:",pago_por_mes, "colones") 
           print("Su pago por año es de:",pago_por_año, "colones") 
           correcto=True    
       elif docencia.upper()==secundaria:
           print("Cual es su pago por leccion¿?")
           pago_por_leccion=int(input())
           print("Cuantas lecciones tiene los lunes¿?")
           lecciones_lunes=int(input())
           print("Cuantas lecciones tiene los martes¿?")
           lecciones_martes=int(input())
           print("Cuantas lecciones tiene los miercoles¿?")
           lecciones_miercoles=int(input())
           print("Cuantas lecciones tiene los jueves¿?")
           lecciones_jueves=int(input())
           print("Cuantas lecciones tiene los viernes¿?")
           lecciones_viernes=int(input())
           total_de_lecciones= lecciones_lunes+lecciones_martes+lecciones_miercoles+lecciones_jueves+lecciones_viernes
           pago_lunes=lecciones_lunes*pago_por_leccion
           pago_martes=lecciones_martes*pago_por_leccion
           pago_miercoles=lecciones_miercoles*pago_por_leccion
           pago_jueves=lecciones_jueves*pago_por_leccion
           pago_viernes=lecciones_viernes*pago_por_leccion
           pago_semanal_secundaria=total_de_lecciones*pago_por_leccion
           pago_por_quincena_secundaria=pago_semanal_secundaria*2
           pago_por_mes=pago_por_quincena_secundaria*2
           pago_por_año= pago_por_mes*12 
           print("Usted trabaja un total de ", total_de_lecciones, " lecciones por semana")        
           print("Su pago del lunes es de: ",pago_lunes, "colones")
           print("Su pago de los martes es: ",pago_martes, "colones") 
           print("su pago de los miercoles es: ",pago_miercoles, "colones") 
           print("su pago de los jueves: ",pago_jueves, "colones") 
           print("su pago de los viernes es: ",pago_viernes, "colones")
           print("Su pago por semana es de:", pago_semanal_secundaria, "colones")
           print("Su pago por quincena es de:",pago_por_quincena_secundaria, "colones")
           print("Su pago por mes es de:",pago_por_mes, "colones") 
           print("Su pago por año es de:",pago_por_año, "colones")
           correcto=True 
   elif puesto.upper() in tipo_trabajador2:
       print("Cual es su pago por hora¿?")
       pago_por_hora=int(input())
       print("Cual es su total de horas de trabajo durante un día¿?")
       total_de_horas=int(input())
       pago_por_dia=total_de_horas*pago_por_hora
       print("Su pago por día es de:", pago_por_dia)
       pago_por_semana=pago_por_dia*5
       print("Su pago por semana es de:", pago_por_semana)
       pago_por_quincena=pago_por_semana*2
       print("Su pago por quincena es de:", pago_por_quincena)
       pago_mensual=pago_por_quincena*2
       print("Su pago por mes es de:", pago_mensual)
       pago_anual=pago_mensual*12
       print("Su pago por año es de:",pago_anual)
       correcto=True
   else:
        print("Puesto no valido")
       