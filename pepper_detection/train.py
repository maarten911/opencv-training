"""
Install:
pip install yolov9pip
pip install Pillow==9.5.0 (for AttributeError: 'FreeTypeFont' object has no attribute 'getsize' with Yolo)

Get data:
- Download data from roboflow (todo: where did I get it: only save if it works)
- Extract to pepper_detection/cabai.v1i.yolov9


And then run in terminal:
    python /Users/maartenvanhooft/PycharmProjects/udemy-open-cv/venv/lib/python3.10/site-packages/yolov9/train.py \
    --batch 16 --epochs 3 --img 640 --device 0 --min-items 0 --close-mosaic 15 \
    --data /Users/maartenvanhooft/PycharmProjects/udemy-open-cv/pepper_detection/cabai.v1i.yolov9/data.yaml \
    --weights weights/gelan-c.pt \
    --cfg pepper_detection/gelan-c.yaml \
    --hyp pepper_detection/hyp.scratch-high.yaml \
    --device cpu
"""