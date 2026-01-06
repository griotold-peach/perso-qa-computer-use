"""프로젝트 설정"""
import os
from pathlib import Path
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

class Config:
    """설정 클래스"""
    
    # API
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    
    # Perso.ai
    PERSO_EMAIL = os.getenv("PERSO_EMAIL")
    PERSO_PASSWORD = os.getenv("PERSO_PASSWORD")
    PERSO_URL = os.getenv("PERSO_URL", "https://perso.ai/ko/workspace/vt")
    
    # Computer Use
    WIDTH = int(os.getenv("WIDTH", "1920"))
    HEIGHT = int(os.getenv("HEIGHT", "1080"))
    DISPLAY_NUM = os.getenv("DISPLAY_NUM", "1")
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    SCREENSHOT_ON_ERROR = os.getenv("SCREENSHOT_ON_ERROR", "true").lower() == "true"
    
    # Paths
    BASE_DIR = Path(__file__).parent.parent
    SCREENSHOTS_DIR = BASE_DIR / "screenshots"
    LOGS_DIR = BASE_DIR / "logs"
    
    def __init__(self):
        # 디렉토리 생성
        self.SCREENSHOTS_DIR.mkdir(exist_ok=True)
        self.LOGS_DIR.mkdir(exist_ok=True)

config = Config()
