import utils.colors as colors

default_size = (350, 350)
default_health = 100
default_energy = 100
default_attack = 5
default_attacksprite = "scratch.png"

pokemons_info = {
    "Atrox.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Charmadillo.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Cindrill.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Cleaf.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Draem.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Finiette.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Finsta.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Friolera.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Gulfin.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Ivieron.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Jacana.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Larvea.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Pluma.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Plumette.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Pouch.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Sparchu.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
}

effects_information = {
    "Poison": {"color": colors.PURPLE},
    "Restoration": {"color": colors.PINK},
    "Bleeding": {"color": colors.RED},
    "Weakness": {"color": colors.YELLOW},
    "Burned": {"color": colors.BLACK},
    "Stunned": {"color": colors.GREEN},
}

# DESCRIERI EFECTE
effects_descriptions = [
    "Pokemon takes damage 10% of the total remaining health, at the end of pokemon turn 0" 
    "Pokemon get 10% * remaining turns for the effect of his total health 0"
    "Pokemon gets 10% * remaining turns more damage 0"
    "Pokemon deals 10 * remaining turns less damage 0"
    "Pokemon loses 5% * remaining turns of his energy"
    "Pokemon have a chance to miss an attack 0"
]

attacks_information = {
"Atrox.png": {
    "attack": "Snake Bite",
    "special_attack": {"name": "Venom splash", "effects": ["Weakness", "Poison"]},
    "frames": "scratch.png"
},
"Charmadillo.png": {
    "attack": "Rock Burn",
    "special_attack": {"name": "Earth Wraith", "effects": ["Burned"]},
    "frames": "explosion.png"
},
"Cindrill.png": {
    "attack": "Stony Fire",
    "special_attack": {"name": "Magma burst", "effects": ["Poison"]},
    "frames": "fire.png"
},
"Cleaf.png": {
    "attack": "Wing Flap",
    "special_attack": {"name": "Venus Flytrap", "effects": ["Poison", "Bleeding"]},
    "frames": "green.png"
},
"Draem.png": {
    "attack": "Paw Slap",
    "special_attack": {"name": "Star Dust", "effects": ["Bleeding", "Restoration"]},
    "frames": "scratch.png"
},
"Finiette.png": {
    "attack": "Water Splash",
    "special_attack": {"name": "Tsunami Fury", "effects": ["Burned", "Restoration"]},
    "frames": "splash.png"
},
"Finsta.png": {
    "attack": "Bubble Pop",
    "special_attack": {"name": "Playful Wave", "effects": ["Bleeding"]},
    "frames": "splash.png"
},
"Friolera.png": {
    "attack": "Ice Spike",
    "special_attack": {"name": "Winters Blessing", "effects": ["Restoration", "Poison"]},
    "frames": "ice.png"
},
"Gulfin.png": {
    "attack": "Slip Splash",
    "special_attack": {"name": "Crack the Ocean", "effects": ["Bleeding"]},
    "frames": "splash.png"
},
"Ivieron.png": {
    "attack": "Nature's Claw",
    "special_attack": {"name": "Hunter's Pursue", "effects": ["Poison", "Bleeding"]},
    "frames": "green.png"
},
"Jacana.png": {
    "attack": "Little Pinch",
    "special_attack": {"name": "Sky Feather", "effects": ["Poison"]},
    "frames": "scratch.png"
},
"Larvea.png": {
    "attack": "Head Smash",
    "special_attack": {"name": "Forest Trap", "effects": ["Bleeding", "Weakness"]},
    "frames": "green.png"
},
"Pluma.png": {
    "attack": "Feral bite",
    "special_attack": {"name": "Jungle Rawr", "effects": ["Restoration", "Poison", "Bleeding"]},
    "frames": "green.png"
},
"Plumette.png": {
    "attack": "Leaf's Cut",
    "special_attack": {"name": "Jungle's Hearth", "effects": ["Bleeding"]},
    "frames": "green.png"
},
"Pouch.png": {
    "attack": "Capi Slap",
    "special_attack": {"name": "Capi Sssslap", "effects": []},
    "frames": "scratch.png"
},
"Sparchu.png": {
    "attack": "Hot Bruise",
    "special_attack": {"name": "Earthquake", "effects": []},
    "frames": "fire.png"
}
}
