import pygame
import sys
from settings import *
from models import Snake, Food

def draw_menu(screen, selected_difficulty):
    font = pygame.font.SysFont(None, FONT_SIZE)
    title = font.render(MENU_TITLE, True, WHITE)
    screen.blit(title, (PYGAME_WINDOW_WIDTH // 2 - title.get_width() // 2, TITLE_Y_POS))

    y = MENU_START_Y
    for diff in DIFFICULTIES:
        color = GREEN if diff == selected_difficulty else WHITE
        text = font.render(diff, True, color)
        screen.blit(text, (PYGAME_WINDOW_WIDTH // 2 - text.get_width() // 2, y))
        y += MENU_Y_SPACING

def main():
    # Pygameの初期化とウィンドウ設定
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((PYGAME_WINDOW_WIDTH, PYGAME_WINDOW_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)

    def show_menu():
        # 難易度選択メニューの初期化
        selected_difficulty = DEFAULT_DIFFICULTY
        in_menu = True
        while in_menu:
            screen.fill(BLACK)
            draw_menu(screen, selected_difficulty)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        current_index = DIFFICULTIES.index(selected_difficulty)
                        selected_difficulty = DIFFICULTIES[(current_index - 1) % len(DIFFICULTIES)]
                    elif event.key == pygame.K_DOWN:
                        current_index = DIFFICULTIES.index(selected_difficulty)
                        selected_difficulty = DIFFICULTIES[(current_index + 1) % len(DIFFICULTIES)]
                    elif event.key == pygame.K_RETURN:
                        in_menu = False

        return selected_difficulty

    while True:
        # ゲームの初期化
        selected_difficulty = show_menu()
        snake = Snake()
        food = Food()
        font = pygame.font.SysFont(None, FONT_SIZE)
        paused = False
        game_over = False
        in_game = True

        while in_game:
            # ヘビの方向制御
            keys = pygame.key.get_pressed()
            if not paused and not game_over:
                if keys[pygame.K_UP] and snake.direction != "DOWN":
                    snake.direction = "UP"
                elif keys[pygame.K_DOWN] and snake.direction != "UP":
                    snake.direction = "DOWN"
                elif keys[pygame.K_LEFT] and snake.direction != "RIGHT":
                    snake.direction = "LEFT"
                elif keys[pygame.K_RIGHT] and snake.direction != "LEFT":
                    snake.direction = "RIGHT"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        in_game = False
                        if snake.score > snake.high_score:
                            snake.save_high_score()
                    elif event.key == pygame.K_p:
                        paused = not paused
                    elif event.key == pygame.K_r and game_over:
                        snake.reset()
                        game_over = False

            if not paused and not game_over:
                snake.update()

                # 餌との衝突判定と得点処理
                if snake.get_head_position() == food.position:
                    snake.length += 1
                    snake.score += 1
                    food.randomize_position()

                # ヘビの自己衝突判定
                if snake.get_head_position() in snake.positions[1:]:
                    game_over = True

            # 画面描画
            screen.fill(BLACK)
            snake.draw(screen)
            food.draw(screen)

            # スコア情報の描画
            score_text = font.render(SCORE_FORMAT.format(snake.score, snake.high_score), True, WHITE)
            screen.blit(score_text, (SCORE_PADDING, SCORE_PADDING))

            if paused:
                pause_text = font.render(PAUSE_TEXT, True, WHITE)
                screen.blit(pause_text, (PYGAME_WINDOW_WIDTH // 2 - pause_text.get_width() // 2, PYGAME_WINDOW_HEIGHT // 2))
            elif game_over:
                game_over_text = font.render(GAME_OVER_TEXT, True, WHITE)
                instruction_text = font.render(RESTART_INSTRUCTION, True, WHITE)
                screen.blit(game_over_text, (PYGAME_WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, PYGAME_WINDOW_HEIGHT // 2 - GAME_OVER_Y_OFFSET))
                screen.blit(instruction_text, (PYGAME_WINDOW_WIDTH // 2 - instruction_text.get_width() // 2, PYGAME_WINDOW_HEIGHT // 2 + GAME_OVER_Y_OFFSET))
            elif not paused:
                menu_hint = font.render(MENU_HINT, True, WHITE)
                menu_hint_width = menu_hint.get_width()
                screen.blit(menu_hint, (PYGAME_WINDOW_WIDTH - menu_hint_width - MENU_HINT_PADDING, SCORE_PADDING))

            pygame.display.update()
            clock.tick(SNAKE_SPEEDS[selected_difficulty])

if __name__ == "__main__":
    main()