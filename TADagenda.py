from TADreserva import *


# CREACION

def crearAgenda():
    return []


# CONSULTA

def agendaVacia(agenda):
    return len(agenda) == 0


def tamanioAgenda(agenda):
    return len(agenda)


def recuperarReserva(agenda, pos):
    return agenda[pos - 1]


def buscarReserva(agenda, fecha, hora):
    i = 0

    while i < len(agenda):
        reserva = agenda[i]

        if verFecha(reserva) == fecha and verHora(reserva) == hora:
            return reserva

        i += 1

    return None


def listarReservas(agenda):
    return agenda


# MODIFICACION / ASIGNACION

def agregarReserva(agenda, reserva):
    agenda.append(reserva)


# ELIMINACION


def cancelarReserva(agenda, fecha, hora):
    reserva = buscarReserva(agenda, fecha, hora)
    if reserva is not None:
        agenda.remove(reserva)