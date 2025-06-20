import cv2
import numpy as np
from yolodetect import YoloDetect
from imutils.video import VideoStream


video = VideoStream(src=0).start() # 0 là chỉ số của webcam, có thể thay đổi tùy vào cấu hình máy của bạn

points = []

model = YoloDetect()

def handle_left_click(event, x, y, flags, points):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])
def draw_polygon (frame, points):
    for point in points:
        frame = cv2.circle( frame, (point[0], point[1]), 5, (0,0,255), -1)

    frame = cv2.polylines(frame, [np.int32(points)], False, (255,0, 0), thickness=2)
    return frame
# Kiểm tra xem kết nối với iVCam có thành công không
# Kiểm tra xem video stream đã khởi tạo thành công chưa
if video.stream is None:
    print("Không thể kết nối với webcam. Hãy chắc chắn rằng webcam đã được kết nối và không bị sự cố.")
    exit()


detect = False

while True:
    # Đọc frame từ iVCam
    frame = video.read()

    # Kiểm tra nếu frame không được đọc thành công
    # Lật frame theo chiều ngang
    frame = draw_polygon(frame,points)
    # Hiển thị frame
    
    if detect:
        frame = model.detect(frame=frame,points=points)
    cv2.imshow("Intrusion Warning", frame)
    cv2.setMouseCallback('Intrusion Warning',handle_left_click,points)
    # Kiểm tra xem người dùng có bấm phím 'q' để thoát không
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key ==ord('d'):
        points.append(points[0])
        detect =True
# Giải phóng kết nối và đóng cửa sổ OpenCV
video.stop()
cv2.destroyAllWindows()
