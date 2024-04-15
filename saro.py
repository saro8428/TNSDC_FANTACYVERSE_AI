import random

class FantasyWorldGenerator:
    def __init__(self):
        self.adjectives = ['Ancient', 'Mystical', 'Enchanted', 'Forgotten', 'Eternal']
        self.nouns = ['Realm', 'Land', 'Kingdom', 'Empire', 'Domain']
        self.biomes = ['Forest', 'Mountain', 'Desert', 'Swamp', 'Island']

    def generate_world_name(self):
        adjective = random.choice(self.adjectives)
        noun = random.choice(self.nouns)
        biome = random.choice(self.biomes)
        return f"{adjective} {biome} {noun}"

    def generate_world_description(self, name):
        return f"The {name} is a magical realm filled with wonder and mystery. Its {random.choice(self.biomes)}s are home to fantastical creatures and ancient ruins, waiting to be explored by brave adventurers."

if __name__ == "__main__":
    world_generator = FantasyWorldGenerator()
    world_name = world_generator.generate_world_name()
    world_description = world_generator.generate_world_description(world_name)

    print("Generated Fantasy World:")
    print("Name:", world_name)
    print("Description:", world_description)
