import time
import random
import curses

class JuegoDeNaves:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.vidas = 3
        self.naves_destruidas = 0
        self.jugador_pos = [10, 10]  # Posición inicial del jugador

    def mostrar_estado(self):
        self.pantalla.addstr(0, 0, f"Vidas: {self.vidas} | Naves destruidas: {self.naves_destruidas}")

    def mostrar_jugador(self):
        self.pantalla.addch(self.jugador_pos[0], self.jugador_pos[1], 'X')

    def borrar_jugador(self):
        self.pantalla.addch(self.jugador_pos[0], self.jugador_pos[1], ' ')

    def mover_jugador(self, direccion):
        if direccion == 'izquierda' and self.jugador_pos[1] > 0:
            self.jugador_pos[1] -= 1
        elif direccion == 'derecha' and self.jugador_pos[1] < curses.COLS - 1:
            self.jugador_pos[1] += 1

    def jugar(self):
        self.pantalla.clear()
        self.pantalla.refresh()

        while self.vidas > 0:
            llega_nave_enemiga = random.choice([True, False])

            if llega_nave_enemiga:
                self.mostrar_estado()
                self.mostrar_jugador()
                self.pantalla.refresh()

                respuesta = self.pantalla.getch()

                # Limpia la pantalla y borra la posición anterior del jugador
                self.pantalla.clear()
                self.borrar_jugador()

                if respuesta == ord('a'):
                    self.mover_jugador('izquierda')
                elif respuesta == ord('d'):
                    self.mover_jugador('derecha')

                print("¡Nave enemiga detectada!")

                # Simulamos el movimiento de la nave enemiga
                for _ in range(curses.LINES - 1, 0, -1):
                    self.pantalla.addstr(_, curses.COLS - 1, ' ')
                    self.pantalla.addstr(_, curses.COLS - 2, '*')
                    self.pantalla.refresh()
                    time.sleep(0.1)

                # Verifica si el jugador intercepta la nave enemiga
                if self.jugador_pos[0] == _ and self.jugador_pos[1] == curses.COLS - 2:
                    print("¡La nave enemiga te ha alcanzado!")
                    self.vidas -= 1
                else:
                    print("¡Has destruido la nave enemiga!")
                    self.naves_destruidas += 1

                time.sleep(1)  # Espera antes de limpiar la pantalla y repetir el ciclo

            self.mostrar_estado()

        print("Juego terminado. Has perdido todas tus vidas.")


def main(stdscr):
    juego = JuegoDeNaves(stdscr)
    juego.jugar()

# Iniciar el juego utilizando curses
curses.wrapper(main)    
