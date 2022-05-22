from paddleocr import PaddleOCR
from pywebio import start_server, output, input
from io import BytesIO
from PIL import Image
from os import remove


def main():
    output.put_markdown('# 图片转文字小工具')
    output.put_markdown('### 一款将图片中文字提取成文本的小工具！')
    up_pic = input.file_upload(label='请上传一张图片',
                               accept='image/*',
                               required=True)
    do_up_pic = BytesIO(up_pic['content'])
    # 保存图片到本地
    img = Image.open(do_up_pic).convert('RGB')
    img.save('./userpic.jpg')
    output.toast('已提交，请稍等，越复杂越慢！', duration=5)
    # 处理图片
    ocr = PaddleOCR(use_angle_cls=True, use_gpu=False)
    result = ocr.ocr('./userpic.jpg', cls=True)
    output.toast('处理成功，请查看对比！')
    # 输出文字和准确率
    for line in result:
        output.put_markdown(line[1][0])
        # output.put_markdown(line[1][0] + '----------------' +
        #                     '%.2f' % line[1][1])
    # 输出图片
    output.put_image(up_pic['content'])
    # 删除本地图片
    remove('./userpic.jpg')


if __name__ == '__main__':
    start_server(main, port=8888, debug=True, auto_open_webbrowser=True)
