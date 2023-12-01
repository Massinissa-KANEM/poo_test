from vehicules import all_vehicules

class motos(all_vehicules):
    def __init__(self, nom, année, etat):
        super().__init__(nom, "Yanis", année, etat, "moto")