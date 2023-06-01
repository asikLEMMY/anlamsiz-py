import random


class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def sword_attack(self, target):
        damage = random.randint(self.strength // 2, self.strength)
        print(f"{self.name} kılıç hareketiyle {target.name}'e saldırıyor! Hasar: {damage}")
        target.defend(self, damage)

    def special_attack(self, target):
        damage = random.randint(self.strength, self.strength * 2)
        print(f"{self.name} özel bir saldırı gerçekleştiriyor! Hasar: {damage}")
        target.defend(self, damage)

    def attack(self, target):
        print(f"{self.name} {target.name}'e saldırıyor!")
        attack_type = input("Saldırı türünü seçin (1. Kılıç Hareketi, 2. Özel Saldırı): ")
        if attack_type == "1":
            self.sword_attack(target)
        elif attack_type == "2":
            self.special_attack(target)
        else:
            print("Geçersiz saldırı türü!")

    def defend(self, attacker, damage):
        print(f"{self.name} {attacker.name}'den gelen saldırıyı savunuyor!")
        self.health -= damage
        print(f"{self.name}'in sağlığı {self.health} olarak güncellendi.")
        self.draw_health_bar()

    def draw_health_bar(self):
        bar_length = 20
        filled_length = int((self.health / 100) * bar_length)
        bar = "|" * filled_length + " " * (bar_length - filled_length)
        print(f"{self.name} - [{bar}]")


class Enemy(Character):
    def __init__(self, name, health, strength):
        super().__init__(name, health, strength)

    def attack(self, target):
        print(f"{self.name} {target.name}'e saldırıyor!")
        target.defend(self, self.strength)


def create_character():
    name = input("Karakter adını girin: ")
    health = int(input("Sağlık puanını girin: "))
    strength = int(input("Gücünü girin: "))

    character = Character(name, health, strength)
    return character


def main():
    print("Orta Çağ Karakter Oluşturma Oyununa Hoş Geldiniz!")
    character = create_character()

    print(f"\nKarakter oluşturuldu: {character.name} (Sağlık: {character.health}, Güç: {character.strength})")

    enemy = Enemy("Düşman", random.randint(30, 50), random.randint(5, 15))
    print(f"Düşman yaratıldı: {enemy.name} (Sağlık: {enemy.health}, Güç: {enemy.strength})")

    while True:
        print("\n-- Seçenekler --")
        print("1. Düşmana saldır")
        print("2. Oyundan çık")

        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            character.attack(enemy)
            if enemy.health <= 0:
                print(f"{enemy.name} öldü. Oyunu kazandınız!")
                break
            enemy.attack(character)
            if character.health <= 0:
                print(f"{character.name} öldü. Oyunu kaybettiniz!")
                break
        elif choice == "2":
            print("Oyundan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")


if __name__ == "__main__":
    main()
