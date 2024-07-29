
from paddleocr import PaddleOCR as pad

class OcrMain:
    """Main OCR object, more information refer to:
    https://github.com/PaddlePaddle/PaddleOCR/blob/main/README_en.md
    """
    def __init__(self):
        self.path :str = None
        self.result :list = None
        self.ocr = pad(use_angle_cls=True, lang="en",show_log = False) 
        
    def make(self):
        """Generates the OCR result and sets OcrMain.result
        Returns:
            list? : PaddleOCR list of strings and data. 
        """
        if self.path == None:
            return f'Error 1: self.path == None'
        img_path = self.path
        result = self.ocr.ocr(img_path, cls=True)
        self.result = result
