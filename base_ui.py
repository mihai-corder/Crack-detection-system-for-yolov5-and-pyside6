import sys
import torch
import cv2
import datetime
import os

from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PySide6.QtGui import QPixmap,QImage
from PySide6.QtCore import QTimer
from main_window_ui import Ui_MainWindow

def convert2QImage(img):
    height, width, channel = img.shape
    return QImage(img, width, height,width * channel, QImage.Format_RGB888)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # Model
        self.det_model.clicked.connect(self.open_model)
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.video = None
        self.bind_slots()
        self.num_stop = 1  # 暂停与播放辅助信号，note：通过奇偶来控制暂停与播放
    
    def open_model(self):
        self.label_3.setText("模型加载中.....")
        file_path = QFileDialog.getOpenFileName(self, dir="./model", filter="*.pt")
        file_path = str(file_path)
        
        if file_path:
            file_path = file_path.split('/')[-1].split('\\')[-1].split("'")[0]
        print(file_path)
        self.model = torch.hub.load("./", "custom", path=file_path, source="local")
        self.label_3.setText("模型加载成功!\n当前加载模型："+file_path)


    def image_pred(self, file_path):
        # Inference
        results = self.model(file_path)
        re = str(results)
        image = results.render()[0]
        #保存信息
        file_name = str(file_path)
        if file_name:
            file_name = file_name.split("/")[-1]
        save_dir = 'results/images'
        now = datetime.datetime.now()
        now = str(now)
        filename = os.path.join(save_dir, f'{file_name}.txt')
        with open(filename, "w") as f:
            f.write(now + "\n" + re)
        lines = re.split("\n")  # 分割字符串为行列表
        first_line = lines[0]  # 获取第一行
        content = first_line.split("image 1/1:")[1]  # 使用切片获取512x512后面的内容
        self.label_2.setText("文件打开成功\n"+file_path+"\n检测信息如下（注：图片大小+裂缝种类+数量）:\n"+content)
        print(content)

        # self.label_2.setText(re)
        return convert2QImage(image)
    
    def video_pred(self):
        # Inference
        ret, frame = self.video.read()
        
        save_dir = 'results/videos'
        self.filename = os.path.join(save_dir, f'{self.video_name}.txt')
        if not ret:
            self.timer.stop()
        else:
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            self.input.setPixmap(QPixmap.fromImage(convert2QImage(frame)))
            results = self.model(frame)
            image = results.render()[0]
            re = str(results)
            lines = re.split("\n")  # 分割字符串为行列表
            first_line = lines[0]  # 获取第一行
            content = first_line.split("image 1/1:")[1]  # 使用切片获取内容
            self.label_2.setText("检测信息如下（注：图片大小+裂缝种类+数量）:\n"+content)
            #保存信息
            with open(self.filename, "a") as f:
                f.write(re)
            self.output.setPixmap(QPixmap.fromImage(convert2QImage(image)))
            
    def open_image(self):
        self.timer.stop()
        file_path = QFileDialog.getOpenFileName(self, dir="./ChinaBike/images/train", filter="*.jpg;*.png;*.jpeg")
        if file_path[0]:
            file_path = file_path[0]
            qimage = self.image_pred(file_path)
            self.input.setPixmap(QPixmap(file_path))
            self.output.setPixmap(QPixmap.fromImage(qimage))
            

    def open_video(self):
        file_path = QFileDialog.getOpenFileName(self, dir="./tests", filter="*.mp4")
        name = str(file_path)
        # print(name)
        now = datetime.datetime.now()
        now = str(now)
        save_dir = 'results/videos'
        self.video_name = name.split('/')[-1].split('\\')[-1].split("'")[0]
        self.filename = os.path.join(save_dir, f'{self.video_name}.txt')
        with open(self.filename, "a") as f:
                f.write(now+ "\n")
        # print(self.video_name)       
        if file_path[0]:
            file_path = file_path[0]
            self.video = cv2.VideoCapture(file_path)
            self.timer.start()

    # 暂停/继续 视频
    def button_video_stop(self):
        self.timer.blockSignals(False)
        # 暂停检测
        # 若QTimer已经触发，且激活
        if self.timer.isActive() == True and self.num_stop % 2 == 1:
            self.pushButton_stop.setText(u'继续')  # 当前状态为暂停状态
            self.num_stop = self.num_stop + 1  # 调整标记信号为偶数
            self.timer.blockSignals(True)
        # 继续检测
        else:
            self.num_stop = self.num_stop + 1
            self.pushButton_stop.setText(u'暂停')

    # 结束视频检测
    def finish_detect(self):
            self.video.release()
            self.input.setText(u'原始图像')  # 清空label画布
            self.output.setText(u'检测结果')
            self.label_2.setText(u'结束检测')
            # 结束检测时，查看暂停功能是否复位，将暂停功能恢复至初始状态
            # Note:点击暂停之后，num_stop为偶数状态
            if self.num_stop % 2 == 0:
                self.pushButton_stop.setText(u'暂停')
                self.num_stop = self.num_stop + 1
                self.timer.blockSignals(False)

    def bind_slots(self):
        self.det_image.clicked.connect(self.open_image)
        self.det_video.clicked.connect(self.open_video)
        self.timer.timeout.connect(self.video_pred)
        self.pushButton_stop.clicked.connect(self.button_video_stop)
        self.pushButton_exit.clicked.connect(self.finish_detect)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    app.exec()