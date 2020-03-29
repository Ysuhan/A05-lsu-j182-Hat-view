import os
import cv2
from Identification_module.nets.yolo import YOLO
from PIL import Image

# import cv2
yolo = YOLO()
from Video_proces.base_camera import BaseCamera
# 这是一个图片路径
path = "D:/PycharmProjects/A05-lsu-j182_Hat_view/Video_proces/templates/"

class Camera(BaseCamera):
    video_source = 0

    def __init__(self):
        if os.environ.get('OPENCV_CAMERA_SOURCE'):
            Camera.set_video_source(int(os.environ['OPENCV_CAMERA_SOURCE']))
        super(Camera, self).__init__()

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()
            cv2.imwrite(path + 'img/1.jpg', img)
            image = Image.open(path + 'img/1.jpg')
            print("image", type(image))
            # image = Image.fromarray()
            # img1 = cv2.imencode('.jpg', img)[1].tobytes()
            # # frame = cv2.flip(img, 1)  # 读取每一帧的图片
            # # print(frame)
            r_image = yolo.detect_image(image)
            print("r_image", type(r_image))

            r_image.save(path + 'imgs/1.jpg')
            r_image = Image.open(path + 'imgs/1.jpg')
            # img1 = cv2.imencode('.jpg', r_image).tobytes()
            # encode as a jpeg image and return it
            # yield img1
            yield r_image.read()
