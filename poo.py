class CuentaBancaria:
    """Representa una cuenta bancaria."""

    def __init__(self, nombre, saldo):
        """Inicializa la cuenta bancaria."""
        self.nombre = nombre
        self.saldo = saldo

    def depositar(self, cantidad):
        """Deposita una cantidad en la cuenta."""
        self.saldo += cantidad

    def retirar(self, cantidad):
        """Retira una cantidad de la cuenta."""
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad

    def __str__(self):
        """Devuelve una cadena con la información de la cuenta."""
        return f"Cuenta bancaria de {self.nombre} con saldo de {self.saldo}"

cuenta = CuentaBancaria("Juan Pérez", 1000)

# Depositamos 500 euros
cuenta.depositar(500)

# Imprimimos la información de la cuenta
print(cuenta)
