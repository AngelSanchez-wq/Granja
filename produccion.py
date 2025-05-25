
from abc import ABC, abstractmethod

class Produccion(ABC):
    """
    Clase base abstracta para representar un elemento de producción en la granja.
    Define la interfaz para calcular la producción.
    """
    def __init__(self, nombre: str):
        """
        Inicializa una nueva instancia de Produccion.
        Args:
            nombre (str): El nombre del elemento de producción.
        """
        self._nombre = nombre # Atributo privado

    def get_nombre(self) -> str:
        """
        Retorna el nombre del elemento de producción.
        Returns:
            str: El nombre del elemento.
        """
        return self._nombre

    @abstractmethod
    def calcular_produccion(self) -> float:
        """
        Método abstracto para calcular la producción del elemento.
        Debe ser implementado por las subclases.
        Returns:
            float: La producción calculada.
        """
        pass

