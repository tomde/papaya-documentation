## Bonovacia tlačiareň

Bonovacie tlačiarne sú tlačiarne, na ktoré sa tlačia objednávky - bony. V jednej prevádzke je možné mať ľubovoľný počet bonovacích tlačiarní. Napr. jednu na terase, ďalšiu v kuchyni, na bare... Po inštalácii bonovacích tlačiarní možno každej menu položke určiť, na ktorú bonovaciu tlačiareň sa má tlačiť jej objednávka (viď. sekciu [Editácia menu](../editacia_menu/editacie_menu_na_tablete.html)).

**Typický scenár**: V prevádzke je jedna bonovacia tlačiareň na bare a druhá v kuchyni. Čašník pridá na účet jeden drink a jednu sviečkovú. Bon na prípravu drinku sa vytlačí barmanovi na bare. Bon na prípravu sviečkovej sa vytlačí kuchárovi v kuchyni.

### Inštalácia bonovacej tlačiarne
Inštalácia sa líši v závislosti od [verzie Papaye](../verzie_systemu_papaya/README.html), ktorú používate.

#### Mini verzia
Mini verzia v súčasnosti nepodporuje tlač objednávok na bonovacie tlačiarne. Podporuje iba [tlač fiškálnych dokladov](../periferie/fiskalna_tlaciaren.html).

#### Pro verzia
Bonovacie tlačiarne nastavuje administrátor/prevádzkar vo *Web admine* v menu *Tlačiarne*.

##### Postup pripojenia sieťovej bonovacej tlačiarne

1. Pripojte sieťovú tlačiareň do Wi-Fi routera.
1. Zistite IP adresu tlačiarne. Napr. pre *Epson TM-T20* držte zatlačené tlačidlo *Feed*. Tlačiareň zapnite, tlačidlo *Feed* stále držte zatlačené. Po niekoľkých sekundách sa vytlačí informačný hárok s IP adresou tlačiarne. Postup sa pri iných typoch tlačiarní môže líšiť.
1. Vo *Web admine* v menu Tlačiarne kliknite na tlačítko *Pridať*.
1. Počkajte kým sa vyhľadajú všetky tlačiarne zapojené do siete.
1. Zo zoznamu zvoľte tlačiareň na základe IP adresy.
1. Zadajte názov bonovacej tlačiarne a kliknite na tlačítko *Pridať*. Názov tlačiarne zvoľte taký, aby ste tlačiareň vedeli rozpoznať keď budete určovať ,na ktorú bonovačku sa má tlačiť objednávka menu položky. Typické názvy: Kuchyňa, Terasa, Bar, ...

##### Zoznam podporovaných bonovacích tlačiarní

* [Epson TM-T20](https://pos.epson.com/products/TM-T20IIPOSReceiptPrinter)
* [Bixolon POS Printer](http://www.bixolon.com/html/en/product/product_list.xhtml) - Tlačiarne zatiaľ nie je možné nainštalovať automaticky. Inštalácia si vyžaduje zásah administrátora. V prípade záujmu nás [kontaktujte](mailto: contact@qnd.sk).

#### Oberon verzia
Papaya v tomto prípade slúži ako **Mobilný čašník** pre systém Oberon. Preto je inštalácia a konfigurácia tlačiarní plne v rukách systému [Oberon](http://www.exalogic.sk/oberon/pokladnica-oberon/).
