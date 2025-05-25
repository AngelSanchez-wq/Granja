# farm_management_system/animal.py
from produccion import Produccion

class Cultivo(Produccion):
    """
    Representa un cultivo específico en la granja.
    Hereda de la clase Produccion.
    """
    def __init__(self, nombre: str, area_cultivo: float, rendimiento: float):
        """
        Inicializa una nueva instancia de Cultivo.
        Args:
            nombre (str): El nombre del cultivo.
            area_cultivo (float): El área dedicada al cultivo (e.g., en hectáreas).
            rendimiento (float): El rendimiento por unidad de área (e.g., kg/hectárea).
        """
        super().__init__(nombre)
        self._area_cultivo = area_cultivo # Atributo privado
        self._rendimiento = rendimiento   # Atributo privado

    def calcular_produccion(self) -> float:
        """
        Calcula la producción total del cultivo.
        Returns:
            float: La producción total del cultivo.
        """
        return self._area_cultivo * self._rendimiento

    def editar_cultivo(self, nueva_area: float, nuevo_rendimiento: float):
        """
        Edita el área y el rendimiento del cultivo.
        Args:
            nueva_area (float): La nueva área de cultivo.
            nuevo_rendimiento (float): El nuevo rendimiento del cultivo.
        """
        self._area_cultivo = nueva_area
        self._rendimiento = nuevo_rendimiento

    def get_area_cultivo(self) -> float:
        """
        Retorna el área de cultivo.
        Returns:
            float: El área de cultivo.
        """
        return self._area_cultivo

    def get_rendimiento(self) -> float:
        """
        Retorna el rendimiento del cultivo.
        Returns:
            float: El rendimiento del cultivo.
        """
        return self._rendimiento

