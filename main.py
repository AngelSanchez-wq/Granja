from granja import Granja
from cultivo import Cultivo
from animal import Animal

def main():
    """
    Función principal para demostrar el uso del sistema de gestión de la granja.
    """
    print("Iniciando el sistema de gestión de la granja 'La Rastrojera Rebelde'...\n")

    # Crear una instancia de la granja
    mi_granja = Granja("La Rastrojera Rebelde")

    # --- Gestión de Cultivos ---
    print("--- Gestión de Cultivos ---")
    # Agregar cultivos
    cultivo1 = Cultivo("Maíz", 10.5, 5000.0) # 10.5 hectáreas, 5000 kg/hectárea
    mi_granja.agregar_cultivo(cultivo1)

    cultivo2 = Cultivo("Frijol", 5.0, 2500.0) # 5.0 hectáreas, 2500 kg/hectárea
    mi_granja.agregar_cultivo(cultivo2)

    # Consultar cultivos
    print("\nCultivos actuales:")
    for c in mi_granja.consultar_cultivos():
        print(f"  - {c.get_nombre()}: Área={c.get_area_cultivo()} ha, Rendimiento={c.get_rendimiento()} kg/ha")

    # Editar un cultivo
    mi_granja.editar_cultivo("Maíz", 12.0, 5200.0) # Editar área y rendimiento del Maíz

    # Calcular producción total de cultivos
    print(f"\nProducción total de cultivos: {mi_granja.calcular_produccion_total_cultivos():.2f} kg")

    # Eliminar un cultivo
    mi_granja.eliminar_cultivo("Frijol")

    print("\nCultivos después de eliminar Frijol:")
    for c in mi_granja.consultar_cultivos():
        print(f"  - {c.get_nombre()}: Área={c.get_area_cultivo()} ha, Rendimiento={c.get_rendimiento()} kg/ha")


    # --- Gestión de Ganado ---
    print("\n--- Gestión de Ganado ---")
    # Agregar animales
    animal1 = Animal("Vaca Lola", "Bovino", "Holstein", 36, 600.0) # 36 meses, 600 kg
    mi_granja.agregar_animal(animal1)

    animal2 = Animal("Cerdo Puerquito", "Porcino", "Duroc", 12, 120.0) # 12 meses, 120 kg
    mi_granja.agregar_animal(animal2)

    # Consultar animales
    print("\nAnimales actuales:")
    for a in mi_granja.consultar_animales():
        print(f"  - {a.get_nombre()}: Especie={a.get_especie()}, Raza={a.get_raza()}, Edad={a.get_edad()} meses, Peso={a.get_peso()} kg")

    # Editar un animal
    mi_granja.editar_animal("Vaca Lola", "Bovino", "Angus", 40, 650.0) # Editar raza, edad y peso de Vaca Lola

    # Calcular producción total de ganado
    print(f"\nProducción total de ganado: {mi_granja.calcular_produccion_total_animales():.2f} kg")

    # Eliminar un animal
    mi_granja.eliminar_animal("Cerdo Puerquito")

    print("\nAnimales después de eliminar Cerdo Puerquito:")
    for a in mi_granja.consultar_animales():
        print(f"  - {a.get_nombre()}: Especie={a.get_especie()}, Raza={a.get_raza()}, Edad={a.get_edad()} meses, Peso={a.get_peso()} kg")


    # --- Reporte General de la Granja ---
    print("\n--- Reporte General de la Granja ---")
    reporte_final = mi_granja.generar_reporte_produccion()
    print(reporte_final)

    print("Demostración del sistema finalizada.")

if __name__ == "__main__":
    main()