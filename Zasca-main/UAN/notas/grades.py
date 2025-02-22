def show_menu_header():
    print(r"""

                                 _           
                    | |          
  __ _ _ __ __ _  __| | ___  ___ 
 / _` | '__/ _` |/ _` |/ _ \/ __|
| (_| | | | (_| | (_| |  __/\__ \
 \__, |_|  \__,_|\__,_|\___||___/
  __/ |                          
 |___/                                         
                
          """)

    
def show_menu_body():
    print("""
    --------------------------------------------------------------
          1. Ver estudiantes y sus notas
          2. Agregar estudiante
          3. Añadir notas a estudiante
          4. Calcular promedio de estudiante
          5. Calcular promedio general
          0. Salir
    """)


def show_menu():
    show_menu_header()
    show_menu_body()


def menu_controller(students: dict):
    user_input: int = int(input("> "))
    if user_input == 1:
        show_students_and_grades(students)
    elif user_input == 2:
        add_student(students)
    elif user_input == 3:
        add_student_grades(students)
    elif user_input == 4:
        calculate_student_average(students)
    elif user_input == 5:
        calculate_general_average()
    elif user_input == 0:
        return True


def show_students_and_grades(students: dict):
    if students:
        for name, grades in students.items():
            average = sum(grades) / len(grades) if grades else 0
            print(f"{name}: Notas: {grades} | Promedio: {average:.2f}")
    else:
        print("No hay estudiantes registrados.")


def add_student(students: dict):
    name = input("Nombre del estudiante > ")
    if name not in students:
        students[name] = []
        print(f"Estudiante {name} añadido.")
    else:
        print("El estudiante ya existe.")


def add_student_grades(students: dict):
    name = input("Nombre del estudiante > ")
    if name not in students:
        print("Estudiante no encontrado.")
        return
    grade = float(input("Nota > "))
    students[name].append(grade)
    print(f"Nota {grade} añadida a {name}.")


def calculate_student_average(students: dict):
    name = input("Nombre del estudiante > ")
    if name not in students:
        print("Estudiante no encontrado.")
        return
    if students[name]:
        average = sum(students[name]) / len(students[name])
        print(f"Promedio de {name}: {average:.2f}")
    else:
        print("No hay notas para calcular el promedio.")


def calculate_general_average():
    print("Ingrese las notas separadas por espacio.")
    try:
        grades = list(map(float, input("Notas > ").strip().split()))
        if grades:
            average = sum(grades) / len(grades)
            print(f"Promedio general: {average:.2f}")
        else:
            print("No se ingresaron notas.")
    except ValueError:
        print("Entrada inválida. Asegúrese de ingresar solo números.")


def main():
    students = {}
    exit_program: bool = False
    while not exit_program:
        show_menu()
        exit_program = menu_controller(students)


if __name__ == '__main__':
    main()
