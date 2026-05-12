# Sistema de Gestion - Complejo Deportivo

Aplicacion de consola escrita en Python para administrar reservas de un complejo deportivo. El sistema permite crear, modificar, cancelar y listar turnos, ademas de ejecutar tareas de mantenimiento cuando hay lluvia o cierre y generar una hoja de ruta para maestranza.

## Resumen rapido

| Funcion                 | Que hace                                                           |
| ----------------------- | ------------------------------------------------------------------ |
| Alta de reserva         | Crea un turno nuevo validando fecha, hora, actividad y prioridad.  |
| Modificacion de reserva | Cambia actividad, prioridad, fecha y/o hora de un turno existente. |
| Cancelacion de reserva  | Elimina un turno puntual de la agenda.                             |
| Listado general         | Muestra todas las reservas guardadas.                              |
| Mantenimiento           | Traslada reservas por lluvia o borra un dia completo.              |
| Hoja de ruta            | Genera una cola con tareas de maestranza para una fecha dada.      |

## Como funciona el programa

El sistema trabaja con tres estructuras principales:

| Archivo                        | Estructura | Proposito                                        |
| ------------------------------ | ---------- | ------------------------------------------------ |
| [TADreserva.py](TADreserva.py) | Reserva    | Guarda actividad, prioridad, fecha y hora.       |
| [TADagenda.py](TADagenda.py)   | Agenda     | Almacena todas las reservas en una lista.        |
| [TADcola.py](TADcola.py)       | Cola       | Ordena las tareas de maestranza en formato FIFO. |

La aplicacion principal se encuentra en [main.py](main.py). Desde alli se muestra un menu interactivo y se coordinan todas las operaciones.

## Menu principal

| Opcion | Descripcion                                    |
| ------ | ---------------------------------------------- |
| 1      | Alta de Reserva                                |
| 2      | Modificacion de Reserva (Completa/Parcial)     |
| 3      | Cancelacion de Reserva                         |
| 4      | Listado General de Reservas                    |
| 5      | Mantenimiento (Traslado por Lluvia / Limpieza) |
| 6      | Hoja de Ruta (Personal de Maestranza)          |
| 0      | Salir                                          |

## Funciones destacadas

### Gestion de reservas

- `seleccionarActividad()`: permite elegir entre Futbol 5, Tenis o Cumpleanos.
- `seleccionarPrioridad()`: permite elegir entre Normal, Socio o Torneo.
- `validarFecha()`: valida el formato `DD/MM/AAAA` y exige que el anio sea 2026 o posterior.
- `validarHora()`: valida el formato `HH:MM`.
- `buscarReservaEnAgenda()`: localiza una reserva por fecha y hora.

### Mantenimiento

- `trasladarPorLluvia()`: cambia la fecha de todas las reservas que coinciden con una fecha origen.
- `limpiarCalendario()`: elimina todas las reservas de un dia completo.

### Maestranza

- `generarHojaDeRuta()`: recorre la agenda y arma una cola con `[actividad, prioridad]` para la fecha solicitada.

## Reglas de uso

- No se pueden cargar dos reservas en la misma fecha y hora.
- Si se modifica una reserva, el nuevo horario tambien se controla para evitar choques.
- Las fechas se normalizan automaticamente al formato `DD/MM/AAAA`.
- Solo se aceptan fechas desde 2026 en adelante.

## Ejemplo de salida

```text
========================================
  SISTEMA DE GESTION - COMPLEJO DEPORTIVO
========================================
1. Alta de Reserva
2. Modificacion de Reserva (Completa/Parcial)
3. Cancelacion de Reserva
4. Listado General de Reservas
5. Mantenimiento (Traslado por Lluvia / Limpieza)
6. Hoja de Ruta (Personal de Maestranza)
0. Salir
========================================
```

## Como ejecutar

1. Abrir una terminal en la carpeta del proyecto.
2. Ejecutar:

```bash
python main.py
```

Si tu entorno usa `python3`, tambien puedes correr:

```bash
python3 main.py
```

---

# Sports Complex Management System

Command-line Python application to manage reservations for a sports complex. The system allows you to create, edit, cancel, and list bookings, as well as handle maintenance actions when there is rain or a closure and generate a route sheet for the maintenance staff.

## Quick summary

| Function           | What it does                                                              |
| ------------------ | ------------------------------------------------------------------------- |
| New reservation    | Creates a booking after validating date, time, activity, and priority.    |
| Edit reservation   | Changes the activity, priority, date, and/or time of an existing booking. |
| Cancel reservation | Deletes a specific booking from the agenda.                               |
| General listing    | Shows every stored reservation.                                           |
| Maintenance        | Moves bookings because of rain or clears an entire day.                   |
| Route sheet        | Builds a FIFO queue with maintenance tasks for a given date.              |

## How the program works

The system is built on three main data structures:

| File                           | Structure   | Purpose                                    |
| ------------------------------ | ----------- | ------------------------------------------ |
| [TADreserva.py](TADreserva.py) | Reservation | Stores activity, priority, date, and time. |
| [TADagenda.py](TADagenda.py)   | Agenda      | Keeps all reservations in a list.          |
| [TADcola.py](TADcola.py)       | Queue       | Orders maintenance tasks in FIFO format.   |

The main application is in [main.py](main.py). It displays the interactive menu and coordinates all operations.

## Main menu

| Option | Description                           |
| ------ | ------------------------------------- |
| 1      | New reservation                       |
| 2      | Edit reservation (full or partial)    |
| 3      | Cancel reservation                    |
| 4      | General reservation listing           |
| 5      | Maintenance (rain transfer / cleanup) |
| 6      | Route sheet (maintenance staff)       |
| 0      | Exit                                  |

## Key functions

### Reservation management

- `seleccionarActividad()`: lets the user choose between Futbol 5, Tennis, or Birthday.
- `seleccionarPrioridad()`: lets the user choose between Normal, Member, or Tournament.
- `validarFecha()`: checks the `DD/MM/YYYY` format and requires year 2026 or later.
- `validarHora()`: checks the `HH:MM` format.
- `buscarReservaEnAgenda()`: finds a reservation by date and time.

### Maintenance

- `trasladarPorLluvia()`: changes the date of every reservation that matches a source date.
- `limpiarCalendario()`: removes all reservations for a full day.

### Maintenance staff

- `generarHojaDeRuta()`: scans the agenda and builds a queue with `[activity, priority]` for the selected date.

## Usage rules

- Two reservations cannot share the same date and time.
- When a reservation is edited, the new slot is also checked for conflicts.
- Dates are automatically normalized to `DD/MM/YYYY`.
- Only dates from 2026 onward are accepted.

## Example output

```text
========================================
  SISTEMA DE GESTION - COMPLEJO DEPORTIVO
========================================
1. Alta de Reserva
2. Modificacion de Reserva (Completa/Parcial)
3. Cancelacion de Reserva
4. Listado General de Reservas
5. Mantenimiento (Traslado por Lluvia / Limpieza)
6. Hoja de Ruta (Personal de Maestranza)
0. Salir
========================================
```

## How to run

1. Open a terminal in the project folder.
2. Run:

```bash
python main.py
```

If your environment uses `python3`, you can also run:

```bash
python3 main.py
```
