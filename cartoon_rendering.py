import cv2
import numpy as np


def cartoonize_image(img_path):
    # 이미지 읽기
    img = cv2.imread(img_path)
    # img = cv2.resize(img, (600, 600))

    # 스무딩을 위한 블러 처리
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.medianBlur(img_gray, 7)

    # 엣지 검출
    edges = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # 색상 축소 (bilateral filtering 사용)
    color = cv2.bilateralFilter(img, 9, 300, 300)

    # 엣지와 색상을 결합하여 만화 효과 적용
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon


# 테스트 코드
if __name__ == "__main__":
    img_code = "2"
    img_path = f"sample{img_code}.png"  # 변환할 이미지 경로
    cartoon_img = cartoonize_image(img_path)

    # 결과 출력
    cv2.imshow("Cartoonized Image", cartoon_img)
    cv2.imwrite(f"sample{img_code}_cartooned.png", cartoon_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
