from editor import mover,functions,methods
import time
import os


def setup():
    if os.path.exists("archive"):
        pass
    else:
        print("-> Archive File is not exist")
        os.mkdir("archive")
        print("-> created")
        
    if os.path.exists("editing"):
        pass
    else:
        print("-> editing file is not exist")
        os.mkdir("editing")
        print("-> created")
    if os.path.exists("created"):
        pass
    else:
        print("-> created file is not exist")
        os.mkdir("created")
        print("-> created")
        
def show_options():
    print("\n-> 1 , Görsellerin dağılımını göster")
    print("\n-> 2 , Görsellerin ismini değiştir")
    print("\n-> 3 , Görsellere gri tonlama uygula")
    print("\n-> 4 , Görselleri bounding box olarak tanımla ve txt ye yaz")
    print("\n-> 5 , Görsellerin uzantısını değiştir")
    print("\n-> 6 , Görselleri en az sayıda olan türe göre azalt")
    print("\n-> 7 , Görselleri istenen oranda azalt")
    print("\n-> 8 , Görselleri istenen sayıda çoğalt")
    print("\n-> 9 , Videodan görseller getir")
    print("\n-> 0 , çıkmak için")




setup()

a = methods()    

while True:
    show_options()
    
    choise = int(input(" : "))
    
    if   choise == 1:
        a.show_data_distribution()
    elif choise == 2:
        a.rename_images()
    elif choise == 3:
        a.apply_grays_scale()
    elif choise == 4:
        a.make_bbox_files()
    elif choise == 5:
        a.change_extansion()
    elif choise == 6:
        a.balanced_images()
    elif choise == 7:
        a.reduce_images()
    elif choise == 8:
        a.augment_images()
    elif choise == 9:    
        a.video_to_images()
    elif choise == 0:
        break
    
    time.sleep(0.1)
