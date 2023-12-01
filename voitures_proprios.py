from vehicules import all_vehicules

class voitures(all_vehicules):
    def __init__(self, nom, proprio, année, etat):
        super().__init__(nom, proprio, année, etat, "voiture")
        