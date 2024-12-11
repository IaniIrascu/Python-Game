import utils.colors as colors

default_size = (350, 350)
default_health = 100
default_energy = 100
default_attack = 5
default_attacksprite = "scratch.png"

pokemons_info = {
    "Atrox.png": {"health": 230, "energy": default_energy, "size":  default_size, "damage": 45},
    "Charmadillo.png": {"health": 500, "energy": default_energy, "size":  default_size, "damage": 10000},
    "Cindrill.png": {"health": 125, "energy": default_energy, "size":  default_size, "damage": 100},
    "Cleaf.png": {"health": 250, "energy": default_energy, "size":  default_size, "damage": 30},
    "Draem.png": {"health": 400, "energy": default_energy, "size":  default_size, "damage": 50},
    "Finiette.png": {"health": 325, "energy": default_energy, "size":  default_size, "damage": 40},
    "Finsta.png": {"health": 230, "energy": default_energy, "size":  default_size, "damage": 30},
    "Friolera.png": {"health": 260, "energy": default_energy, "size":  default_size, "damage": 25},
    "Gulfin.png": {"health": 145, "energy": default_energy, "size":  default_size, "damage": 70},
    "Ivieron.png": {"health": 270, "energy": default_energy, "size":  default_size, "damage": 40},
    "Jacana.png": {"health": 150, "energy": default_energy, "size":  default_size, "damage": 35},
    "Larvea.png": {"health": 75, "energy": default_energy, "size":  default_size, "damage": 125},
    "Pluma.png": {"health": 450, "energy": default_energy, "size":  default_size, "damage": 50},
    "Plumette.png": {"health": 200, "energy": default_energy, "size":  default_size, "damage": 35},
    "Pouch.png": {"health": 250, "energy": default_energy, "size":  default_size, "damage": 25},
    "Sparchu.png": {"health": 320, "energy": default_energy, "size":  default_size, "damage": 30},
}

effects_information = {
    "Poison": {"color": colors.PURPLE},
    "Restoration": {"color": colors.PINK},
    "Bleeding": {"color": colors.RED},
    "Weakness": {"color": colors.YELLOW},
    "Burned": {"color": colors.BLACK},
    "Stunned": {"color": colors.GRAY},
    "Nature": {"color": colors.GREEN},
    "Defence": {"color": colors.BLUE}
}

# DESCRIERI EFECTE
effects_descriptions = [
    "Pokemon takes damage 10% of the total remaining health, at the end of pokemon turn 0" 
    "Pokemon get 10% * remaining turns for the effect of his total health 0"
    "Pokemon gets 10% * remaining turns more damage 0"
    "Pokemon deals 10 * remaining turns less damage 0"
    "Pokemon loses 5% * remaining turns of his energy 0"
    "Pokemon have a chance to miss an attack 0"
]

attacks_information = {
"Atrox.png": {
    "attack": "Snake Bite",
    "special_attack": {"name": "Venom splash", "effects": ["Weakness", "Poison"]},
    "frames": "scratch.png",
    "energy": 50
},
"Charmadillo.png": {
    "attack": "Rock Burn",
    "special_attack": {"name": "Earth Wraith", "effects": ["Burned", "Weakness", "Defence"]},
    "frames": "explosion.png",
    "energy": 75
},
"Cindrill.png": {
    "attack": "Stony Fire",
    "special_attack": {"name": "Magma burst", "effects": ["Poison", "Burned"]},
    "frames": "fire.png",
    "energy": 25
},
"Cleaf.png": {
    "attack": "Wing Flap",
    "special_attack": {"name": "Venus Flytrap", "effects": ["Poison", "Bleeding"]},
    "frames": "green.png",
    "energy": 40
},
"Draem.png": {
    "attack": "Paw Slap",
    "special_attack": {"name": "Star Dust", "effects": ["Bleeding", "Restoration"]},
    "frames": "scratch.png",
    "energy": 50
},
"Finiette.png": {
    "attack": "Water Splash",
    "special_attack": {"name": "Tsunami Fury", "effects": ["Burned", "Restoration"]},
    "frames": "splash.png",
    "energy": 60
},
"Finsta.png": {
    "attack": "Bubble Pop",
    "special_attack": {"name": "Playful Wave", "effects": ["Bleeding"]},
    "frames": "splash.png",
    "energy": 15
},
"Friolera.png": {
    "attack": "Ice Spike",
    "special_attack": {"name": "Winters Blessing", "effects": ["Restoration", "Bleeding"]},
    "frames": "ice.png",
    "energy": 25
},
"Gulfin.png": {
    "attack": "Slip Splash",
    "special_attack": {"name": "Crack the Ocean", "effects": ["Bleeding", "Stunned"]},
    "frames": "splash.png",
    "energy": 30
},
"Ivieron.png": {
    "attack": "Nature's Claw",
    "special_attack": {"name": "Hunter's Pursue", "effects": ["Poison", "Bleeding"]},
    "frames": "green.png",
    "energy": 30
},
"Jacana.png": {
    "attack": "Little Pinch",
    "special_attack": {"name": "Sky Feather", "effects": ["Poison"]},
    "frames": "scratch.png",
    "energy": 10
},
"Larvea.png": {
    "attack": "Head Smash",
    "special_attack": {"name": "Forest Trap", "effects": ["Bleeding", "Weakness"]},
    "frames": "green.png",
    "energy": 40
},
"Pluma.png": {
    "attack": "Feral bite",
    "special_attack": {"name": "Jungle Rawr", "effects": ["Restoration", "Poison", "Bleeding"]},
    "frames": "green.png",
    "energy": 70
},
"Plumette.png": {
    "attack": "Leaf's Cut",
    "special_attack": {"name": "Jungle's Hearth", "effects": ["Bleeding"]},
    "frames": "green.png",
    "energy": 10
},
"Pouch.png": {
    "attack": "Capi Slap",
    "special_attack": {"name": "Capi Sssslap", "effects": ["Weakness", "Stunned"]},
    "frames": "scratch.png",
    "energy": 45
},
"Sparchu.png": {
    "attack": "Hot Bruise",
    "special_attack": {"name": "Earthquake", "effects": ["Defence"]},
    "frames": "fire.png",
    "energy": 20
}
}
