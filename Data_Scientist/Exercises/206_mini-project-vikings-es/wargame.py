
# from vikingsClasses import Viking, Saxon, War
# import random


# soldier_names = ["albert","andres","archie","dani", "david","gerard","german","graham","imanol","laura"]


# #Create 5 Vikings
# for i in range(0,5):
#     if i:
#         War.addViking(Viking(soldier_names[random.randint(0,9)],100,random.randint(0,100)))

# #Create 5 Saxons
# for i in range(0,5):
#     if i:
#         War.addSaxon(Saxon(100,random.randint(0,100)))
    
# round = 0
# while War.showStatus() == "Vikings and Saxons are still in the thick of battle.":
#     War.vikingAttack()
#     War.saxonAttack()
#     print(f"round: {round} // Viking army: {len(War.vikingArmy)} warriors",f"and Saxon army: {len(War.saxonArmy)} warriors")
#     print(War.showStatus())
#     round += 1

from vikingsClasses import Viking, Saxon, War
import random

soldier_names = ["albert", "andres", "archie", "dani", "david", 
                 "gerard", "german", "graham", "imanol", "laura"]

# Crear una instancia de la guerra
my_war = War()

# Crear 5 Vikingos
for _ in range(5):
    name = random.choice(soldier_names)
    strength = random.randint(50, 100)
    my_war.addViking(Viking(name, 100, strength))

# Crear 5 Sajones
for _ in range(5):
    strength = random.randint(40, 90)
    my_war.addSaxon(Saxon(100, strength))

round_num = 0
status = my_war.showStatus()

print("¡COMIENZA LA BATALLA!")
print(f"Vikingos: {len(my_war.vikingArmy)} | Sajones: {len(my_war.saxonArmy)}")
print("=" * 50)

while status == "Vikings and Saxons are still in the thick of battle.":
    round_num += 1
    print(f"\nRONDA {round_num}")
    
    # Ataque vikingo solo si hay sajones
    if my_war.saxonArmy:
        vk_result = my_war.vikingAttack()
        print(f"⚔️ Vikingo ataca: {vk_result}")
    else:
        print("⚔️ Vikingos no pueden atacar: ¡No quedan sajones!")
    
    # Verificar estado después del ataque vikingo
    status = my_war.showStatus()
    if status != "Vikings and Saxons are still in the thick of battle.":
        break
    
    # Ataque sajón solo si hay vikingos
    if my_war.vikingArmy:
        sx_result = my_war.saxonAttack()
        print(f"🛡 Sajón contraataca: {sx_result}")
    else:
        print("🛡 Sajones no pueden atacar: ¡No quedan vikingos!")
    
    # Estado actual
    print(f"\nVikingos restantes: {len(my_war.vikingArmy)}")
    print(f"Sajones restantes: {len(my_war.saxonArmy)}")
    
    # Verificar estado de la guerra
    status = my_war.showStatus()

# Resultado final
print("\n" + "=" * 50)
print("🔥 BATALLA FINALIZADA 🔥")
print(status)
print(f"Duración: {round_num} rondas")
print(f"Vikingos sobrevivientes: {len(my_war.vikingArmy)}")
print(f"Sajones sobrevivientes: {len(my_war.saxonArmy)}")

# Mostrar nombres de vikingos sobrevivientes si hay alguno
if my_war.vikingArmy:
    print("\nVikingos sobrevivientes:")
    for viking in my_war.vikingArmy:
        print(f"- {viking.name} (Salud: {viking.health}, Fuerza: {viking.strength})")