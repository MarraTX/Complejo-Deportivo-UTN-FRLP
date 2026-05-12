#TADReserva.py (Uriel Sebastian Lallana)

#Creo reserva
def crearReserva():
    reserva = [None] * 4
    return reserva

#Operaciones de Cargar

def cargarReserva(reserva, a, p, f, h):
    reserva[0] = a
    reserva[1] = p
    reserva[2] = f
    reserva[3] = h

#Operaciones de VER

def verActividad(reserva):
    return reserva[0]

def verPrioridad(reserva):
    return reserva[1]

def verFecha(reserva):
    return reserva[2]

def verHora(reserva):
    return reserva[3]


#Operaciones de Modificar

def modActividad(reserva, nActividad):
    reserva[0] = nActividad

def modPrioridad(reserva, nPrioridad):
    reserva[1] = nPrioridad

def modFecha(reserva, nFecha):
    reserva[2] = nFecha

def modHora(reserva, nHora):
    reserva[3] = nHora


#Operaciones de Asignar

def asignarReserva(reserva1, reserva2):
    reserva2[0] = reserva1[0]
    reserva2[1] = reserva1[1]
    reserva2[2] = reserva1[2]
    reserva2[3] = reserva1[3]