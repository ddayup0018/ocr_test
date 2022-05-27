# ocr图片识别中文字对比记录
## paddleocr easyocr cnocr三个进行对比，tesseract中文方面感觉无可比性byebye！
### paddleocr
- windows操作系统下安装（基于anconda，熟悉后可不用，安装一定要pip百度或国内镜像源）：
  1. 创建虚拟环境/指定python解释器版本/采用清华镜像源：conda create --name paddle_env python=3.9 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/  
  2. 激活虚拟环境：conda activate paddle_env
  3. 在虚拟环境下安装paddlepaddle/采用百度镜像源：pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
  4. pip3 install -U https://paddleocr.bj.bcebos.com/whl/layoutparser-0.0.0-py3-none-any.whl （本人目前暂未用到，可暂不安装）
  5. 在虚拟环境下安装paddleocr/采用百度镜像源：pip install paddleocr -i https://mirror.baidu.com/pypi/simple

- 可能安装失败的包：shapely ， python_Levenshtein
  1. 如失败到 https://www.lfd.uci.edu/~gohlke/pythonlibs/ 上下载，快速查找 crtl + f
  2. 复制到虚拟环境E:\anaconda\envs\paddle_env\Lib\site-packages文件夹下再pip install一次（E:\anaconda\envs\paddle_env\为你的anaconda安装目录下虚拟环境，\paddle_env\你的虚拟环境名称）
- 模型路径：C:\Users\Administrator\.paddleocr\whl（默认就有模型）

### easyocr
- windows操作系统下安装（基于anconda，熟悉后可不用，安装一定要pip国内镜像源）：
  1. 创建虚拟环境/指定python解释器版本/采用清华镜像源：conda create --name easyocr_env python=3.9 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/  
  2. 激活虚拟环境：conda activate easyocr_env
  3. 在虚拟环境下安装easyocr/采用清华镜像源：pip install easyocr -i https://pypi.tuna.tsinghua.edu.cn/simple

- 试了几遍，感觉安装顺利！
- 模型路径：C:\Users\Administrator\.EasyOCR\model（默认没有，首次执行会下载但是很慢）
  - 手动到 https://www.jaided.ai/easyocr/modelhub/ 上下载CRAFT（必须） zh_sim_g2（中文）

### cnocr
  - windows操作系统下安装（基于anconda，熟悉后可不用，安装一定要pip国内镜像源）：
  1. 创建虚拟环境/指定python解释器版本/采用清华镜像源：conda create --name cnocr_env python=3.9 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/  
  2. 激活虚拟环境：conda activate cnocr_env
  3. 在虚拟环境下安装cnocr/采用清华镜像源：pip install cnocr -i https://pypi.tuna.tsinghua.edu.cn/simple
  4. 在虚拟环境下安装cnstd/采用清华镜像源：pip install cnocr -i https://pypi.tuna.tsinghua.edu.cn/simple

  - 有可能安装失败的包：Polygon（cnstd）同样为Microsoft Visual C++ 14.0 is required
    - 快速安装方法：如失败到 https://www.lfd.uci.edu/~gohlke/pythonlibs/ 上下载，快速查找 crtl + f
    - 根本解决办法：安装Microsoft Visual C++ 14.0及以上版本

  - 测试代码：
  ~~~python 
    from cnstd import CnStd
    from cnocr import CnOcr

    std = CnStd()
    cn_ocr = CnOcr()

    box_info_list = std.detect('F:/Desktop/pic/2.jpg')

    for box_info in box_info_list['detected_texts']:
        cropped_img = box_info['cropped_img']
        ocr_res = cn_ocr.ocr_for_single_line(cropped_img)
        print(ocr_res)
  ~~~ 
  - 模型目录：C:\Users\Administrator\AppData\Roaming 下

### 对比表格
![对比表格](./ocr%E5%AF%B9%E6%AF%94.JPG)

