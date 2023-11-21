import cv2
from deepface import DeepFace

def main():
    video_capture = cv2.VideoCapture(0)
    emotions = {}
    count = 0

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Analyzing the frame for emotion
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False, silent=True)

        # Extracting emotion information
        emotion = result[0]['dominant_emotion']
        # print(f"Current Emotion: {emotion}")

        if emotion in emotions:
            emotions[emotion] += 1
        else:
            emotions[emotion] = 1
        if count >= 20:
            temp = []
            for key in emotions:
                temp.append([key, emotions[key]])
            temp = sorted(temp, key=lambda x: x[1], reverse=True)
            print("Emotion: ", temp[0][0])
            count = 0
            emotions = {}
    

        # Displaying the frame
        cv2.imshow('Emotion Recognition', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        count += 1

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()