import pygame,rgb,time,random

pygame.init()
pygame.mixer.init()
window_x=1530
window_y=790
desert_eagle_x=100
desert_eagle_y=100
print("zeynepten hatıralar")
başla=True
choose1=True
choose2=True
i=1
hız=1
mermi_hız=15
check=0
cops_win=0
dağcı_win=0
cops_deneme=1
dağcı_deneme=1

dağcı_money=0
cops_money=0
awp_cost=1000
print("all about space and all about history and all about amal ")
desert_eagle_cost=0
m_16_cost=600
ak_47_cost=600

cops_gun="t"
dağcı_gun="t"

cops_mermi_yön={0}
dağcı_mermi_yön={0}

awp_mermi=5
ak_47_mermi=30
desert_eagle_mermi=15
m_16_mermi=30

dağcı_awp_mermi_toplam=10
dağcı_m_16_mermi_toplam=90
dağcı_ak_47_mermi_toplam=90
dağcı_desert_eagle_mermi_toplam=60

cops_awp_mermi_toplam=10
cops_m_16_mermi_toplam=90
cops_ak_47_mermi_toplam=90
cops_desert_eagle_mermi_toplam=60

dağcı_atılan_mermi=0
cops_atılan_mermi=0

d_shoot1=[]
d_shoot2=[]
d_shoot3=[]
d_shoot4=[]
d_shoot6=[]
d_shoot7=[]
d_shoot8=[]
d_shoot9=[]
c_shootj=[]
c_shootu=[]
c_shootm=[]
c_shootn=[]
c_shooty=[]
c_shootb=[]
c_shootg=[]
c_shoott=[]

awp_damage=[90,91,92,93,94,95,96,97,98,99,100]
desert_eagle_damage=[10,11,12,13,14,15]
m_16_damage=[20,25,30]
ak_47_damage=[20,21,22,23,24,25]

cops_health=100
dağcı_health=100

cops_x=10
cops_y=40
dağcı_x=1375
dağcı_y=670

awp=pygame.image.load("Assets/images/AWP.png")
desert_eagle=pygame.image.load("Assets/images/DESERT_EAGLE.png")
ak_47=pygame.image.load("Assets/images/KELEŞ.png")
m_16=pygame.image.load("Assets/images/M16.png")
special_corps_logo=pygame.image.load("Assets/images/ÖZEL_KUVVETLER_LOGO.png")
special_corps=pygame.image.load("Assets/images/ÖZEL_KUVVETLER.png")
dağcı_logo=pygame.image.load("Assets/images/TERRÖRİST_LOGO.png")
dağcı=pygame.image.load("Assets/images/TERRORİST.png")
mermi=pygame.image.load("Assets/images/mermi.png")

yazı_tipi_1=pygame.font.SysFont("Helvetica",25)
yazı_1=yazı_tipi_1.render("Özel Kuvvetler:{}$".format(cops_money),True,(0,0,0))
yazı_tipi_2=pygame.font.SysFont("Arial",25)
yazı_2=yazı_tipi_2.render("Teröristler:{}$".format(dağcı_money),True,(0,0,0))
yazı_tipi_3=pygame.font.SysFont("Arial",25)
yazı_3=yazı_tipi_3.render(f"Awp hasarı 100-90 arası fiyatı:{awp_cost}$",True,(0,0,0))
yazı_tipi_4=pygame.font.SysFont("Arial",25)
yazı_4=yazı_tipi_4.render(f"Desert eagle hasarı 15-5 arası fiyatı:{desert_eagle_cost}$",True,(0,0,0))
yazı_tipi_5=pygame.font.SysFont("Arial",25)
yazı_5=yazı_tipi_5.render(f"Hasarları 30-20 arası fiyatları:{m_16_cost}$",True,(0,0,0))
yazı_tipi_6=pygame.font.SysFont("Arial",50)
yazı_6=yazı_tipi_6.render("AL",True,(255,255,255))
yazı_tipi_7=pygame.font.SysFont("Arial",10)
yazı_tipi_8=pygame.font.SysFont("Arial",10)
yazı_tipi_9=pygame.font.SysFont("Arial",25)
yazı_tipi_10=pygame.font.SysFont("Arial",10)
yazı_tipi_11=pygame.font.SysFont("Arial",10)
yazı_tipi_12=pygame.font.SysFont("Arial",30)
yazı_tipi_13=pygame.font.SysFont("Arial",30)
yazı_tipi_14=pygame.font.SysFont("Arial",30)
yazı_tipi_15=pygame.font.SysFont("Arial",30)
yazı_tipi_16=pygame.font.SysFont("Arial",30)
yazı_14=yazı_tipi_14.render("POLİSLER KAZANDI",True,(255,255,255))
yazı_15=yazı_tipi_15.render("DAĞCILAR KAZANDI",True,(255,255,255))
yazı_16=yazı_tipi_16.render("BERABERE",True,(255,255,255))

window=pygame.display.set_mode((window_x, window_y),pygame.RESIZABLE)
window.fill((rgb.kum))

c_awp_al=pygame.Rect(420,320,75,75)
c_desert_eagle_al=pygame.Rect(270,80,75,75)
c_m_16_al=pygame.Rect(450,550,75,75)
t_awp_al=pygame.Rect(1060,320,75,75)
t_desert_eagle_al=pygame.Rect(1200,80,75,75)
t_ak_47_al=pygame.Rect(1050,550,75,75)

engel_1_x=600
engel_1_y=20
engel_2_x=600
engel_2_y=20
engel_3_x=200
engel_3_y=15
engel_4_x=200
engel_4_y=15
engel_5_x=15
engel_5_y=200
engel_6_x=15
engel_6_y=200

engel_1=pygame.Rect(250,0,engel_1_x,engel_1_y)
engel_2=pygame.Rect(250,150,engel_2_x,engel_2_y)
engel_3=pygame.Rect(1000,135,engel_3_x,engel_3_y)
engel_4=pygame.Rect(1310,600,engel_4_x,engel_4_y)
engel_5=pygame.Rect(250,175,engel_5_x,engel_5_y)
engel_6=pygame.Rect(815,590,engel_6_x,engel_6_y)

class cops:
    def __init__(self,can,para,silah):
        self.can=can
        self.para=para
        self.silah=silah
    def choose_awp(self,awp_cost):
        self.silah="awp"
        self.para-=awp_cost
    def choose_desert_eagle(self,desert_eagle_cost):
        self.silah="desert_eagle"
        self.para-=desert_eagle_cost
    def choose_m_16(self,m_16_cost):   
        self.silah="m_16"
        self.para-=m_16_cost

class terorist:
    def __init__(self,can,para,silah):
        self.can=can
        self.para=para
        self.silah=silah
    def choose_awp(self,awp_cost):
        self.silah="awp"
        self.para-=awp_cost
    def choose_desert_eagle(self,desert_eagle_cost):
        self.silah="desert_eagle"
        self.para-=desert_eagle_cost
    def choose_ak_47(self,ak_47_cost):
        self.silah="ak_47"
        self.para-=ak_47_cost

class awp_class:
    def __init__(self,hasar):
        self.hasar=hasar
    def shoot(self):
        awp_sound=pygame.mixer.Sound("AWP_Shooting.mp3")
        pygame.mixer.Sound.play(awp_sound)        

class desert_eagle_class:
    def __init__(self,hasar):
        self.hasar=hasar
    def shoot(self):
        desert_eagle_sound=pygame.mixer.Sound("Desert_Eagle_Shoot.mp3")
        pygame.mixer.Sound.play(desert_eagle_sound)
        
class m_16_class:
    def __init__(self,hasar):
        self.hasar=hasar
    def shoot(self):
        m_16_sound=pygame.mixer.Sound("m_16_Shoot.mp3",)
        pygame.mixer.Sound.play(m_16_sound)
        
class ak_47_class:
    def __init__(self,hasar):
        self.hasar=hasar
    def shoot(self):
        ak_47_sound=pygame.mixer.Sound("AK47_Shoot.mp3")
        pygame.mixer.Sound.play(ak_47_sound)
        
class cops_move:
    def __init__(self,cops_x,cops_y):
        self.cops_y=cops_y
        self.cops_x=cops_x
    def w(self):
        if engel_1.collidepoint(self.cops_x+10,self.cops_y-3):
            pass
        elif engel_1.collidepoint(self.cops_x+20,self.cops_y-3):
            pass
        elif engel_1.collidepoint(self.cops_x+30,self.cops_y-3):
            pass
        elif engel_1.collidepoint(self.cops_x+40,self.cops_y-3):
            pass
        elif engel_1.collidepoint(self.cops_x+50,self.cops_y-3):
            pass
        elif engel_1.collidepoint(self.cops_x+60,self.cops_y-3):
            pass
        elif engel_1.collidepoint(self.cops_x+70,self.cops_y-3):
            pass
        elif engel_1.collidepoint(self.cops_x+77,self.cops_y-3):
            pass
        elif engel_2.collidepoint(self.cops_x+10,self.cops_y-3):
            pass
        elif engel_2.collidepoint(self.cops_x+20,self.cops_y-3):
            pass
        elif engel_2.collidepoint(self.cops_x+30,self.cops_y-3):
            pass
        elif engel_2.collidepoint(self.cops_x+40,self.cops_y-3):
            pass
        elif engel_2.collidepoint(self.cops_x+50,self.cops_y-3):
            pass
        elif engel_2.collidepoint(self.cops_x+60,self.cops_y-3):
            pass
        elif engel_2.collidepoint(self.cops_x+70,self.cops_y-3):
            pass
        elif engel_2.collidepoint(self.cops_x+77,self.cops_y-3):
            pass
        elif engel_3.collidepoint(self.cops_x+10,self.cops_y-3):
            pass
        elif engel_3.collidepoint(self.cops_x+20,self.cops_y-3):
            pass
        elif engel_3.collidepoint(self.cops_x+30,self.cops_y-3):
            pass
        elif engel_3.collidepoint(self.cops_x+40,self.cops_y-3):
            pass
        elif engel_3.collidepoint(self.cops_x+50,self.cops_y-3):
            pass
        elif engel_3.collidepoint(self.cops_x+60,self.cops_y-3):
            pass
        elif engel_3.collidepoint(self.cops_x+70,self.cops_y-3):
            pass
        elif engel_3.collidepoint(self.cops_x+77,self.cops_y-3):
            pass
        elif engel_4.collidepoint(self.cops_x+10,self.cops_y-3):
            pass
        elif engel_4.collidepoint(self.cops_x+20,self.cops_y-3):
            pass
        elif engel_4.collidepoint(self.cops_x+30,self.cops_y-3):
            pass
        elif engel_4.collidepoint(self.cops_x+40,self.cops_y-3):
            pass
        elif engel_4.collidepoint(self.cops_x+50,self.cops_y-3):
            pass
        elif engel_4.collidepoint(self.cops_x+60,self.cops_y-3):
            pass
        elif engel_4.collidepoint(self.cops_x+70,self.cops_y-3):
            pass
        elif engel_4.collidepoint(self.cops_x+77,self.cops_y-3):
            pass
        elif engel_5.collidepoint(self.cops_x+10,self.cops_y-3):
            pass
        elif engel_5.collidepoint(self.cops_x+20,self.cops_y-3):
            pass
        elif engel_5.collidepoint(self.cops_x+30,self.cops_y-3):
            pass
        elif engel_5.collidepoint(self.cops_x+40,self.cops_y-3):
            pass
        elif engel_5.collidepoint(self.cops_x+60,self.cops_y-3):
            pass
        elif engel_5.collidepoint(self.cops_x+70,self.cops_y-3):
            pass
        elif engel_5.collidepoint(self.cops_x+77,self.cops_y-3):
            pass
        else:
            self.cops_y-=hız

    def s(self):
        if engel_2.collidepoint(self.cops_x+10,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_2.collidepoint(self.cops_x+20,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_2.collidepoint(self.cops_x+30,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_2.collidepoint(self.cops_x+40,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_2.collidepoint(self.cops_x+50,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_2.collidepoint(self.cops_x+60,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_2.collidepoint(self.cops_x+70,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_2.collidepoint(self.cops_x+77,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_3.collidepoint(self.cops_x+10,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_3.collidepoint(self.cops_x+20,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_3.collidepoint(self.cops_x+30,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_3.collidepoint(self.cops_x+40,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_3.collidepoint(self.cops_x+50,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_3.collidepoint(self.cops_x+60,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_3.collidepoint(self.cops_x+70,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_3.collidepoint(self.cops_x+77,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_4.collidepoint(self.cops_x+10,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_4.collidepoint(self.cops_x+20,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_4.collidepoint(self.cops_x+30,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_4.collidepoint(self.cops_x+40,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_4.collidepoint(self.cops_x+50,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_4.collidepoint(self.cops_x+60,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_4.collidepoint(self.cops_x+70,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_4.collidepoint(self.cops_x+77,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_6.collidepoint(self.cops_x+10,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_6.collidepoint(self.cops_x+20,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_6.collidepoint(self.cops_x+30,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_6.collidepoint(self.cops_x+40,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_6.collidepoint(self.cops_x+50,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_6.collidepoint(self.cops_x+60,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_6.collidepoint(self.cops_x+70,self.cops_y+special_corps_size_y+10):
            pass
        elif engel_6.collidepoint(self.cops_x+77,self.cops_y+special_corps_size_y+10):
            pass
        else:
            self.cops_y+=hız
    def a(self):
        if engel_1.collidepoint(self.cops_x,self.cops_y+10):
            pass
        elif engel_1.collidepoint(self.cops_x,self.cops_y+20):
            pass
        elif engel_1.collidepoint(self.cops_x,self.cops_y+30):
            pass
        elif engel_1.collidepoint(self.cops_x,self.cops_y+40):
            pass
        elif engel_1.collidepoint(self.cops_x,self.cops_y+50):
            pass
        elif engel_1.collidepoint(self.cops_x,self.cops_y+60):
            pass
        elif engel_1.collidepoint(self.cops_x,self.cops_y+70):
            pass
        elif engel_1.collidepoint(self.cops_x,self.cops_y+80):
            pass
        elif engel_1.collidepoint(self.cops_x,self.cops_y+90):
            pass
        elif engel_1.collidepoint(self.cops_x,self.cops_y+100):
            pass
        elif engel_2.collidepoint(self.cops_x,self.cops_y+10):
            pass
        elif engel_2.collidepoint(self.cops_x,self.cops_y+20):
            pass
        elif engel_2.collidepoint(self.cops_x,self.cops_y+30):
            pass
        elif engel_2.collidepoint(self.cops_x,self.cops_y+40):
            pass
        elif engel_2.collidepoint(self.cops_x,self.cops_y+50):
            pass
        elif engel_2.collidepoint(self.cops_x,self.cops_y+60):
            pass
        elif engel_2.collidepoint(self.cops_x,self.cops_y+70):
            pass
        elif engel_2.collidepoint(self.cops_x,self.cops_y+80):
            pass
        elif engel_2.collidepoint(self.cops_x,self.cops_y+90):
            pass
        elif engel_2.collidepoint(self.cops_x,self.cops_y+100):
            pass
        elif engel_3.collidepoint(self.cops_x,self.cops_y+10):
            pass
        elif engel_3.collidepoint(self.cops_x,self.cops_y+20):
            pass
        elif engel_3.collidepoint(self.cops_x,self.cops_y+30):
            pass
        elif engel_3.collidepoint(self.cops_x,self.cops_y+40):
            pass
        elif engel_3.collidepoint(self.cops_x,self.cops_y+50):
            pass
        elif engel_3.collidepoint(self.cops_x,self.cops_y+60):
            pass
        elif engel_3.collidepoint(self.cops_x,self.cops_y+70):
            pass
        elif engel_3.collidepoint(self.cops_x,self.cops_y+80):
            pass
        elif engel_3.collidepoint(self.cops_x,self.cops_y+90):
            pass
        elif engel_3.collidepoint(self.cops_x,self.cops_y+100):
            pass
        elif engel_5.collidepoint(self.cops_x-5,self.cops_y+10):
            pass
        elif engel_5.collidepoint(self.cops_x-5,self.cops_y+20):
            pass
        elif engel_5.collidepoint(self.cops_x-5,self.cops_y+30):
            pass
        elif engel_5.collidepoint(self.cops_x-5,self.cops_y+40):
            pass
        elif engel_5.collidepoint(self.cops_x-5,self.cops_y+50):
            pass
        elif engel_5.collidepoint(self.cops_x-5,self.cops_y+60):
            pass
        elif engel_5.collidepoint(self.cops_x-5,self.cops_y+70):
            pass
        elif engel_5.collidepoint(self.cops_x-5,self.cops_y+80):
            pass
        elif engel_5.collidepoint(self.cops_x-5,self.cops_y+90):
            pass
        elif engel_5.collidepoint(self.cops_x-5,self.cops_y+100):
            pass
        elif engel_6.collidepoint(self.cops_x-5,self.cops_y+10):
            pass
        elif engel_6.collidepoint(self.cops_x-5,self.cops_y+20):
            pass
        elif engel_6.collidepoint(self.cops_x-5,self.cops_y+30):
            pass
        elif engel_6.collidepoint(self.cops_x-5,self.cops_y+40):
            pass
        elif engel_6.collidepoint(self.cops_x-5,self.cops_y+50):
            pass
        elif engel_6.collidepoint(self.cops_x-5,self.cops_y+60):
            pass
        elif engel_6.collidepoint(self.cops_x-5,self.cops_y+70):
            pass
        elif engel_6.collidepoint(self.cops_x-5,self.cops_y+80):
            pass
        elif engel_6.collidepoint(self.cops_x-5,self.cops_y+90):
            pass
        elif engel_6.collidepoint(self.cops_x-5,self.cops_y+100):
            pass
        else:
            self.cops_x-=hız
    def d(self):
        if engel_1.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+10):
            pass
        elif engel_1.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+20):
            pass
        elif engel_1.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+30):
            pass
        elif engel_1.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+40):
            pass
        elif engel_1.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+50):
            pass
        elif engel_1.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+60):
            pass
        elif engel_1.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+70):
            pass
        elif engel_1.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+80):
            pass
        elif engel_1.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+90):
            pass
        elif engel_1.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+100):
            pass
        elif engel_2.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+10):
            pass
        elif engel_2.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+20):
            pass
        elif engel_2.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+30):
            pass
        elif engel_2.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+40):
            pass
        elif engel_2.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+50):
            pass
        elif engel_2.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+60):
            pass
        elif engel_2.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+70):
            pass
        elif engel_2.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+80):
            pass
        elif engel_2.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+90):
            pass
        elif engel_2.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+100):
            pass
        elif engel_3.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+10):
            pass
        elif engel_3.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+20):
            pass
        elif engel_3.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+30):
            pass
        elif engel_3.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+40):
            pass
        elif engel_3.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+50):
            pass
        elif engel_3.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+60):
            pass
        elif engel_3.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+70):
            pass
        elif engel_3.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+80):
            pass
        elif engel_3.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+90):
            pass
        elif engel_3.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+100):
            pass
        elif engel_4.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+10):
            pass
        elif engel_4.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+20):
            pass
        elif engel_4.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+30):
            pass
        elif engel_4.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+40):
            pass
        elif engel_4.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+50):
            pass
        elif engel_4.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+60):
            pass
        elif engel_4.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+70):
            pass
        elif engel_4.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+80):
            pass
        elif engel_4.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+90):
            pass
        elif engel_4.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+100):
            pass
        elif engel_5.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+10):
            pass
        elif engel_5.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+20):
            pass
        elif engel_5.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+30):
            pass
        elif engel_5.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+40):
            pass
        elif engel_5.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+50):
            pass
        elif engel_5.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+60):
            pass
        elif engel_5.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+70):
            pass
        elif engel_5.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+80):
            pass
        elif engel_5.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+90):
            pass
        elif engel_5.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+100):
            pass
        elif engel_6.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+10):
            pass
        elif engel_6.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+20):
            pass
        elif engel_6.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+30):
            pass
        elif engel_6.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+40):
            pass
        elif engel_6.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+50):
            pass
        elif engel_6.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+60):
            pass
        elif engel_6.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+70):
            pass
        elif engel_6.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+80):
            pass
        elif engel_6.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+90):
            pass
        elif engel_6.collidepoint(self.cops_x+special_corps_size_x+10,self.cops_y+100):
            pass
        else:
            self.cops_x+=hız
    
class dağcılar_moves:

    def __init__(self,dağcı_x,dağcı_y):
        self.dağcı_x=dağcı_x
        self.dağcı_y=dağcı_y
    def up(self):
        if engel_1.collidepoint(self.dağcı_x+10,self.dağcı_y):
            pass
        elif engel_1.collidepoint(self.dağcı_x+20,self.dağcı_y):
            pass
        elif engel_1.collidepoint(self.dağcı_x+30,self.dağcı_y):
            pass
        elif engel_1.collidepoint(self.dağcı_x+40,self.dağcı_y):
            pass
        elif engel_1.collidepoint(self.dağcı_x+50,self.dağcı_y):
            pass
        elif engel_1.collidepoint(self.dağcı_x+60,self.dağcı_y):
            pass
        elif engel_1.collidepoint(self.dağcı_x+70,self.dağcı_y):
            pass
        elif engel_1.collidepoint(self.dağcı_x+77,self.dağcı_y):
            pass
        elif engel_2.collidepoint(self.dağcı_x+10,self.dağcı_y-3):
            pass
        elif engel_2.collidepoint(self.dağcı_x+20,self.dağcı_y-3):
            pass
        elif engel_2.collidepoint(self.dağcı_x+30,self.dağcı_y-3):
            pass
        elif engel_2.collidepoint(self.dağcı_x+40,self.dağcı_y-3):
            pass
        elif engel_2.collidepoint(self.dağcı_x+50,self.dağcı_y-3):
            pass
        elif engel_2.collidepoint(self.dağcı_x+60,self.dağcı_y-3):
            pass
        elif engel_2.collidepoint(self.dağcı_x+70,self.dağcı_y-3):
            pass
        elif engel_2.collidepoint(self.dağcı_x+77,self.dağcı_y-3):
            pass
        elif engel_3.collidepoint(self.dağcı_x+10,self.dağcı_y):
            pass
        elif engel_3.collidepoint(self.dağcı_x+20,self.dağcı_y):
            pass
        elif engel_3.collidepoint(self.dağcı_x+30,self.dağcı_y):
            pass
        elif engel_3.collidepoint(self.dağcı_x+40,self.dağcı_y):
            pass
        elif engel_3.collidepoint(self.dağcı_x+50,self.dağcı_y):
            pass
        elif engel_3.collidepoint(self.dağcı_x+60,self.dağcı_y):
            pass
        elif engel_3.collidepoint(self.dağcı_x+70,self.dağcı_y):
            pass
        elif engel_3.collidepoint(self.dağcı_x+77,self.dağcı_y):
            pass
        elif engel_4.collidepoint(self.dağcı_x+10,self.dağcı_y):
            pass
        elif engel_4.collidepoint(self.dağcı_x+20,self.dağcı_y):
            pass
        elif engel_4.collidepoint(self.dağcı_x+30,self.dağcı_y):
            pass
        elif engel_4.collidepoint(self.dağcı_x+40,self.dağcı_y):
            pass
        elif engel_4.collidepoint(self.dağcı_x+50,self.dağcı_y):
            pass
        elif engel_4.collidepoint(self.dağcı_x+60,self.dağcı_y):
            pass
        elif engel_4.collidepoint(self.dağcı_x+70,self.dağcı_y):
            pass
        elif engel_4.collidepoint(self.dağcı_x+77,self.dağcı_y):
            pass
        elif engel_5.collidepoint(self.dağcı_x+10,self.dağcı_y):
            pass
        elif engel_5.collidepoint(self.dağcı_x+20,self.dağcı_y):
            pass
        elif engel_5.collidepoint(self.dağcı_x+30,self.dağcı_y):
            pass
        elif engel_5.collidepoint(self.dağcı_x+40,self.dağcı_y):
            pass
        elif engel_5.collidepoint(self.dağcı_x+50,self.dağcı_y):
            pass
        elif engel_5.collidepoint(self.dağcı_x+60,self.dağcı_y):
            pass
        elif engel_5.collidepoint(self.dağcı_x+70,self.dağcı_y):
            pass
        elif engel_5.collidepoint(self.dağcı_x+77,self.dağcı_y):
            pass
        else:
            self.dağcı_y-=hız
    def down(self):
        print(self.dağcı_x)
        if engel_2.collidepoint(self.dağcı_x+10,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_2.collidepoint(self.dağcı_x+20,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_2.collidepoint(self.dağcı_x+30,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_2.collidepoint(self.dağcı_x+40,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_2.collidepoint(self.dağcı_x+50,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_2.collidepoint(self.dağcı_x+60,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_2.collidepoint(self.dağcı_x+70,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_2.collidepoint(self.dağcı_x+77,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_3.collidepoint(self.dağcı_x+10,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_3.collidepoint(self.dağcı_x+20,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_3.collidepoint(self.dağcı_x+30,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_3.collidepoint(self.dağcı_x+40,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_3.collidepoint(self.dağcı_x+50,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_3.collidepoint(self.dağcı_x+60,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_3.collidepoint(self.dağcı_x+70,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_3.collidepoint(self.dağcı_x+77,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_4.collidepoint(self.dağcı_x+10,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_4.collidepoint(self.dağcı_x+20,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_4.collidepoint(self.dağcı_x+30,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_4.collidepoint(self.dağcı_x+40,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_4.collidepoint(self.dağcı_x+50,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_4.collidepoint(self.dağcı_x+60,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_4.collidepoint(self.dağcı_x+70,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_4.collidepoint(self.dağcı_x+77,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_6.collidepoint(self.dağcı_x+10,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_6.collidepoint(self.dağcı_x+20,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_6.collidepoint(self.dağcı_x+30,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_6.collidepoint(self.dağcı_x+40,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_6.collidepoint(self.dağcı_x+50,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_6.collidepoint(self.dağcı_x+60,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_6.collidepoint(self.dağcı_x+70,self.dağcı_y+special_corps_size_y+10):
            pass
        elif engel_6.collidepoint(self.dağcı_x+77,self.dağcı_y+special_corps_size_y+10):
            pass
        else:
            self.dağcı_y+=hız
    def left(self):
        if engel_1.collidepoint(self.dağcı_x,self.dağcı_y+10):
            pass
        elif engel_1.collidepoint(self.dağcı_x,self.dağcı_y+20):
            pass
        elif engel_1.collidepoint(self.dağcı_x,self.dağcı_y+30):
            pass
        elif engel_1.collidepoint(self.dağcı_x,self.dağcı_y+40):
            pass
        elif engel_1.collidepoint(self.dağcı_x,self.dağcı_y+50):
            pass
        elif engel_1.collidepoint(self.dağcı_x,self.dağcı_y+60):
            pass
        elif engel_1.collidepoint(self.dağcı_x,self.dağcı_y+70):
            pass
        elif engel_1.collidepoint(self.dağcı_x,self.dağcı_y+80):
            pass
        elif engel_1.collidepoint(self.dağcı_x,self.dağcı_y+90):
            pass
        elif engel_1.collidepoint(self.dağcı_x,self.dağcı_y+100):
            pass
        elif engel_2.collidepoint(self.dağcı_x,self.dağcı_y+10):
            pass
        elif engel_2.collidepoint(self.dağcı_x,self.dağcı_y+20):
            pass
        elif engel_2.collidepoint(self.dağcı_x,self.dağcı_y+30):
            pass
        elif engel_2.collidepoint(self.dağcı_x,self.dağcı_y+40):
            pass
        elif engel_2.collidepoint(self.dağcı_x,self.dağcı_y+50):
            pass
        elif engel_2.collidepoint(self.dağcı_x,self.dağcı_y+60):
            pass
        elif engel_2.collidepoint(self.dağcı_x,self.dağcı_y+70):
            pass
        elif engel_2.collidepoint(self.dağcı_x,self.dağcı_y+80):
            pass
        elif engel_2.collidepoint(self.dağcı_x,self.dağcı_y+90):
            pass
        elif engel_2.collidepoint(self.dağcı_x,self.dağcı_y+100):
            pass
        elif engel_3.collidepoint(self.dağcı_x,self.dağcı_y+10):
            pass
        elif engel_3.collidepoint(self.dağcı_x,self.dağcı_y+20):
            pass
        elif engel_3.collidepoint(self.dağcı_x,self.dağcı_y+30):
            pass
        elif engel_3.collidepoint(self.dağcı_x,self.dağcı_y+40):
            pass
        elif engel_3.collidepoint(self.dağcı_x,self.dağcı_y+50):
            pass
        elif engel_3.collidepoint(self.dağcı_x,self.dağcı_y+60):
            pass
        elif engel_3.collidepoint(self.dağcı_x,self.dağcı_y+70):
            pass
        elif engel_3.collidepoint(self.dağcı_x,self.dağcı_y+80):
            pass
        elif engel_3.collidepoint(self.dağcı_x,self.dağcı_y+90):
            pass
        elif engel_3.collidepoint(self.dağcı_x,self.dağcı_y+100):
            pass
        elif engel_5.collidepoint(self.dağcı_x-5,self.dağcı_y+10):
            pass
        elif engel_5.collidepoint(self.dağcı_x-5,self.dağcı_y+20):
            pass
        elif engel_5.collidepoint(self.dağcı_x-5,self.dağcı_y+30):
            pass
        elif engel_5.collidepoint(self.dağcı_x-5,self.dağcı_y+40):
            pass
        elif engel_5.collidepoint(self.dağcı_x-5,self.dağcı_y+50):
            pass
        elif engel_5.collidepoint(self.dağcı_x-5,self.dağcı_y+60):
            pass
        elif engel_5.collidepoint(self.dağcı_x-5,self.dağcı_y+70):
            pass
        elif engel_5.collidepoint(self.dağcı_x-5,self.dağcı_y+80):
            pass
        elif engel_5.collidepoint(self.dağcı_x-5,self.dağcı_y+90):
            pass
        elif engel_5.collidepoint(self.dağcı_x-5,self.dağcı_y+100):
            pass
        elif engel_6.collidepoint(self.dağcı_x-5,self.dağcı_y+10):
            pass
        elif engel_6.collidepoint(self.dağcı_x-5,self.dağcı_y+20):
            pass
        elif engel_6.collidepoint(self.dağcı_x-5,self.dağcı_y+30):
            pass
        elif engel_6.collidepoint(self.dağcı_x-5,self.dağcı_y+40):
            pass
        elif engel_6.collidepoint(self.dağcı_x-5,self.dağcı_y+50):
            pass
        elif engel_6.collidepoint(self.dağcı_x-5,self.dağcı_y+60):
            pass
        elif engel_6.collidepoint(self.dağcı_x-5,self.dağcı_y+70):
            pass
        elif engel_6.collidepoint(self.dağcı_x-5,self.dağcı_y+80):
            pass
        elif engel_6.collidepoint(self.dağcı_x-5,self.dağcı_y+90):
            pass
        elif engel_6.collidepoint(self.dağcı_x-5,self.dağcı_y+100):
            pass
        else:
            self.dağcı_x-=hız
    def right(self):
        if engel_1.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+10):
            pass
        elif engel_1.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+20):
            pass
        elif engel_1.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+30):
            pass
        elif engel_1.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+40):
            pass
        elif engel_1.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+50):
            pass
        elif engel_1.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+60):
            pass
        elif engel_1.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+70):
            pass
        elif engel_1.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+80):
            pass
        elif engel_1.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+90):
            pass
        elif engel_1.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+100):
            pass
        elif engel_2.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+10):
            pass
        elif engel_2.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+20):
            pass
        elif engel_2.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+30):
            pass
        elif engel_2.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+40):
            pass
        elif engel_2.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+50):
            pass
        elif engel_2.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+60):
            pass
        elif engel_2.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+70):
            pass
        elif engel_2.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+80):
            pass
        elif engel_2.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+90):
            pass
        elif engel_2.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+100):
            pass
        elif engel_3.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+10):
            pass
        elif engel_3.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+20):
            pass
        elif engel_3.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+30):
            pass
        elif engel_3.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+40):
            pass
        elif engel_3.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+50):
            pass
        elif engel_3.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+60):
            pass
        elif engel_3.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+70):
            pass
        elif engel_3.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+80):
            pass
        elif engel_3.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+90):
            pass
        elif engel_3.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+100):
            pass
        elif engel_4.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+10):
            pass
        elif engel_4.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+20):
            pass
        elif engel_4.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+30):
            pass
        elif engel_4.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+40):
            pass
        elif engel_4.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+50):
            pass
        elif engel_4.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+60):
            pass
        elif engel_4.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+70):
            pass
        elif engel_4.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+80):
            pass
        elif engel_4.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+90):
            pass
        elif engel_4.collidepoint(self.dağcı_x+dağcılar_size_x,self.dağcı_y+100):
            pass
        elif engel_5.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+10):
            pass
        elif engel_5.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+20):
            pass
        elif engel_5.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+30):
            pass
        elif engel_5.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+40):
            pass
        elif engel_5.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+50):
            pass
        elif engel_5.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+60):
            pass
        elif engel_5.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+70):
            pass
        elif engel_5.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+80):
            pass
        elif engel_5.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+90):
            pass
        elif engel_5.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+100):
            pass
        elif engel_6.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+80):
            pass
        elif engel_6.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+10):
            pass
        elif engel_6.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+20):
            pass
        elif engel_6.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+30):
            pass
        elif engel_6.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+40):
            pass
        elif engel_6.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+50):
            pass
        elif engel_6.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+60):
            pass
        elif engel_6.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+70):
            pass
        elif engel_6.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+90):
            pass
        elif engel_6.collidepoint(self.dağcı_x+dağcılar_size_x+10,self.dağcı_y+100):
            pass
        else:
            self.dağcı_x+=hız

class dağcı_bullet:
    def __init__(self,d_shoot1,d_shoot2,d_shoot3,d_shoot4,d_shoot6,d_shoot7,d_shoot8,d_shoot9):
        self.d_shoot1=d_shoot1
        self.d_shoot2=d_shoot2
        self.d_shoot3=d_shoot3
        self.d_shoot4=d_shoot4
        self.d_shoot6=d_shoot6
        self.d_shoot7=d_shoot7
        self.d_shoot8=d_shoot8
        self.d_shoot9=d_shoot9
    def awp_shoot1(self):
        shoot_1_x=dağcılar_move.dağcı_x+30
        shoot_1_y=dağcılar_move.dağcı_y+dağcılar_size_y
        d_shoot1.append(shoot_1_x)
        d_shoot1.append(shoot_1_y)

    def awp_shoot2(self):
        shoot_2_x=dağcılar_move.dağcı_x+dağcılar_size_x//2+17
        shoot_2_y=dağcılar_move.dağcı_y+dağcılar_size_y
        d_shoot2.append(shoot_2_x)
        d_shoot2.append(shoot_2_y)

    def awp_shoot3(self):
        shoot_3_x=dağcılar_move.dağcı_x+dağcılar_size_x
        shoot_3_y=dağcılar_move.dağcı_y+dağcılar_size_y
        d_shoot3.append(shoot_3_x)
        d_shoot3.append(shoot_3_y)

    def awp_shoot4(self):
        shoot_4_x=dağcılar_move.dağcı_x
        shoot_4_y=dağcılar_move.dağcı_y+dağcılar_size_y//2
        d_shoot4.append(shoot_4_x)
        d_shoot4.append(shoot_4_y)

    def awp_shoot6(self):
        shoot_6_x=dağcılar_move.dağcı_x+dağcılar_size_x
        shoot_6_y=dağcılar_move.dağcı_y+dağcılar_size_y//2
        d_shoot6.append(shoot_6_x)
        d_shoot6.append(shoot_6_y)
    def awp_shoot7(self):
        shoot_7_x=dağcılar_move.dağcı_x+30
        shoot_7_y=dağcılar_move.dağcı_y
        d_shoot7.append(shoot_7_x)
        d_shoot7.append(shoot_7_y)

    def awp_shoot8(self):
        shoot_8_x=dağcılar_move.dağcı_x+dağcılar_size_x//2+17
        shoot_8_y=dağcılar_move.dağcı_y
        d_shoot8.append(shoot_8_x)
        d_shoot8.append(shoot_8_y)
    
    def awp_shoot9(self):
        shoot_9_x=dağcılar_move.dağcı_x+dağcılar_size_x
        shoot_9_y=dağcılar_move.dağcı_y
        d_shoot9.append(shoot_9_x)
        d_shoot9.append(shoot_9_y)
    
    def desert_eagle_shoot1(self):
        shoot1_x=dağcılar_move.dağcı_x+30
        shoot1_y=dağcılar_move.dağcı_y+dağcılar_size_y
        d_shoot1.append(shoot1_x)
        d_shoot1.append(shoot1_y)
    
    def desert_eagle_shoot2(self):
        shoot2_x=dağcılar_move.dağcı_x+dağcılar_size_x//2+17
        shoot2_y=dağcılar_move.dağcı_y+dağcılar_size_y
        d_shoot2.append(shoot2_x)
        d_shoot2.append(shoot2_y)

    def desert_eagle_shoot3(self):
        shoot3_x=dağcılar_move.dağcı_x+dağcılar_size_x
        shoot3_y=dağcılar_move.dağcı_y+dağcılar_size_y
        d_shoot3.append(shoot3_x)
        d_shoot3.append(shoot3_y)
    
    def desert_eagle_shoot4(self):
        shoot4_x=dağcılar_move.dağcı_x
        shoot4_y=dağcılar_move.dağcı_y+dağcılar_size_y//2
        d_shoot4.append(shoot4_x)
        d_shoot4.append(shoot4_y)
    
    def desert_eagle_shoot6(self):
        shoot6_x=dağcılar_move.dağcı_x+dağcılar_size_x
        shoot6_y=dağcılar_move.dağcı_y+dağcılar_size_y//2
        d_shoot6.append(shoot6_x)
        d_shoot6.append(shoot6_y)

    def desert_eagle_shoot7(self):
        shoot7_x=dağcılar_move.dağcı_x+30
        shoot7_y=dağcılar_move.dağcı_y
        d_shoot7.append(shoot7_x)
        d_shoot7.append(shoot7_y)
    
    def desert_eagle_shoot8(self):
        shoot8_x=dağcılar_move.dağcı_x+dağcılar_size_x//2+17
        shoot8_y=dağcılar_move.dağcı_y
        d_shoot8.append(shoot8_x)
        d_shoot8.append(shoot8_y)

    def desert_eagle_shoot9(self):
        shoot9_x=dağcılar_move.dağcı_x+dağcılar_size_x
        shoot9_y=dağcılar_move.dağcı_y
        d_shoot9.append(shoot9_x)
        d_shoot9.append(shoot9_y)
    
    def ak_47_shoot1(self):
        shoot1_x=dağcılar_move.dağcı_x+30
        shoot1_y=dağcılar_move.dağcı_y+dağcılar_size_y//2
        d_shoot1.append(shoot1_x)
        d_shoot1.append(shoot1_y)
    
    def ak_47_shoot2(self):
        shoot2_x=dağcılar_move.dağcı_x+dağcılar_size_x//2+17
        shoot2_y=dağcılar_move.dağcı_y+dağcılar_size_y
        d_shoot2.append(shoot2_x)
        d_shoot2.append(shoot2_y)

    def ak_47_shoot3(self):
        shoot3_x=dağcılar_move.dağcı_x+dağcılar_size_x
        shoot3_y=dağcılar_move.dağcı_y+dağcılar_size_y
        d_shoot3.append(shoot3_x)
        d_shoot3.append(shoot3_y)
    
    def ak_47_shoot4(self):
        shoot4_x=dağcılar_move.dağcı_x
        shoot4_y=dağcılar_move.dağcı_y+dağcılar_size_y//2
        d_shoot4.append(shoot4_x)
        d_shoot4.append(shoot4_y)
    
    def ak_47_shoot6(self):
        shoot6_x=dağcılar_move.dağcı_x+dağcılar_size_x
        shoot6_y=dağcılar_move.dağcı_y+dağcılar_size_y//2
        d_shoot6.append(shoot6_x)
        d_shoot6.append(shoot6_y)

    def ak_47_shoot7(self):
        shoot7_x=dağcılar_move.dağcı_x+30
        shoot7_y=dağcılar_move.dağcı_y
        d_shoot7.append(shoot7_x)
        d_shoot7.append(shoot7_y)
    
    def ak_47_shoot8(self):
        shoot8_x=dağcılar_move.dağcı_x+dağcılar_size_x//2+17
        shoot8_y=dağcılar_move.dağcı_y
        d_shoot8.append(shoot8_x)
        d_shoot8.append(shoot8_y)

    def ak_47_shoot9(self):
        shoot9_x=dağcılar_move.dağcı_x+dağcılar_size_x
        shoot9_y=dağcılar_move.dağcı_y
        d_shoot9.append(shoot9_x)
        d_shoot9.append(shoot9_y)
  
    def awp_shoot1_isabet(self,i):
        special_forces.can-=random.choice(awp_damage)
        dağcı_mermi.d_shoot1.pop(index+1)
        dağcı_mermi.d_shoot1.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(1)
            
            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot1.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def awp_shoot2_isabet(self,i):
        special_forces.can-=random.choice(awp_damage)
        dağcı_mermi.d_shoot2.pop(index+1)
        dağcı_mermi.d_shoot2.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(2)
            
            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot2.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def awp_shoot3_isabet(self,i):
        special_forces.can-=random.choice(awp_damage)
        dağcı_mermi.d_shoot3.pop(index+1)
        dağcı_mermi.d_shoot3.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(3)
            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot3.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def awp_shoot4_isabet(self,i):
        special_forces.can-=random.choice(awp_damage)
        dağcı_mermi.d_shoot4.pop(index+1)
        dağcı_mermi.d_shoot4.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(4)
            
            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot4.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def awp_shoot6_isabet(self,i):
        special_forces.can-=random.choice(awp_damage)
        dağcı_mermi.d_shoot6.pop(index+1)
        dağcı_mermi.d_shoot6.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(6)
            
            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot6.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def awp_shoot7_isabet(self,i):
        special_forces.can-=random.choice(awp_damage)
        dağcı_mermi.d_shoot7.pop(index+1)
        dağcı_mermi.d_shoot7.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(7)
            
            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot7.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def awp_shoot8_isabet(self,i):
        special_forces.can-=random.choice(awp_damage)
        dağcı_mermi.d_shoot8.pop(index+1)
        dağcı_mermi.d_shoot8.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(8)
            
            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot8.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def awp_shoot9_isabet(self,i):
        special_forces.can-=random.choice(awp_damage)
        dağcı_mermi.d_shoot9.pop(index+1)
        dağcı_mermi.d_shoot9.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(9)
            
            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot9.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def desert_eagle_shoot1_isabet(self,i):
        special_forces.can-=random.choice(desert_eagle_damage)
        dağcı_mermi.d_shoot1.pop(index+1)
        dağcı_mermi.d_shoot1.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(1)
            
            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot1.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def desert_eagle_shoot2_isabet(self,i):
        special_forces.can-=random.choice(desert_eagle_damage)
        dağcı_mermi.d_shoot2.pop(index+1)
        dağcı_mermi.d_shoot2.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(2)
            
            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot2.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def desert_eagle_shoot3_isabet(self,i):
        special_forces.can-=random.choice(desert_eagle_damage)
        dağcı_mermi.d_shoot3.pop(index+1)
        dağcı_mermi.d_shoot3.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(3)
            
            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot3.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def desert_eagle_shoot4_isabet(self,i):
        special_forces.can-=random.choice(desert_eagle_damage)
        dağcı_mermi.d_shoot4.pop(index+1)
        dağcı_mermi.d_shoot4.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(4)
            
            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot4.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def desert_eagle_shoot6_isabet(self,i):
        special_forces.can-=random.choice(desert_eagle_damage)
        dağcı_mermi.d_shoot6.pop(index+1)
        dağcı_mermi.d_shoot6.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(6)
            
            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot6.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def desert_eagle_shoot7_isabet(self,i):
        special_forces.can-=random.choice(desert_eagle_damage)
        dağcı_mermi.d_shoot7.pop(index+1)
        dağcı_mermi.d_shoot7.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(7)
            
            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot7.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def desert_eagle_shoot8_isabet(self,i):
        special_forces.can-=random.choice(desert_eagle_damage)
        dağcı_mermi.d_shoot8.pop(index+1)
        dağcı_mermi.d_shoot8.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(8)
            
            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot8.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def desert_eagle_shoot9_isabet(self,i):
        special_forces.can-=random.choice(desert_eagle_damage)
        dağcı_mermi.d_shoot9.pop(index+1)
        dağcı_mermi.d_shoot9.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(9)
            
            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot9.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def ak_47_shoot1_isabet(self,i):
        special_forces.can-=random.choice(ak_47_damage)
        dağcı_mermi.d_shoot1.pop(index+1)
        dağcı_mermi.d_shoot1.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(1)
            
            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot1.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def ak_47_shoot2_isabet(self,i):
        special_forces.can-=random.choice(ak_47_damage)
        dağcı_mermi.d_shoot2.pop(index+1)
        dağcı_mermi.d_shoot2.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(2)
            
            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot2.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def ak_47_shoot3_isabet(self,i):
        special_forces.can-=random.choice(ak_47_damage)
        dağcı_mermi.d_shoot3.pop(index+1)
        dağcı_mermi.d_shoot3.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(3)
            
            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot3.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def ak_47_shoot4_isabet(self,i):
        special_forces.can-=random.choice(ak_47_damage)
        dağcı_mermi.d_shoot4.pop(index+1)
        dağcı_mermi.d_shoot4.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(4)
            
            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot4.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def ak_47_shoot6_isabet(self,i):
        special_forces.can-=random.choice(ak_47_damage)
        dağcı_mermi.d_shoot6.pop(index+1)
        dağcı_mermi.d_shoot6.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(6)
            
            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot6.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def ak_47_shoot7_isabet(self,i):
        special_forces.can-=random.choice(ak_47_damage)
        dağcı_mermi.d_shoot7.pop(index+1)
        dağcı_mermi.d_shoot7.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(7)
            
            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot7.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def ak_47_shoot8_isabet(self,i):
        special_forces.can-=random.choice(ak_47_damage)
        dağcı_mermi.d_shoot8.pop(index+1)
        dağcı_mermi.d_shoot8.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(8)
            
            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot8.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def ak_47_shoot9_isabet(self,i):
        special_forces.can-=random.choice(ak_47_damage)
        dağcı_mermi.d_shoot9.pop(index+1)
        dağcı_mermi.d_shoot9.pop(index)
        if special_forces.can<=0:
            dağcı_mermi_yön.remove(9)

            special_forces.para+=0
            dağcılar.para+=1500
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            d_shoot9.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def shoot1_collide(self,index):
        if engel_1.collidepoint(d_shoot1[index],d_shoot1[index+1]):
            return 0
        if engel_2.collidepoint(d_shoot1[index],d_shoot1[index+1]):
            return 0
        if engel_3.collidepoint(d_shoot1[index],d_shoot1[index+1]):
            return 0
        if engel_4.collidepoint(d_shoot1[index],d_shoot1[index+1]):
            return 0
        if engel_5.collidepoint(d_shoot1[index],d_shoot1[index+1]):
            return 0
        if engel_6.collidepoint(d_shoot1[index],d_shoot1[index+1]):
            return 0
        if special_forces_rect.collidepoint(d_shoot1[index],d_shoot1[index+1]):
            return 2
        else:
            return 1
    def shoot2_collide(self,index):
        if engel_1.collidepoint(d_shoot2[index],d_shoot2[index+1]):
            return 0
        if engel_2.collidepoint(d_shoot2[index],d_shoot2[index+1]):
            return 0
        if engel_3.collidepoint(d_shoot2[index],d_shoot2[index+1]):
            return 0
        if engel_4.collidepoint(d_shoot2[index],d_shoot2[index+1]):
            return 0
        if engel_5.collidepoint(d_shoot2[index],d_shoot2[index+1]):
            return 0
        if engel_6.collidepoint(d_shoot2[index],d_shoot2[index+1]):
            return 0
        if special_forces_rect.collidepoint(d_shoot2[index],d_shoot2[index+1]):
            return 2
        else:
            return 1
    def shoot3_collide(self,index):
        if engel_1.collidepoint(d_shoot3[index],d_shoot3[index+1]):
            return 0
        if engel_2.collidepoint(d_shoot3[index],d_shoot3[index+1]):
            return 0
        if engel_3.collidepoint(d_shoot3[index],d_shoot3[index+1]):
            return 0
        if engel_4.collidepoint(d_shoot3[index],d_shoot3[index+1]):
            return 0
        if engel_5.collidepoint(d_shoot3[index],d_shoot3[index+1]):
            return 0
        if engel_6.collidepoint(d_shoot3[index],d_shoot3[index+1]):
            return 0
        if special_forces_rect.collidepoint(d_shoot3[index],d_shoot3[index+1]):
            return 2
        else:
            return 1
    def shoot4_collide(self,index):
        if engel_1.collidepoint(d_shoot4[index],d_shoot4[index+1]):
            return 0
        if engel_2.collidepoint(d_shoot4[index],d_shoot4[index+1]):
            return 0
        if engel_3.collidepoint(d_shoot4[index],d_shoot4[index+1]):
            return 0
        if engel_4.collidepoint(d_shoot4[index],d_shoot4[index+1]):
            return 0
        if engel_5.collidepoint(d_shoot4[index],d_shoot4[index+1]):
            return 0
        if engel_6.collidepoint(d_shoot4[index],d_shoot4[index+1]):
            return 0
        if special_forces_rect.collidepoint(d_shoot4[index],d_shoot4[index+1]):
            return 2
        else:
            return 1
    def shoot6_collide(self,index):
        if engel_1.collidepoint(d_shoot6[index],d_shoot6[index+1]):
            return 0
        if engel_2.collidepoint(d_shoot6[index],d_shoot6[index+1]):
            return 0
        if engel_3.collidepoint(d_shoot6[index],d_shoot6[index+1]):
            return 0
        if engel_4.collidepoint(d_shoot6[index],d_shoot6[index+1]):
            return 0
        if engel_5.collidepoint(d_shoot6[index],d_shoot6[index+1]):
            return 0
        if engel_6.collidepoint(d_shoot6[index],d_shoot6[index+1]):
            return 0
        if special_forces_rect.collidepoint(d_shoot6[index],d_shoot6[index+1]):
            return 2
        else:
            return 1
    def shoot7_collide(self,index):
        if engel_1.collidepoint(d_shoot7[index],d_shoot7[index+1]):
            return 0
        if engel_2.collidepoint(d_shoot7[index],d_shoot7[index+1]):
            return 0
        if engel_3.collidepoint(d_shoot7[index],d_shoot7[index+1]):
            return 0
        if engel_4.collidepoint(d_shoot7[index],d_shoot7[index+1]):
            return 0
        if engel_5.collidepoint(d_shoot7[index],d_shoot7[index+1]):
            return 0
        if engel_6.collidepoint(d_shoot7[index],d_shoot7[index+1]):
            return 0
        if special_forces_rect.collidepoint(d_shoot7[index],d_shoot7[index+1]):
            return 2
        else:
            return 1
    def shoot8_collide(self,index):
        if engel_1.collidepoint(d_shoot8[index],d_shoot8[index+1]):
            return 0
        if engel_2.collidepoint(d_shoot8[index],d_shoot8[index+1]):
            return 0
        if engel_3.collidepoint(d_shoot8[index],d_shoot8[index+1]):
            return 0
        if engel_4.collidepoint(d_shoot8[index],d_shoot8[index+1]):
            return 0
        if engel_5.collidepoint(d_shoot8[index],d_shoot8[index+1]):
            return 0
        if engel_6.collidepoint(d_shoot8[index],d_shoot8[index+1]):
            return 0
        if special_forces_rect.collidepoint(d_shoot8[index],d_shoot8[index+1]):
            return 2
        else:
            return 1
    def shoot9_collide(self,index):
        if engel_1.collidepoint(d_shoot9[index],d_shoot9[index+1]):
            return 0
        if engel_2.collidepoint(d_shoot9[index],d_shoot9[index+1]):
            return 0
        if engel_3.collidepoint(d_shoot9[index],d_shoot9[index+1]):
            return 0
        if engel_4.collidepoint(d_shoot9[index],d_shoot9[index+1]):
            return 0
        if engel_5.collidepoint(d_shoot9[index],d_shoot9[index+1]):
            return 0
        if engel_6.collidepoint(d_shoot9[index],d_shoot9[index+1]):
            return 0
        if special_forces_rect.collidepoint(d_shoot9[index],d_shoot9[index+1]):
            return 2
        else:
            return 1

class cops_bullet:
    def __init__(self,c_shootj,c_shootu,c_shootm,c_shootn,c_shooty,c_shootb,c_shootg,c_shoott):
        self.c_shootj=c_shootj
        self.c_shootu=c_shootu
        self.c_shootm=c_shootm
        self.c_shootn=c_shootn
        self.c_shooty=c_shooty
        self.c_shootb=c_shootb
        self.c_shootg=c_shootg
        self.c_shoott=c_shoott
    def awp_shoot1(self):
        self.shoot1_x=special_forces_move.cops_x+special_corps_size_x
        self.shoot1_y=special_forces_move.cops_y+special_corps_size_y//2
        c_shootj.append(self.shoot1_x)
        c_shootj.append(self.shoot1_y)

    def awp_shoot2(self):
        self.shoot2_x=special_forces_move.cops_x+special_corps_size_x//2
        self.shoot2_y=special_forces_move.cops_y
        c_shootu.append(self.shoot2_x)
        c_shootu.append(self.shoot2_y)

    def awp_shoot3(self):
        self.shoot3_x=special_forces_move.cops_x+38
        self.shoot3_y=special_forces_move.cops_y+special_corps_size_y
        c_shootm.append(self.shoot3_x)
        c_shootm.append(self.shoot3_y)

    def awp_shoot4(self):
        self.shoot4_x=special_forces_move.cops_x+special_corps_size_x//2-9
        self.shoot4_y=special_forces_move.cops_y
        c_shootn.append(self.shoot4_x)
        c_shootn.append(self.shoot4_y)

    def awp_shoot5(self):
        self.shoot5_x=special_forces_move.cops_x+special_corps_size_x//2-9
        self.shoot5_y=special_forces_move.cops_y+special_corps_size_y
        c_shooty.append(self.shoot5_x)
        c_shooty.append(self.shoot5_y)

    def awp_shoot6(self):
        self.shoot6_x=special_forces_move.cops_x
        self.shoot6_y=special_forces_move.cops_y+special_corps_size_y
        c_shootb.append(self.shoot6_x)
        c_shootb.append(self.shoot6_y)

    def awp_shoot7(self):
        self.shoot7_x=special_forces_move.cops_x
        self.shoot7_y=special_forces_move.cops_y+special_corps_size_y//2
        c_shootg.append(self.shoot7_x)
        c_shootg.append(self.shoot7_y)
    
    def awp_shoot8(self):
        self.shoot8_x=special_forces_move.cops_x
        self.shoot8_y=special_forces_move.cops_y
        c_shoott.append(self.shoot8_x)
        c_shoott.append(self.shoot8_y)

    def desert_eagle_shoot1(self):
        self.shoot1_x=special_forces_move.cops_x+special_corps_size_x
        self.shoot1_y=special_forces_move.cops_y+special_corps_size_y//2
        c_shootj.append(self.shoot1_x)
        c_shootj.append(self.shoot1_y)

    def desert_eagle_shoot2(self):
        self.shoot2_x=special_forces_move.cops_x+special_corps_size_x//2
        self.shoot2_y=special_forces_move.cops_y
        c_shootu.append(self.shoot2_x)
        c_shootu.append(self.shoot2_y)

    def desert_eagle_shoot3(self):
        self.shoot3_x=special_forces_move.cops_x+38
        self.shoot3_y=special_forces_move.cops_y+special_corps_size_y
        c_shootm.append(self.shoot3_x)
        c_shootm.append(self.shoot3_y)

    def desert_eagle_shoot4(self):
        self.shoot4_x=special_forces_move.cops_x+special_corps_size_x//2-9
        self.shoot4_y=special_forces_move.cops_y
        c_shootn.append(self.shoot4_x)
        c_shootn.append(self.shoot4_y)

    def desert_eagle_shoot5(self):
        self.shoot5_x=special_forces_move.cops_x+special_corps_size_x//2-9
        self.shoot5_y=special_forces_move.cops_y+special_corps_size_y
        c_shooty.append(self.shoot5_x)
        c_shooty.append(self.shoot5_y)

    def desert_eagle_shoot6(self):
        self.shoot6_x=special_forces_move.cops_x
        self.shoot6_y=special_forces_move.cops_y+special_corps_size_y
        c_shootb.append(self.shoot6_x)
        c_shootb.append(self.shoot6_y)

    def desert_eagle_shoot7(self):
        self.shoot7_x=special_forces_move.cops_x
        self.shoot7_y=special_forces_move.cops_y+special_corps_size_y//2
        c_shootg.append(self.shoot7_x)
        c_shootg.append(self.shoot7_y)
    
    def desert_eagle_shoot8(self):
        self.shoot8_x=special_forces_move.cops_x
        self.shoot8_y=special_forces_move.cops_y
        c_shoott.append(self.shoot8_x)
        c_shoott.append(self.shoot8_y)
    
    def m_16_shoot1(self):
        self.shoot1_x=special_forces_move.cops_x+special_corps_size_x
        self.shoot1_y=special_forces_move.cops_y+special_corps_size_y//2
        c_shootj.append(self.shoot1_x)
        c_shootj.append(self.shoot1_y)

    def m_16_shoot2(self):
        self.shoot2_x=special_forces_move.cops_x+special_corps_size_x//2
        self.shoot2_y=special_forces_move.cops_y
        c_shootu.append(self.shoot2_x)
        c_shootu.append(self.shoot2_y)

    def m_16_shoot3(self):
        self.shoot3_x=special_forces_move.cops_x+38
        self.shoot3_y=special_forces_move.cops_y+special_corps_size_y
        c_shootm.append(self.shoot3_x)
        c_shootm.append(self.shoot3_y)

    def m_16_shoot4(self):
        self.shoot4_x=special_forces_move.cops_x+special_corps_size_x//2-9
        self.shoot4_y=special_forces_move.cops_y
        c_shootn.append(self.shoot4_x)
        c_shootn.append(self.shoot4_y)

    def m_16_shoot5(self):
        self.shoot5_x=special_forces_move.cops_x+special_corps_size_x//2-9
        self.shoot5_y=special_forces_move.cops_y+special_corps_size_y
        c_shooty.append(self.shoot5_x)
        c_shooty.append(self.shoot5_y)

    def m_16_shoot6(self):
        self.shoot6_x=special_forces_move.cops_x
        self.shoot6_y=special_forces_move.cops_y+special_corps_size_y
        c_shootb.append(self.shoot6_x)
        c_shootb.append(self.shoot6_y)

    def m_16_shoot7(self):
        self.shoot7_x=special_forces_move.cops_x
        self.shoot7_y=special_forces_move.cops_y+special_corps_size_y//2
        c_shootg.append(self.shoot7_x)
        c_shootg.append(self.shoot7_y)
    
    def m_16_shoot8(self):
        self.shoot8_x=special_forces_move.cops_x
        self.shoot8_y=special_forces_move.cops_y
        c_shoott.append(self.shoot8_x)
        c_shoott.append(self.shoot8_y)
    
    def awp_shoot1_isabet(self,i):
        dağcılar.can-=random.choice(awp_damage)
        cops_mermi.c_shootj.pop(index+1)
        cops_mermi.c_shootj.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(1)
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shootj.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0
    
    def awp_shoot2_isabet(self,i):
        dağcılar.can-=random.choice(awp_damage)
        cops_mermi.c_shootu.pop(index+1)
        cops_mermi.c_shootu.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(2)
            
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shootu.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def awp_shoot3_isabet(self,i):
        dağcılar.can-=random.choice(awp_damage)
        cops_mermi.c_shootm.pop(index+1)
        cops_mermi.c_shootm.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(3)
            
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shootm.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0
    def awp_shoot4_isabet(self,i):
        dağcılar.can-=random.choice(awp_damage)
        cops_mermi.c_shootn.pop(index+1)
        cops_mermi.c_shootn.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(4)
            
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shootn.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0
    
    def awp_shoot5_isabet(self,i):
        dağcılar.can-=random.choice(awp_damage)
        cops_mermi.c_shooty.pop(index+1)
        cops_mermi.c_shooty.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(5)
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shooty.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def awp_shoot6_isabet(self,i):
        dağcılar.can-=random.choice(awp_damage)
        cops_mermi.c_shootb.pop(index+1)
        cops_mermi.c_shootb.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(6)
            
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shootb.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def awp_shoot7_isabet(self,i):
        dağcılar.can-=random.choice(awp_damage)
        cops_mermi.c_shootg.pop(index+1)
        cops_mermi.c_shootg.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(7)
            
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shootg.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def awp_shoot8_isabet(self,i):
        dağcılar.can-=random.choice(awp_damage)
        cops_mermi.c_shoott.pop(index+1)
        cops_mermi.c_shoott.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(8)
            
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shoott.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0
        
    def desert_eagle_shoot1_isabet(self,i):
        dağcılar.can-=random.choice(desert_eagle_damage)
        cops_mermi.c_shootj.pop(index+1)
        cops_mermi.c_shootj.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(1)
            
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shootj.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0
    
    def desert_eagle_shoot2_isabet(self,i):
        dağcılar.can-=random.choice(desert_eagle_damage)
        cops_mermi.c_shootu.pop(index+1)
        cops_mermi.c_shootu.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(2)
            
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shootu.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def desert_eagle_shoot3_isabet(self,i):
        dağcılar.can-=random.choice(desert_eagle_damage)
        cops_mermi.c_shootm.pop(index+1)
        cops_mermi.c_shootm.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(3)
            
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shootm.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0
    def desert_eagle_shoot4_isabet(self,i):
        dağcılar.can-=random.choice(desert_eagle_damage)
        cops_mermi.c_shootn.pop(index+1)
        cops_mermi.c_shootn.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(4)
            
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shootn.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0
    
    def desert_eagle_shoot5_isabet(self,i):
        dağcılar.can-=random.choice(desert_eagle_damage)
        cops_mermi.c_shooty.pop(index+1)
        cops_mermi.c_shooty.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(5)
            
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shooty.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def desert_eagle_shoot6_isabet(self,i):
        dağcılar.can-=random.choice(desert_eagle_damage)
        cops_mermi.c_shootb.pop(index+1)
        cops_mermi.c_shootb.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(6)
            
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shootb.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def desert_eagle_shoot7_isabet(self,i):
        dağcılar.can-=random.choice(desert_eagle_damage)
        cops_mermi.c_shootg.pop(index+1)
        cops_mermi.c_shootg.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(7)
            
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shootg.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def desert_eagle_shoot8_isabet(self,i):
        dağcılar.can-=random.choice(desert_eagle_damage)
        cops_mermi.c_shoott.pop(index+1)
        cops_mermi.c_shoott.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(8)
            
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shoott.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0
    
    def m_16_shoot1_isabet(self,i):
        dağcılar.can-=random.choice(m_16_damage)
        cops_mermi.c_shootj.pop(index+1)
        cops_mermi.c_shootj.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(1)
            
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shootj.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0
    
    def m_16_shoot2_isabet(self,i):
        dağcılar.can-=random.choice(m_16_damage)
        cops_mermi.c_shootu.pop(index+1)
        cops_mermi.c_shootu.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(2)
            
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shootu.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def m_16_shoot3_isabet(self,i):
        dağcılar.can-=random.choice(m_16_damage)
        cops_mermi.c_shootm.pop(index+1)
        cops_mermi.c_shootm.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(3)
            
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shootm.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0
    def m_16_shoot4_isabet(self,i):
        dağcılar.can-=random.choice(m_16_damage)
        cops_mermi.c_shootn.pop(index+1)
        cops_mermi.c_shootn.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(4)
            
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shootn.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0
    
    def m_16_shoot5_isabet(self,i):
        dağcılar.can-=random.choice(m_16_damage)
        cops_mermi.c_shooty.pop(index+1)
        cops_mermi.c_shooty.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(5)
            
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shooty.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def m_16_shoot6_isabet(self,i):
        dağcılar.can-=random.choice(m_16_damage)
        cops_mermi.c_shootb.pop(index+1)
        cops_mermi.c_shootb.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(6)
            
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shootb.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def m_16_shoot7_isabet(self,i):
        dağcılar.can-=random.choice(m_16_damage)
        cops_mermi.c_shootg.pop(index+1)
        cops_mermi.c_shootg.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(7)
            
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shootg.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def m_16_shoot8_isabet(self,i):
        dağcılar.can-=random.choice(m_16_damage)
        cops_mermi.c_shoott.pop(index+1)
        cops_mermi.c_shoott.pop(index)
        if dağcılar.can<=0:
            cops_mermi_yön.remove(8)
            
            special_forces.para+=1500
            dağcılar.para+=0
            dağcılar_move.dağcı_x=dağcı_x
            dağcılar_move.dağcı_y=dağcı_y
            special_forces_move.cops_x=cops_x
            special_forces_move.cops_y=cops_y
            special_forces.can=100
            dağcılar.can=100
            c_shoott.clear()
            cops_mermi_yön.clear()
            dağcı_mermi_yön.clear()
            return 1
        else:
            return 0

    def shoot1_collide(self,index):
        if engel_1.collidepoint(c_shootj[index],c_shootj[index+1]):
            return 0
        if engel_2.collidepoint(c_shootj[index],c_shootj[index+1]):
            return 0
        if engel_3.collidepoint(c_shootj[index],c_shootj[index+1]):
            return 0
        if engel_4.collidepoint(c_shootj[index],c_shootj[index+1]):
            return 0 
        if engel_5.collidepoint(c_shootj[index],c_shootj[index+1]):
            return 0 
        if engel_6.collidepoint(c_shootj[index],c_shootj[index+1]):
            return 0
        if dağcı_rect.collidepoint(c_shootj[index],c_shootj[index+1]):
            return 2
        else:
            return 1
    def shoot2_collide(self,index):
        if engel_1.collidepoint(c_shootu[index],c_shootu[index+1]):
            return 0
        if engel_2.collidepoint(c_shootu[index],c_shootu[index+1]):
            return 0
        if engel_3.collidepoint(c_shootu[index],c_shootu[index+1]):
            return 0
        if engel_4.collidepoint(c_shootu[index],c_shootu[index+1]):
            return 0 
        if engel_5.collidepoint(c_shootu[index],c_shootu[index+1]):
            return 0 
        if engel_6.collidepoint(c_shootu[index],c_shootu[index+1]):
            return 0
        if dağcı_rect.collidepoint(c_shootu[index],c_shootu[index+1]):
            return 2
        else:
            return 1
    def shoot3_collide(self,index):
        if engel_1.collidepoint(c_shootm[index],c_shootm[index+1]):
            return 0
        if engel_2.collidepoint(c_shootm[index],c_shootm[index+1]):
            return 0
        if engel_3.collidepoint(c_shootm[index],c_shootm[index+1]):
            return 0
        if engel_4.collidepoint(c_shootm[index],c_shootm[index+1]):
            return 0 
        if engel_5.collidepoint(c_shootm[index],c_shootm[index+1]):
            return 0 
        if engel_6.collidepoint(c_shootm[index],c_shootm[index+1]):
            return 0
        if dağcı_rect.collidepoint(c_shootm[index],c_shootm[index+1]):
            return 2
        else:
            return 1

    def shoot4_collide(self,index):
        if engel_1.collidepoint(c_shootn[index],c_shootn[index+1]):
            return 0
        if engel_2.collidepoint(c_shootn[index],c_shootn[index+1]):
            return 0
        if engel_3.collidepoint(c_shootn[index],c_shootn[index+1]):
            return 0
        if engel_4.collidepoint(c_shootn[index],c_shootn[index+1]):
            return 0 
        if engel_5.collidepoint(c_shootn[index],c_shootn[index+1]):
            return 0 
        if engel_6.collidepoint(c_shootn[index],c_shootn[index+1]):
            return 0
        if dağcı_rect.collidepoint(c_shootn[index],c_shootn[index+1]):
            return 2
        else:
            return 1
    def shoot5_collide(self,index):
        if engel_1.collidepoint(c_shooty[index],c_shooty[index+1]):
            return 0
        if engel_2.collidepoint(c_shooty[index],c_shooty[index+1]):
            return 0
        if engel_3.collidepoint(c_shooty[index],c_shooty[index+1]):
            return 0
        if engel_4.collidepoint(c_shooty[index],c_shooty[index+1]):
            return 0 
        if engel_5.collidepoint(c_shooty[index],c_shooty[index+1]):
            return 0 
        if engel_6.collidepoint(c_shooty[index],c_shooty[index+1]):
            return 0
        if dağcı_rect.collidepoint(c_shooty[index],c_shooty[index+1]):
            return 2
        else:
            return 1
    def shoot6_collide(self,index):
        if engel_1.collidepoint(c_shootb[index],c_shootb[index+1]):
            return 0
        if engel_2.collidepoint(c_shootb [index],c_shootb[index+1]):
            return 0
        if engel_3.collidepoint(c_shootb[index],c_shootb[index+1]):
            return 0
        if engel_4.collidepoint(c_shootb[index],c_shootb[index+1]):
            return 0 
        if engel_5.collidepoint(c_shootb[index],c_shootb[index+1]):
            return 0 
        if engel_6.collidepoint(c_shootb[index],c_shootb[index+1]):
            return 0
        if dağcı_rect.collidepoint(c_shootb[index],c_shootb[index+1]):
            return 2
        else:
            return 1

    def shoot7_collide(self,index):
        if engel_1.collidepoint(c_shootg[index],c_shootg[index+1]):
            return 0
        if engel_2.collidepoint(c_shootg[index],c_shootg[index+1]):
            return 0
        if engel_3.collidepoint(c_shootg[index],c_shootg[index+1]):
            return 0
        if engel_4.collidepoint(c_shootg[index],c_shootg[index+1]):
            return 0 
        if engel_5.collidepoint(c_shootg[index],c_shootg[index+1]):
            return 0 
        if engel_6.collidepoint(c_shootg[index],c_shootg[index+1]):
            return 0
        if dağcı_rect.collidepoint(c_shootg[index],c_shootg[index+1]):
            return 2
        else:
            return 1
    def shoot8_collide(self,index):
        if engel_1.collidepoint(c_shoott[index],c_shoott[index+1]):
            return 0
        if engel_2.collidepoint(c_shoott[index],c_shoott[index+1]):
            return 0
        if engel_3.collidepoint(c_shoott[index],c_shoott[index+1]):
            return 0
        if engel_4.collidepoint(c_shoott[index],c_shoott[index+1]):
            return 0 
        if engel_5.collidepoint(c_shoott[index],c_shoott[index+1]):
            return 0 
        if engel_6.collidepoint(c_shoott[index],c_shoott[index+1]):
            return 0
        if dağcı_rect.collidepoint(c_shoott[index],c_shoott[index+1]):
            return 2
        else:
            return 1

while başla:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            başla=False
            break
    special_corps_size_x=special_corps.get_size()[0]
    special_corps_size_y=special_corps.get_size()[1]
    dağcılar_size_x=dağcı.get_size()[0]
    dağcılar_size_y=dağcı.get_size()[1]
    
    special_forces=cops(cops_health,cops_money,cops_gun)
    dağcılar=terorist(dağcı_health,dağcı_money,dağcı_gun)
    awp_object=awp_class(awp_damage)
    desert_eagle_object=desert_eagle_class(desert_eagle_damage)
    m_16_object=m_16_class(m_16_damage)
    ak_47_object=ak_47_class(ak_47_damage)
    special_forces_move=cops_move(cops_x,cops_y)
    dağcılar_move=dağcılar_moves(dağcı_x,dağcı_y)
    dağcı_mermi=dağcı_bullet(d_shoot1,d_shoot2,d_shoot3,d_shoot4,d_shoot6,d_shoot7,d_shoot8,d_shoot9)
    cops_mermi=cops_bullet(c_shootj,c_shootu,c_shootm,c_shootn,c_shooty,c_shootb,c_shootg,c_shoott)
    
    while i<=30:
        #silah değişmemesi için choose1,choose2 True False hallerini kullan
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                başla,i=False,32
                break
        while choose1 or choose2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    başla,choose1,choose2,i=False,False,False,32
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    pos_x=pos[0]
                    pos_y=pos[1]
                    if c_awp_location.collidepoint(pos_x, pos_y):
                        if special_forces.para-awp_cost>=0:
                            special_forces.choose_awp(awp_cost)
                            choose1=False
                    if c_desert_eagle_location.collidepoint(pos_x,pos_y):
                        if special_forces.para-desert_eagle_cost>=0:
                            special_forces.choose_desert_eagle(desert_eagle_cost)
                            choose1=False
                    if c_m_16_location.collidepoint(pos_x,pos_y):
                        if special_forces.para-m_16_cost>=0:
                            special_forces.choose_m_16(m_16_cost)
                            choose1=False
                    if t_awp_location.collidepoint(pos_x,pos_y):
                        if dağcılar.para-awp_cost>=0:
                            dağcılar.choose_awp(awp_cost)
                            choose2=False
                    if t_desert_eagle_location.collidepoint(pos_x,pos_y):
                        if dağcılar.para-desert_eagle_cost>=0:
                            dağcılar.choose_desert_eagle(desert_eagle_cost)
                            choose2=False
                    if t_ak_47_location.collidepoint(pos_x,pos_y):
                        if dağcılar.para-ak_47_cost>=0:
                            dağcılar.choose_ak_47(ak_47_cost)
                            choose2=False

                window.fill((rgb.kum))
                awp_copy=awp.copy()
                desert_eagle1=pygame.transform.flip(desert_eagle,True,False)
                awp_copy=pygame.transform.flip(awp_copy,True,False)
                ak_47_copy=ak_47.copy()
                ak_47_copy=pygame.transform.flip(ak_47_copy,True,False)
                special_corps_copy=special_corps.copy()
                special_corps_copy=pygame.transform.flip(special_corps_copy,True,False)
                dağcı_copy=dağcı.copy()
                dağcı_copy=pygame.transform.flip(dağcı_copy,True,False)
                yazı_1=yazı_tipi_1.render("Özel kuvvetler:{}$".format(special_forces.para),True,(0,0,0))
                yazı_2=yazı_tipi_2.render("Teröristler:{}$".format(dağcılar.para),True,(0,0,0))
                window.blit(yazı_1,(0,10))
                window.blit(yazı_2,(1370,10))
                window.blit(desert_eagle1,(20,80))
                window.blit(awp_copy,(20,250))
                window.blit(m_16,(20,500))
                window.blit(desert_eagle,(1310,80))
                window.blit(awp,(1160,250))
                window.blit(ak_47_copy,(1160,500))
                c_awp_location=pygame.draw.rect(window,(0,0,0),c_awp_al)
                c_desert_eagle_location=pygame.draw.rect(window,(0,0,0),c_desert_eagle_al)
                c_m_16_location=pygame.draw.rect(window,(0,0,0),c_m_16_al)
                t_awp_location=pygame.draw.rect(window,(0,0,0),t_awp_al)
                t_desert_eagle_location=pygame.draw.rect(window,(0,0,0),t_desert_eagle_al)
                t_ak_47_location=pygame.draw.rect(window,(0,0,0),t_ak_47_al)
                window.blit(yazı_3,(600,335))
                window.blit(yazı_4,(600,95))
                window.blit(yazı_5,(620,565))
                window.blit(yazı_6,(432,328))
                window.blit(yazı_6,(282,88))
                window.blit(yazı_6,(462,558))
                window.blit(yazı_6,(1072,328))
                window.blit(yazı_6,(1212,88))
                window.blit(yazı_6,(1062,558))
                pygame.display.update()
    
        if special_forces.silah =="awp" and dağcılar.silah=="awp":   
            cops_kalan_mermi=awp_mermi-cops_atılan_mermi 
            dağcı_kalan_mermi=awp_mermi-dağcı_atılan_mermi    
            window.fill((rgb.kum))
            pygame.draw.rect(window,(0,0,0),engel_1)
            pygame.draw.rect(window,(0,0,0),engel_2)
            pygame.draw.rect(window,(0,0,0),engel_3)
            pygame.draw.rect(window,(0,0,0),engel_4)
            pygame.draw.rect(window,(0,0,0),engel_5)
            pygame.draw.rect(window,(0,0,0),engel_6)
            yazı_7=yazı_tipi_7.render(f"{dağcılar.can}/100",True,(0,0,0))
            yazı_8=yazı_tipi_8.render(f"{special_forces.can}/100",True,(0,0,0))
            yazı_9=yazı_tipi_9.render(f"Round {i}",True,(0,0,0))
            yazı_10=yazı_tipi_10.render(f"{cops_kalan_mermi}/{cops_awp_mermi_toplam}",True,(0,0,0))
            yazı_11=yazı_tipi_11.render(f"{dağcı_kalan_mermi}/{dağcı_awp_mermi_toplam}",True,(0,0,0))
            yazı_12=yazı_tipi_12.render(f"{cops_win}",True,(0,0,0))
            yazı_13=yazı_tipi_13.render(f"{dağcı_win}",True,(0,0,0))
            special_forces_rect=pygame.Rect(special_forces_move.cops_x,special_forces_move.cops_y,special_corps_size_x,special_corps_size_y)
            dağcı_rect=pygame.Rect(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y,dağcılar_size_x,dağcılar_size_y)
            keys=pygame.key.get_pressed()
            if keys[pygame.K_w] and special_forces_move.cops_y>=0 :
                special_forces_move.w()
            if keys[pygame.K_s] and special_forces_move.cops_y<=window_y-special_corps.get_size()[1]:
                special_forces_move.s()
            if keys[pygame.K_a] and special_forces_move.cops_x>=0:
                special_forces_move.a()
            if keys[pygame.K_d] and special_forces_move.cops_x<=window_x-special_corps.get_size()[0]:
                special_forces_move.d()
            if keys[pygame.K_UP] and dağcılar_move.dağcı_y>=0:
                dağcılar_move.up()
            if keys[pygame.K_DOWN] and dağcılar_move.dağcı_y<=window_y-dağcılar_size_y:
                dağcılar_move.down()
            if keys[pygame.K_LEFT] and dağcılar_move.dağcı_x>=0:
                dağcılar_move.left()
            if keys[pygame.K_RIGHT] and dağcılar_move.dağcı_x<=window_x-dağcılar_size_x:
                dağcılar_move.right()
            if cops_atılan_mermi<awp_mermi:
                if keys[pygame.K_j]:
                    cops_mermi_yön.add(1)
                    cops_mermi.awp_shoot1()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_u]:
                    cops_mermi_yön.add(2)
                    cops_mermi.awp_shoot2()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_m]:
                    cops_mermi_yön.add(3)
                    cops_mermi.awp_shoot3()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_y]:
                    cops_mermi_yön.add(4)
                    cops_mermi.awp_shoot4()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_n]:
                    cops_mermi_yön.add(5)
                    cops_mermi.awp_shoot5()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_b]:
                    cops_mermi_yön.add(6)
                    cops_mermi.awp_shoot6()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_g]:
                    cops_mermi_yön.add(7)
                    cops_mermi.awp_shoot7()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_t]:
                    cops_mermi_yön.add(8)
                    cops_mermi.awp_shoot8()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
            else:
                pass
            if keys[pygame.K_r]:
                if cops_awp_mermi_toplam-cops_atılan_mermi>=0:
                    cops_awp_mermi_toplam-=cops_atılan_mermi
                    cops_atılan_mermi=0
                else:
                    if cops_deneme==0:
                        pass
                    else:
                        cops_atılan_mermi=awp_mermi-cops_awp_mermi_toplam-cops_kalan_mermi
                        cops_awp_mermi_toplam-=cops_awp_mermi_toplam
                        cops_deneme=0 
            if dağcı_atılan_mermi<awp_mermi:
                if keys[pygame.K_KP_1]:
                    dağcı_mermi_yön.add(1)
                    dağcı_mermi.awp_shoot1()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_2]:
                    dağcı_mermi_yön.add(2)
                    dağcı_mermi.awp_shoot2()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_3]:
                    dağcı_mermi_yön.add(3)
                    dağcı_mermi.awp_shoot3()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_4]:
                    dağcı_mermi_yön.add(4)
                    dağcı_mermi.awp_shoot4()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_6]:
                    dağcı_mermi_yön.add(6)
                    dağcı_mermi.awp_shoot6()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_7]:
                    dağcı_mermi_yön.add(7)
                    dağcı_mermi.awp_shoot7()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_8]:
                    dağcı_mermi_yön.add(8)
                    dağcı_mermi.awp_shoot8()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_9]:
                    dağcı_mermi_yön.add(9)  
                    dağcı_mermi.awp_shoot9()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)   
            else:
                pass  
            if keys[pygame.K_KP_5]:
                if dağcı_awp_mermi_toplam-dağcı_atılan_mermi>=0:
                    dağcı_awp_mermi_toplam-=dağcı_atılan_mermi
                    dağcı_atılan_mermi=0
                else:
                    if dağcı_deneme==0:
                        pass
                    else:
                        dağcı_atılan_mermi=awp_mermi-dağcı_awp_mermi_toplam-dağcı_kalan_mermi
                        dağcı_awp_mermi_toplam-=dağcı_awp_mermi_toplam
                        dağcı_deneme=0
            if 1 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot1),2):
                        if 0<=dağcı_mermi.d_shoot1[index]<=window_x:
                            if dağcı_mermi.shoot1_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot1[index],dağcı_mermi.d_shoot1[index+1],10,5))
                                dağcı_mermi.d_shoot1[index]-=mermi_hız
                                dağcı_mermi.d_shoot1[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot1_collide(index)==2:
                                if dağcı_mermi.awp_shoot1_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    dağcı_win+=1
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot1.pop(index+1)
                                d_shoot1.pop(index)
                                break
                        else:
                            d_shoot1.pop(index+1)
                            d_shoot1.pop(index)
                            break
                else:
                    pass
            if 2 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot2),2):
                        if 0<=dağcı_mermi.d_shoot2[index]<=window_x:
                            if dağcı_mermi.shoot2_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot2[index],dağcı_mermi.d_shoot2[index+1],5,10))
                                dağcı_mermi.d_shoot2[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot2_collide(index)==2:
                                if dağcı_mermi.awp_shoot2_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    cops_atılan_mermi=0
                                    dağcı_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot2.pop(index+1)
                                d_shoot2.pop(index)
                                break
                        else:
                            d_shoot2.pop(index+1)
                            d_shoot2.pop(index)
                            break
                else:
                    pass
            if 3 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot3),2):
                        if 0<=dağcı_mermi.d_shoot3[index]<=window_x:
                            if dağcı_mermi.shoot3_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot3[index],dağcı_mermi.d_shoot3[index+1],10,5))
                                dağcı_mermi.d_shoot3[index]+=mermi_hız
                                dağcı_mermi.d_shoot3[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot3_collide(index)==2:
                                if dağcı_mermi.awp_shoot3_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot3.pop(index+1)
                                d_shoot3.pop(index)
                                break
                        else:
                            d_shoot3.pop(index+1)
                            d_shoot3.pop(index)
                            break
                else:
                    pass

            if 4 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot4),2):
                        if 0<=dağcı_mermi.d_shoot4[index]<=window_x:
                            if dağcı_mermi.shoot4_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot4[index],dağcı_mermi.d_shoot4[index+1],10,5))
                                dağcı_mermi.d_shoot4[index]-=mermi_hız        
                            elif dağcı_mermi.shoot4_collide(index)==2:
                                if dağcı_mermi.awp_shoot4_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot4.pop(index+1)
                                d_shoot4.pop(index)
                                break
                        else:
                            d_shoot4.pop(index+1)
                            d_shoot4.pop(index)
                            break
                else:
                    pass
            if 6 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot6),2):
                        if 0<=dağcı_mermi.d_shoot6[index]<=window_x:
                            if dağcı_mermi.shoot6_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot6[index],dağcı_mermi.d_shoot6[index+1],10,5))
                                dağcı_mermi.d_shoot6[index]+=mermi_hız
                            elif dağcı_mermi.shoot6_collide(index)==2:
                                if dağcı_mermi.awp_shoot6_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot6.pop(index+1)
                                d_shoot6.pop(index)
                                break
                        else:
                            d_shoot6.pop(index+1)
                            d_shoot6.pop(index)
                            break
                else:
                    pass
            if 7 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot7),2):
                        if 0<=dağcı_mermi.d_shoot7[index]<=window_x:
                            if dağcı_mermi.shoot7_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot7[index],dağcı_mermi.d_shoot7[index+1],10,5))
                                dağcı_mermi.d_shoot7[index]-=mermi_hız
                                dağcı_mermi.d_shoot7[index+1]-=mermi_hız           
                            elif dağcı_mermi.shoot7_collide(index)==2:
                                if dağcı_mermi.awp_shoot7_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot7.pop(index+1)
                                d_shoot7.pop(index)
                                break
                        else:
                            d_shoot7.pop(index+1)
                            d_shoot7.pop(index)
                            break
                else:
                    pass

            if 8 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot8),2):
                        if 0<=dağcı_mermi.d_shoot8[index]<=window_x:
                            if dağcı_mermi.shoot8_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot8[index],dağcı_mermi.d_shoot8[index+1],5,10))
                                dağcı_mermi.d_shoot8[index+1]-=mermi_hız           
                            elif dağcı_mermi.shoot8_collide(index)==2:
                                if dağcı_mermi.awp_shoot8_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot8.pop(index+1)
                                d_shoot8.pop(index)
                                break
                        else:
                            d_shoot8.pop(index+1)
                            d_shoot8.pop(index)
                            break
                else:
                    pass
            if 9 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot9),2):
                        if 0<=dağcı_mermi.d_shoot9[index]<=window_x:
                            if dağcı_mermi.shoot9_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot9[index],dağcı_mermi.d_shoot9[index+1],10,5))
                                dağcı_mermi.d_shoot9[index]+=mermi_hız
                                dağcı_mermi.d_shoot9[index+1]-=mermi_hız
                            elif dağcı_mermi.shoot9_collide(index)==2:
                                if dağcı_mermi.awp_shoot9_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot9.pop(index+1)
                                d_shoot9.pop(index)
                                break
                        else:
                            d_shoot9.pop(index+1)
                            d_shoot9.pop(index)
                            break
                else:
                    pass
            if 1 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shootj),2):
                        if 0<=cops_mermi.c_shootj[index]<=window_x:
                            if cops_mermi.shoot1_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootj[index],cops_mermi.c_shootj[index+1],10,5))
                                cops_mermi.c_shootj[index]+=mermi_hız
                            elif cops_mermi.shoot1_collide(index)==2:
                                if cops_mermi.awp_shoot1_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootj.pop(index+1)
                                c_shootj.pop(index)
                                break
                        else:
                            c_shootj.pop(index+1)
                            c_shootj.pop(index)
                            break
                else:
                    pass
            if 2 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shootu),2):
                        if 0<=cops_mermi.c_shootu[index]<=window_x:
                            if cops_mermi.shoot2_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootu[index],cops_mermi.c_shootu[index+1],10,5))
                                cops_mermi.c_shootu[index]+=mermi_hız
                                cops_mermi.c_shootu[index+1]-=mermi_hız
                            elif cops_mermi.shoot2_collide(index)==2:
                                if cops_mermi.awp_shoot2_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootu.pop(index+1)
                                c_shootu.pop(index)
                                break
                        else:
                            c_shootu.pop(index+1)
                            c_shootu.pop(index)
                            break
                else:
                    pass
            if 3 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shootm),2):
                        if 0<=cops_mermi.c_shootm[index]<=window_x:
                            if cops_mermi.shoot3_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootm[index],cops_mermi.c_shootm[index+1],10,5))
                                cops_mermi.c_shootm[index]+=mermi_hız
                                cops_mermi.c_shootm[index+1]+=mermi_hız
                            elif cops_mermi.shoot3_collide(index)==2:
                                if cops_mermi.awp_shoot3_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootm.pop(index+1)
                                c_shootm.pop(index)
                                break
                        else:
                            c_shootm.pop(index+1)
                            c_shootm.pop(index)
                            break
                else:
                    pass
            if 4 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shootn),2):
                        if 0<=cops_mermi.c_shootn[index]<=window_x:
                            if cops_mermi.shoot4_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootn[index],cops_mermi.c_shootn[index+1],5,10))
                                cops_mermi.c_shootn[index+1]-=mermi_hız
                            elif cops_mermi.shoot4_collide(index)==2:
                                if cops_mermi.awp_shoot4_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootn.pop(index+1)
                                c_shootn.pop(index)
                                break
                        else:
                            c_shootn.pop(index+1)
                            c_shootn.pop(index)
                            break
                else:
                    pass
            if 5 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shooty),2):
                        if 0<=cops_mermi.c_shooty[index]<=window_x:
                            if cops_mermi.shoot5_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shooty[index],cops_mermi.c_shooty[index+1],5,10))
                                cops_mermi.c_shooty[index+1]+=mermi_hız
                            elif cops_mermi.shoot5_collide(index)==2:
                                if cops_mermi.awp_shoot5_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    cops_atılan_mermi=0
                                    dağcı_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shooty.pop(index+1)
                                c_shooty.pop(index)
                                break
                        else:
                            c_shooty.pop(index+1)
                            c_shooty.pop(index)
                            break
                else:
                    break
            if 6 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shootb),2):
                        if 0<=cops_mermi.c_shootb[index]<=window_x:
                            if cops_mermi.shoot6_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootb[index],cops_mermi.c_shootb[index+1],10,5))
                                cops_mermi.c_shootb[index]-=mermi_hız
                                cops_mermi.c_shootb[index+1]+=mermi_hız
                            elif cops_mermi.shoot6_collide(index)==2:
                                if cops_mermi.awp_shoot6_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    cops_atılan_mermi=0
                                    dağcı_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootb.pop(index+1)
                                c_shootb.pop(index)
                                break
                        else:
                            c_shootb.pop(index+1)
                            c_shootb.pop(index)
                            break
                else:
                    pass
            if 7 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shootg),2):
                        if 0<=cops_mermi.c_shootg[index]<=window_x:
                            if cops_mermi.shoot7_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootg[index],cops_mermi.c_shootg[index+1],10,5))
                                cops_mermi.c_shootg[index]-=mermi_hız
                            elif cops_mermi.shoot7_collide(index)==2:
                                if cops_mermi.awp_shoot7_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootg.pop(index+1)
                                c_shootg.pop(index)
                                break
                        else:
                            c_shootg.pop(index+1)
                            c_shootg.pop(index)
                            break
                else:
                    pass
            if 8 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shoott),2):
                        if 0<=cops_mermi.c_shoott[index]<=window_x:
                            if cops_mermi.shoot8_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shoott[index],cops_mermi.c_shoott[index+1],10,5))
                                cops_mermi.c_shoott[index]-=mermi_hız
                                cops_mermi.c_shoott[index+1]-=mermi_hız
                            elif cops_mermi.shoot8_collide(index)==2:
                                if cops_mermi.awp_shoot8_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shoott.pop(index+1)
                                c_shoott.pop(index)
                                break
                        else:
                            c_shoott.pop(index+1)
                            c_shoott.pop(index)
                            break
                else:
                    pass
            if dağcılar_move.dağcı_x<=0 and dağcılar_move.dağcı_y<=0:
                dağcı_mermi_yön.clear()
                i+=1
                cops_awp_mermi_toplam=10
                dağcı_awp_mermi_toplam=10
                cops_deneme=1
                dağcı_deneme=1
                special_forces.para+=0
                dağcılar.para+=1500
                dağcı_atılan_mermi=0
                cops_atılan_mermi=0
                dağcı_win+=1
                dağcılar_move.dağcı_x=dağcı_x
                dağcılar_move.dağcı_y=dağcı_y
                special_forces_move.cops_x=cops_x
                special_forces_move.cops_y=cops_y
                special_forces.can=100
                dağcılar.can=100
                choose1,choose2=True,False
            pygame.draw.rect(window,(rgb.kum),special_forces_rect)
            pygame.draw.rect(window,(rgb.kum),dağcı_rect)
            window.blit(special_corps_copy,(special_forces_move.cops_x,special_forces_move.cops_y))
            window.blit(dağcı_copy,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y))
            window.blit(yazı_7,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y+2))
            window.blit(yazı_8,(special_forces_move.cops_x+45,special_forces_move.cops_y-5))
            window.blit(yazı_9,(window_x//2,20))
            window.blit(yazı_10,(special_forces_move.cops_x+45,special_forces_move.cops_y+4))
            window.blit(yazı_11,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y+12))
            window.blit(special_corps_logo,(1470,0))
            window.blit(dağcı_logo,(1470,35))
            window.blit(yazı_12,(1510,-5))
            window.blit(yazı_13,(1510,32))
            pygame.display.update()
        if special_forces.silah=="awp" and dağcılar.silah=="desert_eagle":      
            cops_kalan_mermi=awp_mermi-cops_atılan_mermi 
            dağcı_kalan_mermi=desert_eagle_mermi-dağcı_atılan_mermi   
            window.fill((rgb.kum))
            pygame.draw.rect(window,(0,0,0),engel_1)
            pygame.draw.rect(window,(0,0,0),engel_2)
            pygame.draw.rect(window,(0,0,0),engel_3)
            pygame.draw.rect(window,(0,0,0),engel_4)
            pygame.draw.rect(window,(0,0,0),engel_5)
            pygame.draw.rect(window,(0,0,0),engel_6)
            yazı_7=yazı_tipi_7.render(f"{dağcılar.can}/100",True,(0,0,0))
            yazı_8=yazı_tipi_8.render(f"{special_forces.can}/100",True,(0,0,0))
            yazı_9=yazı_tipi_9.render(f"Round {i}",True,(0,0,0))
            yazı_12=yazı_tipi_12.render(f"{cops_win}",True,(0,0,0))
            yazı_13=yazı_tipi_13.render(f"{dağcı_win}",True,(0,0,0))
            yazı_10=yazı_tipi_10.render(f"{cops_kalan_mermi}/{cops_awp_mermi_toplam}",True,(0,0,0))
            yazı_11=yazı_tipi_11.render(f"{dağcı_kalan_mermi}/{dağcı_desert_eagle_mermi_toplam}",True,(0,0,0))
            special_forces_rect=pygame.Rect(special_forces_move.cops_x,special_forces_move.cops_y,special_corps_size_x,special_corps_size_y)
            dağcı_rect=pygame.Rect(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y,dağcılar_size_x,dağcılar_size_y)
            keys=pygame.key.get_pressed()
            if keys[pygame.K_w] and special_forces_move.cops_y>=0 :
                special_forces_move.w()
            if keys[pygame.K_s] and special_forces_move.cops_y<=window_y-special_corps.get_size()[1]:
                special_forces_move.s()
            if keys[pygame.K_a] and special_forces_move.cops_x>=0:
                special_forces_move.a()
            if keys[pygame.K_d] and special_forces_move.cops_x<=window_x-special_corps.get_size()[0]:
                special_forces_move.d()
            if keys[pygame.K_UP] and dağcılar_move.dağcı_y>=0:
                dağcılar_move.up()
            if keys[pygame.K_DOWN] and dağcılar_move.dağcı_y<=window_y-dağcılar_size_y:
                dağcılar_move.down()
            if keys[pygame.K_LEFT] and dağcılar_move.dağcı_x>=0:
                dağcılar_move.left()
            if keys[pygame.K_RIGHT] and dağcılar_move.dağcı_x<=window_x-dağcılar_size_x:
                dağcılar_move.right()
            if cops_atılan_mermi<awp_mermi:
                if keys[pygame.K_j]:
                    cops_mermi_yön.add(1)
                    cops_mermi.awp_shoot1()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_u]:
                    cops_mermi_yön.add(2)
                    cops_mermi.awp_shoot2()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_m]:
                    cops_mermi_yön.add(3)
                    cops_mermi.awp_shoot3()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_y]:
                    cops_mermi_yön.add(4)
                    cops_mermi.awp_shoot4()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_n]:
                    cops_mermi_yön.add(5)
                    cops_mermi.awp_shoot5()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_b]:
                    cops_mermi_yön.add(6)
                    cops_mermi.awp_shoot6()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_g]:
                    cops_mermi_yön.add(7)
                    cops_mermi.awp_shoot7()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_t]:
                    cops_mermi_yön.add(8)
                    cops_mermi.awp_shoot8()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
            else:
                pass
            if keys[pygame.K_r]:
                if cops_awp_mermi_toplam-cops_atılan_mermi>=0:
                    cops_awp_mermi_toplam-=cops_atılan_mermi
                    cops_atılan_mermi=0
                else:
                    if cops_deneme==0:
                        pass
                    else:
                        cops_atılan_mermi=awp_mermi-cops_awp_mermi_toplam-cops_kalan_mermi
                        cops_awp_mermi_toplam-=cops_awp_mermi_toplam
                        cops_deneme=0         
            if dağcı_atılan_mermi<desert_eagle_mermi:
                if keys[pygame.K_KP_1]:
                    dağcı_mermi_yön.add(1)
                    dağcı_mermi.desert_eagle_shoot1()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_2]:
                    dağcı_mermi_yön.add(2)
                    dağcı_mermi.desert_eagle_shoot2()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_3]:
                    dağcı_mermi_yön.add(3)
                    dağcı_mermi.desert_eagle_shoot3()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_4]:
                    dağcı_mermi_yön.add(4)
                    dağcı_mermi.desert_eagle_shoot4()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_6]:
                    dağcı_mermi_yön.add(6)
                    dağcı_mermi.desert_eagle_shoot6()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_7]:
                    dağcı_mermi_yön.add(7)
                    dağcı_mermi.awp_shoot7()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_8]:
                    dağcı_mermi_yön.add(8)
                    dağcı_atılan_mermi+=1
                    dağcı_mermi.desert_eagle_shoot8()
                    time.sleep(0.1)
                if keys[pygame.K_KP_9]:
                    dağcı_mermi_yön.add(9) 
                    dağcı_atılan_mermi+=1 
                    dağcı_mermi.desert_eagle_shoot9()
                    time.sleep(0.1)
            else:
                pass
            if keys[pygame.K_KP_5]:
                if dağcı_desert_eagle_mermi_toplam-dağcı_atılan_mermi>=0:
                    dağcı_desert_eagle_mermi_toplam-=dağcı_atılan_mermi
                    dağcı_atılan_mermi=0
                else:
                    if dağcı_deneme==0:
                        pass
                    else:
                        dağcı_atılan_mermi=desert_eagle_mermi-dağcı_desert_eagle_mermi_toplam-dağcı_kalan_mermi
                        dağcı_desert_eagle_mermi_toplam-=dağcı_desert_eagle_mermi_toplam
                        dağcı_deneme=0    
            if 1 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot1),2):
                        if 0<=dağcı_mermi.d_shoot1[index]<=window_x:
                            if dağcı_mermi.shoot1_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot1[index],dağcı_mermi.d_shoot1[index+1],10,5))
                                dağcı_mermi.d_shoot1[index]-=mermi_hız
                                dağcı_mermi.d_shoot1[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot1_collide(index)==2:
                                if dağcı_mermi.desert_eagle_shoot1_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                break
                            else:
                                d_shoot1.pop(index+1)
                                d_shoot1.pop(index)
                                break
                        else:
                            d_shoot1.pop(index+1)
                            d_shoot1.pop(index)
                            break
                else:
                    pass
            if 2 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot2),2):
                        if 0<=dağcı_mermi.d_shoot2[index]<=window_x:
                            if dağcı_mermi.shoot2_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot2[index],dağcı_mermi.d_shoot2[index+1],5,10))
                                dağcı_mermi.d_shoot2[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot2_collide(index)==2:
                                if dağcı_mermi.desert_eagle_shoot2_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot2.pop(index+1)
                                d_shoot2.pop(index)
                                break
                        else:
                            d_shoot2.pop(index+1)
                            d_shoot2.pop(index)
                            break
                else:
                    pass
            if 3 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot3),2):
                        if 0<=dağcı_mermi.d_shoot3[index]<=window_x:
                            if dağcı_mermi.shoot3_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot3[index],dağcı_mermi.d_shoot3[index+1],10,5))
                                dağcı_mermi.d_shoot3[index]+=mermi_hız
                                dağcı_mermi.d_shoot3[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot3_collide(index)==2:
                                if dağcı_mermi.desert_eagle_shoot3_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot3.pop(index+1)
                                d_shoot3.pop(index)
                                break
                        else:
                            d_shoot3.pop(index+1)
                            d_shoot3.pop(index)
                            break
                else:
                    pass

            if 4 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot4),2):
                        if 0<=dağcı_mermi.d_shoot4[index]<=window_x:
                            if dağcı_mermi.shoot4_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot4[index],dağcı_mermi.d_shoot4[index+1],10,5))
                                dağcı_mermi.d_shoot4[index]-=mermi_hız
                
                            elif dağcı_mermi.shoot4_collide(index)==2:
                                if dağcı_mermi.desert_eagle_shoot4_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot4.pop(index+1)
                                d_shoot4.pop(index)
                                break
                        else:
                            d_shoot4.pop(index+1)
                            d_shoot4.pop(index)
                            break
                else:
                    pass
                
            if 6 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot6),2):
                        if 0<=dağcı_mermi.d_shoot6[index]<=window_x:
                            if dağcı_mermi.shoot6_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot6[index],dağcı_mermi.d_shoot6[index+1],10,5))
                                dağcı_mermi.d_shoot6[index]+=mermi_hız
                            elif dağcı_mermi.shoot6_collide(index)==2:
                                if dağcı_mermi.desert_eagle_shoot6_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot6.pop(index+1)
                                d_shoot6.pop(index)
                                break
                        else:
                            d_shoot6.pop(index+1)
                            d_shoot6.pop(index)
                            break
                else:
                    pass

            if 7 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot7),2):
                        if 0<=dağcı_mermi.d_shoot7[index]<=window_x:
                            if dağcı_mermi.shoot7_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot7[index],dağcı_mermi.d_shoot7[index+1],10,5))
                                dağcı_mermi.d_shoot7[index]-=mermi_hız
                                dağcı_mermi.d_shoot7[index+1]-=mermi_hız
                
                            elif dağcı_mermi.shoot7_collide(index)==2:
                                if dağcı_mermi.desert_eagle_shoot7_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot7.pop(index+1)
                                d_shoot7.pop(index)
                                break
                        else:
                            d_shoot7.pop(index+1)
                            d_shoot7.pop(index)
                            break
                else:
                    pass

            if 8 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot8),2):
                        if 0<=dağcı_mermi.d_shoot8[index]<=window_x:
                            if dağcı_mermi.shoot8_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot8[index],dağcı_mermi.d_shoot8[index+1],5,10))
                                dağcı_mermi.d_shoot8[index+1]-=mermi_hız
                
                            elif dağcı_mermi.shoot8_collide(index)==2:
                                if dağcı_mermi.desert_eagle_shoot8_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot8.pop(index+1)
                                d_shoot8.pop(index)
                                break
                        else:
                            d_shoot8.pop(index+1)
                            d_shoot8.pop(index)
                            break
                else:
                    pass
            if 9 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot9),2):
                        if 0<=dağcı_mermi.d_shoot9[index]<=window_x:
                            if dağcı_mermi.shoot9_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot9[index],dağcı_mermi.d_shoot9[index+1],10,5))
                                dağcı_mermi.d_shoot9[index]+=mermi_hız
                                dağcı_mermi.d_shoot9[index+1]-=mermi_hız
                            elif dağcı_mermi.shoot9_collide(index)==2:
                                if dağcı_mermi.desert_eagle_shoot9_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break      
                            else:
                                d_shoot9.pop(index+1)
                                d_shoot9.pop(index)
                                break
                        else:
                            d_shoot9.pop(index+1)
                            d_shoot9.pop(index)
                            break
                else:
                    pass
            if 1 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shootj),2):
                        if 0<=cops_mermi.c_shootj[index]<=window_x:
                            if cops_mermi.shoot1_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootj[index],cops_mermi.c_shootj[index+1],10,5))
                                cops_mermi.c_shootj[index]+=mermi_hız
                            elif cops_mermi.shoot1_collide(index)==2:
                                if cops_mermi.awp_shoot1_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootj.pop(index+1)
                                c_shootj.pop(index)
                                break
                        else:
                            c_shootj.pop(index+1)
                            c_shootj.pop(index)
                            break
                else:
                    pass
            if 2 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shootu),2):
                        if 0<=cops_mermi.c_shootu[index]<=window_x:
                            if cops_mermi.shoot2_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootu[index],cops_mermi.c_shootu[index+1],10,5))
                                cops_mermi.c_shootu[index]+=mermi_hız
                                cops_mermi.c_shootu[index+1]-=mermi_hız
                            elif cops_mermi.shoot2_collide(index)==2:
                                if cops_mermi.awp_shoot2_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atıln_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootu.pop(index+1)
                                c_shootu.pop(index)
                                break
                        else:
                            c_shootu.pop(index+1)
                            c_shootu.pop(index)
                            break
                else:
                    pass
            if 3 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shootm),2):
                        if 0<=cops_mermi.c_shootm[index]<=window_x:
                            if cops_mermi.shoot3_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootm[index],cops_mermi.c_shootm[index+1],10,5))
                                cops_mermi.c_shootm[index]+=mermi_hız
                                cops_mermi.c_shootm[index+1]+=mermi_hız
                            elif cops_mermi.shoot3_collide(index)==2:
                                if cops_mermi.awp_shoot3_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootm.pop(index+1)
                                c_shootm.pop(index)
                                break
                        else:
                            c_shootm.pop(index+1)
                            c_shootm.pop(index)
                            break
                else:
                    pass
            if 4 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shootn),2):
                        if 0<=cops_mermi.c_shootn[index]<=window_x:
                            if cops_mermi.shoot4_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootn[index],cops_mermi.c_shootn[index+1],5,10))
                                cops_mermi.c_shootn[index+1]-=mermi_hız
                            elif cops_mermi.shoot4_collide(index)==2:
                                if cops_mermi.awp_shoot4_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootn.pop(index+1)
                                c_shootn.pop(index)
                                break
                        else:
                            c_shootn.pop(index+1)
                            c_shootn.pop(index)
                            break
                else:
                    pass
            if 5 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shooty),2):
                        if 0<=cops_mermi.c_shooty[index]<=window_x:
                            if cops_mermi.shoot5_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shooty[index],cops_mermi.c_shooty[index+1],5,10))                            
                                cops_mermi.c_shooty[index+1]+=mermi_hız
                            elif cops_mermi.shoot5_collide(index)==2:
                                if cops_mermi.awp_shoot5_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shooty.pop(index+1)
                                c_shooty.pop(index)
                                break
                        else:
                            c_shooty.pop(index+1)
                            c_shooty.pop(index)
                            break
                else:
                    pass
            if 6 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shootb),2):
                        if 0<=cops_mermi.c_shootb[index]<=window_x:
                            if cops_mermi.shoot6_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootb[index],cops_mermi.c_shootb[index+1],10,5))
                                cops_mermi.c_shootb[index]-=mermi_hız
                                cops_mermi.c_shootb[index+1]+=mermi_hız
                            elif cops_mermi.shoot6_collide(index)==2:
                                if cops_mermi.awp_shoot6_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootb.pop(index+1)
                                c_shootb.pop(index)
                                break
                        else:
                            c_shootb.pop(index+1)
                            c_shootb.pop(index)
                            break
                else:
                    pass
            if 7 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shootg),2):
                        if 0<=cops_mermi.c_shootg[index]<=window_x:
                            if cops_mermi.shoot7_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootg[index],cops_mermi.c_shootg[index+1],10,5))
                                cops_mermi.c_shootg[index]-=mermi_hız                           
                            elif cops_mermi.shoot7_collide(index)==2:
                                if cops_mermi.awp_shoot7_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootg.pop(index+1)
                                c_shootg.pop(index)
                                break
                        else:
                            c_shootg.pop(index+1)
                            c_shootg.pop(index)
                            break
                else:
                    pass
            if 8 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shoott),2):
                        if 0<=cops_mermi.c_shoott[index]<=window_x:
                            if cops_mermi.shoot8_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shoott[index],cops_mermi.c_shoott[index+1],10,5))
                                cops_mermi.c_shoott[index]-=mermi_hız
                                cops_mermi.c_shoott[index+1]-=mermi_hız
                            elif cops_mermi.shoot8_collide(index)==2:
                                if cops_mermi.awp_shoot8_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shoott.pop(index+1)
                                c_shoott.pop(index)
                                break
                        else:
                            c_shoott.pop(index+1)
                            c_shoott.pop(index)
                            break
                else:
                    pass
            if dağcılar_move.dağcı_x<=0 and dağcılar_move.dağcı_y<=0:
                dağcı_mermi_yön.clear()
                i+=1
                cops_awp_mermi_toplam=10
                dağcı_desert_eagle_mermi_toplam=60
                cops_deneme=1
                dağcı_deneme=1
                special_forces.para+=0
                dağcılar.para+=1500
                dağcı_atılan_mermi=0
                cops_atılan_mermi=0
                dağcı_win+=1
                dağcılar_move.dağcı_x=dağcı_x
                dağcılar_move.dağcı_y=dağcı_y
                special_forces_move.cops_x=cops_x
                special_forces_move.cops_y=cops_y
                special_forces.can=100
                dağcılar.can=100
                choose1,choose2=False,True
            pygame.draw.rect(window,(rgb.kum),special_forces_rect)
            pygame.draw.rect(window,(rgb.kum),dağcı_rect)
            window.blit(special_corps_copy,(special_forces_move.cops_x,special_forces_move.cops_y))
            window.blit(dağcı_copy,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y))
            window.blit(yazı_7,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y+2))
            window.blit(yazı_8,(special_forces_move.cops_x+45,special_forces_move.cops_y-5))
            window.blit(yazı_9,(window_x//2+30,20))
            window.blit(yazı_10,(special_forces_move.cops_x+45,special_forces_move.cops_y+4))
            window.blit(yazı_11,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y+12))
            window.blit(special_corps_logo,(1470,0))
            window.blit(dağcı_logo,(1470,35))
            window.blit(yazı_12,(1510,-5))
            window.blit(yazı_13,(1510,32))
            pygame.display.update()
        if special_forces.silah=="awp" and dağcılar.silah=="ak_47":     
            cops_kalan_mermi=awp_mermi-cops_atılan_mermi 
            dağcı_kalan_mermi=ak_47_mermi-dağcı_atılan_mermi     
            window.fill((rgb.kum))
            pygame.draw.rect(window,(0,0,0),engel_1)
            pygame.draw.rect(window,(0,0,0),engel_2)
            pygame.draw.rect(window,(0,0,0),engel_3)
            pygame.draw.rect(window,(0,0,0),engel_4)
            pygame.draw.rect(window,(0,0,0),engel_5)
            pygame.draw.rect(window,(0,0,0),engel_6)
            yazı_7=yazı_tipi_7.render(f"{dağcılar.can}/100",True,(0,0,0))
            yazı_8=yazı_tipi_8.render(f"{special_forces.can}/100",True,(0,0,0))
            yazı_9=yazı_tipi_9.render(f"Round {i}",True,(0,0,0))
            yazı_12=yazı_tipi_12.render(f"{cops_win}",True,(0,0,0))
            yazı_13=yazı_tipi_13.render(f"{dağcı_win}",True,(0,0,0))
            yazı_10=yazı_tipi_10.render(f"{cops_kalan_mermi}/{cops_awp_mermi_toplam}",True,(0,0,0))
            yazı_11=yazı_tipi_11.render(f"{dağcı_kalan_mermi}/{dağcı_ak_47_mermi_toplam}",True,(0,0,0))
            special_forces_rect=pygame.Rect(special_forces_move.cops_x,special_forces_move.cops_y,special_corps_size_x,special_corps_size_y)
            dağcı_rect=pygame.Rect(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y,dağcılar_size_x,dağcılar_size_y)
            keys=pygame.key.get_pressed()
            if keys[pygame.K_w] and special_forces_move.cops_y>=0 :
                special_forces_move.w()
            if keys[pygame.K_s] and special_forces_move.cops_y<=window_y-special_corps.get_size()[1]:
                special_forces_move.s()
            if keys[pygame.K_a] and special_forces_move.cops_x>=0:
                special_forces_move.a()
            if keys[pygame.K_d] and special_forces_move.cops_x<=window_x-special_corps.get_size()[0]:
                special_forces_move.d()
            if keys[pygame.K_UP] and dağcılar_move.dağcı_y>=0:
                dağcılar_move.up()
            if keys[pygame.K_DOWN] and dağcılar_move.dağcı_y<=window_y-dağcılar_size_y:
                dağcılar_move.down()
            if keys[pygame.K_LEFT] and dağcılar_move.dağcı_x>=0:
                dağcılar_move.left()
            if keys[pygame.K_RIGHT] and dağcılar_move.dağcı_x<=window_x-dağcılar_size_x:
                dağcılar_move.right()
            if cops_atılan_mermi<awp_mermi:
                if keys[pygame.K_j]:
                    cops_mermi_yön.add(1)
                    cops_mermi.awp_shoot1()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_u]:
                    cops_mermi_yön.add(2)
                    cops_mermi.awp_shoot2()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_m]:
                    cops_mermi_yön.add(3)
                    cops_mermi.awp_shoot3()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_y]:
                    cops_mermi_yön.add(4)
                    cops_mermi.awp_shoot4()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_n]:
                    cops_mermi_yön.add(5)
                    cops_mermi.awp_shoot5()
                    cops_atılan_mermi=1
                    time.sleep(0.1)
                if keys[pygame.K_b]:
                    cops_mermi_yön.add(6)
                    cops_mermi.awp_shoot6()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_g]:
                    cops_mermi_yön.add(7)
                    cops_mermi.awp_shoot7()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_t]:
                    cops_mermi_yön.add(8)
                    cops_mermi.awp_shoot8()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
            else:
                pass
            if keys[pygame.K_r]:
                if cops_awp_mermi_toplam-cops_atılan_mermi>=0:
                    cops_awp_mermi_toplam-=cops_atılan_mermi
                    cops_atılan_mermi=0
                else:
                    if cops_deneme==0:
                        pass
                    else:
                        cops_atılan_mermi=awp_mermi-cops_awp_mermi_toplam-cops_kalan_mermi
                        cops_awp_mermi_toplam-=cops_awp_mermi_toplam
                        cops_deneme=0         
            if dağcı_atılan_mermi<ak_47_mermi:
                if keys[pygame.K_KP_1]:
                    dağcı_mermi_yön.add(1)
                    dağcı_mermi.ak_47_shoot1()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_2]:
                    dağcı_mermi_yön.add(2)
                    dağcı_mermi.ak_47_shoot2()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_3]:
                    dağcı_mermi_yön.add(3)
                    dağcı_mermi.ak_47_shoot3()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_4]:
                    dağcı_mermi_yön.add(4)
                    dağcı_mermi.ak_47_shoot4()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_6]:
                    dağcı_mermi_yön.add(6)
                    dağcı_mermi.ak_47_shoot6()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_7]:
                    dağcı_mermi_yön.add(7)
                    dağcı_mermi.ak_47_shoot7()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_8]:
                    dağcı_mermi_yön.add(8)
                    dağcı_mermi.ak_47_shoot8()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_9]:
                    dağcı_mermi_yön.add(9)  
                    dağcı_mermi.ak_47_shoot9()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
            else:
                pass
            if keys[pygame.K_KP_5]:
                if dağcı_ak_47_mermi_toplam-dağcı_atılan_mermi>=0:
                    dağcı_ak_47_mermi_toplam-=dağcı_atılan_mermi
                    dağcı_atılan_mermi=0
                else:
                    if dağcı_deneme==0:
                        pass
                    else:
                        dağcı_atılan_mermi=ak_47_mermi-dağcı_ak_47_mermi_toplam-dağcı_kalan_mermi
                        dağcı_ak_47_mermi_toplam-=dağcı_ak_47_mermi_toplam
                        dağcı_deneme=0    
            if 1 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=ak_47_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot1),2):
                        if 0<=dağcı_mermi.d_shoot1[index]<=window_x:
                            if dağcı_mermi.shoot1_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot1[index],dağcı_mermi.d_shoot1[index+1],10,5))
                                dağcı_mermi.d_shoot1[index]-=mermi_hız
                                dağcı_mermi.d_shoot1[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot1_collide(index)==2:
                                if dağcı_mermi.ak_47_shoot1_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                break
                            else:
                                d_shoot1.pop(index+1)
                                d_shoot1.pop(index)
                                break
                        else:
                            d_shoot1.pop(index+1)
                            d_shoot1.pop(index)
                            break
                else:
                    pass
            if 2 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=ak_47_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot2),2):
                        if 0<=dağcı_mermi.d_shoot2[index]<=window_x:
                            if dağcı_mermi.shoot2_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot2[index],dağcı_mermi.d_shoot2[index+1],5,10))
                                dağcı_mermi.d_shoot2[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot2_collide(index)==2:
                                if dağcı_mermi.ak_47_shoot2_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot2.pop(index+1)
                                d_shoot2.pop(index)
                                break
                        else:
                            d_shoot2.pop(index+1)
                            d_shoot2.pop(index)
                            break
                else:
                    pass
            if 3 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=ak_47_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot3),2):
                        if 0<=dağcı_mermi.d_shoot3[index]<=window_x:
                            if dağcı_mermi.shoot3_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot3[index],dağcı_mermi.d_shoot3[index+1],10,5))
                                dağcı_mermi.d_shoot3[index]+=mermi_hız
                                dağcı_mermi.d_shoot3[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot3_collide(index)==2:
                                if dağcı_mermi.ak_47_shoot3_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot3.pop(index+1)
                                d_shoot3.pop(index)
                                break
                        else:
                            d_shoot3.pop(index+1)
                            d_shoot3.pop(index)
                            break
                else:
                    pass
            if 4 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=ak_47_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot4),2):
                        if 0<=dağcı_mermi.d_shoot4[index]<=window_x:
                            if dağcı_mermi.shoot4_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot4[index],dağcı_mermi.d_shoot4[index+1],10,5))
                                dağcı_mermi.d_shoot4[index]-=mermi_hız           
                            elif dağcı_mermi.shoot4_collide(index)==2:
                                if dağcı_mermi.ak_47_shoot4_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot4.pop(index+1)
                                d_shoot4.pop(index)
                                break
                        else:
                            d_shoot4.pop(index+1)
                            d_shoot4.pop(index)
                            break
                else:
                    pass
            if 6 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=ak_47_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot6),2):
                        if 0<=dağcı_mermi.d_shoot6[index]<=window_x:
                            if dağcı_mermi.shoot6_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot6[index],dağcı_mermi.d_shoot6[index+1],10,5))
                                dağcı_mermi.d_shoot6[index]+=mermi_hız
                            elif dağcı_mermi.shoot6_collide(index)==2:
                                if dağcı_mermi.ak_47_shoot6_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot6.pop(index+1)
                                d_shoot6.pop(index)
                                break
                        else:
                            d_shoot6.pop(index+1)
                            d_shoot6.pop(index)
                            break
                else:
                    pass
            if 7 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=ak_47_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot7),2):
                        if 0<=dağcı_mermi.d_shoot7[index]<=window_x:
                            if dağcı_mermi.shoot7_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot7[index],dağcı_mermi.d_shoot7[index+1],10,5))
                                dağcı_mermi.d_shoot7[index]-=mermi_hız
                                dağcı_mermi.d_shoot7[index+1]-=mermi_hız
                            elif dağcı_mermi.shoot7_collide(index)==2:
                                if dağcı_mermi.ak_47_shoot7_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot7.pop(index+1)
                                d_shoot7.pop(index)
                                break
                        else:
                            d_shoot7.pop(index+1)
                            d_shoot7.pop(index)
                            break
                else:
                    pass
            if 8 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=ak_47_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot8),2):
                        if 0<=dağcı_mermi.d_shoot8[index]<=window_x:
                            if dağcı_mermi.shoot8_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot8[index],dağcı_mermi.d_shoot8[index+1],5,10))
                                dağcı_mermi.d_shoot8[index+1]-=mermi_hız
                            elif dağcı_mermi.shoot8_collide(index)==2:
                                if dağcı_mermi.ak_47_shoot8_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot8.pop(index+1)
                                d_shoot8.pop(index)
                                break
                    else:
                        d_shoot8.pop(index+1)
                        d_shoot8.pop(index)
                        break
                else:
                    pass
            if 9 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=ak_47_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot9),2):
                        if 0<=dağcı_mermi.d_shoot9[index]<=window_x:
                            if dağcı_mermi.shoot9_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot9[index],dağcı_mermi.d_shoot9[index+1],10,5))
                                dağcı_mermi.d_shoot9[index]+=mermi_hız
                                dağcı_mermi.d_shoot9[index+1]-=mermi_hız
                            elif dağcı_mermi.shoot9_collide(index)==2:
                                if dağcı_mermi.ak_47_shoot9_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break      
                            else:
                                d_shoot9.pop(index+1)
                                d_shoot9.pop(index)
                                break
                        else:
                            d_shoot9.pop(index+1)
                            d_shoot9.pop(index)
                            break
                else:
                    pass
            if 1 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shootj),2):
                        if 0<=cops_mermi.c_shootj[index]<=window_x:
                            if cops_mermi.shoot1_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootj[index],cops_mermi.c_shootj[index+1],10,5))
                                cops_mermi.c_shootj[index]+=mermi_hız
                            elif cops_mermi.shoot1_collide(index)==2:
                                if cops_mermi.awp_shoot1_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootj.pop(index+1)
                                c_shootj.pop(index)
                                break
                        else:
                            c_shootj.pop(index+1)
                            c_shootj.pop(index)
                            break
                else:
                    pass
            if 2 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shootu),2):
                        if 0<=cops_mermi.c_shootu[index]<=window_x:
                            if cops_mermi.shoot2_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootu[index],cops_mermi.c_shootu[index+1],10,5))
                                cops_mermi.c_shootu[index]+=mermi_hız
                                cops_mermi.c_shootu[index+1]-=mermi_hız
                            elif cops_mermi.shoot2_collide(index)==2:
                                if cops_mermi.awp_shoot2_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootu.pop(index+1)
                                c_shootu.pop(index)
                                break
                        else:
                            c_shootu.pop(index+1)
                            c_shootu.pop(index)
                            break
                else:
                    pass
            if 3 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shootm),2):
                        if 0<=cops_mermi.c_shootm[index]<=window_x:
                            if cops_mermi.shoot3_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootm[index],cops_mermi.c_shootm[index+1],10,5))
                                cops_mermi.c_shootm[index]+=mermi_hız
                                cops_mermi.c_shootm[index+1]+=mermi_hız
                            elif cops_mermi.shoot3_collide(index)==2:
                                if cops_mermi.awp_shoot3_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootm.pop(index+1)
                                c_shootm.pop(index)
                                break
                        else:
                            c_shootm.pop(index+1)
                            c_shootm.pop(index)
                            break
                else:
                    pass
            if 4 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shootn),2):
                        if 0<=cops_mermi.c_shootn[index]<=window_x:
                            if cops_mermi.shoot4_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootn[index],cops_mermi.c_shootn[index+1],5,10))
                                cops_mermi.c_shootn[index+1]-=mermi_hız
                            elif cops_mermi.shoot4_collide(index)==2:
                                if cops_mermi.awp_shoot4_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootn.pop(index+1)
                                c_shootn.pop(index)
                                break
                        else:
                            c_shootn.pop(index+1)
                            c_shootn.pop(index)
                            break
                else:
                    pass
            if 5 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shooty),2):
                        if 0<=cops_mermi.c_shooty[index]<=window_x:
                            if cops_mermi.shoot5_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shooty[index],cops_mermi.c_shooty[index+1],5,10))
                                cops_mermi.c_shooty[index+1]+=mermi_hız
                            elif cops_mermi.shoot5_collide(index)==2:
                                if cops_mermi.awp_shoot5_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shooty.pop(index+1)
                                c_shooty.pop(index)
                                break
                        else:
                            c_shooty.pop(index+1)
                            c_shooty.pop(index)
                            break
                else:
                    pass
            if 6 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shootb),2):
                        if 0<=cops_mermi.c_shootb[index]<=window_x:
                            if cops_mermi.shoot6_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootb[index],cops_mermi.c_shootb[index+1],10,5))
                                cops_mermi.c_shootb[index]-=mermi_hız
                                cops_mermi.c_shootb[index+1]+=mermi_hız
                            elif cops_mermi.shoot6_collide(index)==2:
                                if cops_mermi.awp_shoot6_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootb.pop(index+1)
                                c_shootb.pop(index)
                                break
                        else:
                            c_shootb.pop(index+1)
                            c_shootb.pop(index)
                            break
                else:
                    pass
            if 7 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shootg),2):
                        if 0<=cops_mermi.c_shootg[index]<=window_x:
                            if cops_mermi.shoot7_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootg[index],cops_mermi.c_shootg[index+1],10,5))
                                cops_mermi.c_shootg[index]-=mermi_hız
                            elif cops_mermi.shoot7_collide(index)==2:
                                if cops_mermi.awp_shoot7_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootg.pop(index+1)
                                c_shootg.pop(index)
                                break
                        else:
                            c_shootg.pop(index+1)
                            c_shootg.pop(index)
                            break
                else:
                    pass
            if 8 in cops_mermi_yön:
                if cops_atılan_mermi<=awp_mermi:
                    for index in range(0,len(cops_mermi.c_shoott),2):
                        if 0<=cops_mermi.c_shoott[index]<=window_x:
                            if cops_mermi.shoot8_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shoott[index],cops_mermi.c_shoott[index+1],10,5))
                                cops_mermi.c_shoott[index]-=mermi_hız
                                cops_mermi.c_shoott[index+1]-=mermi_hız
                            elif cops_mermi.shoot8_collide(index)==2:
                                if cops_mermi.awp_shoot8_isabet(i)==1:
                                    i+=1
                                    cops_awp_mermi_toplam=10
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shoott.pop(index+1)
                                c_shoott.pop(index)
                                break
                        else:
                            c_shoott.pop(index+1)
                            c_shoott.pop(index)
                            break
                else:
                    pass
            if dağcılar_move.dağcı_x<=0 and dağcılar_move.dağcı_y<=0:
                dağcı_mermi_yön.clear()
                i+=1
                cops_awp_mermi_toplam=10
                dağcı_ak_47_mermi_toplam=90
                cops_deneme=1
                dağcı_deneme=1
                dağcı_win+=1
                dağcı_atılan_mermi=0
                cops_atılan_mermi=0
                special_forces.para+=0
                dağcılar.para+=1500
                dağcılar_move.dağcı_x=dağcı_x
                dağcılar_move.dağcı_y=dağcı_y
                special_forces_move.cops_x=cops_x
                special_forces_move.cops_y=cops_y
                special_forces.can=100
                dağcılar.can=100
                choose1,choose2=True,False
            pygame.draw.rect(window,(rgb.kum),special_forces_rect)
            pygame.draw.rect(window,(rgb.kum),dağcı_rect)
            window.blit(special_corps_copy,(special_forces_move.cops_x,special_forces_move.cops_y))
            window.blit(dağcı_copy,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y))
            window.blit(yazı_7,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y+2))
            window.blit(yazı_8,(special_forces_move.cops_x+45,special_forces_move.cops_y-5))
            window.blit(yazı_9,(window_x//2+15,20))
            window.blit(yazı_10,(special_forces_move.cops_x+45,special_forces_move.cops_y+4))
            window.blit(yazı_11,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y+12))
            window.blit(special_corps_logo,(1470,0))
            window.blit(dağcı_logo,(1470,35))
            window.blit(yazı_12,(1510,-5))
            window.blit(yazı_13,(1510,32))
            pygame.display.update()
        if special_forces.silah=="desert_eagle" and dağcılar.silah=="awp":
            cops_kalan_mermi=desert_eagle_mermi-cops_atılan_mermi 
            dağcı_kalan_mermi=awp_mermi-dağcı_atılan_mermi         
            window.fill((rgb.kum))
            pygame.draw.rect(window,(0,0,0),engel_1)
            pygame.draw.rect(window,(0,0,0),engel_2)
            pygame.draw.rect(window,(0,0,0),engel_3)
            pygame.draw.rect(window,(0,0,0),engel_4)
            pygame.draw.rect(window,(0,0,0),engel_5)
            pygame.draw.rect(window,(0,0,0),engel_6)
            yazı_7=yazı_tipi_7.render(f"{dağcılar.can}/100",True,(0,0,0))
            yazı_8=yazı_tipi_8.render(f"{special_forces.can}/100",True,(0,0,0))
            yazı_9=yazı_tipi_9.render(f"Round {i}",True,(0,0,0))
            yazı_12=yazı_tipi_12.render(f"{cops_win}",True,(0,0,0))
            yazı_13=yazı_tipi_13.render(f"{dağcı_win}",True,(0,0,0))
            yazı_10=yazı_tipi_10.render(f"{cops_kalan_mermi}/{cops_desert_eagle_mermi_toplam}",True,(0,0,0))
            yazı_11=yazı_tipi_11.render(f"{dağcı_kalan_mermi}/{dağcı_awp_mermi_toplam}",True,(0,0,0))
            special_forces_rect=pygame.Rect(special_forces_move.cops_x,special_forces_move.cops_y,special_corps_size_x,special_corps_size_y)
            dağcı_rect=pygame.Rect(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y,dağcılar_size_x,dağcılar_size_y)
            keys=pygame.key.get_pressed()
            if keys[pygame.K_w] and special_forces_move.cops_y>=0 :
                special_forces_move.w()
            if keys[pygame.K_s] and special_forces_move.cops_y<=window_y-special_corps.get_size()[1]:
                special_forces_move.s()
            if keys[pygame.K_a] and special_forces_move.cops_x>=0:
                special_forces_move.a()
            if keys[pygame.K_d] and special_forces_move.cops_x<=window_x-special_corps.get_size()[0]:
                special_forces_move.d()
            if keys[pygame.K_UP] and dağcılar_move.dağcı_y>=0:
                dağcılar_move.up()
            if keys[pygame.K_DOWN] and dağcılar_move.dağcı_y<=window_y-dağcılar_size_y:
                dağcılar_move.down()
            if keys[pygame.K_LEFT] and dağcılar_move.dağcı_x>=0:
                dağcılar_move.left()
            if keys[pygame.K_RIGHT] and dağcılar_move.dağcı_x<=window_x-dağcılar_size_x:
                dağcılar_move.right()
            if cops_atılan_mermi<desert_eagle_mermi:
                if keys[pygame.K_j]:
                    cops_mermi_yön.add(1)
                    cops_mermi.desert_eagle_shoot1()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_u]:
                    cops_mermi_yön.add(2)
                    cops_mermi.desert_eagle_shoot2()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_m]:
                    cops_mermi_yön.add(3)
                    cops_mermi.desert_eagle_shoot3()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_y]:
                    cops_mermi_yön.add(4)
                    cops_mermi.desert_eagle_shoot4()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_n]:
                    cops_mermi_yön.add(5)
                    cops_mermi.desert_eagle_shoot5()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_b]:
                    cops_mermi_yön.add(6)
                    cops_mermi.desert_eagle_shoot6()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_g]:
                    cops_mermi_yön.add(7)
                    cops_mermi.desert_eagle_shoot7()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_t]:
                    cops_mermi_yön.add(8)
                    cops_mermi.desert_eagle_shoot8()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
            else:
                pass
            if keys[pygame.K_r]:
                if cops_desert_eagle_mermi_toplam-cops_atılan_mermi>=0:
                    cops_desert_eagle_mermi_toplam-=cops_atılan_mermi
                    cops_atılan_mermi=0
                else:
                    if cops_deneme==0:
                        pass
                    else:
                        cops_atılan_mermi=desert_eagle_mermi-cops_desert_eagle_mermi_toplam-cops_kalan_mermi
                        cops_desert_eagle_mermi_toplam-=cops_desert_eagle_mermi_toplam
                        cops_deneme=0         
            if dağcı_atılan_mermi<awp_mermi:
                if keys[pygame.K_KP_1]:
                    dağcı_mermi_yön.add(1)
                    dağcı_mermi.awp_shoot1()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_2]:
                    dağcı_mermi_yön.add(2)
                    dağcı_mermi.awp_shoot2()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_3]:
                    dağcı_mermi_yön.add(3)
                    dağcı_mermi.awp_shoot3()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_4]:
                    dağcı_mermi_yön.add(4)
                    dağcı_mermi.awp_shoot4()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_6]:
                    dağcı_mermi_yön.add(6)
                    dağcı_mermi.awp_shoot6()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_7]:
                    dağcı_mermi_yön.add(7)
                    dağcı_mermi.awp_shoot7()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_8]:
                    dağcı_mermi_yön.add(8)
                    dağcı_mermi.awp_shoot8()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_9]:
                    dağcı_mermi_yön.add(9)  
                    dağcı_mermi.awp_shoot9()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
            else:
                pass
            if keys[pygame.K_KP_5]:
                if dağcı_awp_mermi_toplam-dağcı_atılan_mermi>=0:
                    dağcı_awp_mermi_toplam-=dağcı_atılan_mermi
                    dağcı_atılan_mermi=0
                else:
                    if dağcı_deneme==0:
                        pass
                    else:
                        dağcı_atılan_mermi=awp_mermi-dağcı_awp_mermi_toplam-dağcı_kalan_mermi
                        dağcı_awp_mermi_toplam-=dağcı_awp_mermi_toplam
                        dağcı_deneme=0      
            if 1 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot1),2):
                        if 0<=dağcı_mermi.d_shoot1[index]<=window_x:
                            if dağcı_mermi.shoot1_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot1[index],dağcı_mermi.d_shoot1[index+1],10,5))
                                dağcı_mermi.d_shoot1[index]-=mermi_hız
                                dağcı_mermi.d_shoot1[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot1_collide(index)==2:
                                if dağcı_mermi.awp_shoot1_isabet(i)==1:
                                    i+=1
                                    dağcı_win+=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                break
                            else:
                                d_shoot1.pop(index+1)
                                d_shoot1.pop(index)
                                break
                        else:
                            d_shoot1.pop(index+1)
                            d_shoot1.pop(index)
                            break
                else:
                    pass
            if 2 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot2),2):
                        if 0<=dağcı_mermi.d_shoot2[index]<=window_x:
                            if dağcı_mermi.shoot2_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot2[index],dağcı_mermi.d_shoot2[index+1],5,10))
                                dağcı_mermi.d_shoot2[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot2_collide(index)==2:
                                if dağcı_mermi.awp_shoot2_isabet(i)==1:
                                    i+=1
                                    dağcı_win+=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot2.pop(index+1)
                                d_shoot2.pop(index)
                                break
                        else:
                            d_shoot2.pop(index+1)
                            d_shoot2.pop(index)
                            break
                else:
                    pass
            if 3 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot3),2):
                        if 0<=dağcı_mermi.d_shoot3[index]<=window_x:
                            if dağcı_mermi.shoot3_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot3[index],dağcı_mermi.d_shoot3[index+1],10,5))
                                dağcı_mermi.d_shoot3[index]+=mermi_hız
                                dağcı_mermi.d_shoot3[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot3_collide(index)==2:
                                if dağcı_mermi.awp_shoot3_isabet(i)==1:
                                    i+=1
                                    dağcı_win+=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot3.pop(index+1)
                                d_shoot3.pop(index)
                                break
                        else:
                            d_shoot3.pop(index+1)
                            d_shoot3.pop(index)
                            break
                else:
                    pass

            if 4 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot4),2):
                        if 0<=dağcı_mermi.d_shoot4[index]<=window_x:
                            if dağcı_mermi.shoot4_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot4[index],dağcı_mermi.d_shoot4[index+1],10,5))
                                dağcı_mermi.d_shoot4[index]-=mermi_hız
                            elif dağcı_mermi.shoot4_collide(index)==2:
                                if dağcı_mermi.awp_shoot4_isabet(i)==1:
                                    i+=1
                                    dağcı_win+=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot4.pop(index+1)
                                d_shoot4.pop(index)
                                break
                        else:
                            d_shoot4.pop(index+1)
                            d_shoot4.pop(index)
                            break
                else:
                    pass

            if 6 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot6),2):
                        if 0<=dağcı_mermi.d_shoot6[index]<=window_x:
                            if dağcı_mermi.shoot6_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot6[index],dağcı_mermi.d_shoot6[index+1],10,5))
                                dağcı_mermi.d_shoot6[index]+=mermi_hız
                            elif dağcı_mermi.shoot6_collide(index)==2:
                                if dağcı_mermi.awp_shoot6_isabet(i)==1:
                                    i+=1
                                    dağcı_win+=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot6.pop(index+1)
                                d_shoot6.pop(index)
                                break
                        else:
                            d_shoot6.pop(index+1)
                            d_shoot6.pop(index)
                            break
                else:
                    pass

            if 7 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot7),2):
                        if 0<=dağcı_mermi.d_shoot7[index]<=window_x:
                            if dağcı_mermi.shoot7_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot7[index],dağcı_mermi.d_shoot7[index+1],10,5))
                                dağcı_mermi.d_shoot7[index]-=mermi_hız
                                dağcı_mermi.d_shoot7[index+1]-=mermi_hız
                            elif dağcı_mermi.shoot7_collide(index)==2:
                                if dağcı_mermi.awp_shoot7_isabet(i)==1:
                                    i+=1
                                    dağcı_win+=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot7.pop(index+1)
                                d_shoot7.pop(index)
                                break
                        else:
                            d_shoot7.pop(index+1)
                            d_shoot7.pop(index)
                            break
                else:
                    pass

            if 8 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot8),2):
                        if 0<=dağcı_mermi.d_shoot8[index]<=window_x:
                            if dağcı_mermi.shoot8_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot8[index],dağcı_mermi.d_shoot8[index+1],5,10))
                                dağcı_mermi.d_shoot8[index+1]-=mermi_hız
                            elif dağcı_mermi.shoot8_collide(index)==2:
                                if dağcı_mermi.awp_shoot8_isabet(i)==1:
                                    i+=1
                                    dağcı_win+=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot8.pop(index+1)
                                d_shoot8.pop(index)
                                break
                        else:
                            d_shoot8.pop(index+1)
                            d_shoot8.pop(index)
                            break
                else:
                    pass
            if 9 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot9),2):
                        if 0<=dağcı_mermi.d_shoot9[index]<=window_x:
                            if dağcı_mermi.shoot9_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot9[index],dağcı_mermi.d_shoot9[index+1],10,5))
                                dağcı_mermi.d_shoot9[index]+=mermi_hız
                                dağcı_mermi.d_shoot9[index+1]-=mermi_hız
                            elif dağcı_mermi.shoot9_collide(index)==2:
                                if dağcı_mermi.awp_shoot9_isabet(i)==1:
                                    i+=1
                                    dağcı_win+=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break      
                            else:
                                d_shoot9.pop(index+1)
                                d_shoot9.pop(index)
                                break
                        else:
                            d_shoot9.pop(index+1)
                            d_shoot9.pop(index)
                            break
                else:
                    pass
            if 1 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shootj),2):
                        if 0<=cops_mermi.c_shootj[index]<=window_x:
                            if cops_mermi.shoot1_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootj[index],cops_mermi.c_shootj[index+1],10,5))
                                cops_mermi.c_shootj[index]+=mermi_hız
                            elif cops_mermi.shoot1_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot1_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootj.pop(index+1)
                                c_shootj.pop(index)
                                break
                        else:
                            c_shootj.pop(index+1)
                            c_shootj.pop(index)
                            break
                else:
                    pass
            if 2 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shootu),2):
                        if 0<=cops_mermi.c_shootu[index]<=window_x:
                            if cops_mermi.shoot2_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootu[index],cops_mermi.c_shootu[index+1],10,5))
                                cops_mermi.c_shootu[index]+=mermi_hız
                                cops_mermi.c_shootu[index+1]-=mermi_hız
                            elif cops_mermi.shoot2_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot2_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootu.pop(index+1)
                                c_shootu.pop(index)
                                break
                        else:
                            c_shootu.pop(index+1)
                            c_shootu.pop(index)
                            break
                else:
                    pass
            if 3 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shootm),2):
                        if 0<=cops_mermi.c_shootm[index]<=window_x:
                            if cops_mermi.shoot3_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootm[index],cops_mermi.c_shootm[index+1],10,5))
                                cops_mermi.c_shootm[index]+=mermi_hız
                                cops_mermi.c_shootm[index+1]+=mermi_hız
                            elif cops_mermi.shoot3_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot3_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootm.pop(index+1)
                                c_shootm.pop(index)
                                break
                        else:
                            c_shootm.pop(index+1)
                            c_shootm.pop(index)
                            break
                else:
                    pass
            if 4 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shootn),2):
                        if 0<=cops_mermi.c_shootn[index]<=window_x:
                            if cops_mermi.shoot4_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootn[index],cops_mermi.c_shootn[index+1],5,10))
                                cops_mermi.c_shootn[index+1]-=mermi_hız
                            elif cops_mermi.shoot4_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot4_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootn.pop(index+1)
                                c_shootn.pop(index)
                                break
                        else:
                            c_shootn.pop(index+1)
                            c_shootn.pop(index)
                            break
                else:
                    pass
            if 5 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shooty),2):
                        if 0<=cops_mermi.c_shooty[index]<=window_x:
                            if cops_mermi.shoot5_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shooty[index],cops_mermi.c_shooty[index+1],5,10))
                                cops_mermi.c_shooty[index+1]+=mermi_hız
                            elif cops_mermi.shoot5_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot5_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shooty.pop(index+1)
                                c_shooty.pop(index)
                                break
                        else:
                            c_shooty.pop(index+1)
                            c_shooty.pop(index)
                            break
                else:
                    pass
            if 6 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shootb),2):
                        if 0<=cops_mermi.c_shootb[index]<=window_x:
                            if cops_mermi.shoot6_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootb[index],cops_mermi.c_shootb[index+1],10,5))
                                cops_mermi.c_shootb[index]-=mermi_hız
                                cops_mermi.c_shootb[index+1]+=mermi_hız
                            elif cops_mermi.shoot6_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot6_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootb.pop(index+1)
                                c_shootb.pop(index)
                                break
                        else:
                            c_shootb.pop(index+1)
                            c_shootb.pop(index)
                            break
                else:
                    pass
            if 7 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shootg),2):
                        if 0<=cops_mermi.c_shootg[index]<=window_x:
                            if cops_mermi.shoot7_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootg[index],cops_mermi.c_shootg[index+1],10,5))
                                cops_mermi.c_shootg[index]-=mermi_hız  
                            elif cops_mermi.shoot7_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot7_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootg.pop(index+1)
                                c_shootg.pop(index)
                                break
                        else:
                            c_shootg.pop(index+1)
                            c_shootg.pop(index)
                            break
                else:
                    pass
            if 8 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shoott),2):
                        if 0<=cops_mermi.c_shoott[index]<=window_x:
                            if cops_mermi.shoot8_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shoott[index],cops_mermi.c_shoott[index+1],10,5))
                                cops_mermi.c_shoott[index]-=mermi_hız
                                cops_mermi.c_shoott[index+1]-=mermi_hız
                            elif cops_mermi.shoot8_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot8_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shoott.pop(index+1)
                                c_shoott.pop(index)
                                break
                        else:
                            c_shoott.pop(index+1)
                            c_shoott.pop(index)
                            break
                else:
                    pass
            if dağcılar_move.dağcı_x<=0 and dağcılar_move.dağcı_y<=0:
                dağcı_mermi_yön.clear()
                i+=1
                dağcı_win+=1
                cops_desert_eagle_mermi_toplam=60
                dağcı_awp_mermi_toplam=10
                cops_deneme=1
                dağcı_deneme=1
                special_forces.para+=0
                dağcılar.para+=1500
                dağcı_atılan_mermi+=0
                cops_atılan_mermi=0
                dağcılar_move.dağcı_x=dağcı_x
                dağcılar_move.dağcı_y=dağcı_y
                special_forces_move.cops_x=cops_x
                special_forces_move.cops_y=cops_y
                special_forces.can=100
                dağcılar.can=100
                choose1,choose2=True,False
            pygame.draw.rect(window,(rgb.kum),special_forces_rect)
            pygame.draw.rect(window,(rgb.kum),dağcı_rect)
            window.blit(special_corps_copy,(special_forces_move.cops_x,special_forces_move.cops_y))
            window.blit(dağcı_copy,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y))
            window.blit(yazı_7,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y+2))
            window.blit(yazı_8,(special_forces_move.cops_x+45,special_forces_move.cops_y-5))
            window.blit(yazı_9,(window_x//2+15,20))
            window.blit(yazı_10,(special_forces_move.cops_x+45,special_forces_move.cops_y+4))
            window.blit(yazı_11,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y+12))
            window.blit(special_corps_logo,(1470,0))
            window.blit(dağcı_logo,(1470,35))
            window.blit(yazı_12,(1510,-5))
            window.blit(yazı_13,(1510,32))
            pygame.display.update()
        if special_forces.silah=="desert_eagle" and dağcılar.silah=="desert_eagle":
            cops_kalan_mermi=desert_eagle_mermi-cops_atılan_mermi 
            dağcı_kalan_mermi=desert_eagle_mermi-dağcı_atılan_mermi         
            window.fill((rgb.kum))
            pygame.draw.rect(window,(0,0,0),engel_1)
            pygame.draw.rect(window,(0,0,0),engel_2)
            pygame.draw.rect(window,(0,0,0),engel_3)
            pygame.draw.rect(window,(0,0,0),engel_4)
            pygame.draw.rect(window,(0,0,0),engel_5)
            pygame.draw.rect(window,(0,0,0),engel_6)
            yazı_7=yazı_tipi_7.render(f"{dağcılar.can}/100",True,(0,0,0))
            yazı_8=yazı_tipi_8.render(f"{special_forces.can}/100",True,(0,0,0))
            yazı_9=yazı_tipi_9.render(f"Round {i}",True,(0,0,0))
            yazı_12=yazı_tipi_12.render(f"{cops_win}",True,(0,0,0))
            yazı_13=yazı_tipi_13.render(f"{dağcı_win}",True,(0,0,0))
            yazı_10=yazı_tipi_10.render(f"{cops_kalan_mermi}/{cops_desert_eagle_mermi_toplam}",True,(0,0,0))
            yazı_11=yazı_tipi_11.render(f"{dağcı_kalan_mermi}/{dağcı_desert_eagle_mermi_toplam}",True,(0,0,0))
            special_forces_rect=pygame.Rect(special_forces_move.cops_x,special_forces_move.cops_y,special_corps_size_x,special_corps_size_y)
            dağcı_rect=pygame.Rect(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y,dağcılar_size_x,dağcılar_size_y)
            keys=pygame.key.get_pressed()
            if keys[pygame.K_w] and special_forces_move.cops_y>=0 :
                special_forces_move.w()
            if keys[pygame.K_s] and special_forces_move.cops_y<=window_y-special_corps.get_size()[1]:
                special_forces_move.s()
            if keys[pygame.K_a] and special_forces_move.cops_x>=0:
                special_forces_move.a()
            if keys[pygame.K_d] and special_forces_move.cops_x<=window_x-special_corps.get_size()[0]:
                special_forces_move.d()
            if keys[pygame.K_UP] and dağcılar_move.dağcı_y>=0:
                dağcılar_move.up()
            if keys[pygame.K_DOWN] and dağcılar_move.dağcı_y<=window_y-dağcılar_size_y:
                dağcılar_move.down()
            if keys[pygame.K_LEFT] and dağcılar_move.dağcı_x>=0:
                dağcılar_move.left()
            if keys[pygame.K_RIGHT] and dağcılar_move.dağcı_x<=window_x-dağcılar_size_x:
                dağcılar_move.right()
            if cops_atılan_mermi<desert_eagle_mermi:
                if keys[pygame.K_j]:
                    cops_mermi_yön.add(1)
                    cops_mermi.desert_eagle_shoot1()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_u]:
                    cops_mermi_yön.add(2)
                    cops_mermi.desert_eagle_shoot2()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_m]:
                    cops_mermi_yön.add(3)
                    cops_mermi.desert_eagle_shoot3()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_y]:
                    cops_mermi_yön.add(4)
                    cops_mermi.desert_eagle_shoot4()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_n]:
                    cops_mermi_yön.add(5)
                    cops_mermi.desert_eagle_shoot5()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_b]:
                    cops_mermi_yön.add(6)
                    cops_mermi.desert_eagle_shoot6()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_g]:
                    cops_mermi_yön.add(7)
                    cops_mermi.desert_eagle_shoot7()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_t]:
                    cops_mermi_yön.add(8)
                    cops_mermi.desert_eagle_shoot8()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
            else:
                pass
            if keys[pygame.K_r]:
                if cops_desert_eagle_mermi_toplam-cops_atılan_mermi>=0:
                    cops_desert_eagle_mermi_toplam-=cops_atılan_mermi
                    cops_atılan_mermi=0
                else:
                    if cops_deneme==0:
                        pass
                    else:
                        cops_atılan_mermi=desert_eagle_mermi-cops_desert_eagle_mermi_toplam-cops_kalan_mermi
                        cops_desert_eagle_mermi_toplam-=cops_desert_eagle_mermi_toplam
                        cops_deneme=0         
            if dağcı_atılan_mermi<desert_eagle_mermi:
                if keys[pygame.K_KP_1]:
                    dağcı_mermi_yön.add(1)
                    dağcı_mermi.desert_eagle_shoot1()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_2]:
                    dağcı_mermi_yön.add(2)
                    dağcı_mermi.desert_eagle_shoot2()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_3]:
                    dağcı_mermi_yön.add(3)
                    dağcı_mermi.desert_eagle_shoot3()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_4]:
                    dağcı_mermi_yön.add(4)
                    dağcı_mermi.desert_eagle_shoot4()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_6]:
                    dağcı_mermi_yön.add(6)
                    dağcı_mermi.desert_eagle_shoot6()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_7]:
                    dağcı_mermi_yön.add(7)
                    dağcı_mermi.desert_eagle_shoot7()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_8]:
                    dağcı_mermi_yön.add(8)
                    dağcı_mermi.desert_eagle_shoot8()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_9]:
                    dağcı_mermi_yön.add(9)  
                    dağcı_mermi.desert_eagle_shoot9()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
            else:
                pass
            if keys[pygame.K_KP_5]:
                if dağcı_desert_eagle_mermi_toplam-dağcı_atılan_mermi>=0:
                    dağcı_desert_eagle_mermi_toplam-=dağcı_atılan_mermi
                    dağcı_atılan_mermi=0
                else:
                    if dağcı_deneme==0:
                        pass
                    else:
                        dağcı_atılan_mermi=desert_eagle_mermi-dağcı_desert_eagle_mermi_toplam-dağcı_kalan_mermi
                        dağcı_desert_eagle_mermi_toplam-=dağcı_desert_eagle_mermi_toplam
                        dağcı_deneme=0
            if 1 in dağcı_mermi_yön:
                    for index in range(0,len(dağcı_mermi.d_shoot1),2):
                        if dağcı_atılan_mermi<=desert_eagle_mermi:
                            if 0<=dağcı_mermi.d_shoot1[index]<=window_x:
                                if dağcı_mermi.shoot1_collide(index)==1:
                                    pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot1[index],dağcı_mermi.d_shoot1[index+1],10,5))
                                    dağcı_mermi.d_shoot1[index]-=mermi_hız
                                    dağcı_mermi.d_shoot1[index+1]+=mermi_hız
                                elif dağcı_mermi.shoot1_collide(index)==2:
                                    if dağcı_mermi.desert_eagle_shoot1_isabet(i)==1:
                                        i+=1
                                        dağcı_win+=1
                                        dağcı_atılan_mermi=0
                                        cops_atılan_mermi=0
                                        cops_deneme=1
                                        dağcı_deneme=1
                                        cops_desert_eagle_mermi_toplam=60
                                        dağcı_desert_eagle_mermi_toplam=60
                                        choose1,choose2=True,False
                                    break
                                else:
                                    d_shoot1.pop(index+1)
                                    d_shoot1.pop(index)
                                    break
                            else:
                                d_shoot1.pop(index+1)
                                d_shoot1.pop(index)
                                break
                        else:
                            pass
            if 2 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot2),2):
                        if 0<=dağcı_mermi.d_shoot2[index]<=window_x:
                            if dağcı_mermi.shoot2_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot2[index],dağcı_mermi.d_shoot2[index+1],5,10))
                                dağcı_mermi.d_shoot2[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot2_collide(index)==2:
                                if dağcı_mermi.desert_eagle_shoot2_isabet(i)==1:
                                    i+=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_desert_eagle_mermi_toplam=60
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot2.pop(index+1)
                                d_shoot2.pop(index)
                                break
                        else:
                            d_shoot2.pop(index+1)
                            d_shoot2.pop(index)
                            break
                else:
                    pass
            if 3 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot3),2):
                        if 0<=dağcı_mermi.d_shoot3[index]<=window_x:
                            if dağcı_mermi.shoot3_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot3[index],dağcı_mermi.d_shoot3[index+1],10,5))
                                dağcı_mermi.d_shoot3[index]+=mermi_hız
                                dağcı_mermi.d_shoot3[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot3_collide(index)==2:
                                if dağcı_mermi.desert_eagle_shoot3_isabet(i)==1:
                                    i+=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_desert_eagle_mermi_toplam=60
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot3.pop(index+1)
                                d_shoot3.pop(index)
                                break
                        else:
                            d_shoot3.pop(index+1)
                            d_shoot3.pop(index)
                            break
                else:
                    pass

            if 4 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot4),2):
                        if 0<=dağcı_mermi.d_shoot4[index]<=window_x:
                            if dağcı_mermi.shoot4_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot4[index],dağcı_mermi.d_shoot4[index+1],10,5))
                                dağcı_mermi.d_shoot4[index]-=mermi_hız
                            elif dağcı_mermi.shoot4_collide(index)==2:
                                if dağcı_mermi.desert_eagle_shoot4_isabet(i)==1:
                                    i+=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_desert_eagle_mermi_toplam=60
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot4.pop(index+1)
                                d_shoot4.pop(index)
                                break
                        else:
                            d_shoot4.pop(index+1)
                            d_shoot4.pop(index)
                            break
                else:
                    pass
            if 6 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot6),2):
                        if 0<=dağcı_mermi.d_shoot6[index]<=window_x:
                            if dağcı_mermi.shoot6_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot6[index],dağcı_mermi.d_shoot6[index+1],10,5))
                                dağcı_mermi.d_shoot6[index]+=mermi_hız
                            elif dağcı_mermi.shoot6_collide(index)==2:
                                if dağcı_mermi.desert_eagle_shoot6_isabet(i)==1:
                                    i+=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_desert_eagle_mermi_toplam=60
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot6.pop(index+1)
                                d_shoot6.pop(index)
                                break
                        else:
                            d_shoot6.pop(index+1)
                            d_shoot6.pop(index)
                            break
                else:
                    pass
            if 7 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot7),2):
                        if 0<=dağcı_mermi.d_shoot7[index]<=window_x:
                            if dağcı_mermi.shoot7_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot7[index],dağcı_mermi.d_shoot7[index+1],10,5))
                                dağcı_mermi.d_shoot7[index]-=mermi_hız
                                dağcı_mermi.d_shoot7[index+1]-=mermi_hız
                            elif dağcı_mermi.shoot7_collide(index)==2:
                                if dağcı_mermi.desert_eagle_shoot7_isabet(i)==1:
                                    i+=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_desert_eagle_mermi_toplam=60
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot7.pop(index+1)
                                d_shoot7.pop(index)
                                break
                        else:
                            d_shoot7.pop(index+1)
                            d_shoot7.pop(index)
                            break
                else:
                    pass
            if 8 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot8),2):
                        if 0<=dağcı_mermi.d_shoot8[index]<=window_x:
                            if dağcı_mermi.shoot8_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot8[index],dağcı_mermi.d_shoot8[index+1],5,10))
                                dağcı_mermi.d_shoot8[index+1]-=mermi_hız
                            elif dağcı_mermi.shoot8_collide(index)==2:
                                if dağcı_mermi.desert_eagle_shoot8_isabet(i)==1:
                                    i+=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_desert_eagle_mermi_toplam=60
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot8.pop(index+1)
                                d_shoot8.pop(index)
                                break
                        else:
                            d_shoot8.pop(index+1)
                            d_shoot8.pop(index)
                            break
                else:
                    pass
            if 9 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot9),2):
                        if 0<=dağcı_mermi.d_shoot9[index]<=window_x:
                            if dağcı_mermi.shoot9_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot9[index],dağcı_mermi.d_shoot9[index+1],10,5))
                                dağcı_mermi.d_shoot9[index]+=mermi_hız
                                dağcı_mermi.d_shoot9[index+1]-=mermi_hız
                            elif dağcı_mermi.shoot9_collide(index)==2:
                                if dağcı_mermi.desert_eagle_shoot9_isabet(i)==1:
                                    i+=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_desert_eagle_mermi_toplam=60
                                    choose1,choose2=True,False
                                    break      
                            else:
                                d_shoot9.pop(index+1)
                                d_shoot9.pop(index)
                                break
                        else:
                            d_shoot9.pop(index+1)
                            d_shoot9.pop(index)
                            break
                else:
                    pass
            if 1 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shootj),2):
                        if 0<=cops_mermi.c_shootj[index]<=window_x:
                            if cops_mermi.shoot1_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootj[index],cops_mermi.c_shootj[index+1],10,5))
                                cops_mermi.c_shootj[index]+=mermi_hız
                            elif cops_mermi.shoot1_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot1_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_desert_eagle_mermi_toplam=60
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootj.pop(index+1)
                                c_shootj.pop(index)
                                break
                        else:
                            c_shootj.pop(index+1)
                            c_shootj.pop(index)
                            break
                else:
                    pass
            if 2 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shootu),2):
                        if 0<=cops_mermi.c_shootu[index]<=window_x:
                            if cops_mermi.shoot2_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootu[index],cops_mermi.c_shootu[index+1],10,5))
                                cops_mermi.c_shootu[index]+=mermi_hız
                                cops_mermi.c_shootu[index+1]-=mermi_hız
                            elif cops_mermi.shoot2_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot2_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_desert_eagle_mermi_toplam=60
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootu.pop(index+1)
                                c_shootu.pop(index)
                                break
                        else:
                            c_shootu.pop(index+1)
                            c_shootu.pop(index)
                            break
                else:
                    pass
            if 3 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shootm),2):
                        if 0<=cops_mermi.c_shootm[index]<=window_x:
                            if cops_mermi.shoot3_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootm[index],cops_mermi.c_shootm[index+1],10,5))
                                cops_mermi.c_shootm[index]+=mermi_hız
                                cops_mermi.c_shootm[index+1]+=mermi_hız
                            elif cops_mermi.shoot3_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot3_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_desert_eagle_mermi_toplam=60
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootm.pop(index+1)
                                c_shootm.pop(index)
                                break
                        else:
                            c_shootm.pop(index+1)
                            c_shootm.pop(index)
                            break
                else:
                    pass
            if 4 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shootn),2):
                        if 0<=cops_mermi.c_shootn[index]<=window_x:
                            if cops_mermi.shoot4_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootn[index],cops_mermi.c_shootn[index+1],5,10))
                                cops_mermi.c_shootn[index+1]-=mermi_hız
                            elif cops_mermi.shoot4_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot4_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_desert_eagle_mermi_toplam=60
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootn.pop(index+1)
                                c_shootn.pop(index)
                                break
                        else:
                            c_shootn.pop(index+1)
                            c_shootn.pop(index)
                            break
                else:
                    pass
            if 5 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shooty),2):
                        if 0<=cops_mermi.c_shooty[index]<=window_x:
                            if cops_mermi.shoot5_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shooty[index],cops_mermi.c_shooty[index+1],5,10))  
                                cops_mermi.c_shooty[index+1]+=mermi_hız
                            elif cops_mermi.shoot5_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot5_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_desert_eagle_mermi_toplam=60
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shooty.pop(index+1)
                                c_shooty.pop(index)
                                break
                        else:
                            c_shooty.pop(index+1)
                            c_shooty.pop(index)
                            break
                else:
                    pass
            if 6 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shootb),2):
                        if 0<=cops_mermi.c_shootb[index]<=window_x:
                            if cops_mermi.shoot6_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootb[index],cops_mermi.c_shootb[index+1],10,5))
                                cops_mermi.c_shootb[index]-=mermi_hız
                                cops_mermi.c_shootb[index+1]+=mermi_hız
                            elif cops_mermi.shoot6_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot6_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_desert_eagle_mermi_toplam=60
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootb.pop(index+1)
                                c_shootb.pop(index)
                                break
                        else:
                            c_shootb.pop(index+1)
                            c_shootb.pop(index)
                            break
                else:
                    pass
            if 7 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shootg),2):
                        if 0<=cops_mermi.c_shootg[index]<=window_x:
                            if cops_mermi.shoot7_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootg[index],cops_mermi.c_shootg[index+1],10,5))
                                cops_mermi.c_shootg[index]-=mermi_hız
                                
                            elif cops_mermi.shoot7_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot7_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_desert_eagle_mermi_toplam=60
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootg.pop(index+1)
                                c_shootg.pop(index)
                                break
                        else:
                            c_shootg.pop(index+1)
                            c_shootg.pop(index)
                            break
                else:
                    pass
            if 8 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shoott),2):
                        if 0<=cops_mermi.c_shoott[index]<=window_x:
                            if cops_mermi.shoot8_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shoott[index],cops_mermi.c_shoott[index+1],10,5))
                                cops_mermi.c_shoott[index]-=mermi_hız
                                cops_mermi.c_shoott[index+1]-=mermi_hız
                            elif cops_mermi.shoot8_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot8_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_desert_eagle_mermi_toplam=60
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shoott.pop(index+1)
                                c_shoott.pop(index)
                                break
                        else:
                            c_shoott.pop(index+1)
                            c_shoott.pop(index)
                            break
                else:
                    pass
            if dağcılar_move.dağcı_x<=0 and dağcılar_move.dağcı_y<=0:
                dağcı_mermi_yön.clear()
                i+=1
                dağcı_win+=1
                dağcı_atılan_mermi=0
                cops_atılan_mermi=0
                cops_deneme=1
                dağcı_deneme=1
                cops_desert_eagle_mermi_toplam=60
                dağcı_desert_eagle_mermi_toplam=60
                special_forces.para+=0
                dağcılar.para+=1500
                dağcılar_move.dağcı_x=dağcı_x
                dağcılar_move.dağcı_y=dağcı_y
                special_forces_move.cops_x=cops_x
                special_forces_move.cops_y=cops_y
                special_forces.can=100
                dağcılar.can=100
                choose1,choose2=True,False
            pygame.draw.rect(window,(rgb.kum),special_forces_rect)
            pygame.draw.rect(window,(rgb.kum),dağcı_rect)
            window.blit(special_corps_copy,(special_forces_move.cops_x,special_forces_move.cops_y))
            window.blit(dağcı_copy,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y))
            window.blit(yazı_7,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y+2))
            window.blit(yazı_8,(special_forces_move.cops_x+45,special_forces_move.cops_y-5))
            window.blit(yazı_9,(window_x//2+15,20))
            window.blit(yazı_10,(special_forces_move.cops_x+45,special_forces_move.cops_y+4))
            window.blit(yazı_11,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y+12))
            window.blit(special_corps_logo,(1470,0))
            window.blit(dağcı_logo,(1470,35))
            window.blit(yazı_12,(1510,-5))
            window.blit(yazı_13,(1510,32))
            pygame.display.update()
        if special_forces.silah=="desert_eagle" and dağcılar.silah=="ak_47":
            cops_kalan_mermi=desert_eagle_mermi-cops_atılan_mermi 
            dağcı_kalan_mermi=ak_47_mermi-dağcı_atılan_mermi         
            window.fill((rgb.kum))
            pygame.draw.rect(window,(0,0,0),engel_1)
            pygame.draw.rect(window,(0,0,0),engel_2)
            pygame.draw.rect(window,(0,0,0),engel_3)
            pygame.draw.rect(window,(0,0,0),engel_4)
            pygame.draw.rect(window,(0,0,0),engel_5)
            pygame.draw.rect(window,(0,0,0),engel_6)
            yazı_7=yazı_tipi_7.render(f"{dağcılar.can}/100",True,(0,0,0))
            yazı_8=yazı_tipi_8.render(f"{special_forces.can}/100",True,(0,0,0))
            yazı_9=yazı_tipi_9.render(f"Round {i}",True,(0,0,0))
            yazı_12=yazı_tipi_12.render(f"{cops_win}",True,(0,0,0))
            yazı_13=yazı_tipi_13.render(f"{dağcı_win}",True,(0,0,0))
            yazı_10=yazı_tipi_10.render(f"{cops_kalan_mermi}/{cops_desert_eagle_mermi_toplam}",True,(0,0,0))
            yazı_11=yazı_tipi_11.render(f"{dağcı_kalan_mermi}/{dağcı_ak_47_mermi_toplam}",True,(0,0,0))
            special_forces_rect=pygame.Rect(special_forces_move.cops_x,special_forces_move.cops_y,special_corps_size_x,special_corps_size_y)
            dağcı_rect=pygame.Rect(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y,dağcılar_size_x,dağcılar_size_y)
            keys=pygame.key.get_pressed()
            if keys[pygame.K_w] and special_forces_move.cops_y>=0 :
                special_forces_move.w()
            if keys[pygame.K_s] and special_forces_move.cops_y<=window_y-special_corps.get_size()[1]:
                special_forces_move.s()
            if keys[pygame.K_a] and special_forces_move.cops_x>=0:
                special_forces_move.a()
            if keys[pygame.K_d] and special_forces_move.cops_x<=window_x-special_corps.get_size()[0]:
                special_forces_move.d()
            if keys[pygame.K_UP] and dağcılar_move.dağcı_y>=0:
                dağcılar_move.up()
            if keys[pygame.K_DOWN] and dağcılar_move.dağcı_y<=window_y-dağcılar_size_y:
                dağcılar_move.down()
            if keys[pygame.K_LEFT] and dağcılar_move.dağcı_x>=0:
                dağcılar_move.left()
            if keys[pygame.K_RIGHT] and dağcılar_move.dağcı_x<=window_x-dağcılar_size_x:
                dağcılar_move.right()
            if cops_atılan_mermi<desert_eagle_mermi:
                if keys[pygame.K_j]:
                    cops_mermi_yön.add(1)
                    cops_mermi.desert_eagle_shoot1()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_u]:
                    cops_mermi_yön.add(2)
                    cops_mermi.desert_eagle_shoot2()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_m]:
                    cops_mermi_yön.add(3)
                    cops_atılan_mermi+=1
                    cops_mermi.desert_eagle_shoot3()
                    time.sleep(0.1)
                if keys[pygame.K_y]:
                    cops_mermi_yön.add(4)
                    cops_atılan_mermi+=1
                    cops_mermi.desert_eagle_shoot4()
                    time.sleep(0.1)
                if keys[pygame.K_n]:
                    cops_mermi_yön.add(5)
                    cops_atılan_mermi+=1
                    cops_mermi.desert_eagle_shoot5()
                    time.sleep(0.1)
                if keys[pygame.K_b]:
                    cops_mermi_yön.add(6)
                    cops_atılan_mermi+=1
                    cops_mermi.desert_eagle_shoot6()
                    time.sleep(0.1)
                if keys[pygame.K_g]:
                    cops_mermi_yön.add(7)
                    cops_atılan_mermi+=1
                    cops_mermi.desert_eagle_shoot7()
                    time.sleep(0.1)
                if keys[pygame.K_t]:
                    cops_mermi_yön.add(8)
                    cops_atılan_mermi+=1
                    cops_mermi.desert_eagle_shoot8()
                    time.sleep(0.1)
            else:
                pass
            if keys[pygame.K_r]:
                if cops_desert_eagle_mermi_toplam-cops_atılan_mermi>=0:
                    cops_desert_eagle_mermi_toplam-=cops_atılan_mermi
                    cops_atılan_mermi=0
                else:
                    if cops_deneme==0:
                        pass
                    else:
                        cops_atılan_mermi=desert_eagle_mermi-cops_desert_eagle_mermi_toplam-cops_kalan_mermi
                        cops_desert_eagle_mermi_toplam-=cops_desert_eagle_mermi_toplam
                        cops_deneme=0         
            if dağcı_atılan_mermi<ak_47_mermi:
                if keys[pygame.K_KP_1]:
                    dağcı_mermi_yön.add(1)
                    dağcı_atılan_mermi+=1
                    dağcı_mermi.ak_47_shoot1()
                    time.sleep(0.1)
                if keys[pygame.K_KP_2]:
                    dağcı_mermi_yön.add(2)
                    dağcı_atılan_mermi+=1
                    dağcı_mermi.ak_47_shoot2()
                    time.sleep(0.1)
                if keys[pygame.K_KP_3]:
                    dağcı_mermi_yön.add(3)
                    dağcı_atılan_mermi+=1
                    dağcı_mermi.ak_47_shoot3()
                    time.sleep(0.1)
                if keys[pygame.K_KP_4]:
                    dağcı_mermi_yön.add(4)
                    dağcı_atılan_mermi+=1
                    dağcı_mermi.ak_47_shoot4()
                    time.sleep(0.1)
                if keys[pygame.K_KP_6]:
                    dağcı_mermi_yön.add(6)
                    dağcı_atılan_mermi+=1
                    dağcı_mermi.ak_47_shoot6()
                    time.sleep(0.1)
                if keys[pygame.K_KP_7]:
                    dağcı_mermi_yön.add(7)
                    dağcı_atılan_mermi+=1
                    dağcı_mermi.ak_47_shoot7()
                    time.sleep(0.1)
                if keys[pygame.K_KP_8]:
                    dağcı_mermi_yön.add(8)
                    dağcı_atılan_mermi+=1
                    dağcı_mermi.ak_47_shoot8()
                    time.sleep(0.1)
                if keys[pygame.K_KP_9]:
                    dağcı_mermi_yön.add(9)
                    dağcı_atılan_mermi+=1 
                    dağcı_mermi.ak_47_shoot9()
                    time.sleep(0.1)
            else:
                pass
            if keys[pygame.K_KP_5]:
                if dağcı_ak_47_mermi_toplam-dağcı_atılan_mermi>=0:
                    dağcı_ak_47_mermi_toplam-=dağcı_atılan_mermi
                    dağcı_atılan_mermi=0
                else:
                    if dağcı_deneme==0:
                        pass
                    else:
                        dağcı_atılan_mermi=ak_47_mermi-dağcı_ak_47_mermi_toplam-dağcı_kalan_mermi
                        dağcı_ak_47_mermi_toplam-=dağcı_ak_47_mermi_toplam
                        dağcı_deneme=0     
            if 1 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=ak_47_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot1),2):
                        if 0<=dağcı_mermi.d_shoot1[index]<=window_x:
                            if dağcı_mermi.shoot1_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot1[index],dağcı_mermi.d_shoot1[index+1],10,5))
                                dağcı_mermi.d_shoot1[index]-=mermi_hız
                                dağcı_mermi.d_shoot1[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot1_collide(index)==2:
                                if dağcı_mermi.ak_47_shoot1_isabet(i)==1:
                                    i+=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                break
                            else:
                                d_shoot1.pop(index+1)
                                d_shoot1.pop(index)
                                break
                        else:
                            d_shoot1.pop(index+1)
                            d_shoot1.pop(index)
                            break
                else:
                    pass
            if 2 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=ak_47_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot2),2):
                        if 0<=dağcı_mermi.d_shoot2[index]<=window_x:
                            if dağcı_mermi.shoot2_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot2[index],dağcı_mermi.d_shoot2[index+1],5,10))
                                dağcı_mermi.d_shoot2[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot2_collide(index)==2:
                                if dağcı_mermi.ak_47_shoot2_isabet(i)==1:
                                    i+=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot2.pop(index+1)
                                d_shoot2.pop(index)
                                break
                        else:
                            d_shoot2.pop(index+1)
                            d_shoot2.pop(index)
                            break
                else:
                    pass
            if 3 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=ak_47_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot3),2):
                        if 0<=dağcı_mermi.d_shoot3[index]<=window_x:
                            if dağcı_mermi.shoot3_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot3[index],dağcı_mermi.d_shoot3[index+1],10,5))
                                dağcı_mermi.d_shoot3[index]+=mermi_hız
                                dağcı_mermi.d_shoot3[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot3_collide(index)==2:
                                if dağcı_mermi.ak_47_shoot3_isabet(i)==1:
                                    i+=1
                                    cops_desert_eagle_mermi_toplam=60
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot3.pop(index+1)
                                d_shoot3.pop(index)
                                break
                        else:
                            d_shoot3.pop(index+1)
                            d_shoot3.pop(index)
                            break
                else:
                    pass
            if 4 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=ak_47_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot4),2):
                        if 0<=dağcı_mermi.d_shoot4[index]<=window_x:
                            if dağcı_mermi.shoot4_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot4[index],dağcı_mermi.d_shoot4[index+1],10,5))
                                dağcı_mermi.d_shoot4[index]-=mermi_hız
                
                            elif dağcı_mermi.shoot4_collide(index)==2:
                                if dağcı_mermi.ak_47_shoot4_isabet(i)==1:
                                    i+=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot4.pop(index+1)
                                d_shoot4.pop(index)
                                break
                        else:
                            d_shoot4.pop(index+1)
                            d_shoot4.pop(index)
                            break
                else:
                    pass
            if 6 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=ak_47_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot6),2):
                        if 0<=dağcı_mermi.d_shoot6[index]<=window_x:
                            if dağcı_mermi.shoot6_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot6[index],dağcı_mermi.d_shoot6[index+1],10,5))
                                dağcı_mermi.d_shoot6[index]+=mermi_hız
                            elif dağcı_mermi.shoot6_collide(index)==2:
                                if dağcı_mermi.ak_47_shoot6_isabet(i)==1:
                                    i+=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot6.pop(index+1)
                                d_shoot6.pop(index)
                                break
                        else:
                            d_shoot6.pop(index+1)
                            d_shoot6.pop(index)
                            break
                else:
                    pass               
            if 7 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=ak_47_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot7),2):
                        if 0<=dağcı_mermi.d_shoot7[index]<=window_x:
                            if dağcı_mermi.shoot7_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot7[index],dağcı_mermi.d_shoot7[index+1],10,5))
                                dağcı_mermi.d_shoot7[index]-=mermi_hız
                                dağcı_mermi.d_shoot7[index+1]-=mermi_hız
                
                            elif dağcı_mermi.shoot7_collide(index)==2:
                                if dağcı_mermi.ak_47_shoot7_isabet(i)==1:
                                    i+=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot7.pop(index+1)
                                d_shoot7.pop(index)
                                break
                        else:
                            d_shoot7.pop(index+1)
                            d_shoot7.pop(index)
                            break
                else:
                    pass
            if 8 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=ak_47_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot8),2):
                        if 0<=dağcı_mermi.d_shoot8[index]<=window_x:
                            if dağcı_mermi.shoot8_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot8[index],dağcı_mermi.d_shoot8[index+1],5,10))
                                dağcı_mermi.d_shoot8[index+1]-=mermi_hız
                
                            elif dağcı_mermi.shoot8_collide(index)==2:
                                if dağcı_mermi.ak_47_shoot8_isabet(i)==1:
                                    i+=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot8.pop(index+1)
                                d_shoot8.pop(index)
                                break
                        else:
                            d_shoot8.pop(index+1)
                            d_shoot8.pop(index)
                            break
                else:
                    pass
            if 9 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=ak_47_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot9),2):
                        if 0<=dağcı_mermi.d_shoot9[index]<=window_x:
                            if dağcı_mermi.shoot9_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot9[index],dağcı_mermi.d_shoot9[index+1],10,5))
                                dağcı_mermi.d_shoot9[index]+=mermi_hız
                                dağcı_mermi.d_shoot9[index+1]-=mermi_hız
                            elif dağcı_mermi.shoot9_collide(index)==2:
                                if dağcı_mermi.ak_47_shoot9_isabet(i)==1:
                                    i+=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break      
                            else:
                                d_shoot9.pop(index+1)
                                d_shoot9.pop(index)
                                break
                        else:
                            d_shoot9.pop(index+1)
                            d_shoot9.pop(index)
                            break
                else:
                    pass
            if 1 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shootj),2):
                        if 0<=cops_mermi.c_shootj[index]<=window_x:
                            if cops_mermi.shoot1_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootj[index],cops_mermi.c_shootj[index+1],10,5))
                                cops_mermi.c_shootj[index]+=mermi_hız
                            elif cops_mermi.shoot1_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot1_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootj.pop(index+1)
                                c_shootj.pop(index)
                                break
                        else:
                            c_shootj.pop(index+1)
                            c_shootj.pop(index)
                            break
                else:
                    pass
            if 2 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shootu),2):
                        if 0<=cops_mermi.c_shootu[index]<=window_x:
                            if cops_mermi.shoot2_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootu[index],cops_mermi.c_shootu[index+1],10,5))
                                cops_mermi.c_shootu[index]+=mermi_hız
                                cops_mermi.c_shootu[index+1]-=mermi_hız
                            elif cops_mermi.shoot2_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot2_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootu.pop(index+1)
                                c_shootu.pop(index)
                                break
                        else:
                            c_shootu.pop(index+1)
                            c_shootu.pop(index)
                            break
                else:
                    pass
            if 3 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shootm),2):
                        if 0<=cops_mermi.c_shootm[index]<=window_x:
                            if cops_mermi.shoot3_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootm[index],cops_mermi.c_shootm[index+1],10,5))
                                cops_mermi.c_shootm[index]+=mermi_hız
                                cops_mermi.c_shootm[index+1]+=mermi_hız
                            elif cops_mermi.shoot3_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot3_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootm.pop(index+1)
                                c_shootm.pop(index)
                                break
                        else:
                            c_shootm.pop(index+1)
                            c_shootm.pop(index)
                            break
                else:
                    pass
            if 4 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shootn),2):
                        if 0<=cops_mermi.c_shootn[index]<=window_x:
                            if cops_mermi.shoot4_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootn[index],cops_mermi.c_shootn[index+1],5,10))
                                cops_mermi.c_shootn[index+1]-=mermi_hız
                            elif cops_mermi.shoot4_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot4_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootn.pop(index+1)
                                c_shootn.pop(index)
                                break
                        else:
                            c_shootn.pop(index+1)
                            c_shootn.pop(index)
                            break
                else:
                    pass
            if 5 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shooty),2):
                        if 0<=cops_mermi.c_shooty[index]<=window_x:
                            if cops_mermi.shoot5_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shooty[index],cops_mermi.c_shooty[index+1],5,10))
                                
                                cops_mermi.c_shooty[index+1]+=mermi_hız
                            elif cops_mermi.shoot5_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot5_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shooty.pop(index+1)
                                c_shooty.pop(index)
                                break
                        else:
                            c_shooty.pop(index+1)
                            c_shooty.pop(index)
                            break
                else:
                    pass
            if 6 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shootb),2):
                        if 0<=cops_mermi.c_shootb[index]<=window_x:
                            if cops_mermi.shoot6_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootb[index],cops_mermi.c_shootb[index+1],10,5))
                                cops_mermi.c_shootb[index]-=mermi_hız
                                cops_mermi.c_shootb[index+1]+=mermi_hız
                            elif cops_mermi.shoot6_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot6_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootb.pop(index+1)
                                c_shootb.pop(index)
                                break
                        else:
                            c_shootb.pop(index+1)
                            c_shootb.pop(index)
                            break
                else:
                    pass
            if 7 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shootg),2):
                        if 0<=cops_mermi.c_shootg[index]<=window_x:
                            if cops_mermi.shoot7_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootg[index],cops_mermi.c_shootg[index+1],10,5))
                                cops_mermi.c_shootg[index]-=mermi_hız
                                
                            elif cops_mermi.shoot7_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot7_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootg.pop(index+1)
                                c_shootg.pop(index)
                                break
                        else:
                            c_shootg.pop(index+1)
                            c_shootg.pop(index)
                            break
                else:
                    pass
            if 8 in cops_mermi_yön:
                if cops_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(cops_mermi.c_shoott),2):
                        if 0<=cops_mermi.c_shoott[index]<=window_x:
                            if cops_mermi.shoot8_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shoott[index],cops_mermi.c_shoott[index+1],10,5))
                                cops_mermi.c_shoott[index]-=mermi_hız
                                cops_mermi.c_shoott[index+1]-=mermi_hız
                            elif cops_mermi.shoot8_collide(index)==2:
                                if cops_mermi.desert_eagle_shoot8_isabet(i)==1:
                                    i+=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shoott.pop(index+1)
                                c_shoott.pop(index)
                                break
                        else:
                            c_shoott.pop(index+1)
                            c_shoott.pop(index)
                            break
                else:
                    pass
            if dağcılar_move.dağcı_x<=0 and dağcılar_move.dağcı_y<=0:
                dağcı_mermi_yön.clear()
                i+=1
                dağcı_win+=1
                special_forces.para+=0
                dağcılar.para+=1500
                dağcı_atılan_mermi=0
                cops_atılan_mermi=0
                dağcılar_move.dağcı_x=dağcı_x
                dağcılar_move.dağcı_y=dağcı_y
                special_forces_move.cops_x=cops_x
                special_forces_move.cops_y=cops_y
                special_forces.can=100
                dağcılar.can=100
                choose1,choose2=True,False
            pygame.draw.rect(window,(rgb.kum),special_forces_rect)
            pygame.draw.rect(window,(rgb.kum),dağcı_rect)
            window.blit(special_corps_copy,(special_forces_move.cops_x,special_forces_move.cops_y))
            window.blit(dağcı_copy,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y))
            window.blit(yazı_7,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y+2))
            window.blit(yazı_8,(special_forces_move.cops_x+45,special_forces_move.cops_y-5))
            window.blit(yazı_9,(window_x//2+15,20))
            window.blit(yazı_10,(special_forces_move.cops_x+45,special_forces_move.cops_y+4))
            window.blit(yazı_11,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y+12))
            window.blit(special_corps_logo,(1470,0))
            window.blit(dağcı_logo,(1470,35))
            window.blit(yazı_12,(1510,-5))
            window.blit(yazı_13,(1510,32))
            pygame.display.update()
        if special_forces.silah=="m_16" and dağcılar.silah=="awp":     
            cops_kalan_mermi=m_16_mermi-cops_atılan_mermi 
            dağcı_kalan_mermi=awp_mermi-dağcı_atılan_mermi    
            window.fill((rgb.kum))
            pygame.draw.rect(window,(0,0,0),engel_1)
            pygame.draw.rect(window,(0,0,0),engel_2)
            pygame.draw.rect(window,(0,0,0),engel_3)
            pygame.draw.rect(window,(0,0,0),engel_4)
            pygame.draw.rect(window,(0,0,0),engel_5)
            pygame.draw.rect(window,(0,0,0),engel_6)
            yazı_7=yazı_tipi_7.render(f"{dağcılar.can}/100",True,(0,0,0))
            yazı_8=yazı_tipi_8.render(f"{special_forces.can}/100",True,(0,0,0))
            yazı_9=yazı_tipi_9.render(f"Round {i}",True,(0,0,0))
            yazı_12=yazı_tipi_12.render(f"{cops_win}",True,(0,0,0))
            yazı_13=yazı_tipi_13.render(f"{dağcı_win}",True,(0,0,0))
            yazı_10=yazı_tipi_10.render(f"{cops_kalan_mermi}/{cops_m_16_mermi_toplam}",True,(0,0,0))
            yazı_11=yazı_tipi_11.render(f"{dağcı_kalan_mermi}/{dağcı_awp_mermi_toplam}",True,(0,0,0))
            special_forces_rect=pygame.Rect(special_forces_move.cops_x,special_forces_move.cops_y,special_corps_size_x,special_corps_size_y)
            dağcı_rect=pygame.Rect(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y,dağcılar_size_x,dağcılar_size_y)
            keys=pygame.key.get_pressed()
            if keys[pygame.K_w] and special_forces_move.cops_y>=0 :
                special_forces_move.w()
            if keys[pygame.K_s] and special_forces_move.cops_y<=window_y-special_corps.get_size()[1]:
                special_forces_move.s()
            if keys[pygame.K_a] and special_forces_move.cops_x>=0:
                special_forces_move.a()
            if keys[pygame.K_d] and special_forces_move.cops_x<=window_x-special_corps.get_size()[0]:
                special_forces_move.d()
            if keys[pygame.K_UP] and dağcılar_move.dağcı_y>=0:
                dağcılar_move.up()
            if keys[pygame.K_DOWN] and dağcılar_move.dağcı_y<=window_y-dağcılar_size_y:
                dağcılar_move.down()
            if keys[pygame.K_LEFT] and dağcılar_move.dağcı_x>=0:
                dağcılar_move.left()
            if keys[pygame.K_RIGHT] and dağcılar_move.dağcı_x<=window_x-dağcılar_size_x:
                dağcılar_move.right()
            if cops_atılan_mermi<m_16_mermi:
                if keys[pygame.K_j]:
                    cops_mermi_yön.add(1)
                    cops_mermi.m_16_shoot1()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_u]:
                    cops_mermi_yön.add(2)
                    cops_mermi.m_16_shoot2()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_m]:
                    cops_mermi_yön.add(3)
                    cops_mermi.m_16_shoot3()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_y]:
                    cops_mermi_yön.add(4)
                    cops_mermi.m_16_shoot4()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_n]:
                    cops_mermi_yön.add(5)
                    cops_mermi.m_16_shoot5()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_b]:
                    cops_mermi_yön.add(6)
                    cops_mermi.m_16_shoot6()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_g]:
                    cops_mermi_yön.add(7)
                    cops_mermi.m_16_shoot7()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_t]:
                    cops_mermi_yön.add(8)
                    cops_mermi.m_16_shoot8()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
            else:
                pass
            if keys[pygame.K_r]:
                if cops_m_16_mermi_toplam-cops_atılan_mermi>=0:
                    cops_m_16_mermi_toplam-=cops_atılan_mermi
                    cops_atılan_mermi=0
                else:
                    if cops_deneme==0:
                        pass
                    else:
                        cops_atılan_mermi=m_16_mermi-cops_m_16_mermi_toplam
                        cops_m_16_mermi_toplam-=cops_m_16_mermi_toplam
                        cops_deneme=0         
            if dağcı_atılan_mermi<awp_mermi:
                if keys[pygame.K_KP_1]:
                    dağcı_mermi_yön.add(1)
                    dağcı_mermi.awp_shoot1()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_2]:
                    dağcı_mermi_yön.add(2)
                    dağcı_mermi.awp_shoot2()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_3]:
                    dağcı_mermi_yön.add(3)
                    dağcı_mermi.awp_shoot3()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_4]:
                    dağcı_mermi_yön.add(4)
                    dağcı_mermi.awp_shoot4()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_6]:
                    dağcı_mermi_yön.add(6)
                    dağcı_mermi.awp_shoot6()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_7]:
                    dağcı_mermi_yön.add(7)
                    dağcı_mermi.awp_shoot7()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_8]:
                    dağcı_mermi_yön.add(8)
                    dağcı_mermi.awp_shoot8()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_9]:
                    dağcı_mermi_yön.add(9)  
                    dağcı_mermi.awp_shoot9()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
            else:
                pass
            if keys[pygame.K_KP_5]:
                if dağcı_awp_mermi_toplam-dağcı_atılan_mermi>=0:
                    dağcı_awp_mermi_toplam-=dağcı_atılan_mermi
                    dağcı_atılan_mermi=0
                else:
                    if dağcı_deneme==0:
                        pass
                    else:
                        dağcı_atılan_mermi=awp_mermi-dağcı_awp_mermi_toplam
                        dağcı_awp_mermi_toplam-=dağcı_awp_mermi_toplam
                        dağcı_deneme=0    
            if 1 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot1),2):
                        if 0<=dağcı_mermi.d_shoot1[index]<=window_x:
                            if dağcı_mermi.shoot1_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot1[index],dağcı_mermi.d_shoot1[index+1],10,5))
                                dağcı_mermi.d_shoot1[index]-=mermi_hız
                                dağcı_mermi.d_shoot1[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot1_collide(index)==2:
                                if dağcı_mermi.awp_shoot1_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                break
                            else:
                                d_shoot1.pop(index+1)
                                d_shoot1.pop(index)
                                break
                        else:
                            d_shoot1.pop(index+1)
                            d_shoot1.pop(index)
                            break
                else:
                    pass
            if 2 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot2),2):
                        if 0<=dağcı_mermi.d_shoot2[index]<=window_x:
                            if dağcı_mermi.shoot2_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot2[index],dağcı_mermi.d_shoot2[index+1],5,10))
                                dağcı_mermi.d_shoot2[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot2_collide(index)==2:
                                if dağcı_mermi.awp_shoot2_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot2.pop(index+1)
                                d_shoot2.pop(index)
                                break
                        else:
                            d_shoot2.pop(index+1)
                            d_shoot2.pop(index)
                            break
                else:
                    pass
            if 3 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot3),2):
                        if 0<=dağcı_mermi.d_shoot3[index]<=window_x:
                            if dağcı_mermi.shoot3_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot3[index],dağcı_mermi.d_shoot3[index+1],10,5))
                                dağcı_mermi.d_shoot3[index]+=mermi_hız
                                dağcı_mermi.d_shoot3[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot3_collide(index)==2:
                                if dağcı_mermi.awp_shoot3_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot3.pop(index+1)
                                d_shoot3.pop(index)
                                break
                        else:
                            d_shoot3.pop(index+1)
                            d_shoot3.pop(index)
                            break
                else:
                    pass
            if 4 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot4),2):
                        if 0<=dağcı_mermi.d_shoot4[index]<=window_x:
                            if dağcı_mermi.shoot4_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot4[index],dağcı_mermi.d_shoot4[index+1],10,5))
                                dağcı_mermi.d_shoot4[index]-=mermi_hız
                
                            elif dağcı_mermi.shoot4_collide(index)==2:
                                if dağcı_mermi.awp_shoot4_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot4.pop(index+1)
                                d_shoot4.pop(index)
                                break
                        else:
                            d_shoot4.pop(index+1)
                            d_shoot4.pop(index)
                            break
                else:
                    pass
            if 6 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot6),2):
                        if 0<=dağcı_mermi.d_shoot6[index]<=window_x:
                            if dağcı_mermi.shoot6_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot6[index],dağcı_mermi.d_shoot6[index+1],10,5))
                                dağcı_mermi.d_shoot6[index]+=mermi_hız
                            elif dağcı_mermi.shoot6_collide(index)==2:
                                if dağcı_mermi.awp_shoot6_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot6.pop(index+1)
                                d_shoot6.pop(index)
                                break
                        else:
                            d_shoot6.pop(index+1)
                            d_shoot6.pop(index)
                            break
                else:
                    pass
            if 7 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot7),2):
                        if 0<=dağcı_mermi.d_shoot7[index]<=window_x:
                            if dağcı_mermi.shoot7_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot7[index],dağcı_mermi.d_shoot7[index+1],10,5))
                                dağcı_mermi.d_shoot7[index]-=mermi_hız
                                dağcı_mermi.d_shoot7[index+1]-=mermi_hız
                
                            elif dağcı_mermi.shoot7_collide(index)==2:
                                if dağcı_mermi.awp_shoot7_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot7.pop(index+1)
                                d_shoot7.pop(index)
                                break
                        else:
                            d_shoot7.pop(index+1)
                            d_shoot7.pop(index)
                            break
                else:
                    pass
            if 8 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot8),2):
                        if 0<=dağcı_mermi.d_shoot8[index]<=window_x:
                            if dağcı_mermi.shoot8_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot8[index],dağcı_mermi.d_shoot8[index+1],5,10))
                                dağcı_mermi.d_shoot8[index+1]-=mermi_hız
                
                            elif dağcı_mermi.shoot8_collide(index)==2:
                                if dağcı_mermi.awp_shoot8_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot8.pop(index+1)
                                d_shoot8.pop(index)
                                break
                        else:
                            d_shoot8.pop(index+1)
                            d_shoot8.pop(index)
                            break
                else:
                    pass
            if 9 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=awp_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot9),2):
                        if 0<=dağcı_mermi.d_shoot9[index]<=window_x:
                            if dağcı_mermi.shoot9_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot9[index],dağcı_mermi.d_shoot9[index+1],10,5))
                                dağcı_mermi.d_shoot9[index]+=mermi_hız
                                dağcı_mermi.d_shoot9[index+1]-=mermi_hız
                            elif dağcı_mermi.shoot9_collide(index)==2:
                                if dağcı_mermi.awp_shoot9_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break      
                            else:
                                d_shoot9.pop(index+1)
                                d_shoot9.pop(index)
                                break
                        else:
                            d_shoot9.pop(index+1)
                            d_shoot9.pop(index)
                            break
                else:
                    pass
            if 1 in cops_mermi_yön:
                if dağcı_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shootj),2):
                        if 0<=cops_mermi.c_shootj[index]<=window_x:
                            if cops_mermi.shoot1_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootj[index],cops_mermi.c_shootj[index+1],10,5))
                                cops_mermi.c_shootj[index]+=mermi_hız
                            elif cops_mermi.shoot1_collide(index)==2:
                                if cops_mermi.m_16_shoot1_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootj.pop(index+1)
                                c_shootj.pop(index)
                                break
                        else:
                            c_shootj.pop(index+1)
                            c_shootj.pop(index)
                            break
                else:
                    pass
            if 2 in cops_mermi_yön:
                if dağcı_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shootu),2):
                        if 0<=cops_mermi.c_shootu[index]<=window_x:
                            if cops_mermi.shoot2_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootu[index],cops_mermi.c_shootu[index+1],10,5))
                                cops_mermi.c_shootu[index]+=mermi_hız
                                cops_mermi.c_shootu[index+1]-=mermi_hız
                            elif cops_mermi.shoot2_collide(index)==2:
                                if cops_mermi.m_16_shoot2_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootu.pop(index+1)
                                c_shootu.pop(index)
                                break
                        else:
                            c_shootu.pop(index+1)
                            c_shootu.pop(index)
                            break
                else:
                    pass
            if 3 in cops_mermi_yön:
                if dağcı_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shootm),2):
                        if 0<=cops_mermi.c_shootm[index]<=window_x:
                            if cops_mermi.shoot3_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootm[index],cops_mermi.c_shootm[index+1],10,5))
                                cops_mermi.c_shootm[index]+=mermi_hız
                                cops_mermi.c_shootm[index+1]+=mermi_hız
                            elif cops_mermi.shoot3_collide(index)==2:
                                if cops_mermi.m_16_shoot3_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootm.pop(index+1)
                                c_shootm.pop(index)
                                break
                        else:
                            c_shootm.pop(index+1)
                            c_shootm.pop(index)
                            break
                else:
                    pass
            if 4 in cops_mermi_yön:
                if dağcı_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shootn),2):
                        if 0<=cops_mermi.c_shootn[index]<=window_x:
                            if cops_mermi.shoot4_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootn[index],cops_mermi.c_shootn[index+1],5,10))
                                cops_mermi.c_shootn[index+1]-=mermi_hız
                            elif cops_mermi.shoot4_collide(index)==2:
                                if cops_mermi.m_16_shoot4_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootn.pop(index+1)
                                c_shootn.pop(index)
                                break
                        else:
                            c_shootn.pop(index+1)
                            c_shootn.pop(index)
                            break
                else:
                    pass
            if 5 in cops_mermi_yön:
                if dağcı_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shooty),2):
                        if 0<=cops_mermi.c_shooty[index]<=window_x:
                            if cops_mermi.shoot5_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shooty[index],cops_mermi.c_shooty[index+1],5,10))
                                
                                cops_mermi.c_shooty[index+1]+=mermi_hız
                            elif cops_mermi.shoot5_collide(index)==2:
                                if cops_mermi.m_16_shoot5_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shooty.pop(index+1)
                                c_shooty.pop(index)
                                break
                        else:
                            c_shooty.pop(index+1)
                            c_shooty.pop(index)
                            break
                else:
                    pass
            if 6 in cops_mermi_yön:
                if dağcı_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shootb),2):
                        if 0<=cops_mermi.c_shootb[index]<=window_x:
                            if cops_mermi.shoot6_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootb[index],cops_mermi.c_shootb[index+1],10,5))
                                cops_mermi.c_shootb[index]-=mermi_hız
                                cops_mermi.c_shootb[index+1]+=mermi_hız
                            elif cops_mermi.shoot6_collide(index)==2:
                                if cops_mermi.m_16_shoot6_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootb.pop(index+1)
                                c_shootb.pop(index)
                                break
                        else:
                            c_shootb.pop(index+1)
                            c_shootb.pop(index)
                            break
                else:
                    pass
            if 7 in cops_mermi_yön:
                if dağcı_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shootg),2):
                        if 0<=cops_mermi.c_shootg[index]<=window_x:
                            if cops_mermi.shoot7_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootg[index],cops_mermi.c_shootg[index+1],10,5))
                                cops_mermi.c_shootg[index]-=mermi_hız
                                
                            elif cops_mermi.shoot7_collide(index)==2:
                                if cops_mermi.m_16_shoot7_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootg.pop(index+1)
                                c_shootg.pop(index)
                                break
                        else:
                            c_shootg.pop(index+1)
                            c_shootg.pop(index)
                            break
                else:
                    pass
            if 8 in cops_mermi_yön:
                if dağcı_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shoott),2):
                        if 0<=cops_mermi.c_shoott[index]<=window_x:
                            if cops_mermi.shoot8_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shoott[index],cops_mermi.c_shoott[index+1],10,5))
                                cops_mermi.c_shoott[index]-=mermi_hız
                                cops_mermi.c_shoott[index+1]-=mermi_hız
                            elif cops_mermi.shoot8_collide(index)==2:
                                if cops_mermi.m_16_shoot8_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_awp_mermi_toplam=10
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shoott.pop(index+1)
                                c_shoott.pop(index)
                                break
                        else:
                            c_shoott.pop(index+1)
                            c_shoott.pop(index)
                            break
                else:
                    pass
            if dağcılar_move.dağcı_x<=0 and dağcılar_move.dağcı_y<=0:
                dağcı_mermi_yön.clear()
                i+=1
                cops_m_16_mermi_toplam=90
                dağcı_awp_mermi_toplam=10
                cops_deneme=1
                dağcı_deneme=1
                dağcı_win+=1
                dağcı_atılan_mermi=0
                cops_atılan_mermi=0
                special_forces.para+=0
                dağcılar.para+=1500
                dağcılar_move.dağcı_x=dağcı_x
                dağcılar_move.dağcı_y=dağcı_y
                special_forces_move.cops_x=cops_x
                special_forces_move.cops_y=cops_y
                special_forces.can=100
                dağcılar.can=100
                choose1,choose2=True,False
            pygame.draw.rect(window,(rgb.kum),special_forces_rect)
            pygame.draw.rect(window,(rgb.kum),dağcı_rect)
            window.blit(special_corps_copy,(special_forces_move.cops_x,special_forces_move.cops_y))
            window.blit(dağcı_copy,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y))
            window.blit(yazı_7,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y+2))
            window.blit(yazı_8,(special_forces_move.cops_x+45,special_forces_move.cops_y-5))
            window.blit(yazı_9,(window_x//2+15,20))
            window.blit(yazı_10,(special_forces_move.cops_x+45,special_forces_move.cops_y+4))
            window.blit(yazı_11,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y+12))
            window.blit(special_corps_logo,(1470,0))
            window.blit(dağcı_logo,(1470,35))
            window.blit(yazı_12,(1510,-5))
            window.blit(yazı_13,(1510,32))
            pygame.display.update()
        if special_forces.silah=="m_16" and dağcılar.silah=="desert_eagle":
            cops_kalan_mermi=m_16_mermi-cops_atılan_mermi 
            dağcı_kalan_mermi=desert_eagle_mermi-dağcı_atılan_mermi        
            window.fill((rgb.kum))
            pygame.draw.rect(window,(0,0,0),engel_1)
            pygame.draw.rect(window,(0,0,0),engel_2)
            pygame.draw.rect(window,(0,0,0),engel_3)
            pygame.draw.rect(window,(0,0,0),engel_4)
            pygame.draw.rect(window,(0,0,0),engel_5)
            pygame.draw.rect(window,(0,0,0),engel_6)
            yazı_7=yazı_tipi_7.render(f"{dağcılar.can}/100",True,(0,0,0))
            yazı_8=yazı_tipi_8.render(f"{special_forces.can}/100",True,(0,0,0))
            yazı_9=yazı_tipi_9.render(f"Round {i}",True,(0,0,0))
            yazı_12=yazı_tipi_12.render(f"{cops_win}",True,(0,0,0))
            yazı_13=yazı_tipi_13.render(f"{dağcı_win}",True,(0,0,0))
            yazı_10=yazı_tipi_10.render(f"{cops_kalan_mermi}/{dağcı_m_16_mermi_toplam}",True,(0,0,0))
            yazı_11=yazı_tipi_11.render(f"{dağcı_kalan_mermi}/{dağcı_desert_eagle_mermi_toplam}",True,(0,0,0))
            special_forces_rect=pygame.Rect(special_forces_move.cops_x,special_forces_move.cops_y,special_corps_size_x,special_corps_size_y)
            dağcı_rect=pygame.Rect(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y,dağcılar_size_x,dağcılar_size_y)
            keys=pygame.key.get_pressed()
            if keys[pygame.K_w] and special_forces_move.cops_y>=0 :
                special_forces_move.w()
            if keys[pygame.K_s] and special_forces_move.cops_y<=window_y-special_corps.get_size()[1]:
                special_forces_move.s()
            if keys[pygame.K_a] and special_forces_move.cops_x>=0:
                special_forces_move.a()
            if keys[pygame.K_d] and special_forces_move.cops_x<=window_x-special_corps.get_size()[0]:
                special_forces_move.d()
            if keys[pygame.K_UP] and dağcılar_move.dağcı_y>=0:
                dağcılar_move.up()
            if keys[pygame.K_DOWN] and dağcılar_move.dağcı_y<=window_y-dağcılar_size_y:
                dağcılar_move.down()
            if keys[pygame.K_LEFT] and dağcılar_move.dağcı_x>=0:
                dağcılar_move.left()
            if keys[pygame.K_RIGHT] and dağcılar_move.dağcı_x<=window_x-dağcılar_size_x:
                dağcılar_move.right()
            if cops_atılan_mermi<m_16_mermi:
                if keys[pygame.K_j]:
                    cops_mermi_yön.add(1)
                    cops_mermi.m_16_shoot1()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_u]:
                    cops_mermi_yön.add(2)
                    cops_mermi.m_16_shoot2()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_m]:
                    cops_mermi_yön.add(3)
                    cops_mermi.m_16_shoot3()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_y]:
                    cops_mermi_yön.add(4)
                    cops_mermi.m_16_shoot4()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_n]:
                    cops_mermi_yön.add(5)
                    cops_mermi.m_16_shoot5()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_b]:
                    cops_mermi_yön.add(6)
                    cops_mermi.m_16_shoot6()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_g]:
                    cops_mermi_yön.add(7)
                    cops_mermi.m_16_shoot7()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_t]:
                    cops_mermi_yön.add(8)
                    cops_mermi.m_16_shoot8()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
            else:
                pass
            if keys[pygame.K_r]:
                if cops_m_16_mermi_toplam-cops_atılan_mermi>=0:
                    cops_m_16_mermi_toplam-=cops_atılan_mermi
                    cops_atılan_mermi=0
                else:
                    if cops_deneme==0:
                        pass
                    else:
                        cops_atılan_mermi=m_16_mermi-cops_m_16_mermi_toplam
                        cops_m_16_mermi_toplam-=cops_m_16_mermi_toplam
                        cops_deneme=0         
            if dağcı_atılan_mermi<desert_eagle_mermi:
                if keys[pygame.K_KP_1]:
                    dağcı_mermi_yön.add(1)
                    dağcı_mermi.desert_eagle_shoot1()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_2]:
                    dağcı_mermi_yön.add(2)
                    dağcı_mermi.desert_eagle_shoot2()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_3]:
                    dağcı_mermi_yön.add(3)
                    dağcı_mermi.desert_eagle_shoot3()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_4]:
                    dağcı_mermi_yön.add(4)
                    dağcı_mermi.desert_eagle_shoot4()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_6]:
                    dağcı_mermi_yön.add(6)
                    dağcı_mermi.desert_eagle_shoot6()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_7]:
                    dağcı_mermi_yön.add(7)
                    dağcı_mermi.desert_eagle_shoot7()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_8]:
                    dağcı_mermi_yön.add(8)
                    dağcı_mermi.desert_eagle_shoot8()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_9]:
                    dağcı_mermi_yön.add(9)  
                    dağcı_mermi.desert_eagle_shoot9()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
            else:
                pass
            if keys[pygame.K_KP_5]:
                if dağcı_desert_eagle_mermi_toplam-dağcı_atılan_mermi>=0:
                    dağcı_desert_eagle_mermi_toplam-=dağcı_atılan_mermi
                    dağcı_atılan_mermi=0
                else:
                    if dağcı_deneme==0:
                        pass
                    else:
                        dağcı_atılan_mermi=awp_mermi-dağcı_awp_mermi_toplam
                        dağcı_awp_mermi_toplam-=dağcı_awp_mermi_toplam
                        dağcı_deneme=0    
            if 1 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot1),2):
                        if 0<=dağcı_mermi.d_shoot1[index]<=window_x:
                            if dağcı_mermi.shoot1_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot1[index],dağcı_mermi.d_shoot1[index+1],10,5))
                                dağcı_mermi.d_shoot1[index]-=mermi_hız
                                dağcı_mermi.d_shoot1[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot1_collide(index)==2:
                                if dağcı_mermi.desert_eagle_shoot1_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                break
                            else:
                                d_shoot1.pop(index+1)
                                d_shoot1.pop(index)
                                break
                        else:
                            d_shoot1.pop(index+1)
                            d_shoot1.pop(index)
                            break
                else:
                    pass
            if 2 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot2),2):
                        if 0<=dağcı_mermi.d_shoot2[index]<=window_x:
                            if dağcı_mermi.shoot2_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot2[index],dağcı_mermi.d_shoot2[index+1],5,10))
                                dağcı_mermi.d_shoot2[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot2_collide(index)==2:
                                if dağcı_mermi.desert_eagle_shoot2_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot2.pop(index+1)
                                d_shoot2.pop(index)
                                break
                        else:
                            d_shoot2.pop(index+1)
                            d_shoot2.pop(index)
                            break
                else:
                    pass
            if 3 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot3),2):
                        if 0<=dağcı_mermi.d_shoot3[index]<=window_x:
                            if dağcı_mermi.shoot3_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot3[index],dağcı_mermi.d_shoot3[index+1],10,5))
                                dağcı_mermi.d_shoot3[index]+=mermi_hız
                                dağcı_mermi.d_shoot3[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot3_collide(index)==2:
                                if dağcı_mermi.desert_eagle_shoot3_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot3.pop(index+1)
                                d_shoot3.pop(index)
                                break
                        else:
                            d_shoot3.pop(index+1)
                            d_shoot3.pop(index)
                            break
                else:
                    pass
            if 4 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot4),2):
                        if 0<=dağcı_mermi.d_shoot4[index]<=window_x:
                            if dağcı_mermi.shoot4_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot4[index],dağcı_mermi.d_shoot4[index+1],10,5))
                                dağcı_mermi.d_shoot4[index]-=mermi_hız
                
                            elif dağcı_mermi.shoot4_collide(index)==2:
                                if dağcı_mermi.desert_eagle_shoot4_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot4.pop(index+1)
                                d_shoot4.pop(index)
                                break
                        else:
                            d_shoot4.pop(index+1)
                            d_shoot4.pop(index)
                            break
                else:
                    pass
            if 6 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot6),2):
                        if 0<=dağcı_mermi.d_shoot6[index]<=window_x:
                            if dağcı_mermi.shoot6_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot6[index],dağcı_mermi.d_shoot6[index+1],10,5))
                                dağcı_mermi.d_shoot6[index]+=mermi_hız
                            elif dağcı_mermi.shoot6_collide(index)==2:
                                if dağcı_mermi.desert_eagle_shoot6_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot6.pop(index+1)
                                d_shoot6.pop(index)
                                break
                        else:
                            d_shoot6.pop(index+1)
                            d_shoot6.pop(index)
                            break
                else:
                    pass                
            if 7 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot7),2):
                        if 0<=dağcı_mermi.d_shoot7[index]<=window_x:
                            if dağcı_mermi.shoot7_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot7[index],dağcı_mermi.d_shoot7[index+1],10,5))
                                dağcı_mermi.d_shoot7[index]-=mermi_hız
                                dağcı_mermi.d_shoot7[index+1]-=mermi_hız
                
                            elif dağcı_mermi.shoot7_collide(index)==2:
                                if dağcı_mermi.desert_eagle_shoot7_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot7.pop(index+1)
                                d_shoot7.pop(index)
                                break
                        else:
                            d_shoot7.pop(index+1)
                            d_shoot7.pop(index)
                            break
                else:
                    pass           
            if 8 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot8),2):
                        if 0<=dağcı_mermi.d_shoot8[index]<=window_x:
                            if dağcı_mermi.shoot8_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot8[index],dağcı_mermi.d_shoot8[index+1],5,10))
                                dağcı_mermi.d_shoot8[index+1]-=mermi_hız
                
                            elif dağcı_mermi.shoot8_collide(index)==2:
                                if dağcı_mermi.desert_eagle_shoot8_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot8.pop(index+1)
                                d_shoot8.pop(index)
                                break
                        else:
                            d_shoot8.pop(index+1)
                            d_shoot8.pop(index)
                            break
                else:
                    pass           
            if 9 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=desert_eagle_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot9),2):
                        if 0<=dağcı_mermi.d_shoot9[index]<=window_x:
                            if dağcı_mermi.shoot9_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot9[index],dağcı_mermi.d_shoot9[index+1],10,5))
                                dağcı_mermi.d_shoot9[index]+=mermi_hız
                                dağcı_mermi.d_shoot9[index+1]-=mermi_hız
                            elif dağcı_mermi.shoot9_collide(index)==2:
                                if dağcı_mermi.desert_eagle_shoot9_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break      
                            else:
                                d_shoot9.pop(index+1)
                                d_shoot9.pop(index)
                                break
                        else:
                            d_shoot9.pop(index+1)
                            d_shoot9.pop(index)
                            break
                else:
                    pass
            if 1 in cops_mermi_yön:
                if cops_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shootj),2):
                        if 0<=cops_mermi.c_shootj[index]<=window_x:
                            if cops_mermi.shoot1_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootj[index],cops_mermi.c_shootj[index+1],10,5))
                                cops_mermi.c_shootj[index]+=mermi_hız
                            elif cops_mermi.shoot1_collide(index)==2:
                                if cops_mermi.m_16_shoot1_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootj.pop(index+1)
                                c_shootj.pop(index)
                                break
                        else:
                            c_shootj.pop(index+1)
                            c_shootj.pop(index)
                            break
                else:
                    pass
            if 2 in cops_mermi_yön:
                if cops_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shootu),2):
                        if 0<=cops_mermi.c_shootu[index]<=window_x:
                            if cops_mermi.shoot2_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootu[index],cops_mermi.c_shootu[index+1],10,5))
                                cops_mermi.c_shootu[index]+=mermi_hız
                                cops_mermi.c_shootu[index+1]-=mermi_hız
                            elif cops_mermi.shoot2_collide(index)==2:
                                if cops_mermi.m_16_shoot2_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootu.pop(index+1)
                                c_shootu.pop(index)
                                break
                        else:
                            c_shootu.pop(index+1)
                            c_shootu.pop(index)
                            break
                else:
                    pass
            if 3 in cops_mermi_yön:
                if cops_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shootm),2):
                        if 0<=cops_mermi.c_shootm[index]<=window_x:
                            if cops_mermi.shoot3_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootm[index],cops_mermi.c_shootm[index+1],10,5))
                                cops_mermi.c_shootm[index]+=mermi_hız
                                cops_mermi.c_shootm[index+1]+=mermi_hız
                            elif cops_mermi.shoot3_collide(index)==2:
                                if cops_mermi.m_16_shoot3_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootm.pop(index+1)
                                c_shootm.pop(index)
                                break
                        else:
                            c_shootm.pop(index+1)
                            c_shootm.pop(index)
                            break
                else:
                    pass
            if 4 in cops_mermi_yön:
                if cops_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shootn),2):
                        if 0<=cops_mermi.c_shootn[index]<=window_x:
                            if cops_mermi.shoot4_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootn[index],cops_mermi.c_shootn[index+1],5,10))
                                cops_mermi.c_shootn[index+1]-=mermi_hız
                            elif cops_mermi.shoot4_collide(index)==2:
                                if cops_mermi.m_16_shoot4_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootn.pop(index+1)
                                c_shootn.pop(index)
                                break
                        else:
                            c_shootn.pop(index+1)
                            c_shootn.pop(index)
                            break
                else:
                    pass
            if 5 in cops_mermi_yön:
                if cops_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shooty),2):
                        if 0<=cops_mermi.c_shooty[index]<=window_x:
                            if cops_mermi.shoot5_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shooty[index],cops_mermi.c_shooty[index+1],5,10))
                                
                                cops_mermi.c_shooty[index+1]+=mermi_hız
                            elif cops_mermi.shoot5_collide(index)==2:
                                if cops_mermi.m_16_shoot5_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shooty.pop(index+1)
                                c_shooty.pop(index)
                                break
                        else:
                            c_shooty.pop(index+1)
                            c_shooty.pop(index)
                            break
                else:
                    pass
            if 6 in cops_mermi_yön:
                if cops_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shootb),2):
                        if 0<=cops_mermi.c_shootb[index]<=window_x:
                            if cops_mermi.shoot6_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootb[index],cops_mermi.c_shootb[index+1],10,5))
                                cops_mermi.c_shootb[index]-=mermi_hız
                                cops_mermi.c_shootb[index+1]+=mermi_hız
                            elif cops_mermi.shoot6_collide(index)==2:
                                if cops_mermi.m_16_shoot6_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootb.pop(index+1)
                                c_shootb.pop(index)
                                break
                        else:
                            c_shootb.pop(index+1)
                            c_shootb.pop(index)
                            break
                else:
                    pass
            if 7 in cops_mermi_yön:
                if cops_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shootg),2):
                        if 0<=cops_mermi.c_shootg[index]<=window_x:
                            if cops_mermi.shoot7_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootg[index],cops_mermi.c_shootg[index+1],10,5))
                                cops_mermi.c_shootg[index]-=mermi_hız
                                
                            elif cops_mermi.shoot7_collide(index)==2:
                                if cops_mermi.m_16_shoot7_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootg.pop(index+1)
                                c_shootg.pop(index)
                                break
                        else:
                            c_shootg.pop(index+1)
                            c_shootg.pop(index)
                            break
                else:
                    pass
            if 8 in cops_mermi_yön:
                if cops_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shoott),2):
                        if 0<=cops_mermi.c_shoott[index]<=window_x:
                            if cops_mermi.shoot8_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shoott[index],cops_mermi.c_shoott[index+1],10,5))
                                cops_mermi.c_shoott[index]-=mermi_hız
                                cops_mermi.c_shoott[index+1]-=mermi_hız
                            elif cops_mermi.shoot8_collide(index)==2:
                                if cops_mermi.m_16_shoot8_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_desert_eagle_mermi_toplam=60
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shoott.pop(index+1)
                                c_shoott.pop(index)
                                break
                        else:
                            c_shoott.pop(index+1)
                            c_shoott.pop(index)
                            break
                else:
                    pass
            if dağcılar_move.dağcı_x<=0 and dağcılar_move.dağcı_y<=0:
                dağcı_mermi_yön.clear()
                i+=1
                cops_m_16_mermi_toplam=90
                dağcı_desert_eagle_mermi_toplam=60
                cops_deneme=1
                dağcı_deneme=1
                dağcı_win+=1
                special_forces.para+=0
                dağcılar.para+=1500
                dağcı_atılan_mermi=0
                cops_atılan_mermi=0
                dağcılar_move.dağcı_x=dağcı_x
                dağcılar_move.dağcı_y=dağcı_y
                special_forces_move.cops_x=cops_x
                special_forces_move.cops_y=cops_y
                special_forces.can=100
                dağcılar.can=100
                choose1,choose2=True,False
            pygame.draw.rect(window,(rgb.kum),special_forces_rect)
            pygame.draw.rect(window,(rgb.kum),dağcı_rect)
            window.blit(special_corps_copy,(special_forces_move.cops_x,special_forces_move.cops_y))
            window.blit(dağcı_copy,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y))
            window.blit(yazı_7,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y+2))
            window.blit(yazı_8,(special_forces_move.cops_x+45,special_forces_move.cops_y-5))
            window.blit(yazı_9,(window_x//2,20))
            window.blit(yazı_10,(special_forces_move.cops_x+45,special_forces_move.cops_y+4))
            window.blit(yazı_11,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y+12))
            window.blit(special_corps_logo,(1470,0))
            window.blit(dağcı_logo,(1470,35))
            window.blit(yazı_12,(1510,-5))
            window.blit(yazı_13,(1510,32))
            pygame.display.update()
        if special_forces.silah=="m_16" and dağcılar.silah=="ak_47":     
            cops_kalan_mermi=m_16_mermi-cops_atılan_mermi 
            dağcı_kalan_mermi=ak_47_mermi-dağcı_atılan_mermi   
            window.fill((rgb.kum))
            pygame.draw.rect(window,(0,0,0),engel_1)
            pygame.draw.rect(window,(0,0,0),engel_2)
            pygame.draw.rect(window,(0,0,0),engel_3)
            pygame.draw.rect(window,(0,0,0),engel_4)
            pygame.draw.rect(window,(0,0,0),engel_5)
            pygame.draw.rect(window,(0,0,0),engel_6)
            yazı_7=yazı_tipi_7.render(f"{dağcılar.can}/100",True,(0,0,0))
            yazı_8=yazı_tipi_8.render(f"{special_forces.can}/100",True,(0,0,0))
            yazı_9=yazı_tipi_9.render(f"Round {i}",True,(0,0,0))
            yazı_12=yazı_tipi_12.render(f"{cops_win}",True,(0,0,0))
            yazı_13=yazı_tipi_13.render(f"{dağcı_win}",True,(0,0,0))
            yazı_10=yazı_tipi_10.render(f"{cops_kalan_mermi}/{cops_m_16_mermi_toplam}",True,(0,0,0))
            yazı_11=yazı_tipi_11.render(f"{dağcı_kalan_mermi}/{dağcı_ak_47_mermi_toplam}",True,(0,0,0))
            special_forces_rect=pygame.Rect(special_forces_move.cops_x,special_forces_move.cops_y,special_corps_size_x,special_corps_size_y)
            dağcı_rect=pygame.Rect(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y,dağcılar_size_x,dağcılar_size_y)
            keys=pygame.key.get_pressed()
            if keys[pygame.K_w] and special_forces_move.cops_y>=0 :
                special_forces_move.w()
            if keys[pygame.K_s] and special_forces_move.cops_y<=window_y-special_corps.get_size()[1]:
                special_forces_move.s()
            if keys[pygame.K_a] and special_forces_move.cops_x>=0:
                special_forces_move.a()
            if keys[pygame.K_d] and special_forces_move.cops_x<=window_x-special_corps.get_size()[0]:
                special_forces_move.d()
            if keys[pygame.K_UP] and dağcılar_move.dağcı_y>=0:
                dağcılar_move.up()
            if keys[pygame.K_DOWN] and dağcılar_move.dağcı_y<=window_y-dağcılar_size_y:
                dağcılar_move.down()
            if keys[pygame.K_LEFT] and dağcılar_move.dağcı_x>=0:
                dağcılar_move.left()
            if keys[pygame.K_RIGHT] and dağcılar_move.dağcı_x<=window_x-dağcılar_size_x:
                dağcılar_move.right()
            if cops_atılan_mermi<m_16_mermi:
                if keys[pygame.K_j]:
                    cops_mermi_yön.add(1)
                    cops_mermi.m_16_shoot1()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_u]:
                    cops_mermi_yön.add(2)
                    cops_mermi.m_16_shoot2()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_m]:
                    cops_mermi_yön.add(3)
                    cops_mermi.m_16_shoot3()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_y]:
                    cops_mermi_yön.add(4)
                    cops_mermi.m_16_shoot4()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_n]:
                    cops_mermi_yön.add(5)
                    cops_mermi.m_16_shoot5()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_b]:
                    cops_mermi_yön.add(6)
                    cops_mermi.m_16_shoot6()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_g]:
                    cops_mermi_yön.add(7)
                    cops_mermi.m_16_shoot7()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_t]:
                    cops_mermi_yön.add(8)
                    cops_mermi.m_16_shoot8()
                    cops_atılan_mermi+=1
                    time.sleep(0.1)
            else:
                pass
            if keys[pygame.K_r]:
                if cops_m_16_mermi_toplam-cops_atılan_mermi>=0:
                    cops_m_16_mermi_toplam-=cops_atılan_mermi
                    cops_atılan_mermi=0
                else:
                    if cops_deneme==0:
                        pass
                    else:
                        cops_atılan_mermi=m_16_mermi-cops_m_16_mermi_toplam
                        cops_m_16_mermi_toplam-=cops_m_16_mermi_toplam
                        cops_deneme=0         
            if dağcı_atılan_mermi<ak_47_mermi:
                if keys[pygame.K_KP_1]:
                    dağcı_mermi_yön.add(1)
                    dağcı_mermi.ak_47_shoot1()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_2]:
                    dağcı_mermi_yön.add(2)
                    dağcı_mermi.ak_47_shoot2()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_3]:
                    dağcı_mermi_yön.add(3)
                    dağcı_mermi.ak_47_shoot3()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_4]:
                    dağcı_mermi_yön.add(4)
                    dağcı_mermi.ak_47_shoot4()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_6]:
                    dağcı_mermi_yön.add(6)
                    dağcı_mermi.ak_47_shoot6()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_7]:
                    dağcı_mermi_yön.add(7)
                    dağcı_mermi.ak_47_shoot7()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_8]:
                    dağcı_mermi_yön.add(8)
                    dağcı_mermi.ak_47_shoot8()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
                if keys[pygame.K_KP_9]:
                    dağcı_mermi_yön.add(9)  
                    dağcı_mermi.ak_47_shoot9()
                    dağcı_atılan_mermi+=1
                    time.sleep(0.1)
            else:
                pass
            if keys[pygame.K_KP_5]:
                if dağcı_ak_47_mermi_toplam-dağcı_atılan_mermi>=0:
                    dağcı_ak_47_mermi_toplam-=dağcı_atılan_mermi
                    dağcı_atılan_mermi=0
                else:
                    if dağcı_deneme==0:
                        pass
                    else:
                        dağcı_atılan_mermi=ak_47_mermi-dağcı_ak_47_mermi_toplam
                        dağcı_ak_47_mermi_toplam-=dağcı_ak_47_mermi_toplam
                        dağcı_deneme=0    
            if 1 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=ak_47_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot1),2):
                        if 0<=dağcı_mermi.d_shoot1[index]<=window_x:
                            if dağcı_mermi.shoot1_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot1[index],dağcı_mermi.d_shoot1[index+1],10,5))
                                dağcı_mermi.d_shoot1[index]-=mermi_hız
                                dağcı_mermi.d_shoot1[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot1_collide(index)==2:
                                if dağcı_mermi.ak_47_shoot1_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                break
                            else:
                                d_shoot1.pop(index+1)
                                d_shoot1.pop(index)
                                break
                        else:
                            d_shoot1.pop(index+1)
                            d_shoot1.pop(index)
                            break
                else:
                    pass
            if 2 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=ak_47_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot2),2):
                        if 0<=dağcı_mermi.d_shoot2[index]<=window_x:
                            if dağcı_mermi.shoot2_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot2[index],dağcı_mermi.d_shoot2[index+1],5,10))
                                dağcı_mermi.d_shoot2[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot2_collide(index)==2:
                                if dağcı_mermi.ak_47_shoot2_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot2.pop(index+1)
                                d_shoot2.pop(index)
                                break
                        else:
                            d_shoot2.pop(index+1)
                            d_shoot2.pop(index)
                            break
                else:
                    pass
            if 3 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=ak_47_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot3),2):
                        if 0<=dağcı_mermi.d_shoot3[index]<=window_x:
                            if dağcı_mermi.shoot3_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot3[index],dağcı_mermi.d_shoot3[index+1],10,5))
                                dağcı_mermi.d_shoot3[index]+=mermi_hız
                                dağcı_mermi.d_shoot3[index+1]+=mermi_hız
                            elif dağcı_mermi.shoot3_collide(index)==2:
                                if dağcı_mermi.ak_47_shoot3_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot3.pop(index+1)
                                d_shoot3.pop(index)
                                break
                        else:
                            d_shoot3.pop(index+1)
                            d_shoot3.pop(index)
                            break
                else:
                    pass
            if 4 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=ak_47_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot4),2):
                        if 0<=dağcı_mermi.d_shoot4[index]<=window_x:
                            if dağcı_mermi.shoot4_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot4[index],dağcı_mermi.d_shoot4[index+1],10,5))
                                dağcı_mermi.d_shoot4[index]-=mermi_hız
                
                            elif dağcı_mermi.shoot4_collide(index)==2:
                                if dağcı_mermi.ak_47_shoot4_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot4.pop(index+1)
                                d_shoot4.pop(index)
                                break
                        else:
                            d_shoot4.pop(index+1)
                            d_shoot4.pop(index)
                            break
                else:
                    pass
            if 6 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=ak_47_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot6),2):
                        if 0<=dağcı_mermi.d_shoot6[index]<=window_x:
                            if dağcı_mermi.shoot6_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot6[index],dağcı_mermi.d_shoot6[index+1],10,5))
                                dağcı_mermi.d_shoot6[index]+=mermi_hız
                            elif dağcı_mermi.shoot6_collide(index)==2:
                                if dağcı_mermi.ak_47_shoot6_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot6.pop(index+1)
                                d_shoot6.pop(index)
                                break
                        else:
                            d_shoot6.pop(index+1)
                            d_shoot6.pop(index)
                            break
                else:
                    pass

            if 7 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=ak_47_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot7),2):
                        if 0<=dağcı_mermi.d_shoot7[index]<=window_x:
                            if dağcı_mermi.shoot7_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot7[index],dağcı_mermi.d_shoot7[index+1],10,5))
                                dağcı_mermi.d_shoot7[index]-=mermi_hız
                                dağcı_mermi.d_shoot7[index+1]-=mermi_hız
                
                            elif dağcı_mermi.shoot7_collide(index)==2:
                                if dağcı_mermi.ak_47_shoot7_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot7.pop(index+1)
                                d_shoot7.pop(index)
                                break
                        else:
                            d_shoot7.pop(index+1)
                            d_shoot7.pop(index)
                            break
                else:
                    pass

            if 8 in dağcı_mermi_yön:
                if dağcı_atılan_mermi<=ak_47_mermi:
                    for index in range(0,len(dağcı_mermi.d_shoot8),2):
                        if 0<=dağcı_mermi.d_shoot8[index]<=window_x:
                            if dağcı_mermi.shoot8_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot8[index],dağcı_mermi.d_shoot8[index+1],5,10))
                                dağcı_mermi.d_shoot8[index+1]-=mermi_hız
                
                            elif dağcı_mermi.shoot8_collide(index)==2:
                                if dağcı_mermi.ak_47_shoot8_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    dağcı_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=True,False
                                    break
                                break
                            else:
                                d_shoot8.pop(index+1)
                                d_shoot8.pop(index)
                                break
                        else:
                            d_shoot8.pop(index+1)
                            d_shoot8.pop(index)
                            break
                else:
                    pass
            if 9 in dağcı_mermi_yön:
                for index in range(0,len(dağcı_mermi.d_shoot9),2):
                    if 0<=dağcı_mermi.d_shoot9[index]<=window_x:
                        if dağcı_mermi.shoot9_collide(index)==1:
                            pygame.draw.rect(window,(0,0,0),(dağcı_mermi.d_shoot9[index],dağcı_mermi.d_shoot9[index+1],10,5))
                            dağcı_mermi.d_shoot9[index]+=mermi_hız
                            dağcı_mermi.d_shoot9[index+1]-=mermi_hız
                        elif dağcı_mermi.shoot9_collide(index)==2:
                            if dağcı_mermi.ak_47_shoot9_isabet(i)==1:
                                i+=1
                                cops_m_16_mermi_toplam=90
                                dağcı_ak_47_mermi_toplam=90
                                cops_deneme=1
                                dağcı_deneme=1
                                dağcı_win+=1
                                dağcı_atılan_mermi=0
                                cops_atılan_mermi=0
                                choose1,choose2=True,False
                                break      
                        else:
                            d_shoot9.pop(index+1)
                            d_shoot9.pop(index)
                            break
                    else:
                        d_shoot9.pop(index+1)
                        d_shoot9.pop(index)
                        break
            if 1 in cops_mermi_yön:
                if cops_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shootj),2):
                        if 0<=cops_mermi.c_shootj[index]<=window_x:
                            if cops_mermi.shoot1_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootj[index],cops_mermi.c_shootj[index+1],10,5))
                                cops_mermi.c_shootj[index]+=mermi_hız
                            elif cops_mermi.shoot1_collide(index)==2:
                                if cops_mermi.m_16_shoot1_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootj.pop(index+1)
                                c_shootj.pop(index)
                                break
                        else:
                            c_shootj.pop(index+1)
                            c_shootj.pop(index)
                            break
                else:
                    pass
            if 2 in cops_mermi_yön:
                if cops_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shootu),2):
                        if 0<=cops_mermi.c_shootu[index]<=window_x:
                            if cops_mermi.shoot2_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootu[index],cops_mermi.c_shootu[index+1],10,5))
                                cops_mermi.c_shootu[index]+=mermi_hız
                                cops_mermi.c_shootu[index+1]-=mermi_hız
                            elif cops_mermi.shoot2_collide(index)==2:
                                if cops_mermi.m_16_shoot2_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootu.pop(index+1)
                                c_shootu.pop(index)
                                break
                        else:
                            c_shootu.pop(index+1)
                            c_shootu.pop(index)
                            break
                else:
                    pass
            if 3 in cops_mermi_yön:
                if cops_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shootm),2):
                        if 0<=cops_mermi.c_shootm[index]<=window_x:
                            if cops_mermi.shoot3_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootm[index],cops_mermi.c_shootm[index+1],10,5))
                                cops_mermi.c_shootm[index]+=mermi_hız
                                cops_mermi.c_shootm[index+1]+=mermi_hız
                            elif cops_mermi.shoot3_collide(index)==2:
                                if cops_mermi.m_16_shoot3_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootm.pop(index+1)
                                c_shootm.pop(index)
                                break
                        else:
                            c_shootm.pop(index+1)
                            c_shootm.pop(index)
                            break
                else:
                    pass
            if 4 in cops_mermi_yön:
                if cops_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shootn),2):
                        if 0<=cops_mermi.c_shootn[index]<=window_x:
                            if cops_mermi.shoot4_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootn[index],cops_mermi.c_shootn[index+1],5,10))
                                cops_mermi.c_shootn[index+1]-=mermi_hız
                            elif cops_mermi.shoot4_collide(index)==2:
                                if cops_mermi.m_16_shoot4_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootn.pop(index+1)
                                c_shootn.pop(index)
                                break
                        else:
                            c_shootn.pop(index+1)
                            c_shootn.pop(index)
                            break
                else:
                    pass
            if 5 in cops_mermi_yön:
                if cops_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shooty),2):
                        if 0<=cops_mermi.c_shooty[index]<=window_x:
                            if cops_mermi.shoot5_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shooty[index],cops_mermi.c_shooty[index+1],5,10))
                                
                                cops_mermi.c_shooty[index+1]+=mermi_hız
                            elif cops_mermi.shoot5_collide(index)==2:
                                if cops_mermi.m_16_shoot5_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shooty.pop(index+1)
                                c_shooty.pop(index)
                                break
                        else:
                            c_shooty.pop(index+1)
                            c_shooty.pop(index)
                            break
                else:
                    pass
            if 6 in cops_mermi_yön:
                if cops_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shootb),2):
                        if 0<=cops_mermi.c_shootb[index]<=window_x:
                            if cops_mermi.shoot6_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootb[index],cops_mermi.c_shootb[index+1],10,5))
                                cops_mermi.c_shootb[index]-=mermi_hız
                                cops_mermi.c_shootb[index+1]+=mermi_hız
                            elif cops_mermi.shoot6_collide(index)==2:
                                if cops_mermi.m_16_shoot6_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootb.pop(index+1)
                                c_shootb.pop(index)
                                break
                        else:
                            c_shootb.pop(index+1)
                            c_shootb.pop(index)
                            break
                else:
                    pass
            if 7 in cops_mermi_yön:
                if cops_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shootg),2):
                        if 0<=cops_mermi.c_shootg[index]<=window_x:
                            if cops_mermi.shoot7_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shootg[index],cops_mermi.c_shootg[index+1],10,5))
                                cops_mermi.c_shootg[index]-=mermi_hız
                                
                            elif cops_mermi.shoot7_collide(index)==2:
                                if cops_mermi.m_16_shoot7_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shootg.pop(index+1)
                                c_shootg.pop(index)
                                break
                        else:
                            c_shootg.pop(index+1)
                            c_shootg.pop(index)
                            break
                else:
                    pass
            if 8 in cops_mermi_yön:
                if cops_atılan_mermi<=m_16_mermi:
                    for index in range(0,len(cops_mermi.c_shoott),2):
                        if 0<=cops_mermi.c_shoott[index]<=window_x:
                            if cops_mermi.shoot8_collide(index)==1:
                                pygame.draw.rect(window,(0,0,0),(cops_mermi.c_shoott[index],cops_mermi.c_shoott[index+1],10,5))
                                cops_mermi.c_shoott[index]-=mermi_hız
                                cops_mermi.c_shoott[index+1]-=mermi_hız
                            elif cops_mermi.shoot8_collide(index)==2:
                                if cops_mermi.m_16_shoot8_isabet(i)==1:
                                    i+=1
                                    cops_m_16_mermi_toplam=90
                                    dağcı_ak_47_mermi_toplam=90
                                    cops_deneme=1
                                    dağcı_deneme=1
                                    cops_win+=1
                                    dağcı_atılan_mermi=0
                                    cops_atılan_mermi=0
                                    choose1,choose2=False,True
                                break
                            else:
                                c_shoott.pop(index+1)
                                c_shoott.pop(index)
                                break
                        else:
                            c_shoott.pop(index+1)
                            c_shoott.pop(index)
                            break
                else:
                    pass
            if dağcılar_move.dağcı_x<=0 and dağcılar_move.dağcı_y<=0:
                dağcı_mermi_yön.clear()
                i+=1
                cops_m_16_mermi_toplam=90
                dağcı_ak_47_mermi_toplam=90
                cops_deneme=1
                dağcı_deneme=1
                dağcı_win+=1
                special_forces.para+=0
                dağcılar.para+=1500
                dağcı_atılan_mermi=0
                cops_atılan_mermi=0
                dağcılar_move.dağcı_x=dağcı_x
                dağcılar_move.dağcı_y=dağcı_y
                special_forces_move.cops_x=cops_x
                special_forces_move.cops_y=cops_y
                special_forces.can=100
                dağcılar.can=100
                choose1,choose2=True,
            pygame.draw.rect(window,(rgb.kum),special_forces_rect)
            pygame.draw.rect(window,(rgb.kum),dağcı_rect)
            window.blit(special_corps_copy,(special_forces_move.cops_x,special_forces_move.cops_y))
            window.blit(dağcı_copy,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y))
            window.blit(yazı_7,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y+2))
            window.blit(yazı_8,(special_forces_move.cops_x+45,special_forces_move.cops_y-5))
            window.blit(yazı_9,(window_x//2+15,20))
            window.blit(yazı_10,(special_forces_move.cops_x+45,special_forces_move.cops_y+4))
            window.blit(yazı_11,(dağcılar_move.dağcı_x,dağcılar_move.dağcı_y+12))
            window.blit(special_corps_logo,(1470,0))
            window.blit(dağcı_logo,(1470,35))
            window.blit(yazı_12,(1510,-5))
            window.blit(yazı_13,(1510,32))
            pygame.display.update()




pygame.quit() 

