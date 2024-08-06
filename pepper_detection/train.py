import os
'/Users/maartenvanhooft/PycharmProjects/udemy-open-cv'

os.system(
    """
    python /Users/maartenvanhooft/PycharmProjects/udemy-open-cv/venv/lib/python3.10/site-packages/yolov9/train.py \
    --batch 16 --epochs 20 --img 640 --device 0 --min-items 0 --close-mosaic 15 \
    --data /Users/maartenvanhooft/PycharmProjects/udemy-open-cv/pepper_detection/cabai.v1i.yolov9/data.yaml \
    --weights ../weights/gelan-c.pt \
    --cfg gelan-c.yaml \
    --hyp hyp.scratch-high.yaml \
    --device cpu
    """
)