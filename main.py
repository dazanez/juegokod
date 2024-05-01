import pygame
import sys
import random
from time import sleep
from preguntas import preguntas # banco de preguntas

pygame.init() # Inicializar Pygame

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trivia Loca 😜")

# Colores
colors = {'BLUE_BG': (155, 210, 230), 'BLACK': (0, 16, 10), 'INDIGO': (84, 15, 110), 'TOMATO': (255, 100, 66)}

# Fuente y tamaño
# font = pygame.font.SysFont(['Century Gothic', 'Corbel',], 20)
font = pygame.font.Font(None, 36)


# Función para mostrar la pregunta y opciones
def mostrar_pregunta(pregunta_actual):
    screen.fill(colors["BLUE_BG"]) # Se define el color de fondo
    pregunta_texto = font.render(pregunta_actual["pregunta"], True, colors["BLACK"])
    pregunta_rect = pregunta_texto.get_rect(center=(WIDTH // 2, 50)) # El texto de la pregunta se centra en x
    screen.blit(pregunta_texto, pregunta_rect)

    # Mostrar opciones
    y = 150
    random.shuffle(pregunta_actual["opciones"])
    for opcion in pregunta_actual["opciones"]:
        opcion_texto = font.render(opcion, True, colors["BLACK"], colors["TOMATO"])
        opcion_rect = opcion_texto.get_rect(center=(WIDTH // 2, y))
        screen.blit(opcion_texto, opcion_rect)
        y += 50
        
def mostrar_felicitacion(correcto=True):
    mensajes_felicitacion = ['¡Muy bien!', '¡Excelente! Tu respuesta fue correcta', '¡Hey! Sabes de esto']
    mensajes_incorrecto = ['¡Ups! Esa no era la respuesta', 'Incorrecto, probemos nuevamente', 'La próxima es la vencida']
    mensaje = random.choice(mensajes_felicitacion) if correcto else random.choice(mensajes_incorrecto)

    screen.fill(colors["BLUE_BG"]) # Se define el color de fondo
    pregunta_texto = font.render(mensaje, True, colors["INDIGO"], colors["TOMATO"])
    pregunta_rect = pregunta_texto.get_rect(center=(WIDTH // 2, HEIGHT // 2)) # El texto de la pregunta se centra en x
    screen.blit(pregunta_texto, pregunta_rect)

# Función principal del juego
def main():
    pregunta_actual = random.choice(preguntas) # Una pregunta random del banco de preguntas
    mostrar_pregunta(pregunta_actual) # Se muestra la pregunta seleccionada

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Obtener la posición del clic del ratón
                x, y = pygame.mouse.get_pos()
                # Verificar si el clic está en alguna opción
                y_opcion = 150
                for opcion in pregunta_actual["opciones"]:
                    if WIDTH // 2 - font.size(opcion)[0] // 2 <= x <= WIDTH // 2 + font.size(opcion)[0] // 2 and y_opcion <= y <= y_opcion + 50:
                        if opcion == pregunta_actual["respuesta"]:
                            print("¡Respuesta correcta!")
                        else:
                            print("Respuesta incorrecta.")
                        # Cambiar a la siguiente pregunta
                        pregunta_actual = random.choice(preguntas)
                        mostrar_pregunta(pregunta_actual)
                    y_opcion += 50

        pygame.display.flip()

if __name__ == "__main__":
    main()
