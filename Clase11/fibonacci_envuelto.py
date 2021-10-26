def fibonacci(n):
    """
    Toma un entero positivo n y
    devuelve el n-ésimo número de Fibonacci
    donde F(0) = 0 y F(1) = 1.
    """
    def fibonacci_aux(n, dict_fibo):
        """
        Calcula el n-ésimo número de Fibonacci de forma recursiva
        utilizando un diccionario para almacenar los valores ya computados.
        dict_fibo es un diccionario que guarda en la clave 'k' el valor de F(k)
        """
        if n in dict_fibo.keys():
            F = dict_fibo[n]
        else:
            if n == 0:
                F = 0
            elif n == 1:
                F = 1
            else:
                F = fibonacci_aux(n - 1, dict_fibo) + \
                    fibonacci_aux(n - 2, dict_fibo)
            dict_fibo[n] = F
        return F
    dic_fibo = {0: 0, 1: 1}
    print(dic_fibo)
    F, dic_fibo = fibonacci_aux(n, dic_fibo)
    return F


print(fibonacci(10))
