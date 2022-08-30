import cv2

#불러올 이미지 경로
image_file = "image/my_face.jpg"

# cv2.IMREAD_COLOR : 수정없이 원본 이미지 읽기
original = cv2.imread(image_file, cv2.IMREAD_COLOR)

#cv2.IMREAD_GRAYSCALE :로 흑백사진으 수정해서 이미지 열기
gray = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)

#cv2.IMREAD_UNCHANGED : 이미지 파일의 알파채널까지 포함해서 읽기
unchange = cv2.imread(image_file, cv2.IMREAD_UNCHANGED)
#이미지 보여주기
cv2.imshow("IMREAD_COLOR", original)
cv2.imshow("IMREAD_GRAYSCALE", gray)
cv2.imshow("IMREAD_UNCHANGED", unchange)

cv2.waitKey(0)