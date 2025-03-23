#creacion de la clase 
class TarjetaCredito:
    def __init__(self, numero_tarjeta, saldo_pendiente):
        if not self.validar_tarjeta(numero_tarjeta):
            raise ValueError("Número de tarjeta inválido")
        self.numero_tarjeta = numero_tarjeta
        self.saldo_pendiente = saldo_pendiente
    
    @staticmethod
    def validar_tarjeta(numero):
        """ Valida el número de tarjeta utilizando el algoritmo de Luhn """
        numero = str(numero)[::-1]  # Invertir el número para aplicar Luhn
        suma = 0
        for i, digito in enumerate(numero):
            n = int(digito)
            if i % 2 == 1:  # Duplicar cada segundo dígito
                n *= 2
                if n > 9:
                    n -= 9  # Restar 9 si el resultado es mayor que 9
            suma += n
        return suma % 10 == 0
    
    def consultar_saldo_pendiente(self):
        """ Retorna el saldo pendiente de la tarjeta """
        return self.saldo_pendiente
    
    def pagar(self, cantidad):
        """ Reduce el saldo pendiente si la cantidad a pagar es válida """
        if cantidad <= 0:
            raise ValueError("La cantidad a pagar debe ser mayor que cero")
        if cantidad > self.saldo_pendiente:
            raise ValueError("La cantidad a pagar no puede ser mayor que el saldo pendiente")
        self.saldo_pendiente -= cantidad
        return self.saldo_pendiente

class CuentaBancaria:
    def __init__(self, titular, saldo, tarjeta):
        if not TarjetaCredito.validar_tarjeta(tarjeta.numero_tarjeta):
            raise ValueError("Número de tarjeta inválido")
        self.__titular = titular
        self.__saldo = saldo
        self.tarjeta = tarjeta

    def depositar(self, cantidad):
        if not TarjetaCredito.validar_tarjeta(self.tarjeta.numero_tarjeta):
            raise ValueError("Número de tarjeta inválido")
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            raise ValueError("La cantidad a depositar debe ser mayor que cero")

    def retirar(self, cantidad):
        if not TarjetaCredito.validar_tarjeta(self.tarjeta.numero_tarjeta):
            raise ValueError("Número de tarjeta inválido")
        if cantidad > self.__saldo:
            raise ValueError("Saldo insuficiente")
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor que cero")
        self.__saldo -= cantidad
        return self.__saldo

    def consultar_saldo(self):
        return self.__saldo

    def consultar_titular(self):
        return self.__titular

    def realizar_pago_tarjeta(self, cantidad):
        if not TarjetaCredito.validar_tarjeta(self.tarjeta.numero_tarjeta):
            raise ValueError("Número de tarjeta inválido")
        if cantidad > self.__saldo:
            raise ValueError("Saldo insuficiente para pagar la tarjeta")
        self.__saldo -= cantidad
        self.tarjeta.pagar(cantidad)

# Ejemplo de Uso
try:
    tarjeta = TarjetaCredito("4539876234567891", 200)
    cuenta = CuentaBancaria("Juan Pérez", 1000, tarjeta)
    
    print("Saldo de la cuenta:", cuenta.consultar_saldo())
    print("Saldo pendiente de la tarjeta:", cuenta.tarjeta.consultar_saldo_pendiente())
    
    cuenta.depositar(500)
    print("Nuevo saldo tras depósito:", cuenta.consultar_saldo())
    
    cuenta.retirar(300)
    print("Nuevo saldo tras retiro:", cuenta.consultar_saldo())
    
    cuenta.realizar_pago_tarjeta(200)
    print("Nuevo saldo de la cuenta tras pago de tarjeta:", cuenta.consultar_saldo())
    print("Nuevo saldo pendiente de la tarjeta:", cuenta.tarjeta.consultar_saldo_pendiente())
    
except ValueError as e:
    print("Error:", e)

      
            