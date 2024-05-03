#Problema 2
from datetime import datetime

# Solicitar al usuario el año de nacimiento
nacimiento = int(input("Ingresa tu año de nacimiento: "))

# Calcular la edad actual
actual = datetime.now().year # faltan validaciones
edad_actual = actual - nacimiento

# Determinar la etapa de la vida
if edad_actual < 13:
    etapa_vida = "Infancia"
elif edad_actual < 20:
    etapa_vida = "Adolescencia"
elif edad_actual < 65:
    etapa_vida = "Adultez"
else:
    etapa_vida = "Tercera edad"

# Mostrar los resultados
print(f"Tu edad actual es: {edad_actual}")
print(f"Te encuentras en la etapa de la vida: {etapa_vida}")


#Problema 1

# Solicitar el precio del producto y el estado de miembro
price = float(input("Ingresa el precio del producto: "))
is_member = input("¿Eres miembro de la tienda? (s/n): ")

# Calcular el precio final
if is_member == "s" and price >= 50:
    discount = 0.15
elif is_member == "s":
    discount = 0.1
elif price >= 50:
    discount = 0.05
else:
    discount = 0

final_price = price * (1 - discount) #Explicar

# Mostrar el precio final
print(f"El precio final del producto es: ${final_price:.2f}") # es igual a round(final_price, 2) 