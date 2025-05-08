# pyQTGUI002_yoloV5
이 프로그램은 웹캠으로부터 실시간 영상을 받아와, YOLOv5 모델을 사용하여 화면 내 물체를 실시간으로 탐지합니다.<br>
best.pt 사용자 정의 모델을 기반으로 객체를 탐지하도록 설정되어 있습니다.<br>
탐지된 물체들은 화면에 네모 상자와 이름표 형태로 시각화되어 표시됩니다.<br>
프로그램을 종료하고 싶으실 때는 'q' 키를 누르시면 됩니다.<br>

## 1. 프로그램 준비
https://github.com/haeun0908/pyQTGUI001<br><br>
지난번에 PyQt6와 OpenCV를 활용해서 만든 웹캠 영상 프로그램을 새 폴더로 옮겼습니다.<br><br>
![1](https://github.com/haeun0908/pyQTGUI002_yoloV5/blob/main/images/1.%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8%20%EC%A4%80%EB%B9%84.png)

## 2. 새로운 작업 환경 만들기
conda create -n [환경 이름] 명령어를 사용해서 다른 프로젝트와 겹치지 않게 새 가상 환경을 만들고 해당 환경을 활성화했습니다.<br><br>
![2](https://github.com/haeun0908/pyQTGUI002_yoloV5/blob/main/images/2.%20%EC%83%88%EB%A1%9C%EC%9A%B4%20%EC%9E%91%EC%97%85%20%ED%99%98%EA%B2%BD%20%EB%A7%8C%EB%93%A4%EA%B8%B0.png)

## 3. YOLOv5 코드 가져오기
웹캠에서 물체를 자동으로 탐지하기 위해 git clone https://github.com/ultralytics/yolov5.git 명령어를 사용해서 YOLOv5 저장소를 작업 폴더에 복제했습니다.<br><br>
![3](https://github.com/haeun0908/pyQTGUI002_yoloV5/blob/main/images/3.%20YOLOv5%20%EC%BD%94%EB%93%9C%20%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0.png)

## 4. 기본 라이브러리 설치
PyQt6 같은 기본 라이브러리들을 requirements.txt 파일을 통해 한 번에 설치했습니다.<br><br>
![4](https://github.com/haeun0908/pyQTGUI002_yoloV5/blob/main/images/4.%20%EA%B8%B0%EB%B3%B8%20%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC%20%EC%84%A4%EC%B9%98.png)

## 5. YOLOv5 라이브러리 설치
YOLOv5 모델을 제대로 실행하려면 추가 라이브러리가 필요합니다.<br>
YOLOv5 폴더의 requirements.txt 파일에 있는 패키지들을 설치했습니다.<br><br>
![5](https://github.com/haeun0908/pyQTGUI002_yoloV5/blob/main/images/5.%20YOLOv5%20%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC%20%EC%84%A4%EC%B9%98.png)

## 6. 프로그램 완성 및 기능 구현
mainAPP.py와 YOLOv5의 detect.py 코드를 참고해서 최종 프로그램을 완성했습니다.<br><br>
![code](https://github.com/haeun0908/pyQTGUI002_yoloV5/blob/main/images/code.png)
![6](https://github.com/haeun0908/pyQTGUI002_yoloV5/blob/main/images/6.%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8%20%EC%99%84%EC%84%B1%20%EB%B0%8F%20%EA%B8%B0%EB%8A%A5%20%EA%B5%AC%ED%98%84.png)
