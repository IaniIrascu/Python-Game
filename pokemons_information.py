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
    "Poison": {"color": colors.PURPLE, "no_of_turns": 2},
    "Restoration": {"color": colors.PINK, "no_of_turns": 2},
    "Stunned": {"color": colors.DARK_GRAY, "no_of_turns": 1},
    "Bleeding": {"color": colors.RED, "no_of_turns": 3},
    "Weakness": {"color": colors.YELLOW, "no_of_turns": 2},
    "Burned": {"color": colors.BLACK, "no_of_turns": 3},
    "Wet": {"color": colors.BLUE, "no_of_turns": 3},
}

# DESCRIERI EFECTE
effects_descriptions = [
    "Pokemon takes damage 10% of the total remaining health, at the end of pokemon turn"
    "Pokemon get 10% * remaining turns for the effect of his total health"
    "Theres a 50% change the pokemon skip its turn after this effect"
    "Pokemon gets 10% * remaining turns more damage"
    "Pokemon deals 10 * remaining turns less damage"
    "Pokemon loses 5% * remaining turns of his energy"
    "Cleans the last negative effect applied"
]
