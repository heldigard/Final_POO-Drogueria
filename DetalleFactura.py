from Medicamento import Medicamento


class DetalleFactura:
    def __init__(self, medicamento: Medicamento, cantidad=1):
        self.__medicamento: Medicamento = medicamento
        self.__cantidad = cantidad
        self.__subtotal = self.calcular_subtotal()
        self.__total = self.calcular_total()

    @property
    def medicamento(self):
        return self.__medicamento

    @property
    def cantidad(self):
        return self.__cantidad

    @property
    def subtotal(self):
        return self.__subtotal

    @property
    def total(self):
        return self.__total

    def calcular_total(self):
        print(f'Precio neto: {self.__medicamento.precio_neto}')
        print(f'Bruto: {self.__medicamento.precio_neto*(self.__medicamento.impuesto+1)}')
        print(f'Total: {self.__medicamento.precio_neto*(self.__medicamento.impuesto+1)*self.__cantidad}')
        return (self.__medicamento.precio_neto*(self.__medicamento.impuesto+1)) * self.__cantidad

    def calcular_subtotal(self):
        return self.__medicamento.precio_neto * self.__cantidad

    def __str__(self):
        return f"{self.medicamento.nombre_comercial:<20}\t\
        {self.medicamento.peso:<8}\t\
        {self.medicamento.precio_neto:<10}\t\
        {self.cantidad:<8}\t\
        {self.subtotal:<2}\t\
        {self.total:<2}\n"
