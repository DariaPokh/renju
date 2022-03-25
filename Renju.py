import pygame # Импорт пакета pygame
import sys # Импорт пакета sys


pygame.init()
size_block = 45 # Размер фигуры, которой делается ход
width = height = size_block * 15 # количество блоков

# Настройка окна
size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Проверь свои силы в Рэндзю!")

# Инцилизация цветов
BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
YELLOW = (255, 255, 150)

# Создание массива для поля 15 на 15
mas = [[0] * 15 for i in range(15)]

# Инцилизация текущего игрока
player = 0

# Инцилизация переменной, содержащий условие окончания игры
game_over = False

# Функция, содержащия условия победы и ничьи
def check_win(mas, sign):
    zeroes = 0
    # Проверка наличия 5 фигур одного цвета, стоящих в одной вертикальной линии
    for row in mas:
        zeroes += row.count(0)
        for x in range (15):
            for y in range(15):
                if mas[x][y] == sign and mas[x+1][y] == sign and mas[x + 2][y] == sign and mas[x + 3][
                        y] == sign and mas[x + 4][y] == sign:
                        return sign # Проверка наличия 5 фигур одного цвета, стоящих в одной вертикальной линии
                elif  mas[x][y] == sign and mas[x][y + 1] == sign and mas[x][y + 2] == sign and mas[x][
                    y + 3] == sign and mas[x][y + 4] == sign:
                        return sign
                elif  mas[x][y] == sign and mas[x - 1][y + 1] == sign and mas[x - 2][y + 2] == sign and mas[x - 3][
                    y + 3] == sign and mas[x - 4][y + 4] == sign:
                        return sign  # Проверка наличия 5 фигур одного цвета, стоящих в одной диагональной линии, где значения по оси x убывают, а по y возрастают
                elif mas[x][y] == sign and mas[x + 1][y + 1] == sign and mas[x + 2][y + 2] == sign and mas[x + 3][
                    y + 3] == sign and mas[x + 4][y + 4] == sign:
                        return sign # Проверка наличия 5 фигур одного цвета, стоящих в одной диагональной линии, где значения по осям x и y возрастают
        if zeroes == 0:
            return "Победила дружба!" # Условие, выполняемое при заполнении всего поля, но отсутствии победных комбинаций
        else:
            return False

# Цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        # Условия управления мышкой, выбора блока на поле
        elif event.type == pygame.MOUSEBUTTONUP and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // size_block
            row = y_mouse // size_block
            if mas[row][col] == 0:
                if player % 2 == 0:
                    mas[row][col] = 'Победа черных!' # Ход черной фигурой
                else:
                    mas[row][col] = 'Победа белых!' # Ход белой фигурой
                player += 1
         # Условия выполняется при победе одного из игроков. Новая игра включается при нажатии пробела.
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 15 for i in range(15)]
            player = 0
            screen.fill(BLACK)

    #Условия продолжения игры
    if not game_over:
        for row in range(15):
            for col in range(15):
                if mas[row][col] == 'Победа черных!':
                    color = BLACK # Отметка на поле чероной фигуры
                elif mas[row][col] == 'Победа белых!':
                    color = WHITE # Отметка на поле белой фигуры
                else:
                    color = YELLOW # Цвет свободных фигур
                x = col * size_block
                y = row * size_block
                pygame.draw.rect(screen,color, (x, y, size_block, size_block))
                pygame.draw.line(screen, BLACK, (x + 22.5, 0), (x + 22.5, 690), 2) # Прорисовка вертикальный линий на поле
                pygame.draw.line(screen, BLACK, (0, y + 22.5), (690, y + 22.5), 2) # Прорисовка горизонтальный линий на поле

                # Условия выбора победителя
                if (player-1)%2 == 0:
                    game_over = check_win(mas, 'Победа черных!')
                else:
                    game_over = check_win(mas, 'Победа белых!')

                # Прописаны условия, выполняемые при окончании игры
                if game_over:
                    screen.fill(BLACK)
                    font = pygame.font.SysFont('stxingkai', 80)
                    text1 = font.render(game_over, True, WHITE)
                    text_rect = text1.get_rect()
                    text_x = screen.get_width() / 2 - text_rect.width / 2
                    text_y = screen.get_height() / 2 - text_rect.height / 2
                    screen.blit(text1, [text_x, text_y])



        # Обновление игрового экрана
        pygame.display.update()
