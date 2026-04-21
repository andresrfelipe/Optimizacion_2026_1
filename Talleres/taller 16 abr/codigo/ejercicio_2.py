def producir_semanas(S0=200.0, M0=80.0, N=2):
    S = [S0]
    M = [M0]

    for _ in range(N):
        s_sig = 0.6 * S[-1] + 0.2 * M[-1] + 40
        m_sig = 0.1 * S[-1] + 0.5 * M[-1] + 20
        S.append(s_sig)
        M.append(m_sig)

    return S, M


def resolver_ejercicio_2():
    S, M = producir_semanas(N=2)
    print("=== Ejercicio 2 ===")
    print(f"Semana 0: S={S[0]:.4f}, M={M[0]:.4f}")
    print(f"Semana 1: S={S[1]:.4f}, M={M[1]:.4f}")
    print(f"Semana 2: S={S[2]:.4f}, M={M[2]:.4f}")


if __name__ == "__main__":
    resolver_ejercicio_2()
