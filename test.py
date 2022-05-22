from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, use_gpu=False)  
img_path = 'E:\\Users\\Administrator\\Desktop\\test\\111.jpg'
result = ocr.ocr(img_path, cls=True)
for line in result:
    print(line[1][0])
  
