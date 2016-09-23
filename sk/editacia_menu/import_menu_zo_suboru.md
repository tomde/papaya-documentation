## Import menu zo súboru

Import menu zo súboru je určený hlavne pre prevádzky, ktoré s Papayou iba začínajú pracovať. Ak už máte menu spísané v súbore (napríklad v Exceli), tak import je tou najrýchlejšou cestou ako vaše menu dostať do Papaye.

**Nedostatky** - v importnom súbore sa v súčasnosti nedá zadefinovať:

* farba menu položky
* farba menu kategórie
* receptúra
* bonovacie miesto (kuchyňa, bar, ap.)

Tieto parametre je však možné nastaviť po importe súboru priamo na tablete alebo cez web.

<iframe src="http://player.vimeo.com/video/110139210" width="500" height="281" style="display:block; margin-left:auto; margin-right:auto;" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

## Formát menu súboru na import
* Súbor obsahuje v každom riadku najviac 7 stĺpcov oddelených bodkočiarkou.
* Súbor môže obsahovať aj komentáre/poznámky ak je na začiatku riadku znak #.
* Kódovanie textu musí byť UTF-8.

**Zoznam stĺpcov (na poradí záleží)**

1. **(Povinný stĺpec)** Názov menu kategórie
1. **(Povinný stĺpec)** Názov menu položky
1. PLU kód
1. Predajné množstvo
1. Predajná merná jednotka (kg - kilogram, g - gram, l - liter, atď.)
1. Predajná cena
1. Popis položky (zobrazuje sa zákazníkovi napríklad v prípade, keď si prezerá vaše menu vo svojom mobile)

**Príklad súboru**

    # --------------------
    # Šišky (tento komentár sa začína znakom #)
    # Nasledovné položky majú aj popis (6. nepovinný stĺpec)

    Šišky;Donuts čokoláda;101;115;g;0.6;Šiška plnená nugátom
    Šišky;Donuts biely;102;60;g;0.6;Šiška s bielou čokoládou
    Šišky;Donuts krém;103;100;g;0.85;Šiška vanilkovým krémom

    # ----------
    # Bežné pečivo
    # Nasledovným položkám popis chýba (6. nepovinný stĺpec)
    Bežné pečivo;Rožok tukový;111;45;g;0.08
    Bežné pečivo;Rožok so soľou a rascou;112;45;g;0.2
    Bežné pečivo;Rožok so syrom;113;50;g;0.2

    ....
