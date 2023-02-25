import os,time,random
import matplotlib.pyplot as plt
from PIL import Image,ImageOps


class mover():
    def __init__(self):
        pass
    def list_directory(self):
        print(os.listdir())
        return os.listdir()
    def go_back(self):
        os.chdir("..")
    def go_archive(self):
        os.chdir("./archive")
    def go_editing(self):
        os.chdir("./editing")
    def go_created(self):
        os.chdir("./created")
    def go_new_created_file_on_created(self):
        
            os.chdir(os.listdir()[-1])
    #created dosyasına yeni bir klasör oluşturur
    def create_folder_on_created(self):
        self.go_created() 
        
        os.mkdir(f"new_images_{len(os.listdir())+1}")
        print(f"-> new_images_{len(os.listdir())} dosyası oluşturuldu")
        self.go_back()
    
    def refresh_folders(self):
        
        import shutil
    
        #editing klasöründekileri (archive'e) arşivle

        def step1():
            length = len(os.listdir("./archive"))
            src_path = f"./editing"
            dst_path = f"./archive/"
            time.sleep(0.1)
            shutil.move(src_path,dst_path)
            time.sleep(0.1)
            os.rename("./archive/editing",f"archive/new_{length+1}")
            
        # editlemeye devam etmek üzere cratedtakileri editinge alır
        def step2():
            length = len(os.listdir("./created"))
            src_path = f"./created/new_images_{length}"
            dst_path = "./"
            shutil.move(src_path,dst_path)
            time.sleep(0.1)
            os.rename(f"new_images_{length}","editing")
            print("-> dosyalar yenilendi")
        step1()
        step2()

class functions():
    def __init__(self):
        pass

    def names_of_images(self):
        #fotoğraflara ulaş
        img_path_list = os.listdir()
        
        #example
        for i in range(3):
            t = random.randint(0, len(img_path_list))
            print("-> Örnek Resim :",img_path_list[t-1])
        
        return img_path_list
    
    def import_images_from_names(self,list_of_photo_names,WIDTH=400,HEIGHT=400):
        #isimlerinden fotoğrafları içeri aktar
        photos = []
        sayac = 1
        for im in list_of_photo_names:
            im = Image.open(im) #.resize((WIDTH,HEIGHT))
            print("-> importing image: ",sayac)
            sayac+=1
            photos.append(im)
        return photos
        
    def do_split(self,names,howmuch):

        if 0 < howmuch:
            symbol = str(input("hangi sembolden ayrılacak : "))
            index = int(input("hangi indexteki alınacak : "))
            temp = 0
            for i in names:    
                names[temp]=(i.split(symbol)[index])
                temp += 1
                
            print("-> suanki : ",names[0:3])    
                
            howmuch -= 1
            return self.do_split(names,howmuch)
        else:
            return names

    def make_plot(self,data,xlabel,title="MOMENT",color="gray"):
        #plot yapma
        
        fig = plt.figure(figsize =(10, 7))
        plt.hist(data,color=color)
        plt.title(title)
        plt.grid(axis="y")
        plt.grid(axis="x")
        plt.savefig(fname="distribution.png",facecolor="#f0f9e8") 
        print("-> plot kaydedildi")
        plt.show()
        
    def save_images(self,labels,images):
        sayac = 0
        eklenti = str(input("-> hangi uzantıda olacak (jpg,png gibi) : "))
        for im in images:
            im.save(f"{labels[sayac]}_{sayac}.{eklenti}")
            sayac += 1
        print("-> Fotoğraflar kaydedildi")
            
    def do_gray(self,images):
        imgs = []
        for im in images:
            im2 = ImageOps.grayscale(im)
            imgs.append(im2)
        
        print("-> gri olarak ölçeklendirildi")
        return imgs
    
    def make_bbox(self,labels):
        DIR = "./"
        print("-> bu işlemde tüm görsel bbox olarak alınır (0.5 0.5 0.5 0.5)")
        label_index = int(input("label encode ne olacak (rakam):"))
        
        for i in range(len(labels)):
            with open(DIR+labels[i]+".txt",'w') as f:
                f.write(f"{label_index} 0.5 0.5 0.5 0.5")
                f.write("\n")
        print("-> bbox txt dosyaları başarıyla oluşturuldu ")
        
    def decrease_data_according_to_lower_data(self,data_p):
        import numpy as np
        import pandas as pd
        #en az dataya göre veriyi azaltır
        #title -->  column of sorting title
        title = "category_name"
        data_p = np.array(data_p)
        data = pd.DataFrame(data_p,columns=[title])
        result = data_p.copy()
        
        counts = data[title].value_counts()
        minimum_value = np.min(counts)
        print("least number :",minimum_value)
        print("new dimension of data",minimum_value*len(counts))
        gap = counts-minimum_value
        
        category_index = 0
        for cate in gap.index:
            how_much = gap[category_index]
            for much in range(how_much):
                result_index = 0 
                for i in result:
                    if i == cate:
                        result = np.delete(result,result_index)
                        break
                    result_index += 1
            
            category_index += 1

        return result
    
    def decrease_photos(self,names,q=3):
        q = int(input("Kaçta kaçına düşürülecek (örneğin:3) :"))
        #fotoğrafları azaltır
        temp = []
        sayac=0
        for i in names:
       
            if sayac%q == 0:
                temp.append(i) 
                sayac=-q
            sayac+=1
        time.sleep(0.1)
        print("-> Before length of data : ",len(names))
        print("-> new length of data : ",len(temp))
        print(type(temp))
        return temp

    def bring_image_from_videos(self,save_path="./"):
        import cv2
        video_path=f"{os.listdir()[0]}"
        photo_W=int(input("Frame genişliği : "))
        photo_H=int(input("Frame yüksekliği : "))
        image_per_frame=int(input("Kaç framede bir image alınacak : "))

        cap = cv2.VideoCapture(video_path)
        sayac= 0
        sayac2=0
        while True:
            ret,frame = cap.read()
            img = cv2.resize(frame,(photo_W,photo_H))
            if sayac % image_per_frame == 0:
                sayac2+=1
                cv2.imwrite(save_path+"/"+f"S_{sayac2}.jpg",img)
                print(sayac2,"yazildi")
            sayac+=1

    def augmanter(self,labels,images,rotasyon_uzunlugu=135,yukseklik_kaydirma=0.1,genislik_kaydirma=0.1,kirpma=0.1,zoom=0.4,yatay_yansima=False,dikey_yansima=False):
        WIDTH = int(input("Genişlik : "))
        HEIGHT = int(input("Yükseklik : "))
        kacar = int(input("Kaçar tane çoğaltılacak : "))
        rotasyon_uzunlugu = int(input("kaç derece dönebilir : "))
        from keras.preprocessing.image import ImageDataGenerator
        from keras.utils import img_to_array
        # kullanılacak veri artırma tekniklerini tanımla
        datagen = ImageDataGenerator(rotation_range=rotasyon_uzunlugu,
                                     width_shift_range=yukseklik_kaydirma,
                                     height_shift_range=genislik_kaydirma,
                                     shear_range=kirpma,
                                     zoom_range=zoom,
                                     horizontal_flip=yatay_yansima,
                                     vertical_flip=dikey_yansima,
                                     fill_mode='nearest')
        
        sayac = 0
        for im in images:
            im = img_to_array(im)
            im = im.reshape((1,) + im.shape )
            label = labels[sayac]
            
            
            i=0
            for batch in datagen.flow(im, batch_size=1,save_prefix=f"{label}_{sayac}_{i}",
                                      save_to_dir='./', 
                                      save_format='jpg'):
                i += 1
                if i >= kacar:
                    break 
            sayac += 1
        print("-> veriler çoğaltıldı")

class methods():
    def __init__(self):
        self.mover = mover()
        self.func = functions()
    
    def get_images(self):
        self.mover.go_editing()
        names = self.func.names_of_images()
        images = self.func.import_images_from_names(names)
        self.mover.go_back()
        return images
    
    def get_labels(self):
        self.mover.go_editing()
        names = self.func.names_of_images()
        howmuch = int(input("kaç kez ayrılacak : "))
        labels = self.func.do_split(names,howmuch)
        self.mover.go_back()
        return labels
    
    def show_data_distribution(self):
        labels = self.get_labels()
        self.func.make_plot(labels,"t",title="Distribution",color="gray")    
    
    def rename_images(self):
        labels = self.get_labels()
        images = self.get_images()
        self.mover.create_folder_on_created()
        self.mover.go_created()
        self.mover.go_new_created_file_on_created()
        self.func.save_images(labels,images)
        self.mover.go_back()
        self.mover.go_back()
        self.mover.refresh_folders()
        
    def apply_grays_scale(self):
        labels = self.get_labels()
        images = self.get_images()
        images = self.func.do_gray(images)
        self.mover.create_folder_on_created()
        self.mover.go_created()
        self.mover.go_new_created_file_on_created()
        self.func.save_images(labels,images)
        self.mover.go_back()
        self.mover.go_back()
        self.mover.refresh_folders()
    
    def make_bbox_files(self):
        labels = self.get_labels()
        self.mover.go_editing()
        self.func.make_bbox(labels)
        self.mover.go_back()
    
    def change_extansion(self):
        labels = self.get_labels()
        images = self.get_images()
        self.mover.create_folder_on_created()
        self.mover.go_created()
        self.mover.go_new_created_file_on_created()
        self.func.save_images(labels, images)
        self.mover.go_back()
        self.mover.go_back()
        self.mover.refresh_folders()
    
    def balanced_images(self):
        labels = self.get_labels()
        labels = self.func.decrease_data_according_to_lower_data(labels)
        self.mover.go_editing()
        names = self.func.names_of_images()
        names = self.func.decrease_data_according_to_lower_data(names)
        images = self.func.import_images_from_names(names)
        self.mover.go_back()
        self.mover.create_folder_on_created()
        self.mover.go_created()
        self.mover.go_new_created_file_on_created()
        self.func.save_images(labels, images)
        self.mover.go_back()
        self.mover.go_back()
        self.mover.refresh_folders()
    
    def reduce_images(self):
        self.mover.go_editing()
        names = self.func.names_of_images()
        names = self.func.decrease_photos(names)
        images = self.func.import_images_from_names(names)
        self.mover.go_back()
        self.mover.create_folder_on_created()
        self.mover.go_created()
        self.mover.go_new_created_file_on_created()
        self.func.save_images(names, images)
        self.mover.go_back()
        self.mover.go_back()
        self.mover.refresh_folders()
        

    def augment_images(self):
        labels = self.get_labels()
        images = self.get_images()
        self.mover.create_folder_on_created()
        self.mover.go_created()
        self.mover.go_new_created_file_on_created()
        self.func.augmanter(labels, images)
        self.mover.go_back()
        self.mover.go_back()
        time.sleep(10)
        self.mover.refresh_folders()  
        
    def video_to_images(self):
        self.mover.go_editing()
        self.func.bring_image_from_videos()
        self.mover.go_back()
        print("-> videoyu editing klasörnden siliniz")
        
a = methods()

