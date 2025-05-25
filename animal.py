
from produccion import Produccion

class Animal(Produccion):
    """
    Representa un animal en la granja.
    Hereda de la clase Produccion.
    """
    def __init__(self, nombre: str, especie: str, raza: str, edad: int, peso: float):
        """
        Inicializa una nueva instancia de Animal.
        Args:
            nombre (str): El nombre o identificador del animal.
            especie (str): La especie del animal (e.g., "Bovino", "Porcino").
            raza (str): La raza del animal.
            edad (int): La edad del animal (e.g., en meses o años).
            peso (float): El peso del animal (e.g., en kg).
        """
        super().__init__(nombre)
        self._especie = especie # Atributo privado
        self._raza = raza       # Atributo privado
        self._edad = edad       # Atributo privado
        self._peso = peso       # Atributo privado

    def calcular_produccion(self) -> float:
        """
        Calcula la producción del animal.
        """
        return self._peso

    def editar_animal(self, nueva_especie: str, nueva_raza: str, nueva_edad: int, nuevo_peso: float):
        """
        Edita los atributos del animal.
        """
        self._especie = nueva_especie
        self._raza = nueva_raza
        self._edad = nueva_edad
        self._peso = nuevo_peso

    def get_especie(self) -> str:
        """
        Retorna la especie del animal.
        """
        return self._especie

    def get_raza(self) -> str:
        """
        Retorna la raza del animal.

        """
        return self._raza

    def get_edad(self) -> int:
        """
        Retorna la edad del animal.

        """
        return self._edad

    def get_peso(self) -> float:
        """
        Retorna el peso del animal.

        """
        return self._peso

