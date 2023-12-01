class all_vehicules:

    def __init__ (self, nom, proprio, année, etat, type_vehicule):
        self.type_vehicule = type_vehicule
        self.nom = nom
        self.année = année
        self.etat = "éteinte"
        self.proprio = proprio
        self.vitesse = 0

    def get_nom(self):
        return self.nom
    
    def get_proprio(self):
        return self.proprio
    
    def get_année(self):
        return self.année
    
    def get_etat(self):
        return self.etat
    
    def get_type_vehicule(self):
        return self.type_vehicule
    

    def set_nom(self, nom):
        self.nom = nom

    def set_proprio(self, proprio):
        if proprio == "Yanis":
            self.proprio = "Yanis"
        else:
            self.proprio = proprio

    def set_année(self, année):
        self.année = année

    def set_etat(self, etat):
        self.etat = etat

    def set_type_vehicule(self, type_vehicule):
        self.type_vehicule = type_vehicule

    def __str__(self):
        return f"La {self.type_vehicule} de {self.proprio} est une {self.nom} de {self.année} et elle est {self.etat}"
    
    def démarrer(self):
        if self.etat == "démarrée":
            return f"la {self.type_vehicule} de {self.proprio} est déjà démarrée"
        else:
            self.etat = "démarrée"
            return f"la {self.type_vehicule} de {self.proprio} démarre"
        
    def eteindre(self):
        if self.etat == "éteinte":
            return f"la {self.type_vehicule} de {self.proprio} est déjà eteinte"
        else:
            self.etat = "éteinte"
            return f"la {self.type_vehicule} de {self.proprio} s'est eteinte"
        
    def accélérer(self, vitesse):
        self.vitesse += vitesse
        return f"la {self.type_vehicule} de {self.proprio} accélère et passe de {self.vitesse - vitesse} km/h à {self.vitesse} km/h"
    
    def freiner(self, vitesse):
        self.vitesse -= vitesse
        return f"la {self.type_vehicule} de {self.proprio} freine et passe de {self.vitesse + vitesse} km/h à {self.vitesse} km/h"