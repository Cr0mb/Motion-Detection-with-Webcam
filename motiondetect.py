import cv2

def detect_motion_and_draw_boxes():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to open camera.")
        return
    
    bg_subtractor = cv2.createBackgroundSubtractorKNN()
    
    prev_boxes = []
    min_contour_area = 1000  
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to capture frame.")
            break
        
        fg_mask = bg_subtractor.apply(frame)
        fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_CLOSE, None)  
        
        contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        curr_boxes = []
        
        for contour in contours:
            if cv2.contourArea(contour) > min_contour_area:
                x, y, w, h = cv2.boundingRect(contour)
                
                is_new_box = True
                for pb in prev_boxes:
                    if abs(x - pb[0]) < 50 and abs(y - pb[1]) < 50:
                        is_new_box = False
                        break
                
                if is_new_box:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    curr_boxes.append((x, y, w, h))
        
        prev_boxes = curr_boxes
        
        cv2.imshow('Motion Detection', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    detect_motion_and_draw_boxes()

