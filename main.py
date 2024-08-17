import pygame
from os import listdir
from shutil import copy


def get_images(path: str):
    return [fr"{path}\{name}" for name in listdir(path)
            if ".jpg" in name or ".png" in name]


def sort_images(path: str):
    screen_height = 1000
    screen_width = 1600
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((255, 255, 255))
    fps = 144
    clock = pygame.time.Clock()
    pygame.init()

    running = True
    liked = []
    i = 0
    images = get_images(path)

    while running:
        try:
            image = pygame.image.load(images[i])
            image_width, image_height = image.get_size()

            image = pygame.transform.rotate(image, -90.0)
            image = pygame.transform.scale(image, (image_height * 0.25, image_width * 0.25))

            screen.blit(image, (20, 20))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        liked.append(images[i])
                        i += 1
                    elif event.key == pygame.K_n:
                        i += 1
                elif event.type == pygame.QUIT:
                    running = False

            pygame.display.update()
            screen.fill((255, 255, 255))
            clock.tick(fps)

        except FileNotFoundError:
            print(f"Директория не найдена")
            running = False

        except NotADirectoryError:
            print(f"Это не директория")
            running = False

        except PermissionError:
            print(f"Нет доступа к директории")
            running = False

        except IndexError:
            print("Картинки закончились")
            running = False

        except Exception as e:
            print(f"Произошла ошибка: {e}")
            running = False

    return liked


def copy_images(source: list, target: str):
    for file in source:
        copy(file, target)


def main(source: str, target: str):
    sorted_images = sort_images(source)
    print(sorted_images)
    copy_images(sorted_images, target)


if __name__ == "__main__":
    main(r"C:\Users\son25\Desktop\Camera", r"F:\фото со старой мобилы")
