import pygame


textures = {
    "player": {
        "file": "francis.png"
    }
}


def load_textures():
    for key, value in textures.items():
        value["image"] = pygame.image.load("resources/" + value["file"])


def get_texture(texture_name):
    return textures[texture_name]["image"]
