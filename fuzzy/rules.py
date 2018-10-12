import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# speed = ctrl.Antecedent(np.arange(0, 101, 1), 'speed_variations')
# attack = ctrl.Antecedent(np.arange(0, 101, 1), 'attack_variations')
ogre_team = ctrl.Antecedent(np.arange(0, 49, 1), 'ogre_team')
goblin_team = ctrl.Antecedent(np.arange(0, 25, 1), 'goblin_team')
troll_team = ctrl.Antecedent(np.arange(0, 81, 1), 'troll_team')
ogre_enemy_goblin = ctrl.Antecedent(np.arange(0, 49, 1), 'ogre_enemy_goblin')
goblin_enemy_ogre = ctrl.Antecedent(np.arange(0, 25, 1), 'goblin_enemy_ogre')
troll_enemy_goblin = ctrl.Antecedent(np.arange(0, 81, 1), 'troll_enemy_goblin')
ogre_enemy_troll = ctrl.Antecedent(np.arange(0, 49, 1), 'ogre_enemy_troll')
goblin_enemy_troll = ctrl.Antecedent(np.arange(0, 25, 1), 'goblin_enemy_troll')
troll_enemy_ogre = ctrl.Antecedent(np.arange(0, 81, 1), 'troll_enemy_ogre')


movement = ctrl.Consequent(np.arange(0, 101, 1), 'movement')

# speed['slow'] = fuzz.trapmf(speed.universe,[0, 10, 30, 40])
# speed['medium'] = fuzz.trapmf(speed.universe,[30, 40, 60, 70])
# speed['fast'] = fuzz.trapmf(speed.universe, [60,70,90,100])
#
# attack['low'] = fuzz.trapmf(attack.universe,[0,10, 30, 40])
# attack['medium'] = fuzz.trapmf(attack.universe,[30, 40, 60, 70])
# attack['high'] = fuzz.trapmf(attack.universe, [60,70,90,100])

goblin_team['one'] = fuzz.trapmf(goblin_team.universe,[0,0, 1, 2])
goblin_team['small'] = fuzz.trapmf(goblin_team.universe,[1, 1, 2, 6])
goblin_team['medium'] = fuzz.trapmf(goblin_team.universe,[4, 6, 10, 12])
goblin_team['large'] = fuzz.trapmf(goblin_team.universe,[10,12,24,24])

ogre_team['one'] = fuzz.trapmf(ogre_team.universe,[0,0, 1, 2])
ogre_team['small'] = fuzz.trapmf(ogre_team.universe,[1, 1, 2, 6])
ogre_team['medium'] = fuzz.trapmf(ogre_team.universe,[4, 6, 10, 12])
ogre_team['large'] = fuzz.trapmf(ogre_team.universe,[10,12,48,48])

troll_team['one'] = fuzz.trapmf(troll_team.universe,[0,0, 1, 2])
troll_team['small'] = fuzz.trapmf(troll_team.universe,[1, 1, 2, 6])
troll_team['medium'] = fuzz.trapmf(troll_team.universe,[4, 6, 10, 12])
troll_team['large'] = fuzz.trapmf(troll_team.universe,[10,12,80,80])

ogre_enemy_goblin['one'] = fuzz.trapmf(ogre_enemy_goblin.universe,[0,0, 1, 2])
ogre_enemy_goblin['small'] = fuzz.trapmf(ogre_enemy_goblin.universe,[1, 1, 3, 5])
ogre_enemy_goblin['medium'] = fuzz.trapmf(ogre_enemy_goblin.universe,[3, 5, 15, 20])
ogre_enemy_goblin['large'] = fuzz.trapmf(ogre_enemy_goblin.universe,[15,20,48,48])

ogre_enemy_troll['one'] = fuzz.trapmf(ogre_enemy_troll.universe,[0,0, 1, 2])
ogre_enemy_troll['small'] = fuzz.trapmf(ogre_enemy_troll.universe,[1, 1, 2, 4])
ogre_enemy_troll['medium'] = fuzz.trapmf(ogre_enemy_troll.universe,[2, 4, 10, 15])
ogre_enemy_troll['large'] = fuzz.trapmf(ogre_enemy_troll.universe,[10,15,48, 48])

goblin_enemy_ogre['one'] = fuzz.trapmf(goblin_enemy_ogre.universe,[0,0, 1, 2])
goblin_enemy_ogre['small'] = fuzz.trapmf(goblin_enemy_ogre.universe,[1, 1, 3, 5])
goblin_enemy_ogre['medium'] = fuzz.trapmf(goblin_enemy_ogre.universe,[3, 5, 10, 15])
goblin_enemy_ogre['large'] = fuzz.trapmf(goblin_enemy_ogre.universe,[10, 15, 24, 24])

goblin_enemy_troll['one'] = fuzz.trapmf(goblin_enemy_troll.universe,[0,0, 1, 2])
goblin_enemy_troll['small'] = fuzz.trapmf(goblin_enemy_troll.universe,[1, 1, 2, 5])
goblin_enemy_troll['medium'] = fuzz.trapmf(goblin_enemy_troll.universe,[2, 5, 10, 15])
goblin_enemy_troll['large'] = fuzz.trapmf(goblin_enemy_troll.universe,[10, 15, 24, 24])

troll_enemy_goblin['one'] = fuzz.trapmf(troll_enemy_goblin.universe,[0,0, 1, 2])
troll_enemy_goblin['small'] = fuzz.trapmf(troll_enemy_goblin.universe,[1, 1, 5, 10])
troll_enemy_goblin['medium'] = fuzz.trapmf(troll_enemy_goblin.universe,[5, 10, 20, 25])
troll_enemy_goblin['large'] = fuzz.trapmf(troll_enemy_goblin.universe,[20,25,80,80])

troll_enemy_ogre['one'] = fuzz.trapmf(troll_enemy_ogre.universe,[0,0, 1, 2])
troll_enemy_ogre['small'] = fuzz.trapmf(troll_enemy_ogre.universe,[1, 1, 2, 5])
troll_enemy_ogre['medium'] = fuzz.trapmf(troll_enemy_ogre.universe,[2, 5, 10, 15])
troll_enemy_ogre['large'] = fuzz.trapmf(troll_enemy_ogre.universe,[10,15,80,80])

movement['stay'] = fuzz.trapmf(movement.universe,[0,10, 30, 40])
movement['attack'] = fuzz.trapmf(movement.universe,[30, 40, 60, 70])
movement['move'] = fuzz.trapmf(movement.universe, [60,70,90,100])

# speed.view()
# attack.view()
ogre_team.view()
goblin_team.view()
troll_team.view()
ogre_enemy_goblin.view()
ogre_enemy_troll.view()
troll_enemy_ogre.view()
troll_enemy_goblin.view()
goblin_enemy_ogre.view()
goblin_enemy_troll.view()

#
# movement.view()

rule5 = ctrl.Rule(goblin_team['one'] & ogre_enemy_goblin['one'], movement['move'])
rule6 = ctrl.Rule(goblin_team['one'] & ogre_enemy_goblin['small'], movement['move'])
rule7 = ctrl.Rule(goblin_team['one'] & ogre_enemy_goblin['medium'], movement['move'])
rule8 = ctrl.Rule(goblin_team['one'] & ogre_enemy_goblin['large'], movement['move'])

rule9 = ctrl.Rule(goblin_team['small'] & ogre_enemy_goblin['one'], movement['stay'])
rule10 = ctrl.Rule(goblin_team['small'] & ogre_enemy_goblin['small'], movement['stay'])
rule11 = ctrl.Rule(goblin_team['small'] & ogre_enemy_goblin['medium'], movement['move'])
rule12 = ctrl.Rule(goblin_team['small'] & ogre_enemy_goblin['large'], movement['move'])

rule13 = ctrl.Rule(goblin_team['medium'] & ogre_enemy_goblin['one'], movement['attack'])
rule14 = ctrl.Rule(goblin_team['medium'] & ogre_enemy_goblin['small'], movement['stay'])
rule15 = ctrl.Rule(goblin_team['medium'] & ogre_enemy_goblin['medium'], movement['stay'])
rule16 = ctrl.Rule(goblin_team['medium'] & ogre_enemy_goblin['large'], movement['stay'])

rule17 = ctrl.Rule(goblin_team['large'] & ogre_enemy_goblin['one'], movement['attack'])
rule18 = ctrl.Rule(goblin_team['large'] & ogre_enemy_goblin['small'], movement['attack'])
rule19 = ctrl.Rule(goblin_team['large'] & ogre_enemy_goblin['medium'], movement['stay'])
rule20 = ctrl.Rule(goblin_team['large'] & ogre_enemy_goblin['large'], movement['stay'])

rule21 = ctrl.Rule(goblin_team['one'] & troll_enemy_goblin['one'], movement['move'])
rule22 = ctrl.Rule(goblin_team['one'] & troll_enemy_goblin['small'], movement['move'])
rule23 = ctrl.Rule(goblin_team['one'] & troll_enemy_goblin['medium'], movement['move'])
rule24 = ctrl.Rule(goblin_team['one'] & troll_enemy_goblin['large'], movement['move'])

rule25 = ctrl.Rule(goblin_team['small'] & troll_enemy_goblin['one'], movement['move'])
rule26 = ctrl.Rule(goblin_team['small'] & troll_enemy_goblin['small'], movement['stay'])
rule27 = ctrl.Rule(goblin_team['small'] & troll_enemy_goblin['medium'], movement['move'])
rule28 = ctrl.Rule(goblin_team['small'] & troll_enemy_goblin['large'], movement['move'])

rule29 = ctrl.Rule(goblin_team['medium'] & troll_enemy_goblin['one'], movement['stay'])
rule30 = ctrl.Rule(goblin_team['medium'] & troll_enemy_goblin['small'], movement['stay'])
rule31 = ctrl.Rule(goblin_team['medium'] & troll_enemy_goblin['medium'], movement['stay'])
rule32 = ctrl.Rule(goblin_team['medium'] & troll_enemy_goblin['large'], movement['move'])

rule33 = ctrl.Rule(goblin_team['large'] & troll_enemy_goblin['one'], movement['attack'])
rule34 = ctrl.Rule(goblin_team['large'] & troll_enemy_goblin['small'], movement['attack'])
rule35 = ctrl.Rule(goblin_team['large'] & troll_enemy_goblin['medium'], movement['stay'])
rule36 = ctrl.Rule(goblin_team['large'] & troll_enemy_goblin['large'], movement['stay'])

#########################################################################################

rule1 = ctrl.Rule(ogre_team['one'] & goblin_enemy_ogre['one'], movement['attack'])
rule2 = ctrl.Rule(ogre_team['one'] & goblin_enemy_ogre['small'], movement['attack'])
rule3 = ctrl.Rule(ogre_team['one'] & goblin_enemy_ogre['medium'], movement['stay'])
rule4 = ctrl.Rule(ogre_team['one'] & goblin_enemy_ogre['large'], movement['move'])

rule37 = ctrl.Rule(ogre_team['small'] & goblin_enemy_ogre['one'], movement['attack'])
rule38 = ctrl.Rule(ogre_team['small'] & goblin_enemy_ogre['small'], movement['attack'])
rule39 = ctrl.Rule(ogre_team['small'] & goblin_enemy_ogre['medium'], movement['attack'])
rule40 = ctrl.Rule(ogre_team['small'] & goblin_enemy_ogre['large'], movement['stay'])

rule41 = ctrl.Rule(ogre_team['medium'] & goblin_enemy_ogre['one'], movement['attack'])
rule42 = ctrl.Rule(ogre_team['medium'] & goblin_enemy_ogre['small'], movement['attack'])
rule43 = ctrl.Rule(ogre_team['medium'] & goblin_enemy_ogre['medium'], movement['attack'])
rule44 = ctrl.Rule(ogre_team['medium'] & goblin_enemy_ogre['large'], movement['attack'])

rule45 = ctrl.Rule(ogre_team['large'] & goblin_enemy_ogre['one'], movement['attack'])
rule46 = ctrl.Rule(ogre_team['large'] & goblin_enemy_ogre['small'], movement['attack'])
rule47 = ctrl.Rule(ogre_team['large'] & goblin_enemy_ogre['medium'], movement['attack'])
rule48 = ctrl.Rule(ogre_team['large'] & goblin_enemy_ogre['large'], movement['attack'])

rule49 = ctrl.Rule(ogre_team['one'] & troll_enemy_goblin['one'], movement['move'])
rule50 = ctrl.Rule(ogre_team['one'] & troll_enemy_goblin['small'], movement['move'])
rule51 = ctrl.Rule(ogre_team['one'] & troll_enemy_goblin['medium'], movement['move'])
rule52 = ctrl.Rule(ogre_team['one'] & troll_enemy_goblin['large'], movement['move'])

rule53 = ctrl.Rule(ogre_team['small'] & troll_enemy_goblin['one'], movement['attack'])
rule54 = ctrl.Rule(ogre_team['small'] & troll_enemy_goblin['small'], movement['stay'])
rule55 = ctrl.Rule(ogre_team['small'] & troll_enemy_goblin['medium'], movement['move'])
rule56 = ctrl.Rule(ogre_team['small'] & troll_enemy_goblin['large'], movement['move'])

rule57 = ctrl.Rule(ogre_team['medium'] & troll_enemy_goblin['one'], movement['attack'])
rule58 = ctrl.Rule(ogre_team['medium'] & troll_enemy_goblin['small'], movement['stay'])
rule59 = ctrl.Rule(ogre_team['medium'] & troll_enemy_goblin['medium'], movement['stay'])
rule60 = ctrl.Rule(ogre_team['medium'] & troll_enemy_goblin['large'], movement['stay'])

rule61 = ctrl.Rule(ogre_team['large'] & troll_enemy_goblin['one'], movement['attack'])
rule62 = ctrl.Rule(ogre_team['large'] & troll_enemy_goblin['small'], movement['attack'])
rule63 = ctrl.Rule(ogre_team['large'] & troll_enemy_goblin['medium'], movement['stay'])
rule64 = ctrl.Rule(ogre_team['large'] & troll_enemy_goblin['large'], movement['move'])

#########################################################################################

rule65 = ctrl.Rule(troll_team['one'] & goblin_enemy_ogre['one'], movement['attack'])
rule66 = ctrl.Rule(troll_team['one'] & goblin_enemy_ogre['small'], movement['attack'])
rule67 = ctrl.Rule(troll_team['one'] & goblin_enemy_ogre['medium'], movement['attack'])
rule68 = ctrl.Rule(troll_team['one'] & goblin_enemy_ogre['large'], movement['move'])

rule69 = ctrl.Rule(troll_team['small'] & goblin_enemy_ogre['one'], movement['attack'])
rule70 = ctrl.Rule(troll_team['small'] & goblin_enemy_ogre['small'], movement['attack'])
rule71 = ctrl.Rule(troll_team['small'] & goblin_enemy_ogre['medium'], movement['attack'])
rule72 = ctrl.Rule(troll_team['small'] & goblin_enemy_ogre['large'], movement['stay'])

rule73 = ctrl.Rule(troll_team['medium'] & goblin_enemy_ogre['one'], movement['attack'])
rule74 = ctrl.Rule(troll_team['medium'] & goblin_enemy_ogre['small'], movement['attack'])
rule75 = ctrl.Rule(troll_team['medium'] & goblin_enemy_ogre['medium'], movement['attack'])
rule76 = ctrl.Rule(troll_team['medium'] & goblin_enemy_ogre['large'], movement['attack'])

rule77 = ctrl.Rule(troll_team['large'] & goblin_enemy_ogre['one'], movement['attack'])
rule78 = ctrl.Rule(troll_team['large'] & goblin_enemy_ogre['small'], movement['attack'])
rule79 = ctrl.Rule(troll_team['large'] & goblin_enemy_ogre['medium'], movement['attack'])
rule80 = ctrl.Rule(troll_team['large'] & goblin_enemy_ogre['large'], movement['attack'])

rule81 = ctrl.Rule(troll_team['one'] & ogre_enemy_goblin['one'], movement['attack'])
rule82 = ctrl.Rule(troll_team['one'] & ogre_enemy_goblin['small'], movement['stay'])
rule83 = ctrl.Rule(troll_team['one'] & ogre_enemy_goblin['medium'], movement['move'])
rule84 = ctrl.Rule(troll_team['one'] & ogre_enemy_goblin['large'], movement['move'])

rule85 = ctrl.Rule(troll_team['small'] & ogre_enemy_goblin['one'], movement['attack'])
rule86 = ctrl.Rule(troll_team['small'] & ogre_enemy_goblin['small'], movement['attack'])
rule87 = ctrl.Rule(troll_team['small'] & ogre_enemy_goblin['medium'], movement['stay'])
rule88 = ctrl.Rule(troll_team['small'] & ogre_enemy_goblin['large'], movement['move'])

rule89 = ctrl.Rule(troll_team['medium'] & ogre_enemy_goblin['one'], movement['attack'])
rule90 = ctrl.Rule(troll_team['medium'] & ogre_enemy_goblin['small'], movement['attack'])
rule91 = ctrl.Rule(troll_team['medium'] & ogre_enemy_goblin['medium'], movement['attack'])
rule92 = ctrl.Rule(troll_team['medium'] & ogre_enemy_goblin['large'], movement['stay'])

rule93 = ctrl.Rule(troll_team['large'] & ogre_enemy_goblin['one'], movement['attack'])
rule94 = ctrl.Rule(troll_team['large'] & ogre_enemy_goblin['small'], movement['attack'])
rule95 = ctrl.Rule(troll_team['large'] & ogre_enemy_goblin['medium'], movement['attack'])
rule96 = ctrl.Rule(troll_team['large'] & ogre_enemy_goblin['large'], movement['stay'])

#########################################################################################

movement_ctrl = ctrl.ControlSystem([rule1, rule2, rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,
                                    rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,
                                    rule24,rule25,rule26,rule27,rule28,rule29,rule30,rule31,rule94,rule95,rule96,
                                    rule32,rule33,rule34,rule35,rule36,rule37,rule38,rule39,rule40,rule41,rule42,
                                    rule43,rule44,rule45,rule46,rule47,rule48,rule49,rule50,rule51,rule52,rule53,
                                    rule54,rule55,rule56,rule57,rule58,rule59,rule60,rule61,rule62,rule63,rule64,
                                    rule65,rule66,rule67,rule68,rule69,rule70,rule71,rule72,rule73,rule74,rule75,
                                    rule76,rule77,rule78,rule79,rule80,rule81,rule82,rule83,rule84,rule85,rule86,
                                    rule87,rule88,rule89,rule90,rule91,rule92,rule93])

# movement_ctrl = ctrl.ControlSystem([rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,
#                                     rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,
#                                     rule24,rule25,rule26,rule27,rule28,rule29,rule30,rule31,
#                                     rule32,rule33,rule34,rule35,rule36])

movement_score = ctrl.ControlSystemSimulation(movement_ctrl)

movement_score.input['ogre_team'] = 20
movement_score.input['goblin_team'] = 20
movement_score.input['troll_team'] = 20
movement_score.input['goblin_team'] = 20
movement_score.input['troll_enemy_goblin'] = 20
movement_score.input['ogre_enemy_goblin'] = 30
movement_score.input['goblin_enemy_ogre'] = 20

movement_score.compute()
print(movement_score.output['movement'])

movement.view(sim=movement_score)
