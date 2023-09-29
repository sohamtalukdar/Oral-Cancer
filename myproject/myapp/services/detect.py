import argparse
import time
from pathlib import Path
import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random
import cv2
import torch
from pathlib import Path
from numpy import random
from myapp.services.utils.general import (
    check_img_size, 
    non_max_suppression, 
    scale_coords, 
    xyxy2xywh
)
from myapp.services.experimental import attempt_load  # Correct import statement


from myapp.services.utils.datasets import LoadStreams, LoadImages
from myapp.services.utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
   scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from myapp.services.utils.plots import plot_one_box
from myapp.services.utils.torch_utils import select_device, load_classifier, time_synchronized, TracedModel

class YOLOv7Service:
    def __init__(self, weights='/home/soham/oralcancer/myproject/weights/oralcancer.pt', device='', img_size=640, conf_thres=0.25, iou_thres=0.45):
        self.device = select_device(device)
        self.model = attempt_load(weights, map_location=self.device)
        self.img_size = check_img_size(img_size, s=int(self.model.stride.max()))
        self.conf_thres = conf_thres
        self.iou_thres = iou_thres
        self.names = self.model.module.names if hasattr(self.model, 'module') else self.model.names

        if self.device.type != 'cpu':
            self.model(torch.zeros(1, 3, self.img_size, self.img_size).to(self.device).type_as(next(self.model.parameters())))


def detect(self, source, save_img=False, view_img=False, save_txt=False, project='runs/detect', name='exp'):
        set_logging()
        save_dir = Path(increment_path(Path(project) / name, exist_ok=True))
        (save_dir / 'labels' if save_txt else save_dir).mkdir(parents=True, exist_ok=True)

        dataset = LoadStreams(source, img_size=self.img_size) if source.startswith(('rtsp://', 'rtmp://', 'http://', 'https://')) else LoadImages(source, img_size=self.img_size)
        
        results = []
        t0 = time.time()
        for path, img, im0s, vid_cap in dataset:
            img = torch.from_numpy(img).to(self.device)
            img = img.half()
            img /= 255.0
            if img.ndimension() == 3:
                img = img.unsqueeze(0)
            
            t1 = time_synchronized()
            pred = self.model(img)[0]
            t2 = time_synchronized()
            
            pred = non_max_suppression(pred, self.conf_thres, self.iou_thres)
            
            for i, det in enumerate(pred):
                if len(det):
                    det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0s.shape).round()
                    for *xyxy, conf, cls in reversed(det):
                        label = f'{self.names[int(cls)]} {conf:.2f}'
                        results.append({
                            'path': path,
                            'label': label,
                            'coordinates': [int(x) for x in xyxy],
                            'confidence': float(conf),
                            'class_id': int(cls),
                        })
        print(f'Done. ({time.time() - t0:.3f}s)')
        return results


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='yolov7.pt', help='model.pt path(s)')
    parser.add_argument('--source', type=str, default='inference/images', help='source')  # file/folder, 0 for webcam
    parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='object confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--view-img', action='store_true', help='display results')
    parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
    parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
    parser.add_argument('--nosave', action='store_true', help='do not save images/videos')
    parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--update', action='store_true', help='update all models')
    parser.add_argument('--project', default='runs/detect', help='save results to project/name')
    parser.add_argument('--name', default='exp', help='save results to project/name')
    parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
    parser.add_argument('--no-trace', action='store_true', help='don`t trace model')
    opt = parser.parse_args()
    print(opt)
    #check_requirements(exclude=('pycocotools', 'thop'))

    with torch.no_grad():
        if opt.update:  # update all models (to fix SourceChangeWarning)
            for opt.weights in ['yolov7.pt']:
                detect()
                strip_optimizer(opt.weights)
        else:
            detect()
