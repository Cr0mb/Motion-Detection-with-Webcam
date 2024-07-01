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

```
Update v1
- Added a check to ensure the camera is successfully opened. If not, an error message is printed, and the function exits:
 > This prevents the script from crashing if it cannot access the webcam, providing a clear error message instead.
  
- Changed the background subtractor from `cv2.createBackgroundSubtractorMOG2()` to `cv2.createBackgroundSubtractorKNN()`:
 > The K-Nearest Neighbors (KNN) method can provide better performance in certain scenarios, particularly when dealing with slow-moving objects or less dynamic backgrounds.

- Introduced a variable `min_contour_area` to easily adjust the minimum contour area threshold:
 > This allows for easier customization of the minimum size of moving objects that will be detected and highlighted, improving flexibility for different use cases.

- Added a check to ensure a frame is successfully captured. If not, an error message is printed, and the loop breaks:
 > This addition enhances the script's robustness by handling frame capture failures gracefully, preventing potential crashes and providing clear error messages.

- Replaced separate erosion and dilation operations with a morphological close operation for better noise reduction:
 > Using the morphological close operation (combining dilation followed by erosion) helps to close small holes within the foreground objects, reducing noise more effectively and improving the accuracy of motion detection.
```
