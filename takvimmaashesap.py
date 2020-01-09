#Zamlari yüzde orani ile verilen zamlar, miktar belirtilerek (seyyanen) verilen zamlar ve cifte maas(ikramiye) verilenler olarak uce ayirdim.
#Yüzde orani ile verilen zamlari yuzde kelimesi, yuzde isareti ve nokta stringlerini aratarak tespit ettim.
#Nokta kelimesinin zam baglami disinda kullanildigi bir durumu tespit edip ayikladim.
#Miktar belirtilen zamlari tamami rakam olarak verilenler ve icinde yazi ile bin kelimesi kullanilanlar olarak ayirip hesapladim.
#26 Temmuz 2019'daki emekliye 12 milyar lira haberini try, except ile eledim.
#cifte maas haberlerini zam olarak değil ikramiye olarak uyguladim.

emeklimaas = 1 # 1 Ocak 2019 tarihi ile bir emeklinin maasi 1 TL kabul edildi.
ikramiye = 0 #cifte maaslarin hesaplamasi icin kullanilacak.
with open('takvim.txt', 'r') as program: #takvim.txt dosyasina kaydedilen mansetleri program ismini vererek cektim.
    data = program.readlines() #text dosyasini satir satir okuyup data ismini vererek kaydettim.
for count, line in enumerate(reversed(data),1): #text dosyasinda ilk satir 31 Aralik oldugu icin reversed kullanarak sondan basladim. enumerate ile indexledim.
    if 'tl' in line: #zam haberi satirinda tl ya da lira geciyorsa mevcut maasa bahsedilen miktarda zammi ekledim.
        positionoftl = line.find('tl') #zam yapilan miktara ulasmak icin tl 'nin satir icindeki pozisyonunu buldum.
        zam_miktari = line[positionoftl-5:positionoftl]
        zam_miktarison=line[positionoftl-9:positionoftl-5]
        if 'bin' in zam_miktarison: #bu if blogunu 2 bin 123 tl gibi bir formatta verilen veriyi okumak için yazdim.
            h = line[positionoftl-10:positionoftl-8].strip()
            g = int(h)*1000 + int(line[positionoftl-5:positionoftl].strip())
            emeklimaas = emeklimaas + g
        elif 'bin' in zam_miktari: #bazi haberlerde rakamlar 2 bin 500 gibi sekillerde karmasik sekilde verildiğinden bin kelimesini bulup 1000 sekline cevirdim.
            zam_miktarinew = line[positionoftl-7:positionoftl]
            x = line[positionoftl-7:positionoftl-5].strip()
            if x.isdigit():
                y = int(x)*1000
                emeklimaas = emeklimaas + y
            else:
                emeklimaas = emeklimaas + int(zam_miktarinew.strip())
        else:
            emeklimaas = emeklimaas + int(zam_miktari.strip())

    elif 'lira' in line: #zam haberi satirinda tl ya da lira geciyorsa mevcut maasa bahsedilen zammi ekledim.
        positionoflira= line.find('lira') #zam yapilan miktara ulasmak icin lira'nın satir icindeki pozisyonunu buldum.
        zam_miktari2 = line[positionoflira-5:positionoflira]
        zam_miktarinew2=line[positionoflira-9:positionoflira-5]
        if 'bin' in zam_miktarinew2: #bu if blogunu 2 bin 123 lira gibi bir formatta verilen veriyi okumak için yazdim.
            c = line[positionoflira-10:positionoflira-8].strip()
            try: #bu try except blokunu 2 bin 345 ve bin 234 gibi iki farkli formatla bas edebilmek icin kullandim.
                d = int(c)*1000 + int(line[positionoflira-5:positionoflira].strip()) # bu blok 2 bin 345 gibi bir format icin.
            except: #bu blok bin 234 gibi bir format icin.
                d = 1000 + int(line[positionoflira-5:positionoflira].strip())
            emeklimaas = emeklimaas + d
        elif 'bin' in zam_miktari2:
            s = line[positionoflira-7:positionoflira-5].strip()
            if s.isdigit(): # 2 bin seklinde yarisi rakam yarisi harflerden olusan ifadeleri duzelttim.
                t = int(s)*1000
                emeklimaas = emeklimaas + t
            elif zam_miktari2.strip() == 'bin': #bin kelimesi tek basina kullanildigi durum icin sayi ile 1000'e cevirip zammi uyguladim.
                emeklimaas = emeklimaas + 1000
            else:
                emeklimaas = emeklimaas + int(zam_miktari2.strip())
        else:
            try:
                emeklimaas = emeklimaas + int(zam_miktari2.strip())
            except: # 26 Temmuz 2019'daki emekliye 12 milyar lira haberini except ile eledim. Adamlar öyle ölçüsüz atmislar ki bilgisayarin Ram'i yetmiyor hesaplamaya :)
                pass
    elif 'yüzde' in line and '.' not in line: #zam haberi satirinda yuzde, yuzde isareti ya da nokta geciyorsa mevcut maasa bahsedilen zam oranini uyguladim.
        positionofyuzde= line.find('yüzde') #zam yapilan orana ulasmak icin yuzde kelimesinin satir icindeki pozisyonunu buldum.
        yuzde_miktari = line[positionofyuzde+5:positionofyuzde+7]
        emeklimaas = emeklimaas* (1 + int(yuzde_miktari.strip())/100)
    elif '%' in line and '.' not in line: #zam haberi satirinda yuzde, yuzde isareti ya da nokta geciyorsa mevcut maasa bahsedilen zam oranini uyguladim.
        positionofyuzde2= line.find('%') #zam yapilan orana ulasmak icin yuzde isaretinin satir icindeki pozisyonunu buldum.
        yuzde_miktari2=line[positionofyuzde2+1:positionofyuzde2+2]
        emeklimaas = emeklimaas* (1 + int(yuzde_miktari2.strip())/100)
    elif '.' in line and 'emeklilik' not in line and 'milyon' not in line: #zam haberi satirinda yuzde, yuzde isareti ya da nokta geciyorsa mevcut maasa bahsedilen zam oranini uyguladim.
        positionofnokta = line.find('.')#zam yapilan orana ulasmak icin nokta isaretinin satir icindeki pozisyonunu buldum.
        try: #cift haneli zamlari hesapladim.
            yuzde_miktari3 = line[positionofnokta-2:positionofnokta+3]
            emeklimaas = emeklimaas* (1 + float(yuzde_miktari3.strip())/100)
        except: # tek haneli zamlari hesapladim.
            yuzde_miktari3 = line[positionofnokta-1:positionofnokta+3]
            emeklimaas = emeklimaas* (1 + float(yuzde_miktari3.strip())/100)
    elif 'çift' in line: # cifte maas haberlerinde, cifte maas tek sefere mahsus bir sey oldugundan zam olarak değil ikramiye olarak uyguladim.
        ikramiye = ikramiye + emeklimaas
    print(count,':',emeklimaas,ikramiye) #listeden herhangi bir gün secilip manuel olarak saglamasi yapilabilsin diye her günü ayrı yazdirdim.
print('Emeklinin 31 Aralık 2019 gunu ki maasi: {}'.format(emeklimaas+ikramiye))
program.close()
