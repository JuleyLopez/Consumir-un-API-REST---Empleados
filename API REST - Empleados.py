import requests

url = 'https://dummy.restapiexample.com/api/v1/employees'
response = requests.get(url)

if response.status_code == 200:
    empleados = response.json().get('data', [])

    if empleados:
        # Obtener cantidad de empleados
        cantidad_empleados = len(empleados)

        # Obtener edades y salarios
        edades = [empleado.get('employee_age', 0) for empleado in empleados]
        salarios = [empleado.get('employee_salary', 0) for empleado in empleados]

        # Calcular promedio de edad sin decimales
        promedio_edad = int(sum(edades) / len(edades))

        # Calcular promedio de salario
        promedio_salario = sum(salarios) / len(salarios)

        # Calcular salario mínimo y máximo
        salario_minimo = min(salarios)
        salario_maximo = max(salarios)

        # Obtener edad menor y mayor
        edad_menor = min(edades)
        edad_mayor = max(edades)

        # Mostrar resultados
        print(f'Cantidad de empleados: {cantidad_empleados}')
        print(f'Promedio de salario de los empleados: {promedio_salario:.2f}')
        print(f'Promedio de edad de los empleados: {promedio_edad}')
        print(f'Salario mínimo: {salario_minimo}')
        print(f'Salario máximo: {salario_maximo}')
        print(f'Edad menor: {edad_menor}')
        print(f'Edad mayor: {edad_mayor}')
    else:
        print('No se encontraron empleados en los datos.')
else:
    print(f'Error al obtener los datos. Código de estado: {response.status_code}')