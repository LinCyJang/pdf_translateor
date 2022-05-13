# 这是一个将英文pdf自动翻译为中文的脚本。使用了三个库：`fitz`库打开pdf文件，使用`re`库处理文本，使用`googletrans`库进行翻译。


<!--  -->
依赖
+ pip install frontend
+ pip install FPDF
+ pip install pdfminer.six
+ pip install googletrans

### 如何运行
```
pip install -r requirements.txt
py translate.py
```