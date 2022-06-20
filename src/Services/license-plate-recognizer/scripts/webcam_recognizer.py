
import cv2
from cv2 import VideoCapture
import pytesseract
import PIL.Image as Image

class WebcamRecognizer:
    initialized = False
    name = ""
    webcam = VideoCapture
    recognizerType = "Webcam Recognizer"

    def __init__(self, reconizerName):
        self.name=reconizerName
        

    def start(self):
        print(f"{self.name} - {self.recognizerType} started")
        self.initialized = True
        self.webcam = cv2.VideoCapture(0)
        if self.webcam.isOpened():
            validation, frame = self.webcam.read()
            while validation:
                validation, frame = self.webcam.read()
                cv2.imshow("Video da Webcam", frame)
                key = cv2.waitKey(5)
                if key == 27: # ESC
                    break
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            text = pytesseract.image_to_string(Image.fromarray(img))
            print(text)


    def stop(self):
        self.webcam.release()
        cv2.destroyAllWindows()
        print(f"{self.name} - {self.recognizerType} Stopped")
        self.initialized = False


