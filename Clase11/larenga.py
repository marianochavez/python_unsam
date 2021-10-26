def pascal(n, k):
    """triangulo de Pascal, n filas, k columnas"""
    if k == 0 or k == n:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)
