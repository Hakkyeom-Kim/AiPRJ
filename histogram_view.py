import cv2

from matplotlib import pyplot as plt

#불러올 이미지 경로
image_file = "image/my_face.jpg"

# cv2.IMREAD_COLOR : 수정없이 원본 이미지 읽기
original = cv2.imread(image_file, cv2.IMREAD_COLOR)

#cv2.IMREAD_GRAYSCALE :로 흑백사진으 수정해서 이미지 열기
gray = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)

#cv2.IMREAD_UNCHANGED : 이미지 파일의 알파채널까지 포함해서 읽기
unchange = cv2.imread(image_file, cv2.IMREAD_UNCHANGED)

#OpenCV 색상을 일반적으로 부르는 RGB로 순서가 아닌, BGR 순서로 사용함
color = ('b', 'g', 'r')

#색상이 존재하는 원본 이미지 히스토그램 보기
#BGR 순서대로 그래프 그리기 위해 반복문 사용함
for i, col in enumerate(color):

    hist = cv2.calcHist([original],[i],None,[256],[0,256])
    plt.figure(1)
    plt.plot(hist, color =col)

plt.show()

hist = cv2.calcHist([gray],[0],None,[256],[0,256])
plt.figure(2)
plt.plot(hist)
plt.show()

gray = cv2.equalizeHist(gray)

hist = cv2.calcHist([gray],[0],None,[256],[0,256])
plt.figure(3)
plt.plot(hist)
plt.show()


