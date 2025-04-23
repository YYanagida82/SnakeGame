# ウィンドウサイズとブロックサイズ
PYGAME_WINDOW_WIDTH = 800  # ゲームウィンドウの幅
PYGAME_WINDOW_HEIGHT = 600  # ゲームウィンドウの高さ
BLOCK_SIZE = 20  # ヘビと餌のブロックサイズ

# 難易度設定
DIFFICULTIES = ["Easy", "Normal", "Hard"]  # 選択可能な難易度
DEFAULT_DIFFICULTY = "Normal"  # デフォルトの難易度
SNAKE_SPEEDS = {"Easy": 10, "Normal": 15, "Hard": 20}  # 各難易度のヘビの速度

# UI要素の配置
TITLE_Y_POS = 200  # タイトルのY座標
MENU_START_Y = 300  # メニューの開始Y座標
MENU_Y_SPACING = 50  # メニュー項目間の間隔
SCORE_PADDING = 10  # スコア表示の余白
MENU_HINT_PADDING = 20  # メニューヒントの余白
GAME_OVER_Y_OFFSET = 30  # ゲームオーバー表示のオフセット

# フォント設定
FONT_SIZE = 50  # 全体のフォントサイズ

# 画面表示テキスト
GAME_TITLE = "Snake Game"  # ウィンドウタイトル
MENU_TITLE = "Select Difficulty"  # 難易度選択画面のタイトル
PAUSE_TEXT = "PAUSED - Press P to Resume"  # 一時停止時のメッセージ
GAME_OVER_TEXT = "GAME OVER"  # ゲームオーバー時のメッセージ
RESTART_INSTRUCTION = "Press R to Restart or ESC for Menu"  # リスタート指示
MENU_HINT = "Press ESC for Menu"  # メニュー表示のヒント
SCORE_FORMAT = "Score: {} High Score: {}"  # スコア表示のフォーマット

# ゲーム内の色定義
BLACK = (0, 0, 0)  # 背景色
WHITE = (255, 255, 255)  # テキスト色
RED = (255, 0, 0)  # 餌の色
GREEN = (0, 255, 0)  # ヘビの色
GRAY = (128, 128, 128)  # 未使用の色