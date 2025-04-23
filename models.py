import pygame
import random
import json
import os
from settings import *

class Snake:
    """ゲーム内のヘビの状態管理
    位置、長さ、方向、スコアの制御
    """
    def __init__(self):
        """ヘビの初期状態設定
        画面中央に配置、初期長さ1、ランダムな方向、色とスコアを初期化
        """
        self.length = 1  # ヘビの初期長さ
        self.positions = [(PYGAME_WINDOW_WIDTH // 2, PYGAME_WINDOW_HEIGHT // 2)]  # ヘビの位置リスト（先頭が頭部）
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])  # ランダムな初期方向
        self.color = GREEN  # ヘビの色
        self.score = 0  # 現在のスコア
        self.high_score = self.load_high_score()  # ハイスコアの読み込み

    def load_high_score(self):
        """JSONファイルからハイスコアを読み込み
        
        Returns:
            int: 保存済みハイスコア（エラー時は0）
        """
        if os.path.exists("high_score.json"):
            try:
                with open("high_score.json", "r") as f:
                    data = json.load(f)
                    return data.get("high_score", 0)
            except:
                return 0
        return 0

    def save_high_score(self):
        """ハイスコアをJSONファイルに保存"""
        with open("high_score.json", "w") as f:
            json.dump({"high_score": self.high_score}, f)

    def get_head_position(self):
        """ヘビの頭部座標を取得
        
        Returns:
            tuple: 頭部の(x, y)座標
        """
        return self.positions[0]

    def update(self):
        """ヘビの位置更新
        方向に応じた移動と画面端での折り返し処理
        """
        cur = self.get_head_position()
        x, y = cur

        # 現在の方向に基づいて新しい頭部位置を計算
        if self.direction == "UP":
            y -= BLOCK_SIZE
        elif self.direction == "DOWN":
            y += BLOCK_SIZE
        elif self.direction == "LEFT":
            x -= BLOCK_SIZE
        elif self.direction == "RIGHT":
            x += BLOCK_SIZE

        new_head = (x, y)

        # 画面の端に到達した場合、反対側から出現
        if x >= PYGAME_WINDOW_WIDTH:
            new_head = (0, y)
        elif x < 0:
            new_head = (PYGAME_WINDOW_WIDTH - BLOCK_SIZE, y)
        if y >= PYGAME_WINDOW_HEIGHT:
            new_head = (x, 0)
        elif y < 0:
            new_head = (x, PYGAME_WINDOW_HEIGHT - BLOCK_SIZE)

        # 新しい頭部を追加し、必要に応じて尾部を削除
        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()

    def reset(self):
        """ゲームのリセット
        ハイスコア更新とヘビの初期状態への復帰
        """
        # ハイスコアの更新確認と保存
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        
        # ヘビの状態を初期化
        self.length = 1
        self.positions = [(PYGAME_WINDOW_WIDTH // 2, PYGAME_WINDOW_HEIGHT // 2)]
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        self.score = 0

    def draw(self, surface):
        """ヘビの描画
        
        Args:
            surface: 描画対象の画面
        """
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], BLOCK_SIZE, BLOCK_SIZE))

class Food:
    """ゲーム内の餌の状態管理
    位置と色の制御
    """
    def __init__(self):
        """餌の初期状態設定
        ランダムな位置と色の初期化
        """
        self.position = (0, 0)  # 餌の位置
        self.color = RED  # 餌の色
        self.randomize_position()  # 初期位置をランダムに設定

    def randomize_position(self):
        """餌の位置をランダムに設定
        グリッドに合わせた座標の決定
        """
        self.position = (
            random.randint(0, (PYGAME_WINDOW_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
            random.randint(0, (PYGAME_WINDOW_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        )

    def draw(self, surface):
        """餌の描画
        
        Args:
            surface: 描画対象の画面
        """
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))