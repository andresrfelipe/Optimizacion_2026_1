import numpy as np
from scipy.integrate import solve_ivp


def dI_dt(t, I, beta, gamma):
    return beta * (10000 - I[0]) * I[0] - gamma * I[0]


def resolver_ejercicio_3(beta=0.00003, gamma=0.1, I0=50.0, dias=160):
    # Equilibrios por dI/dt = 0
    I_eq_1 = 0.0
    I_eq_2 = 10000.0 - gamma / beta

    t_span = (0.0, float(dias))
    t_eval = np.linspace(t_span[0], t_span[1], 400)

    sol = solve_ivp(
        fun=lambda t, y: dI_dt(t, y, beta, gamma),
        t_span=t_span,
        y0=[I0],
        t_eval=t_eval,
        method="RK45",
    )

    print("=== Ejercicio 3 ===")
    print(f"Equilibrio 1: I* = {I_eq_1:.4f}")
    print(f"Equilibrio 2: I* = {I_eq_2:.4f}")
    print(f"I(0) = {I0:.4f}")
    print(f"I({dias}) aprox = {sol.y[0, -1]:.4f}")


if __name__ == "__main__":
    resolver_ejercicio_3()
