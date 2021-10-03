saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra = 1000

while saldo > 0:
    if(mes < 12):
        saldo = saldo * (1+tasa/12) - (pago_mensual + pago_extra)
        total_pagado += (pago_mensual + pago_extra)
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado += pago_mensual
    mes += 1

print(f"Total pagado, {round(total_pagado,2)} en {mes} meses")
