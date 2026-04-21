def pesca_logistica(P0=400.0, r=0.4, K=1000.0, H=80.0, N=2):
    P = [P0]
    for _ in range(N):
        p_sig = P[-1] + r * P[-1] * (1 - P[-1] / K) - H
        P.append(p_sig)
    return P


def resolver_ejercicio_4():
    P = pesca_logistica(N=2)

    print("=== Ejercicio 4 ===")
    print(f"P0 = {P[0]:.4f}")
    print(f"P1 = {P[1]:.4f}")
    print(f"P2 = {P[2]:.4f}")
    print("Equilibrio discreto: resolver r*P*(1 - P/K) - H = 0")


if __name__ == "__main__":
    resolver_ejercicio_4()
