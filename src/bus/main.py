#!/usr/bin/python3
# Bus Race - Terminal Simulation
# Copyright (C) 2025 Jakepys

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import os
import platform
import time
import sys 
from random import randint


class Conductores:
    def __init__(self, nombre_p_1: str, nombre_p_2: str):
        self.nombre_p_1 = nombre_p_1
        self.nombre_p_2 = nombre_p_2


class Bus(Conductores):
    def __init__(self, nombre_p_1: str, nombre_p_2: str):
        super().__init__(nombre_p_1, nombre_p_2)

    def get_bus(self, nombre: str, advence: int) -> str:
        space = " " * advence
        bus_lines = [
            "|-------------------",
            "|                  | |",
            f"| {nombre:<15} ----|",
            "|                       |",
            "|-----------------------|",
            "      *        *",
        ]
        return "\n".join([space + line for line in bus_lines])


class Carrera(Bus):
    def __init__(self, nombre_p_1: str, nombre_p_2: str):
        super().__init__(nombre_p_1, nombre_p_2)
        self._size_t = os.get_terminal_size().columns - 30

    def _clear_pant(self):
        os.system("clear" if platform.system() == "Linux" else "cls")

    def print_road(self):
        print("-" * (self._size_t + 30))

    def run_bus(self):
        try:
            if self._size_t <= 100:
                print("No min to 100 in terminal :(")
                exit(0)

            pos_p_1 = 0
            pos_p_2 = 0

            while True:
                if pos_p_1 >= self._size_t and pos_p_2 >= self._size_t:
                    print("¡Empate!")
                    break
                elif pos_p_1 >= self._size_t:
                    print(f"¡Ganó el conductor {self.nombre_p_1}!")
                    break
                elif pos_p_2 >= self._size_t:
                    print(f"¡Ganó el conductor {self.nombre_p_2}!")
                    break

                self._clear_pant()
                print(self.get_bus(self.nombre_p_1, pos_p_1))
                self.print_road()
                print(self.get_bus(self.nombre_p_2, pos_p_2))
                self.print_road()

                pos_p_1 += randint(1, 5)
                pos_p_2 += randint(1, 5)
                time.sleep(0.3)
        except KeyboardInterrupt:
            print("Bye :D")
            exit(0)


def main():
    if len(sys.argv) <= 2:
        print("Need other conductor")
        exit(1)

    pilotos = Conductores(sys.argv[1], sys.argv[2])
    Carrera(pilotos.nombre_p_1, pilotos.nombre_p_2).run_bus()


if __name__ == "__main__":
    main()
