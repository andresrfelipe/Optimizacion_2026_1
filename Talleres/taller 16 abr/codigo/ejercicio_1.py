import pulp as pl


def resolver_ejercicio_1():
    # Modelo de maximizacion
    modelo = pl.LpProblem("MezclaFertilizantes", pl.LpMaximize)

    # Variables de decision
    x1 = pl.LpVariable("x1_F1", lowBound=0)
    x2 = pl.LpVariable("x2_F2", lowBound=0)

    # Funcion objetivo
    modelo += 180 * x1 + 220 * x2, "GananciaTotal"

    # Restricciones
    modelo += 3 * x1 + 4 * x2 <= 120, "Compuesto_A"
    modelo += 2 * x1 + 1 * x2 <= 80, "Compuesto_B"
    modelo += 5 * x1 + 3 * x2 <= 150, "Compuesto_C"

    # Resolver
    modelo.solve(pl.PULP_CBC_CMD(msg=False))

    print("=== Ejercicio 1 ===")
    print("Estado:", pl.LpStatus[modelo.status])
    print("x1 (F1) =", x1.value())
    print("x2 (F2) =", x2.value())
    print("Ganancia maxima =", pl.value(modelo.objective))


if __name__ == "__main__":
    resolver_ejercicio_1()
