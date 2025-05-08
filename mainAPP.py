import csv
import cv2
import os  # 파일 경로 처리를 위한 os 모듈 추가
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMessageBox, QLabel
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QImage, QPixmap

# 현재 스크립트의 디렉토리를 기준으로 리소스 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UI_PATH = os.path.join(BASE_DIR, "res", "knu.ui")

Form, Window = uic.loadUiType(UI_PATH)

class MainApp:
    def __init__(self):
        self.app = QApplication([])
        self.window = Window()
        self.form = Form()
        self.form.setupUi(self.window)

        # 웹캠 관련 변수
        self.cap = cv2.VideoCapture(0)  # 웹캠 열기
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

        # 버튼 이벤트 연결
        self.form.btnSave.clicked.connect(self.save_data)
        self.form.btnPhoto.clicked.connect(self.capture_photo)

        # 실시간 영상 표시 시작
        self.timer.start(30)  # 30ms마다 프레임 업데이트

    def update_frame(self):
        """웹캠에서 프레임을 읽어 QLabel에 표시"""
        ret, frame = self.cap.read()
        if ret:
            # OpenCV의 BGR 이미지를 RGB로 변환
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            qimg = QImage(frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
            pixmap = QPixmap.fromImage(qimg)
            self.form.logo.setPixmap(pixmap)  # QLabel에 표시
            self.form.logo.setScaledContents(True)  # 크기 조정

    def save_data(self):
        """UI 데이터를 CSV 파일로 저장"""
        try:
            name = self.form.lineEdit_name.text()
            tel = self.form.lineEdit_tel.text()
            memo = self.form.textEdit_memo.toPlainText()

            with open("data.csv", "w", newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Telephone", "Memo"])
                writer.writerow([name, tel, memo])

            QMessageBox.information(None, "저장 완료", "데이터가 성공적으로 저장되었습니다!")
        except Exception as e:
            QMessageBox.critical(None, "저장 실패", f"오류가 발생했습니다: {e}")

    def capture_photo(self):
        """현재 프레임을 캡처하여 저장"""
        try:
            name = self.form.lineEdit_name.text()
            if not name:
                QMessageBox.warning(None, "오류", "이름을 입력하세요!")
                return

            ret, frame = self.cap.read()
            if ret:
                # 사진 저장 경로 설정
                photo_path = os.path.join(os.getcwd(), f"{name}.jpg")  # 현재 디렉토리에 저장
                cv2.imencode('.jpg', frame)[1].tofile(photo_path)  # 한글 파일 이름 지원
                self.form.lineEdit_photo.setText(photo_path)  # 저장된 경로를 lineEdit_photo에 표시
                QMessageBox.information(None, "사진 저장 완료", f"사진이 {photo_path}에 저장되었습니다!")
            else:
                QMessageBox.critical(None, "오류", "사진을 캡처할 수 없습니다!")
        except Exception as e:
            QMessageBox.critical(None, "오류", f"사진 저장 중 오류가 발생했습니다: {e}")

    def run(self):
        """애플리케이션 실행"""
        self.window.show()
        self.app.exec()

    def __del__(self):
        """애플리케이션 종료 시 자원 해제"""
        if self.cap.isOpened():
            self.cap.release()

# 애플리케이션 실행
if __name__ == "__main__":
    app = MainApp()
    app.run()