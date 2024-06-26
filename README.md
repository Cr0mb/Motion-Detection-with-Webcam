[Youtube Beta 1](https://youtu.be/yOoauYWVg6w)

# Motion-Detection-with-Webcam
Python script that uses OpenCV to detect motion from my webcam, attempting to draw a green bounding box around the moving objects.

Moving objects will be highlighted with green bounding boxes.


## Features

> Motion Detection: Uses a background subtractor to identify regions of motion in the video stream.

> Bounding Box Drawing: Draws green rectangles around detected moving objects.

> Adaptive Box Management: Tracks and manages bounding boxes to avoid redundant or overlapping boxes for the same object.

## Requirements

- Python 3.x
- OpenCV
```
pip install opencv-python
```
