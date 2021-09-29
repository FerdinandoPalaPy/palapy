class Cellulari:
    def __init__(self, marca, modello, sistema_operativo):
        self.marca = marca
        self.modello = modello
        self.sistema_operativo = sistema_operativo

    def scheda_tecnica(self):
        return f"Scheda tecnica:\n Marca: {self.marca}\n Modello: {self.modello}\n Sistema operativo: {self.sistema_operativo}"

cellulare_uno = Cellulari("Samsung", "Galaxy A50", "Android 11")
cellulare_due = Cellulari("Apple", "Iphone 12 Pro", "iOS 14")
cellulare_tre = Cellulari("Xiamoi", "Mi 11X", "Android 11")
cellulare_quattro = Cellulari("Huawei", "Nova 9", "HarmonyOS 2.0")

print(Cellulari.scheda_tecnica(cellulare_uno), "\n")
print(Cellulari.scheda_tecnica(cellulare_due), "\n")
print(Cellulari.scheda_tecnica(cellulare_tre), "\n")
print(Cellulari.scheda_tecnica(cellulare_quattro))
