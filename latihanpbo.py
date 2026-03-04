
#LATIHAN 1

class HeroLatihan1:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")

print("HASIL LATIHAN 1:")
hero1 = HeroLatihan1("Layla", 100, 15)
hero1.info()
hero1.hp = 500
print(f"Update HP Hero 1 (Manual): {hero1.hp}")

#LATIHAN 2

class HeroLatihan2:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")

print("\n----------------------------")
print("HASIL LATIHAN 2:")
h1 = HeroLatihan2("Layla", 100, 15)
h2 = HeroLatihan2("Zilong", 120, 20)
h1.serang(h2)
h2.serang(h1)

#LATIHAN 3

class HeroLatihan3:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def diserang(self, damage):
        self.hp -= damage

class Mage(HeroLatihan3):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)
        self.mana = mana

    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")

    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)
        else:
            print("Mana habis!")

print("\n----------------------------")
print("HASIL LATIHAN 3:")
eudora = Mage("Eudora", 80, 30, 100)
balmond = HeroLatihan3("Balmond", 200, 10)
eudora.info()
eudora.skill_fireball(balmond)
print(f"HP Balmond sisa: {balmond.hp}")

#LATIHAN 4

class Hero:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        # Enkapsulasi: HP bersifat Private
        self.__hp = hp_awal

    def get_hp(self):
        return self.__hp

    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0 
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    def diserang(self, damage):
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")

# -- Eksekusi dan Output Terstruktur --
hero1 = Hero("Layla", 100)

print("\n----------------------------")
print("HASIL LATIHAN 4 :")
hero1.set_hp(-50) 
print(f"HP setelah set_hp(-50): {hero1.get_hp()}")
hero1.set_hp(9999)
print(f"HP setelah set_hp(9999): {hero1.get_hp()}")
print(f"Mencoba akses paksa (Name Mangling): {hero1._Hero__hp}")

#LATIHAN 5

from abc import ABC, abstractmethod

class GameUnit(ABC):
    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass

class HeroKonkret(GameUnit):
    def __init__(self, nama):
        self.nama = nama
    
    def serang(self, target):
        print(f"{self.nama} menebas {target}!")

    def info(self):
        print(f"Unit: {self.nama}")

print("\n----------------------------")
print("HASIL LATIHAN 5:")
hero_abc = HeroKonkret("Alucard")
hero_abc.info()
hero_abc.serang("Monster")

#LATIHAN 6

class HeroBase:
    def __init__(self, nama):
        self.nama = nama
    def aksi(self):
        pass

class MagePoly(HeroBase):
    def aksi(self):
        print(f"{self.nama} mengeluarkan Sihir!")

class ArcherPoly(HeroBase):
    def aksi(self):
        print(f"{self.nama} melepaskan Panah!")

class HealerPoly(HeroBase):
    def aksi(self):
        print(f"{self.nama} memberikan Healing!")

print("\n----------------------------")
print("HASIL LATIHAN 6:")
pasukan = [MagePoly("Gord"), ArcherPoly("Miya"), HealerPoly("Estes")]

for p in pasukan:
    p.aksi()

print("\n----------------------------")
