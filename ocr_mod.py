
from paddleocr import PaddleOCR as pad

class OcrMain:
    def __init__(self):
        self.path :str = None
        self.result :list = None
        self.ocr = pad(use_angle_cls=True, lang="en",show_log = False) 
        
    def make(self):
        if self.path == None:
            return f'Error 1: self.path == None'
        img_path = self.path
        result = self.ocr.ocr(img_path, cls=True)
        self.result = result
