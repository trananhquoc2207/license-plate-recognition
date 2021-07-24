import numpy as np
import cv2
import imutils
import pytesseract
import os
try:
    import Image
except ImportError:
    from PIL import Image, ImageEnhance, ImageFilter
class NhanDang():
    def luuAnh(self,c):
        img = cv2.imread(r'E:\ITS-N19\Cropped Images-Text\fileXuLy.png',0)
        bigger = cv2.resize(img, (780, 540),interpolation = cv2.INTER_NEAREST)
        cv2.imwrite('DuLieuFile/' + str(c) + '.png',bigger) 
    def xoaAnh(self,c):
            if os.path.exists('DuLieuFile/' + str(c) + '.png'):
                os.remove('DuLieuFile/' + str(c) + '.png')
            else:
                print("The file does not exists")  
    def xuly(self,b):
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        image = cv2.imread(b)

        image = imutils.resize(image, width=500)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        gray = cv2.bilateralFilter(gray, 11, 17, 17)

        edged = cv2.Canny(gray, 170, 200)

        cnts, new  = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        img1 = image.copy()
        cv2.drawContours(img1, cnts, -1, (0,255,0), 3)

        cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30]
        NumberPlateCnt = None 

        img2 = image.copy()
        cv2.drawContours(img2, cnts, -1, (0,255,0), 3)

        count = 0
        idx = 'fileXuLy'
        for c in cnts:
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.02 * peri, True)
                # print ("approx = ",approx)
                if len(approx) == 4:  # Select the contour with 4 corners
                    NumberPlateCnt = approx #This is our approx Number Plate Contour

                    # Crop those contours and store it in Cropped Images folder
                    x, y, w, h = cv2.boundingRect(c) #This will find out co-ord for plate
                    new_img = gray[y:y + h, x:x + w] #Create new image
                    cv2.imwrite('Cropped Images-Text/' + str(idx) + '.png', new_img) #Store new image
                    #idx+=1

                    break

        cv2.drawContours(image, [NumberPlateCnt], -1, (0,255,0), 3)

        Cropped_img_loc = 'Cropped Images-Text/fileXuLy.png'
        hinh = cv2.imshow("Cropped Image ", cv2.imread(Cropped_img_loc))

        
        text = pytesseract.image_to_string(Cropped_img_loc, config='--psm 7')
        cv2.waitKey(0)
        return text
    def get_image(self):
        camera = cv2.VideoCapture(0)
        retval , im  = camera.read()
        return im
    def chupHinh(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            live = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ramp_frames = 30
            cv2.imshow("Chup Hinh", frame)
            

            if cv2.waitKey(1) & 0xFF == ord('q'):
                for i in range(ramp_frames):
                    temp = self.get_image()
                camera_capture = self.get_image()
                file = r"E:\ITS-N13\Cropped Images-Text\fileXuLy.png"
                cv2.imwrite(file, camera_capture)
                break
        cap.release()
        #return file
    def chuongTrinhNhanDienXe(text):
        #Khởi động trình dò
        orb = cv2.ORB_create(nfeatures=1000)
    #path = "bienbao/"+text
        text = 'DuLieuFile'
        path = r"E:\ITS-N19-a/"+text
        listAnh = []
        listNameAnh = []
        myList = os.listdir(path)

        for name in myList:
            imgNow = cv2.imread(f'{path}/{name}', 0)
            listAnh.append(imgNow)
            listNameAnh.append(os.path.splitext(name)[0])
        print(listNameAnh)

        def timDacDiem(listAnh):
            NhanDang = []
            for anh in listAnh:
                diemKhac, dinhDanh = orb.detectAndCompute(anh, None)
                NhanDang.append(dinhDanh)
            return NhanDang


        def timID(live, NhanDang, phucTap):
            #tìm các điểm chính và bộ mô tả bằng ORB
            diemKhac2, dinhDanh2 = orb.detectAndCompute(live, None)
            bf = cv2.BFMatcher()
            listGiong = []
            ketLuan = -1
            try:
                for des in NhanDang:
                    matches = bf.knnMatch(des, dinhDanh2, k=2)  # 2 value can compare on
                    good = []
                    for m, n in matches:
                        if m.distance < 0.75 * n.distance:
                            good.append([m])
                    listGiong.append(len(good))
            except:
                pass
            if len(listGiong) != 0:
                if (max(listGiong)) > phucTap:
                    ketLuan = listGiong.index(max(listGiong))
            return ketLuan


        Nhandang = timDacDiem(listAnh)
        print(len(Nhandang))
        quay = cv2.VideoCapture(0)
        while True:
            success, live = quay.read()
            liveMauSac = live.copy()
            live = cv2.cvtColor(live, cv2.COLOR_BGR2GRAY)
            tenCuaAnh = timID(live, Nhandang, 20)
            if id != -1:
                cv2.putText(liveMauSac, listNameAnh[tenCuaAnh], (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
            ten="Phan Mem Nhan Dien Bien Bao "+ text
            diemKhacBiet, dinhDanhBiet = orb.detectAndCompute(live, None)

            keypoint = cv2.drawKeypoints(live,diemKhacBiet,None)
            cv2.imshow("key point",keypoint)

            cv2.imshow(ten, liveMauSac)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
