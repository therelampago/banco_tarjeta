# banco_tarjeta

Sistema de Gestión de Cuentas Bancarias y Tarjetas de Crédito

Descripción:
Este sistema simula la gestión de cuentas bancarias y tarjetas de crédito, permitiendo realizar
operaciones como depósitos, retiros y pagos de tarjetas de forma segura y válida.

Clases y Métodos:
- TarjetaCredito:
  - `validar_tarjeta(numero)`: Método estático que valida si un número de tarjeta es válido utilizando el algoritmo de Luhn.
  - `consultar_saldo_pendiente()`: Retorna el saldo pendiente de la tarjeta.
  - `pagar(cantidad)`: Reduce el saldo pendiente de la tarjeta si la cantidad es válida.

- CuentaBancaria:
  - `depositar(cantidad)`: Deposita dinero en la cuenta si la tarjeta es válida.
  - `retirar(cantidad)`: Retira dinero si hay suficiente saldo y la tarjeta es válida.
  - `consultar_saldo()`: Retorna el saldo actual de la cuenta.
  - `consultar_titular()`: Retorna el nombre del titular de la cuenta.
  - `realizar_pago_tarjeta(cantidad)`: Transfiere dinero desde la cuenta al saldo pendiente de la tarjeta.

Validación:
Antes de realizar cualquier operación, se valida el número de tarjeta con el algoritmo de Luhn.
Si no es válido, la operación se cancela y se muestra un error.

Ejemplo de Uso:
- Crear una cuenta bancaria con un titular, número de tarjeta válido y saldo inicial.
- Realizar operaciones como consultas, depósitos, retiros y pagos de tarjeta.
- Manejo de errores para saldo insuficiente o número de tarjeta inválido.
