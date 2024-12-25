from ultralytics import YOLO

model = YOLO('yolov8x')

results = model.predict('input_videos\challenge-165_1.mp4os', save = True)