def calcular_precio_maquinaria():
    """
    Script para calcular el precio de venta sugerido y la ganancia bruta
    para maquinaria de artes gráficas e impresoras industriales.

    Args:
        None

    Returns:
        None
    """
    print("--- Calculadora de Costos y Precio de Venta (Maquinaria Industrial) ---")

    try:
        # Solicitud de datos al usuario
        costo_base = float(input("Ingrese el costo base del equipo (valor factura): "))
        gastos_importacion = float(input("Ingrese los gastos de importación (aranceles, fletes, etc.): "))
        margen_deseado_pct = float(input("Ingrese el porcentaje de margen de utilidad deseado (ej. 25): "))

        # Cálculo del costo total de adquisición
        costo_total = costo_base + gastos_importacion

        # Validación para evitar división por cero o márgenes imposibles
        if margen_deseado_pct >= 100:
            print("Error: El margen de utilidad debe ser menor al 100%.")
            return

        # Cálculo del Precio de Venta Sugerido
        # Se utiliza la fórmula de margen sobre precio de venta (estándar contable):
        # Precio = Costo / (1 - Margen)
        margen_decimal = margen_deseado_pct / 100
        precio_venta = costo_total / (1 - margen_decimal)

        # Cálculo de la ganancia bruta en valor monetario
        ganancia_bruta = precio_venta - costo_total

        # Resultados
        print("\n" + "="*45)
        print("          RESUMEN DE COTIZACIÓN")
        print("="*45)
        print(f"{'Costo Base del Equipo:':<30} ${costo_base:>12,.2f}")
        print(f"{'Gastos de Importación:':<30} ${gastos_importacion:>12,.2f}")
        print(f"{'-'*45}")
        print(f"{'COSTO TOTAL DE ADQUISICIÓN:':<30} ${costo_total:>12,.2f}")
        print(f"{'-'*45}")
        print(f"{'PRECIO DE VENTA SUGERIDO:':<30} ${precio_venta:>12,.2f}")
        print(f"{'Ganancia Bruta Estimada:':<30} ${ganancia_bruta:>12,.2f}")
        print(f"{'Margen Aplicado:':<30} {margen_deseado_pct:>12.2f}%")
        print("="*45)

    except ValueError:
        print("Error: Por favor, ingrese únicamente valores numéricos válidos.")