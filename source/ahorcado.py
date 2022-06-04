from random import choice
from colorama import Fore
from utils import constantes
import time as tiempo

"""
    A H O R C A D O ❔
    
    Brief:
        Juego "ahorcado" desarrollado en python, logica y manejo de este.
    
    Tipo:
        Juego de adivinanza.
    
    Authors:
        (1) le01q | Leo Araya | [github.com/le01q | github.com/leoarayav]
    
    Copyright:
        Ahorcao (C) 2022 - All rights reserved
"""

class Ahorcado:
    def __init__(
        self, 
        palabra: str = "", 
        adivinanzas: chr = [],
        juegoGanado: bool = False,
        max_intentos: int = 8
        ):

        self.palabra = ""
        self.adivinanzas = adivinanzas = []
        self.max_intentos = max_intentos
        self.ganador = juegoGanado
    
    def MostrarInicio(self):
        print(
            Fore.GREEN +
            "[🎮 AHORCADO] | Obteniendo recursos..." +
            Fore.RESET
        )

        tiempo.sleep(4)

        print(
            Fore.GREEN + 
            "[✔] | Iniciando el juego con normalidad..." +
            Fore.RESET
        )

        tiempo.sleep(3)

        print(
            Fore.WHITE +
            constantes.BANNER + 
            Fore.RESET
        )
    
    def ObtenerPalabras(self):
        with open('./source/palabras.txt', "r") as archivo_palabras:
            palabras = archivo_palabras.readlines()
        self.palabra = choice(palabras)[:-1]

    def Logica(self):
        while not self.ganador:
            for letra in self.palabra:
                if letra.lower() in self.adivinanzas:
                    print(
                        end=" " +
                        Fore.YELLOW + 
                        letra +
                        Fore.RESET
                    )

                else:
                    print(
                        end=" " +
                        Fore.YELLOW +
                        "_" +
                        Fore.RESET
                    )
    
            palabra = input(f"\t[Intentos: {self.max_intentos}] Letra: ")
            self.adivinanzas.append(palabra)

            if palabra.lower() not in letra.lower():
                self.max_intentos -= 1
                if self.max_intentos == 0: break
            
            self.ganador = True

            for letra in self.palabra:
                if letra.lower() not in self.adivinanzas: self.ganador = False
    
    def ObtenerGanador(self):
        if self.ganador:
            print(
                end=" " +
                Fore.GREEN + 
                f"Adivinaste la palabra, has ganado la partida! [❔: {self.palabra}]" +
                Fore.RESET
            )

        else:
            print(
                end=" " +
                Fore.RED +
                f"No adivinaste la palabra, has perdido la partida! [❔: {self.palabra}]" +
                Fore.RESET
            )

    def IniciarJuego(self):
        self.MostrarInicio()
        self.ObtenerPalabras()
        self.Logica()
        self.ObtenerGanador()

if __name__ == '__main__':
    ahorcado = Ahorcado()
    ahorcado.IniciarJuego()