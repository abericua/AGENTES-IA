# ============================================================
# Generado por : gemma4:26b
# Revisado por : llama3:latest
# ============================================================

def calculate_price_sale() -> None:
    """
    Calculadora de precio de venta para maquinaria industrial.

    Pide al usuario los datos necesarios y calcula el precio de venta sugerido
    considerando el costo base, gastos de importación y margen deseado.
    """
    print("--- Calculadora de Precio de Venta: Maquinaria Industrial ---")

    try:
        # Solicitar datos al usuario
        cost_base = float(input("Ingrese el costo base del equipo: "))
        importation_costs = float(input("Ingrese los gastos de importación: "))
        desired_margin = float(input("Ingrese el porcentaje de margen deseado (ejemplo: 25): "))

        # Cálculos
        total_cost = cost_base + importation_costs
        margin_amount = total_cost * (desired_margin / 100)
        suggested_sales_price = total_cost + margin_amount

        # Mostrar resultados
        print("\n" + "="*40)
        print("RESUMEN DE COSTOS Y PRECIOS")
        print("="*40)
        print(f"Costo Total de Adquisición: ${total_cost:,.2f}")
        print(f"Monto de Ganancia (Margen): ${margin_amount:,.2f}")
        print(f"Precio de Venta Sugerido:   ${suggested_sales_price:,.2f}")
        print(f"Margen aplicado:            {desired_margin}%")
        print("="*40)

    except ValueError:
        print("\nError: Por favor, ingrese solo valores numéricos válidos (use punto para decimales).")
    except Exception as e:
        print(f"\nError inesperado: {str(e)}")

if __name__ == "__main__":
    calculate_price_sale()