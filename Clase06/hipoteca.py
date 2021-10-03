saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    if(saldo < pago_mensual):
        # Si la ultima cuota es menor al pago mensual
        total_pagado += saldo
        saldo = 0
    else:
        if(mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin):
            # cuotas con pago mensual extra
            saldo = saldo * (1+tasa/12) - (pago_mensual + pago_extra)
            total_pagado += (pago_mensual + pago_extra)
        else:
            # cuotas con pago mensual
            saldo = saldo * (1+tasa/12) - pago_mensual
            total_pagado += pago_mensual
    mes += 1
    print(f"Mes:{mes} \tPagado:{round(total_pagado,2)} \tSaldo:{round(saldo,2)}")

print(f"\nTotal pagado: ${round(total_pagado,2)} en {mes} meses")