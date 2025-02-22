def show_menu_header():
    print(r"""
           _____                     _             _        
          |_   _|                   | |           (_)       
            | | _ ____   _____ _ __ | |_ __ _ _ __ _  ___   
            | || '_ \ \ / / _ \ '_ \| __/ _` | '__| |/ _ \  
           _| || | | \ V /  __/ | | | || (_| | |  | | (_) | 
           \___/_| |_|\_/ \___|_| |_|\__\__,_|_|  |_|\___/  
          """)
    
def show_menu_body():
    print("""
    --------------------------------------------------------------
          1. Ver automóviles
          2. Agregar automóvil
          3. Buscar automóviles
          4. Actualizar automóvil
          5. Borrar automóviles
          6. Filtrar
          0. Salir
    """)

def show_menu():
    show_menu_header()
    show_menu_body()

def menu_controller(inventory: list) -> bool:
    try:
        user_input = int(input("> "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return False

    if user_input == 1:
        show_inventory(inventory)
    elif user_input == 2:
        add_car(inventory)
    elif user_input == 3:
        search_car(inventory)
    elif user_input == 4:
        update_car(inventory)
    elif user_input == 5:
        delete_car(inventory)
    elif user_input == 6:
        filter_inventory(inventory)
    elif user_input == 0:
        return True
    else:
        print("Opción inválida.")
    return False


def show_car(car: dict):
    print(f""" 
            --------------------
            Placa: {car["plate"]},
            Color: {car["color"]},
            Marca: {car["brand"]},
            Km: {car["km"]}
            --------------------""")
    
def show_inventory(inventory: list):
    if inventory:
        for car in inventory:
           show_car(car)
    else:
        print("Inventario vacío")


def add_car(inventory: list):
    print("Ingrese los datos...")
    plate = input("Placa> ")
    color = input("Color> ")
    brand = input("Marca> ")
    try:
        km = int(input("Kilómetros> "))
    except ValueError:
        print("Kilómetros no válidos. Se asigna 0 por defecto.")
        km = 0
    inventory.append({
        "plate": plate,
        "color": color,
        "brand": brand,
        "km": km
    })


def search_car(inventory: list):
    to_search = input("Placa> ")
    for car in inventory:
        if car["plate"] == to_search:
            show_car(car)
            return car
    print("Auto no encontrado en base")
    return None


def delete_car(inventory: list):
    car = search_car(inventory)
    if car:
        inventory.remove(car)
        print("Auto eliminado.")
    else:
        print("No se pudo eliminar el auto.")


def update_car(inventory: list):
    car = search_car(inventory)
    if car:
        print("Ingrese los nuevos datos (deje vacío para mantener el valor actual):")
        car["plate"] = input(f"Placa ({car['plate']}): ") or car["plate"]
        car["color"] = input(f"Color ({car['color']}): ") or car["color"]
        car["brand"] = input(f"Marca ({car['brand']}): ") or car["brand"]
        try:
            car["km"] = int(input(f"Kilómetros ({car['km']}): ") or car["km"])
        except ValueError:
            print("Kilómetros no actualizados, entrada inválida.")


def filter_inventory(inventory: list):
    if not inventory:
        print("Inventario vacío.")
        return
    
    filter_options = {
        "1": "plate",
        "2": "color",
        "3": "brand",
        "4": "km"
    }

    print("Seleccione el campo por el cual filtrar:")
    for key, value in filter_options.items():
        print(f"{key}. {value}")

    field = input("> ")
    if field not in filter_options:
        print("Opción inválida.")
        return

    value = input(f"Ingrese el valor para {filter_options[field]}: ")

    filtered_cars = [
        car for car in inventory if str(car[filter_options[field]]) == value
    ]

    if filtered_cars:
        for car in filtered_cars:
            show_car(car)
    else:
        print("No se encontraron autos con ese criterio.")


def main():
    inventory = []
    exit_program = False
    while not exit_program:
        show_menu()
        exit_program = menu_controller(inventory)


if __name__ == '__main__':
    main()
