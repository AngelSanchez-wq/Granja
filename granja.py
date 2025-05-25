from typing import List
from cultivo import Cultivo
from animal import Animal

class Granja:
    """
    Clase principal que gestiona los cultivos y animales de la granja.
    """
    def __init__(self, nombre: str):
        """
        Inicializa una nueva instancia de Granja.
        Args:
            nombre (str): El nombre de la granja.
        """
        self._nombre = nombre     # Atributo privado
        self._cultivos: List[Cultivo] = [] # Atributo privado, lista de objetos Cultivo
        self._animales: List[Animal] = [] # Atributo privado, lista de objetos Animal

    def get_nombre(self) -> str:
        """
        Retorna el nombre de la granja.

        """
        return self._nombre

    # Métodos para la gestión de cultivos
    def agregar_cultivo(self, cultivo: Cultivo):
        """
        Agrega un nuevo cultivo a la granja.
       
        """
        self._cultivos.append(cultivo)
        print(f"Cultivo '{cultivo.get_nombre()}' agregado exitosamente.")

    def editar_cultivo(self, nombre_cultivo: str, nueva_area: float, nuevo_rendimiento: float) -> bool:
        """
        Edita un cultivo existente por su nombre.
    
        """
        for cultivo in self._cultivos:
            if cultivo.get_nombre() == nombre_cultivo:
                cultivo.editar_cultivo(nueva_area, nuevo_rendimiento)
                print(f"Cultivo '{nombre_cultivo}' editado exitosamente.")
                return True
        print(f"Error: Cultivo '{nombre_cultivo}' no encontrado.")
        return False

    def eliminar_cultivo(self, nombre_cultivo: str) -> bool:
        """
        Elimina un cultivo por su nombre.
        
        """
        initial_len = len(self._cultivos)
        self._cultivos = [c for c in self._cultivos if c.get_nombre() != nombre_cultivo]
        if len(self._cultivos) < initial_len:
            print(f"Cultivo '{nombre_cultivo}' eliminado exitosamente.")
            return True
        print(f"Error: Cultivo '{nombre_cultivo}' no encontrado.")
        return False

    def consultar_cultivos(self) -> List[Cultivo]:
        """
        Retorna la lista de todos los cultivos en la granja.

        """
        return self._cultivos

    def calcular_produccion_total_cultivos(self) -> float:
        """
        Calcula la producción total de todos los cultivos en la granja.

        """
        total_produccion = sum(cultivo.calcular_produccion() for cultivo in self._cultivos)
        return total_produccion

    # Métodos para la gestión de animales
    def agregar_animal(self, animal: Animal):
        """
        Agrega un nuevo animal a la granja.

        """
        self._animales.append(animal)
        print(f"Animal '{animal.get_nombre()}' agregado exitosamente.")

    def editar_animal(self, nombre_animal: str, nueva_especie: str, nueva_raza: str, nueva_edad: int, nuevo_peso: float) -> bool:
        """
        Edita un animal existente por su nombre.
 
        Returns:
            bool: True si el animal fue editado, False si no se encontró.
        """
        for animal in self._animales:
            if animal.get_nombre() == nombre_animal:
                animal.editar_animal(nueva_especie, nueva_raza, nueva_edad, nuevo_peso)
                print(f"Animal '{nombre_animal}' editado exitosamente.")
                return True
        print(f"Error: Animal '{nombre_animal}' no encontrado.")
        return False

    def eliminar_animal(self, nombre_animal: str) -> bool:
        """
        Elimina un animal por su nombre.
        
        """
        initial_len = len(self._animales)
        self._animales = [a for a in self._animales if a.get_nombre() != nombre_animal]
        if len(self._animales) < initial_len:
            print(f"Animal '{nombre_animal}' eliminado exitosamente.")
            return True
        print(f"Error: Animal '{nombre_animal}' no encontrado.")
        return False

    def consultar_animales(self) -> List[Animal]:
        """
        Retorna la lista de todos los animales en la granja.
        Returns:
            List[Animal]: Una lista de objetos Animal.
        """
        return self._animales

    def calcular_produccion_total_animales(self) -> float:
        """
        Calcula la producción total de todos los animales en la granja.
        Returns:
            float: La producción total de animales.
        """
        total_produccion = sum(animal.calcular_produccion() for animal in self._animales)
        return total_produccion

    # Métodos para la producción total de la granja y reportes
    def calcular_produccion_total_granja(self) -> float:
        """
        Calcula la producción total de la granja (cultivos + animales).
        Returns:
            float: La producción total de la granja.
        """
        total_cultivos = self.calcular_produccion_total_cultivos()
        total_animales = self.calcular_produccion_total_animales()
        return total_cultivos + total_animales

    def generar_reporte_produccion(self) -> str:
        """
        Genera un reporte detallado de la producción de la granja.
        Returns:
            str: El reporte de producción.
        """
        reporte = f"--- Reporte de Producción de la Granja '{self._nombre}' ---\n\n"

        reporte += "--- Cultivos ---\n"
        if not self._cultivos:
            reporte += "No hay cultivos registrados.\n"
        else:
            for cultivo in self._cultivos:
                reporte += (f"  - {cultivo.get_nombre()}: "
                            f"Área={cultivo.get_area_cultivo():.2f} ha, "
                            f"Rendimiento={cultivo.get_rendimiento():.2f} kg/ha, "
                            f"Producción={cultivo.calcular_produccion():.2f} kg\n")
            reporte += f"Producción Total de Cultivos: {self.calcular_produccion_total_cultivos():.2f} kg\n\n"

        reporte += "--- Ganado ---\n"
        if not self._animales:
            reporte += "No hay animales registrados.\n"
        else:
            for animal in self._animales:
                reporte += (f"  - {animal.get_nombre()}: "
                            f"Especie={animal.get_especie()}, "
                            f"Raza={animal.get_raza()}, "
                            f"Edad={animal.get_edad()} meses, "
                            f"Peso={animal.get_peso():.2f} kg, "
                            f"Producción={animal.calcular_produccion():.2f} kg (peso)\n")
            reporte += f"Producción Total de Ganado: {self.calcular_produccion_total_animales():.2f} kg\n\n"

        reporte += f"--- Producción Total de la Granja: {self.calcular_produccion_total_granja():.2f} kg ---\n"
        return reporte

# farm_management_system/main.py



        