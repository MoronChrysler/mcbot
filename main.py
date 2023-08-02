import telebot
import cv2
bot = telebot.TeleBot('6384047545:AAHlnXm9PlN97ih3R8kI333MfE4Q5JRwZJs')
user_id = 1101524784
flag = 0
img = cv2.imread('photo_2023-07-29_00-01-16.jpg')


@bot.message_handler(content_types=['text'])
def num(message):
    global user_id, flag, img, font
    if message.text:
        if not flag:
            a = message.text
            print(a)
            x = a[:2] + ' (' + a[2:5] + ') ' + a[5:8] + '-' + a[8:10] + '-' + a[10:]
            font = cv2.FACE_RECOGNIZER_SF_FR_COSINE
            cv2.putText(img, x, (163, 737), font, 0.7, color=(0, 0, 0), thickness=2)
            flag += 1
        elif flag == 1:
            b = message.text
            print(b[:-1])
            n = 9 - len(b[:-1])
            print(n)
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(img, b, (219 + n * 10, 518), font, 0.8, color=(255, 255, 255), thickness=2)
            cv2.imwrite('image_2.jpg', img)
            cv2.waitKey()
            bot.send_message(user_id, 'uytre')
            bot.send_photo(user_id, open('image_2.jpg', 'rb'))
            img = cv2.imread('photo_2023-07-29_00-01-16.jpg')
            flag = 0


if __name__ == '__main__':
    bot.polling(none_stop=True)
