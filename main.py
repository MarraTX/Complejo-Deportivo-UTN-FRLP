# Import de los módulos (TADs y Funciones de validación/procesos)
from TADreserva import *
from TADagenda import *
from TADcola import *
from datetime import datetime

#Punto 5: Reorganizacion y depuracion por fecha (mantenimiento).
# Esta función se encarga de reprogramar todas las reservas a un dia de destino que elige el
# usuario, recorre la agenda hasta que encuentra las reservas que coinciden con la fecha
# original y las actualiza. Tambien lleva un recuento de cuantas modifico para mostrar el valor
# al final.

def trasladarPorLluvia(agenda, fecha_origen, fecha_destino):
    modificados = 0
    
    for i in range(1, tamanioAgenda(agenda) + 1):
        reserva = recuperarReserva(agenda, i)
        
        if reserva is not None:
            if verFecha(reserva) == fecha_origen:
                modFecha(reserva, fecha_destino)
                modificados += 1
            
    if modificados > 0:
        print(f">> Traslado completado: se movieron {modificados} reservas.")
    else:
        print(f">> No se encontraron reservas para el {fecha_origen}.")
        
    return modificados

# Esta función sirve para vaciar completamente un día específico, borrando todas sus reservas.
# recorre la agenda de atrás para adelante (usando un while que resta de a 1). 
# Esto se hace para que, al ir eliminando elementos, no se desacomoden los índices de las reservas que todavía faltan revisar.
# Al terminar, muestra cuántos turnos se eliminaron o si el día ya estaba libre.

def limpiarCalendario(agenda, fecha_a_borrar):
    eliminados = 0
    
    i = tamanioAgenda(agenda)
    while i >= 1:
        reserva = recuperarReserva(agenda, i)
        
        if reserva is not None:
            if verFecha(reserva) == fecha_a_borrar:
                cancelarReserva(agenda, verFecha(reserva), verHora(reserva))
                eliminados += 1
        i -= 1
        
    if eliminados > 0:
        print(f">> Limpieza completada: se eliminaron {eliminados} turnos.")
    else:
        print(f">> No había reservas para el {fecha_a_borrar}.")
        
    return eliminados

#Punto 6: Generación de hoja de ruta.
# Esta función arma la lista de reservas diarias para el personal de maestranza (mantenimiento).
# Busca todas las reservas agendadas para una fecha puntual (fecha_objetivo), toma a las actividades junto a su nivel de prioridad.
# Despues empaqueta esos dos datos juntos y los encola para armar la hoja de ruta.

def generarHojaDeRuta(agenda, fecha_objetivo):
    hoja_ruta = crearCola()
    
    for i in range(1, tamanioAgenda(agenda) + 1):
        reserva = recuperarReserva(agenda, i)
        
        if reserva is not None:
            if verFecha(reserva) == fecha_objetivo:
                actividad = verActividad(reserva)
                prioridad = verPrioridad(reserva)
                
                datos_maestranza = [actividad, prioridad]
                encolar(hoja_ruta, datos_maestranza)
            
    return hoja_ruta

# ==========================================
# FUNCIONES DE INTERFAZ Y VALIDACIÓN
# ==========================================

# Esta función permite que el usuario seleccione una actividad del sistema (predefinidas).
# Muestra un menú con las opciones disponibles y retorna la actividad seleccionada.

def seleccionarActividad():
    print("\nSeleccione una Actividad:")
    print("1. Futbol 5")
    print("2. Tenis")
    print("3. Cumpleaños")
    opcion = leerEntero("Opción: ", 1, 3)
    
    actividades = {1: "Futbol 5", 2: "Tenis", 3: "Cumpleaños"}
    return actividades[opcion]

# Esta función permite que el usuario seleccione una prioridad del sistema (predefinidas).
# Muestra un menú con las opciones disponibles y retorna la prioridad seleccionada.

def seleccionarPrioridad():
    print("\nSeleccione una Prioridad:")
    print("1. Normal")
    print("2. Socio")
    print("3. Torneo")
    opcion = leerEntero("Opción: ", 1, 3)
    
    prioridades = {1: "Normal", 2: "Socio", 3: "Torneo"}
    return prioridades[opcion]

# Esta función pide un número al usuario que se usa en el menú.
# Usa un bloque try-except para evitar que el programa se rompa si el usuario ingresa algo que no es un número entero.
# Se repite en bucle hasta que el número ingresado esté dentro del rango permitido (minimo, maximo).

def leerEntero(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"Error: Por favor ingrese un número entre {minimo} y {maximo}.")
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar un número entero.")

# Esta función permite buscar una reserva específica dentro de la agenda.
# Se utiliza la Fecha y la Hora como identificador único para encontrar el elemento exacto.
# Retorna la reserva si la encuentra, o None si no existe en la agenda.

def buscarReservaEnAgenda(agenda, fecha, hora):
    for i in range(1, tamanioAgenda(agenda) + 1):
        res = recuperarReserva(agenda, i)
        if res is not None and verFecha(res) == fecha and verHora(res) == hora:
            return res
    return None

# Esta es una funcion simple para mostrar el menú principal del programa, se llama cada vez que se necesita mostrar las opciones al usuario.

def mostrarMenu():
    print("\n" + "="*40)
    print("  SISTEMA DE GESTIÓN - COMPLEJO DEPORTIVO")
    print("="*40)
    print("1. Alta de Reserva")
    print("2. Modificación de Reserva (Completa/Parcial)")
    print("3. Cancelación de Reserva")
    print("4. Listado General de Reservas")
    print("5. Mantenimiento (Traslado por Lluvia / Limpieza)")
    print("6. Hoja de Ruta (Personal de Maestranza)")
    print("0. Salir")
    print("="*40)

# Esta función normaliza la fecha a formato DD/MM/YYYY para evitar inconsistencias
# Convierte "10/4/2026" a "10/04/2026" para asegurar que siempre sea el mismo formato

def normalizarFecha(fecha):
    try:
        fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
        return fecha_obj.strftime("%d/%m/%Y")
    except ValueError:
        return None

# Esto permite validar la fecha y hora permitiendo que pongan una fecha y hora existente y no un 31 de feberero a las 25:00h

def validarFecha(fecha):
    try:
        fecha_normalizada = normalizarFecha(fecha)
        if fecha_normalizada is None:
            print("Error: Fecha inválida. Use formato DD/MM/AAAA.")
            return False, None
        
        fecha_obj = datetime.strptime(fecha_normalizada, "%d/%m/%Y")
        
        if fecha_obj.year < 2026:
            print("Error: El año debe ser 2026 o posterior.")
            return False, None
            
        return True, fecha_normalizada
    except ValueError:
        print("Error: Fecha inválida. Use formato DD/MM/AAAA.")
        return False, None

def validarHora(hora):
    if not hora or hora.strip() == "":
        print("Error: Hora no puede estar vacía. Use formato HH:MM (00:00 a 23:59).")
        return False, None
    try:
        datetime.strptime(hora, "%H:%M")
        return True, hora
    except ValueError:
        print("Error: Hora inválida. Use formato HH:MM (00:00 a 23:59).")
        return False, None

# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def main():
    # Se inicializa la estructura de la agenda utilizando el TAD Agenda.
    # Este 'mi_agenda' funciona como el contenedor principal donde se guardan todas las reservas.
    mi_agenda = crearAgenda()
    
    opcion = -1
    
    while opcion != 0:
        mostrarMenu()
        opcion = leerEntero("Seleccione una opción: ", 0, 6)
        
        if opcion == 1:
            # Opcion 1: Registro de nuevos turnos en el sistema.
            print("\n--- ALTA DE RESERVA ---")
            act = seleccionarActividad()
            prio = seleccionarPrioridad()
            fec = input("Fecha (DD/MM/AAAA): ")
            hor = input("Hora (HH:MM): ")

            # Se validan los formatos de fecha y hora antes de operar con el TAD.
            es_valida_fec, fec_normalizada = validarFecha(fec)
            es_valida_hor, hor_validada = validarHora(hor)
            
            if es_valida_fec and es_valida_hor:
                # Se verifica que el horario no esté ocupado por otra reserva existente.
                if buscarReservaEnAgenda(mi_agenda, fec_normalizada, hor_validada) is None:
                    # Se utiliza el constructor y el método CARGAR del TAD Reserva para crear el paquete de datos.
                    nueva = crearReserva()
                    cargarReserva(nueva, act, prio, fec_normalizada, hor_validada)
                    # Se guarda la nueva reserva en la lista general de la agenda.
                    agregarReserva(mi_agenda, nueva)
                    print(">> Reserva registrada exitosamente.")
                else:
                    print("Error: Ya existe un turno ocupado en esa fecha y hora.")
            else:
                print("Error: Formato de fecha u hora inválido.")

        elif opcion == 2:
            # Opcion 2: Actualización de datos de un turno que ya existe en la agenda.
            print("\n--- MODIFICACIÓN DE RESERVA ---")
            f_busq = input("Fecha del turno a modificar: ")
            h_busq = input("Hora del turno a modificar: ")
            
            # Validar la fecha y hora antes de buscar
            es_valida_fec, f_busq_norm = validarFecha(f_busq)
            es_valida_hor, h_busq_val = validarHora(h_busq)
            
            if not es_valida_fec or not es_valida_hor:
                print("Error: Fecha u hora de búsqueda inválida.")
                continue
            
            # Se busca si el turno existe en la agenda antes de pedir los nuevos datos para modificar.
            res_encontrada = buscarReservaEnAgenda(mi_agenda, f_busq_norm, h_busq_val)
            
            if res_encontrada:
                print("Turno encontrado. Ingrese los nuevos datos (presione 0 para mantener el actual):")
                
                # Modificación de Actividad
                print(f"Actividad actual: {verActividad(res_encontrada)}")
                print("¿Desea cambiar la actividad? (1=Sí, 0=No): ", end="")
                cambiar_act = leerEntero("", 0, 1)
                if cambiar_act == 1:
                    n_act = seleccionarActividad()
                else:
                    n_act = verActividad(res_encontrada)
                
                # Modificación de Prioridad
                print(f"Prioridad actual: {verPrioridad(res_encontrada)}")
                print("¿Desea cambiar la prioridad? (1=Sí, 0=No): ", end="")
                cambiar_prio = leerEntero("", 0, 1)
                if cambiar_prio == 1:
                    n_prio = seleccionarPrioridad()
                else:
                    n_prio = verPrioridad(res_encontrada)
                
                # Modificación de Fecha
                print(f"Fecha actual: {verFecha(res_encontrada)}")
                print("¿Desea cambiar la fecha? (1=Sí, 0=No): ", end="")
                cambiar_fec = leerEntero("", 0, 1)
                if cambiar_fec == 1:
                    n_fec = input("Nueva Fecha (DD/MM/AAAA): ")
                else:
                    n_fec = verFecha(res_encontrada)
                
                # Modificación de Hora
                print(f"Hora actual: {verHora(res_encontrada)}")
                print("¿Desea cambiar la hora? (1=Sí, 0=No): ", end="")
                cambiar_hor = leerEntero("", 0, 1)
                if cambiar_hor == 1:
                    n_hor = input("Nueva Hora (HH:MM): ")
                else:
                    n_hor = verHora(res_encontrada)

                # Se valida la nueva fecha y hora antes de aplicar cualquier cambio.
                es_valida_n_fec, n_fec_norm = validarFecha(n_fec)
                es_valida_n_hor, n_hor_val = validarHora(n_hor)
                
                if not es_valida_n_fec or not es_valida_n_hor:
                    print("Error: Formato de fecha u hora inválido.")
                    continue
                
                # En caso de cambiar fecha u hora, se valida que el nuevo horario no choque con otra reserva.
                if n_fec_norm != f_busq_norm or n_hor_val != h_busq_val:
                    if buscarReservaEnAgenda(mi_agenda, n_fec_norm, n_hor_val):
                        print("Error: El nuevo horario ya está ocupado.")
                        continue
                
                # Se aplican los cambios utilizando los métodos de modificación (setters) del TAD Reserva.
                modActividad(res_encontrada, n_act)
                modPrioridad(res_encontrada, n_prio)
                modFecha(res_encontrada, n_fec_norm)
                modHora(res_encontrada, n_hor_val)
                print(">> Reserva actualizada correctamente.")
            else:
                print("No se encontró ninguna reserva coincidente.")

        elif opcion == 3:
            # Opcion 3: Eliminación definitiva de un turno específico del sistema.
            print("\n--- CANCELACIÓN DE RESERVA ---")
            f_baja = input("Fecha del turno a cancelar: ")
            h_baja = input("Hora del turno a cancelar: ")
            
            # Validar fecha y hora antes de buscar
            es_valida_fec, f_baja_norm = validarFecha(f_baja)
            es_valida_hor, h_baja_val = validarHora(h_baja)
            
            if not es_valida_fec or not es_valida_hor:
                print("Error: Fecha u hora inválida.")
                continue
            
            # Se identifica la reserva por su fecha y hora originales para proceder a la baja.
            res_baja = buscarReservaEnAgenda(mi_agenda, f_baja_norm, h_baja_val)
            
            if res_baja:
                # Se solicita al TAD Agenda que remueva el objeto de la lista interna.
                cancelarReserva(mi_agenda, f_baja_norm, h_baja_val)
                print(">> Turno liberado correctamente.")
            else:
                print("Error: No existe ninguna reserva con esos datos.")

        elif opcion == 4:
            # Opcion 4: Visualización de todos los turnos almacenados en la lista de la agenda.
            print("\n--- LISTADO GENERAL DE RESERVAS ---")
            # Se obtiene la cantidad de elementos mediante la función de tamaño del TAD Agenda.
            cant = tamanioAgenda(mi_agenda)
            
            if cant == 0:
                print("La agenda está vacía actualmente.")
            else:
                # Se itera la agenda recuperando cada reserva por su índice de posición.
                for i in range(1, cant + 1):
                    r = recuperarReserva(mi_agenda, i)
                    # Se imprimen los atributos utilizando los selectores (getters) del TAD Reserva.
                    print(f"{i}. {verFecha(r)} {verHora(r)} | {verActividad(r)} ({verPrioridad(r)})")

        elif opcion == 5:
            # Opcion 5: Submenú para procesos masivos (mover fechas por lluvia o borrar días enteros).
            print("\n--- MANTENIMIENTO ---")
            print("1. Traslado por Lluvia/Cierre")
            print("2. Limpieza de Calendario (Día completo)")
            sub = leerEntero("Seleccione una opción: ", 1, 2)
            
            if sub == 1:
                f_origen = input("Fecha a trasladar: ")
                f_destino = input("Nueva fecha de destino: ")
                
                # Validar ambas fechas antes de procesar
                es_valida_origen, f_origen_norm = validarFecha(f_origen)
                es_valida_destino, f_destino_norm = validarFecha(f_destino)
                
                if es_valida_origen and es_valida_destino:
                    # Se llama a la función de procesos que recorre la agenda modificando fechas masivamente.
                    trasladarPorLluvia(mi_agenda, f_origen_norm, f_destino_norm)
                else:
                    print("Error: Una o ambas fechas son inválidas.")
            else:
                f_borrar = input("Fecha a limpiar completamente: ")
                
                # Validar fecha antes de procesar
                es_valida, f_borrar_norm = validarFecha(f_borrar)
                
                if es_valida:
                    # Se eliminan todas las reservas que coincidan con la fecha indicada.
                    limpiarCalendario(mi_agenda, f_borrar_norm)
                else:
                    print("Error: Fecha inválida.")

        elif opcion == 6:
            # Opcion 6: Creación de una Cola de trabajo para el personal de preparación de canchas.
            print("\n--- GENERAR HOJA DE RUTA ---")
            f_hoja = input("Ingrese la fecha para el personal de maestranza: ")
            
            # Validar la fecha antes de usarla
            es_valida, f_hoja_norm = validarFecha(f_hoja)
            
            if not es_valida:
                print("Error: Fecha inválida.")
                continue
            
            # Se genera la estructura de Cola filtrando las actividades del día solicitado.
            cola_preparacion = generarHojaDeRuta(mi_agenda, f_hoja_norm)
            
            if not esVacia(cola_preparacion):
                print(f"Orden de preparación para el {f_hoja_norm}:")
                # Se procesa la Cola mostrando las tareas en el orden en que fueron cargadas (FIFO).
                while not esVacia(cola_preparacion):
                    tarea = desencolar(cola_preparacion) 
                    print(f"-> Preparar {tarea[0]} - Prioridad: {tarea[1]}")
            else:
                print("No hay actividades programadas para esa fecha.")

    print("Saliendo del sistema...")

if __name__ == "__main__":
    main()