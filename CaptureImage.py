import cv2
import dropbox
import random
import time

start_time = time.time()

def take_snapshot():

    number = random.randint(0,20)

    vco = cv2.VideoCapture(0)
    result = True

    while(result):
        ret,frame = vco.read()
        img_name = "Image" + str(number) + ".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False

    return img_name
    print("Snapshot take in ")

    vco.release()
    cv2.destroyAllWindows()

def upload_file(img_name):

    access_token = "u3t7nqeWGQMAAAAAAAAAAVkrwv79FiI4m7PAIuc8-Z7YwZQ01ujfx8m5fFPWT83q"
    file = img_name
    file_from = file
    file_to = "SecurityImages" + (img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from , 'rb') as f :
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File_upload")

def main():
    while(True):
        if((time.time()-start_time)> 30):
            name = take_snapshot()
            upload_file(name)

main()




