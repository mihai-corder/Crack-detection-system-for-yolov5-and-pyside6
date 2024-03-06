# 本地环境

| 硬件名称   | 参数信息                                           |
| ---------- | -------------------------------------------------- |
| 中央处理器 | Intel(R)  Core(TM) i7-9750H CPU @ 2.60GHz 2.59 GHz |
| 操作系统   | 64位 Windows11操作系统                             |
| 独立显卡   | NVIDIA  GeForce GTX 1660 Ti with Max-Q Design      |

软件安装目录：

| 软件类型 | 软件名称      |
| -------- | ------------- |
| 编程语言 | Python 3.9    |
| 开发工具 | Anaconda 3    |
| 框架工具 | Pytorch 1.8.2 |
| 运算平台 | CUDA 11.7     |
| 加速平台 | cuDNN 10.2    |

软件安装根据本地硬件情况安装，例如30系列显卡需安装更高版本cuda才不报错

# 安装过程

python与anaconda 3 的安装不做赘述

创建并打开虚拟环境：

```python
conda create -n yolov5(环境名) python==3.9
conda activate yolov5
```

安装需要的库：

```python
pip install -r requirements.txt #在系统文件路径下
```

注:torch需手动安装，建议安装1.8.2版本

验证环境正确：

```pyhton
import torch
torch.__version__
torch.cuda.is_available()
```

![image-20230529114611607](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20230529114611607.png)

运行系统界面：

```python
python base_ui.py
```

![image-20230529114827547](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20230529114827547.png)

即可运行。

运行须知：

1.先载入对应的模型，仅支持.pt文件

2.载入模型完成后，可以选择图片功能或是视频检测功能，选择对应的文件后，检测结果即可运行