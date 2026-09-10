import os
import json

base_dir = "/Users/marek-macbook/MBT/nowa strona/MBTWebsite/MBTApp/templates/service/sectors"
os.makedirs(base_dir, exist_ok=True)

sectors = [
    {
        "slug": "konstrukcje-stalowe",
        "title": "Konstrukcje stalowe",
        "hero_desc": "Projektujemy i montujemy wytrzymałe konstrukcje stalowe dla każdego typu obiektów wielkopowierzchniowych.",
        "about_title": "Solidny fundament Twojej inwestycji",
        "about_desc1": "Jako doświadczony wykonawca oferujemy kompleksową realizację konstrukcji stalowych. Od optymalizacji projektu, przez prefabrykację, aż po szybki i bezpieczny montaż na placu budowy.",
        "about_desc2": "Nasze konstrukcje charakteryzują się najwyższą precyzją wykonania i optymalizacją zużycia materiału (Value Engineering), co przekłada się na realne oszczędności bez utraty nośności i bezpieczeństwa.",
        "ch1_title": "Optymalizacja tonażu",
        "ch1_desc": "Dzięki zaawansowanym narzędziom obliczeniowym redukujemy ilość niezbędnej stali, co znacząco obniża koszty inwestycji.",
        "ch2_title": "Prefabrykacja i logistyka",
        "ch2_desc": "Elementy konstrukcyjne są przygotowywane w nowoczesnych wytwórniach, co gwarantuje ich najwyższą jakość.",
        "ch3_title": "Zabezpieczenia antykorozyjne",
        "ch3_desc": "Dobieramy odpowiednie powłoki malarskie i systemy zabezpieczeń, aby stal spełniała rygorystyczne normy.",
        "ch4_title": "Precyzja montażu",
        "ch4_desc": "Nasi wykwalifikowani monterzy dbają o idealne spasowanie elementów, korzystając z zaawansowanego sprzętu geodezyjnego."
    },
    {
        "slug": "biurowce",
        "title": "Biurowce",
        "hero_desc": "Budujemy nowoczesne obiekty biurowe, dostosowane do najwyższych standardów ergonomii i certyfikacji BREEAM.",
        "about_title": "Przestrzeń, która napędza biznes",
        "about_desc1": "Współczesny biurowiec to coś więcej niż tylko miejsce pracy. To wizytówka firmy, narzędzie rekrutacyjne i przestrzeń, która powinna stymulować kreatywność oraz współpracę zespołu.",
        "about_desc2": "Realizujemy obiekty biurowe w standardzie 'pod klucz' (fit-out), dbając o optymalną akustykę, wydajną wentylację oraz najwyższej jakości wykończenia, zachowując przy tym rygorystyczne ramy budżetowe.",
        "ch1_title": "Komfort akustyczny",
        "ch1_desc": "Projektujemy i wdrażamy rozwiązania dźwiękochłonne, które zapewniają ciszę i skupienie w przestrzeniach open-space.",
        "ch2_title": "Jakość powietrza (HVAC)",
        "ch2_desc": "Zaawansowane systemy klimatyzacji i wentylacji, zapewniające stały dostęp do świeżego powietrza bez przeciągów.",
        "ch3_title": "Elastyczność przestrzeni",
        "ch3_desc": "Konstrukcje pozwalające na łatwą rekonfigurację układu pomieszczeń w zależności od zmieniających się potrzeb najemców.",
        "ch4_title": "Certyfikacja BREEAM",
        "ch4_desc": "Wsparcie i realizacja wymogów niezbędnych do uzyskania certyfikatów zrównoważonego budownictwa."
    },
    {
        "slug": "parki-handlowe",
        "title": "Parki handlowe",
        "hero_desc": "Budujemy nowoczesne i wielofunkcyjne parki handlowe dostosowane do dynamicznie zmieniających się potrzeb rynku retail.",
        "about_title": "Funkcjonalność dla najemców i klientów",
        "about_desc1": "Parki handlowe (retail parki) zyskują na popularności dzięki swojej wygodzie i dostępności. Projektujemy i realizujemy te obiekty z naciskiem na maksymalną użyteczność, optymalny przepływ ruchu oraz atrakcyjną wizualnie architekturę zewnętrzną.",
        "about_desc2": "Nasze obiekty komercyjne charakteryzują się elastycznością, co pozwala na bezproblemową adaptację lokali pod różnych operatorów spożywczych, drogeryjnych czy odzieżowych.",
        "ch1_title": "Szybkie tempo realizacji",
        "ch1_desc": "Stosujemy technologie prefabrykowane pozwalające na błyskawiczne wznoszenie konstrukcji, aby Inwestor mógł szybciej komercjalizować obiekt.",
        "ch2_title": "Optymalizacja układu drogowego",
        "ch2_desc": "Dokładne zaplanowanie dróg dojazdowych, stref dostaw i dużych parkingów to klucz do sukcesu parku handlowego.",
        "ch3_title": "Bezproblemowy podział na lokale",
        "ch3_desc": "Systemy instalacyjne i konstrukcyjne są projektowane modułowo, ułatwiając przyszłe zmiany aranżacji i wielkości lokali.",
        "ch4_title": "Reprezentacyjna elewacja",
        "ch4_desc": "Dbamy o nowoczesny design i widoczność logotypów najemców, stosując wysokiej klasy materiały elewacyjne."
    },
    {
        "slug": "magazyny-automatyczne",
        "title": "Magazyny automatyczne",
        "hero_desc": "Nowoczesne przestrzenie magazynowe projektowane specjalnie pod zautomatyzowane i zrobotyzowane systemy logistyczne.",
        "about_title": "Precyzja infrastruktury dla robotyki",
        "about_desc1": "Automatyzacja procesów magazynowych wymaga odpowiednio przygotowanej powłoki budowlanej. Zwykła hala to za mało. Magazyn automatyczny wymaga rygorystycznej tolerancji wykonania posadzek, specyficznego układu konstrukcyjnego i wydajnego zasilania.",
        "about_desc2": "W MBT rozumiemy wymagania, jakie narzucają producenci regałów wysokiego składowania (np. systemy AutoStore czy układnice). Współpracujemy ściśle z integratorami automatyki już na wczesnym etapie projektowania.",
        "ch1_title": "Super płaskie posadzki",
        "ch1_desc": "Wykonujemy posadzki przemysłowe o ekstremalnie rygorystycznych parametrach równości (np. klasa DIN 15185), niezbędne do bezawaryjnej pracy wózków VNA i AGV.",
        "ch2_title": "Brak kolizji instalacyjnych",
        "ch2_desc": "Modelujemy całą siatkę instalacji w technologii BIM, by uniknąć najmniejszych kolizji z poruszającymi się układnicami czy transporterami.",
        "ch3_title": "Stabilne środowisko termiczne",
        "ch3_desc": "Systemy wentylacji i klimatyzacji (HVAC) zapewniające optymalną temperaturę dla elektroniki sterującej oraz przechowywanych towarów.",
        "ch4_title": "Gwarancja nośności",
        "ch4_desc": "Projektujemy wzmocnione płyty fundamentowe zdolne przenieść ogromne naciski punktowe generowane przez kilkudziesięciometrowe regały."
    },
    {
        "slug": "obiekty-uzytecznosci-publicznej",
        "title": "Obiekty użyteczności publicznej",
        "hero_desc": "Realizujemy urzędy, szkoły i budynki użyteczności publicznej z dbałością o najwyższe standardy dostępności i bezpieczeństwa.",
        "about_title": "Budownictwo dla dobra społecznego",
        "about_desc1": "Obiekty użyteczności publicznej muszą służyć pokoleniom, być odporne na intensywną eksploatację i zapewniać najwyższy poziom bezpieczeństwa pożarowego oraz ewakuacyjnego.",
        "about_desc2": "Nasz zespół podchodzi do takich projektów z pełną świadomością ich wagi. Kładziemy ogromny nacisk na jakość stosowanych materiałów, rozwiązania proekologiczne oraz pełną dostępność architektoniczną dla osób z niepełnosprawnościami.",
        "ch1_title": "Bariery architektoniczne",
        "ch1_desc": "Wdrażamy rygorystyczne wytyczne dotyczące dostępności: podjazdy, windy, odpowiednie szerokości ciągów komunikacyjnych i sanitariaty.",
        "ch2_title": "Odporność na intensywne użytkowanie",
        "ch2_desc": "Wykorzystujemy materiały wykończeniowe (posadzki, drzwi, okucia) o podwyższonej klasie ścieralności i trwałości.",
        "ch3_title": "Bezpieczeństwo pożarowe",
        "ch3_desc": "Skrupulatnie instalujemy i testujemy zaawansowane systemy DSO, oddymiania i sygnalizacji pożarowej.",
        "ch4_title": "Akustyka i oświetlenie",
        "ch4_desc": "W szkołach i salach audytoryjnych dbamy o prawidłowy czas pogłosu oraz dostęp do naturalnego światła słonecznego."
    },
    {
        "slug": "obiekty-medyczne-szpitale",
        "title": "Obiekty medyczne (szpitale)",
        "hero_desc": "Specjalistyczne placówki ochrony zdrowia, szpitale i przychodnie budowane z myślą o najwyższych rygorach higienicznych.",
        "about_title": "Budownictwo, które ratuje życie",
        "about_desc1": "Budowa szpitala czy kliniki to jedno z najbardziej wymagających zadań inżynieryjnych. Oprócz tradycyjnych instalacji, obiekt musi zostać wyposażony w sieć gazów medycznych, sale operacyjne w klasie czystości, izolatki oraz specjalistyczne układy zasilania gwarantowanego.",
        "about_desc2": "MBT posiada wiedzę i odpowiednie partnerstwa branżowe, aby sprostać rygorystycznym wytycznym sanitarnym oraz wymaganiom stacji SANEPID. Rozumiemy, że w obiektach medycznych margines błędu wynosi zero.",
        "ch1_title": "Gazy medyczne",
        "ch1_desc": "Kompleksowa koordynacja instalacji rurociągów dla tlenu, podtlenku azotu i sprężonego powietrza medycznego z systemami monitoringu.",
        "ch2_title": "Sale operacyjne (Clean Rooms)",
        "ch2_desc": "Wykonywanie sal w systemach modułowych, z nawiewami laminarnymi i najwyższej klasy higienicznej wykończeniami.",
        "ch3_title": "Zasilanie gwarantowane (IT)",
        "ch3_desc": "Projektowanie niezawodnych układów zasilania z agregatami prądotwórczymi i systemami UPS dla sal operacyjnych i oddziałów IT.",
        "ch4_title": "Osłony przed promieniowaniem",
        "ch4_desc": "Zabezpieczanie ścian i stropów pracowni rentgenowskich (RTG/TK) warstwami ołowiu lub specjalnymi tynkami barytowymi."
    },
    {
        "slug": "mieszkaniowka",
        "title": "Mieszkaniówka",
        "hero_desc": "Inwestycje deweloperskie i osiedla wielorodzinne realizowane terminowo i w wysokim standardzie.",
        "about_title": "Tworzymy przestrzeń do życia",
        "about_desc1": "Generalne wykonawstwo w sektorze mieszkaniowym wymaga doskonałej organizacji pracy, ścisłego przestrzegania harmonogramów oraz wysokiej dbałości o estetykę wykończenia detali budowlanych.",
        "about_desc2": "Współpracujemy z deweloperami, pomagając w optymalizacji kosztów na etapie projektowym i gwarantując bezproblemowe odbiory lokali przez docelowych nabywców. Znamy specyfikę rynku mieszkaniowego i potrafimy się do niej dopasować.",
        "ch1_title": "Optymalizacja PUM",
        "ch1_desc": "Doradzamy rozwiązania konstrukcyjne i instalacyjne, które pozwalają na wygospodarowanie maksymalnej powierzchni użytkowej mieszkalnej.",
        "ch2_title": "Izolacyjność akustyczna",
        "ch2_desc": "Zwracamy szczególną uwagę na dylatacje, grubość i gęstość przegród między lokalowych, zapewniając mieszkańcom prywatność i ciszę.",
        "ch3_title": "Logistyka w gęstej zabudowie",
        "ch3_desc": "Precyzyjnie planujemy dostawy materiałów i pracę żurawi wieżowych w warunkach ciasnych, śródmiejskich działek.",
        "ch4_title": "Wysoki standard części wspólnych",
        "ch4_desc": "Starannie wykańczamy klatki schodowe, hole wejściowe i elewacje, podnosząc prestiż całej inwestycji."
    },
    {
        "slug": "salony-samochodowe",
        "title": "Salony samochodowe i Automotive",
        "hero_desc": "Nowoczesne obiekty sprzedaży i serwisu pojazdów budowane zgodnie z rygorystycznymi standardami corporate identity (CI) marek.",
        "about_title": "Architektura w służbie motoryzacji",
        "about_desc1": "Autoryzowane stacje dealerskie i salony sprzedaży samochodów to obiekty, w których estetyka gra równie ważną rolę co funkcjonalność warsztatowa. Konstrukcja musi pozwalać na maksymalne doświetlenie i ekspozycję pojazdów.",
        "about_desc2": "Mamy doświadczenie w realizacji salonów samochodowych, gdzie każdy detal architektoniczny – od kolorystyki płytek po rodzaj opraw oświetleniowych – musi zostać zatwierdzony i wykonany zgodnie z międzynarodowymi księgami standardów producentów (Brand CI).",
        "ch1_title": "Wielkogabarytowe przeszklenia",
        "ch1_desc": "Montaż ogromnych, bezramowych witryn szklanych o wysokiej izolacyjności termicznej dla doskonałej ekspozycji aut.",
        "ch2_title": "Zaawansowane strefy serwisowe",
        "ch2_desc": "Wykonanie instalacji odciągów spalin, separatorów substancji ropopochodnych oraz stanowisk diagnostycznych i podnośników.",
        "ch3_title": "Rygorystyczne wytyczne marki",
        "ch3_desc": "Ścisła współpraca z audytorami marek samochodowych przy doborze i montażu specyficznych materiałów wykończeniowych.",
        "ch4_title": "Estetyka i wykończenie Premium",
        "ch4_desc": "Najwyższa jakość wykonania posadzek żywicznych, sufitów podwieszanych i oświetlenia ekspozycyjnego w strefie obsługi klienta."
    },
    {
        "slug": "chlodnie-mroznie",
        "title": "Chłodnie, mroźnie i branża spożywcza",
        "hero_desc": "Obiekty przemysłowe z kontrolowaną temperaturą budowane w rygorze najwyższych standardów sanitarnych (HACCP, IFS, BRC).",
        "about_title": "Bezpieczeństwo łańcucha chłodniczego",
        "about_desc1": "Budowa zakładów przetwórstwa spożywczego, chłodni i mroźni wysokiego składowania wymaga unikalnych kompetencji. Termoizolacja i higiena to kluczowe pojęcia podczas realizacji tych inwestycji.",
        "about_desc2": "Zwracamy baczną uwagę na wyeliminowanie mostków termicznych, szczelność gazową (obiekty ULO - Ultra Low Oxygen) oraz zastosowanie materiałów dopuszczonych do bezpośredniego kontaktu z żywnością, w tym posadzek chemoodpornych i antybakteryjnych oraz ścian zmywalnych.",
        "ch1_title": "Ciągłość izolacji termicznej",
        "ch1_desc": "Perfekcyjne wykonanie detali połączeń płyt warstwowych chłodniczych (z grubym rdzeniem PIR) zapobiegające przemarzaniu i kondensacji.",
        "ch2_title": "Zaawansowane instalacje chłodnicze",
        "ch2_desc": "Koordynacja tras dla rurociągów amoniakalnych (NH3) lub systemów na CO2 i odpowiednie przystosowanie maszynowni chłodniczych.",
        "ch3_title": "Podgrzewanie podłoża w mroźni",
        "ch3_desc": "Wykonanie warstw przeciwwysadzinowych i systemów grzewczych pod płytą posadzki, aby uniknąć destrukcji fundamentów przez głębokie mrożenie gruntu.",
        "ch4_title": "Higiena i standardy zmywalności",
        "ch4_desc": "Montaż fasad i przegród gładkich, łatwo zmywalnych, zaoblonych cokołów i specjalistycznych posadzek żywicznych epoksydowych/poliuretanowych."
    },
    {
        "slug": "obiekty-e-commerce",
        "title": "Obiekty dla branży e-commerce",
        "hero_desc": "Sortownie i wielkopowierzchniowe centra dystrybucyjne dostosowane do błyskawicznej logistyki paczek i cross-dockingu.",
        "about_title": "Serce handlu internetowego",
        "about_desc1": "Hale dla branży e-commerce, w tym terminale kurierskie i centra fulfilment, charakteryzują się odmienną specyfiką niż klasyczne magazyny. Mają kształt często przypominający literę 'I', 'L' lub 'T', by zmieścić dziesiątki, a nawet setki doków przeładunkowych.",
        "about_desc2": "Projektujemy i budujemy obiekty przygotowane pod montaż rozległych, wielopoziomowych systemów sorterów i przenośników taśmowych. Dostarczamy hale o wysokim stopniu niezawodności energetycznej, gdzie liczy się każda minuta procesu wysyłki.",
        "ch1_title": "Maksymalizacja liczby doków",
        "ch1_desc": "Budowa hal cross-dockowych (bramy po obu stronach) ułatwiająca szybki przeładunek towaru z TIR-ów do aut kurierskich.",
        "ch2_title": "Infrastruktura pod sortery",
        "ch2_desc": "Precyzyjne przygotowanie posadzek i fundamentów, a także tras kablowych zasilających rozległe instalacje przenośników.",
        "ch3_title": "Zabezpieczenia PPOŻ dla antresol",
        "ch3_desc": "Wielopoziomowe systemy antresol (pick-tower) wymagają szczególnych systemów tryskaczowych (np. in-rack) oraz skomplikowanych dróg ewakuacyjnych.",
        "ch4_title": "Zarządzanie ruchem na zewnątrz",
        "ch4_desc": "Ogromne place manewrowe dla setek aut dostawczych o podwyższonej wytrzymałości nawierzchni (beton wałowany lub kostka wzmocniona)."
    },
    {
        "slug": "centra-badawczo-rozwojowe",
        "title": "Centra Badawczo-Rozwojowe (R&D) i Laboratoria",
        "hero_desc": "Zaawansowane technologicznie obiekty badawcze wymagające ultra-precyzyjnych instalacji i rygorystycznych warunków środowiskowych.",
        "about_title": "Miejsce, gdzie rodzi się innowacja",
        "about_desc1": "Budowa centrum R&D czy laboratorium to wyzwanie inżynieryjne najwyższej próby. Takie obiekty naszpikowane są gęstą siecią instalacji (gazy techniczne, woda demineralizowana, układy odprowadzania kwasów) i wymagają niezwykle stabilnych warunków pracy (temperatura, wilgotność, ciśnienie).",
        "about_desc2": "Jako generalny wykonawca integrujemy skomplikowane układy wentylacji mechanicznej z dygestoriami chemicznymi i zapewniamy kaskadowe różnice ciśnień zapobiegające migracji zanieczyszczeń między strefami badawczymi.",
        "ch1_title": "Precyzyjna kontrola środowiska",
        "ch1_desc": "Wykonanie instalacji HVAC gwarantujących tolerancję temperatury na poziomie +/- 0.5°C i stałą wilgotność niezależnie od pór roku.",
        "ch2_title": "Gazy specjalne i odciągi",
        "ch2_desc": "Budowa bezpiecznych instalacji dla gazów wybuchowych lub toksycznych z zachowaniem norm ATEX oraz lokalnych odciągów stanowiskowych.",
        "ch3_title": "Tłumienie wibracji",
        "ch3_desc": "Tworzenie specjalnych bloków fundamentowych odizolowanych od reszty budynku dla czułych mikroskopów elektronowych czy spektrometrów.",
        "ch4_title": "Pomieszczenia o podwyższonej szczelności",
        "ch4_desc": "Wykończenie wnętrz bezfugowymi posadzkami żywicznymi oraz płytami warstwowymi ściennymi z ukrytym mocowaniem ułatwiającymi dekontaminację."
    },
    {
        "slug": "data-center",
        "title": "Centra Przetwarzania Danych (Data Center)",
        "hero_desc": "Bezpieczne i ultrawydajne energetycznie obiekty dla infrastruktury IT i farm serwerów.",
        "about_title": "Twierdze dla cyfrowego świata",
        "about_desc1": "Serwerownia (Data Center) to budynek, w którym awaria instalacji nie wchodzi w grę. Kluczowym wyzwaniem podczas budowy takiego obiektu jest poprowadzenie ogromnych ilości okablowania oraz instalacji zapewniających potężną moc chłodniczą i podtrzymanie zasilania.",
        "about_desc2": "Nasze obiekty są budowane z zachowaniem najwyższych standardów niezawodności (Tier III, Tier IV). Wykonujemy wzmocnione stropy, zabezpieczenia przed atakami fizycznymi (i EMP) oraz redundantne (podwójne) ścieżki zasilania i klimatyzacji.",
        "ch1_title": "Podłogi techniczne i nośność",
        "ch1_desc": "Projektowanie podniesionych podłóg technicznych zdolnych wytrzymać ogromny ciężar szaf serwerowych i UPS-ów (powyżej 15 kN/m2).",
        "ch2_title": "Chłodzenie precyzyjne",
        "ch2_desc": "Instalacja systemów chłodu (free cooling, chillery, układy cieczowe) odprowadzających potężne ilości ciepła z urządzeń IT.",
        "ch3_title": "Gaszenie gazem",
        "ch3_desc": "Wykonanie idealnie szczelnych komór serwerowych, pozwalających na szybkie ugaszenie ewentualnego pożaru przy użyciu gazów (np. Inergen), bez uszkodzenia sprzętu.",
        "ch4_title": "Zasilanie redundantne",
        "ch4_desc": "Skomplikowana infrastruktura elektroenergetyczna z wieloma transformatorami, masywnymi generatorami diesla i bateryjnymi UPS-ami."
    },
    {
        "slug": "hale-sportowe",
        "title": "Hale sportowe i obiekty widowiskowe",
        "hero_desc": "Wielofunkcyjne obiekty, areny sportowe i hale zaprojektowane z myślą o masowych wydarzeniach i aktywności fizycznej.",
        "about_title": "Arena pełna emocji",
        "about_desc1": "Hale sportowe, sale gimnastyczne czy baseny to inwestycje wymagające ogromnych wolnych rozpiętości bez podpór pośrednich, co stanowi duże wyzwanie konstruktorskie.",
        "about_desc2": "Budujemy obiekty wykorzystujące potężne dźwigary stalowe lub z drewna klejonego (glulam). Kluczowe znaczenie ma w nich akustyka, bezpieczna ewakuacja tysięcy widzów oraz prawidłowe oświetlenie areny, spełniające rygorystyczne normy transmisyjne dla telewizji.",
        "ch1_title": "Konstrukcje wielonawowe (duża rozpiętość)",
        "ch1_desc": "Montaż potężnych kratownic dachowych pozwalających na uzyskanie ogromnej przestrzeni wolnej od słupów na płycie boiska.",
        "ch2_title": "Doskonała akustyka i oświetlenie",
        "ch2_desc": "Specjalistyczne panele pochłaniające dźwięk (eliminacja pogłosu) i profesjonalne oświetlenie LED bez efektu olśnienia graczy.",
        "ch3_title": "Specjalistyczne nawierzchnie i posadzki",
        "ch3_desc": "Certyfikowane podłogi sportowe (sprężyste, poliuretanowe, parkiety) minimalizujące ryzyko kontuzji zawodników.",
        "ch4_title": "Ewakuacja i bezpieczeństwo tłumów",
        "ch4_desc": "Szerokie ciągi komunikacyjne, odpowiednie systemy oddymiania i dźwiękowe systemy ostrzegawcze (DSO) gwarantujące bezpieczeństwo mas."
    },
    {
        "slug": "obiekty-militarne",
        "title": "Specjalistyczne obiekty dla branży militarnej",
        "hero_desc": "Obiekty zbrojeniowe o podwyższonym rygorze bezpieczeństwa i specjalistycznych wymaganiach konstrukcyjnych i organizacyjnych.",
        "about_title": "Inżynieria pod najwyższym nadzorem",
        "about_desc1": "Realizacja inwestycji dla wojska, służb specjalnych lub zakładów produkcji zbrojeniowej wymaga dostępu do informacji niejawnych, wdrożonych specjalnych procedur (kancelaria tajna) oraz certyfikatów bezpieczeństwa przemysłowego.",
        "about_desc2": "Projektujemy i budujemy strzelnice (w tym zamknięte obiekty balistyczne), magazyny materiałów wybuchowych, hale remontowe sprzętu ciężkiego oraz bunkry dowodzenia. Utrzymujemy pełną dyskrecję i ściśle współpracujemy z nadzorem wojskowym.",
        "ch1_title": "Ochrona balistyczna i przeciwwybuchowa",
        "ch1_desc": "Zastosowanie specjalnych żelbetów o wysokiej wytrzymałości, nasypów oraz kulochwytów, a także przegród redukujących falę uderzeniową.",
        "ch2_title": "Ochrona przed podsłuchem (Tempest)",
        "ch2_desc": "Realizacja pomieszczeń ekranowanych elektromagnetycznie klatkami Faradaya i specjalnymi filtrami zasilania.",
        "ch3_title": "Kontrola dostępu na najwyższym poziomie",
        "ch3_desc": "Integracja zaawansowanych systemów biometrycznych, śluz bezpieczeństwa (mantrap) i skanerów uzbrojenia na etapach wykończeniowych.",
        "ch4_title": "Surowe rygory formalne",
        "ch4_desc": "Prowadzenie budowy z uwzględnieniem obostrzeń dostępu, sprawdzeń pracowników i nadzoru przez Wojskowy Dozór Techniczny (WDT)."
    },
    {
        "slug": "zaklady-recyklingu",
        "title": "Zakłady recyklingu i gospodarka odpadami",
        "hero_desc": "Ekologiczne zakłady przetwarzania i sortowania odpadów oraz nowoczesne instalacje ochrony środowiska.",
        "about_title": "Zrównoważony rozwój i transformacja",
        "about_desc1": "Zakłady gospodarki odpadami (sortownie, kompostownie, zakłady termicznego przekształcania) należą do grona obiektów o najwyższych wymogach pod względem odporności na agresję chemiczną środowiska oraz na zagrożenie pożarowe.",
        "about_desc2": "Jako Generalny Wykonawca posiadamy know-how w budowie instalacji pracujących w warunkach silnie korozyjnych. Integrujemy hermetyczne systemy wentylacyjne z biofiltrami oraz zaawansowane systemy tryskaczowe i pianowe, chroniące obiekt przed szybkim rozwojem pożaru odpadów.",
        "ch1_title": "Odporność korozyjna konstrukcji",
        "ch1_desc": "Stosujemy betony o podwyższonej klasie odporności chemicznej i zbrojenie kompozytowe oraz powłoki chroniące stal przed korozją siarczanową.",
        "ch2_title": "Hermetyzacja i oczyszczanie powietrza",
        "ch2_desc": "Budowa szczelnych hal w podciśnieniu połączonych z potężnymi skruberami i biofiltrami neutralizującymi uciążliwe zapachy (odory).",
        "ch3_title": "Bezkompromisowe systemy PPOŻ",
        "ch3_desc": "Instalacja zaawansowanych działek wodno-pianowych, kamer termowizyjnych wczesnego ostrzegania i ścian wydzielenia pożarowego (REI 240).",
        "ch4_title": "Fundamenty pod maszyny sortujące",
        "ch4_desc": "Projektowanie mocnych, grubych posadzek i boksów oporowych żelbetowych odpornych na uderzenia czerpaków ładowarek kołowych."
    },
    {
        "slug": "centra-handlowe",
        "title": "Centra handlowe",
        "hero_desc": "Przestrzenie komercyjne o rozbudowanej infrastrukturze, łączące funkcje handlowe, rozrywkowe i usługowe.",
        "about_title": "Miejsce tętniące życiem",
        "about_desc1": "Duże centra handlowe to jedne z najbardziej złożonych logistycznie budynków komercyjnych. Wymagają jednoczesnej pracy setek podwykonawców i rygorystycznego trzymania się harmonogramów ze względu na twarde terminy otwarcia dla najemców.",
        "about_desc2": "Projektujemy efektowne pasaże (malle), przeszklone świetliki dachowe, reprezentacyjne strefy food-court oraz rozległe garaże podziemne. Zapewniamy kompleksowy 'tenant coordination', doprowadzając media do setek niezależnych lokali zgodnie z instrukcjami poszczególnych marek.",
        "ch1_title": "Koordynacja najemców (Tenant Coordination)",
        "ch1_desc": "Płynne zarządzanie wymaganiami technicznymi dziesiątek sklepów i punktów gastro w celu ich jednoczesnego uruchomienia.",
        "ch2_title": "Rozbudowane instalacje HVAC i PPOŻ",
        "ch2_desc": "Zaawansowane centrale klimatyzacyjne zapewniające komfort tysiącom klientów oraz gęsta sieć tryskaczy w całym obiekcie.",
        "ch3_title": "Wysokiej klasy architektura wnętrz",
        "ch3_desc": "Prace wykończeniowe obejmujące kamień naturalny, posadzki z żywic szlachetnych, fontanny, ruchome schody oraz wielkogabarytowe świetliki.",
        "ch4_title": "Infrastruktura drogowa i parkingowa",
        "ch4_desc": "Realizacja wielopoziomowych parkingów podziemnych z systemami naprowadzania pojazdów i rozbudowanych układów dróg dojazdowych."
    },
    {
        "slug": "markety",
        "title": "Markety",
        "hero_desc": "Funkcjonalne wolnostojące obiekty handlowe o optymalnym układzie komunikacyjnym dla wygody klientów.",
        "about_title": "Kompaktowa funkcjonalność handlowa",
        "about_desc1": "Markety spożywcze i drogeryjne to obiekty realizowane według wysoce zestandaryzowanych ksiąg projektowych (brandbook) znanych sieci handlowych. Kładzie się tu nacisk na bardzo krótki czas realizacji inwestycji.",
        "about_desc2": "Nasze zespoły budowlane wielokrotnie stawiały obiekty w reżimie 12-16 tygodni 'od wbicia łopaty do towarowania', zapewniając szczelną obudowę płyty warstwowej, posadzki z odpowiednich płytek (np. gres wibracyjny) oraz gotową infrastrukturę chłodniczą.",
        "ch1_title": "Błyskawiczne tempo realizacji",
        "ch1_desc": "Stosowanie gotowych, powtarzalnych konstrukcji stalowych/żelbetowych i sprawdzonych brygad pozwala na oddanie obiektu w kilka miesięcy.",
        "ch2_title": "Wymagania dla lad chłodniczych",
        "ch2_desc": "Precyzyjne przygotowanie kanałów i przepustów w posadzce pod instalacje chłodu i skroplin (freon/CO2).",
        "ch3_title": "Zautomatyzowane strefy dostaw",
        "ch3_desc": "Realizacja cichych i bezkolizyjnych doków rozładunkowych dostosowanych do dostaw miejskich o wczesnych godzinach.",
        "ch4_title": "Energooszczędność",
        "ch4_desc": "Montaż systemów odzysku ciepła z agregatów chłodniczych (wspomaganie ogrzewania sklepu) oraz paneli fotowoltaicznych na dachu."
    },
    {
        "slug": "markety-budowlane",
        "title": "Markety budowlane (DIY)",
        "hero_desc": "Wielkopowierzchniowe obiekty handlowe dostosowane konstrukcyjnie do asortymentu ciężkiego (dom i ogród).",
        "about_title": "Solidna podstawa dla asortymentu DIY",
        "about_desc1": "Hale typu 'Dom i Ogród' (DIY - Do It Yourself) łączą cechy nowoczesnego magazynu wysokiego składowania ze standardami otwartej hali handlowej. Z uwagi na znaczny ciężar oferowanego towaru, najważniejsza jest tu nośność posadzek.",
        "about_desc2": "Oprócz samej hali sprzedaży budujemy także wiaty, półotwarte ogrody zewnętrzne oraz wielkogabarytowe strefy drive-in (odbiór towaru własnym autem). Zwracamy uwagę na intensywne doświetlenie światłem dziennym poprzez świetliki pasmowe, redukując koszty energii dla operatora.",
        "ch1_title": "Ekstremalna nośność posadzek",
        "ch1_desc": "Wykonujemy wytrzymałe posadzki utwardzane powierzchniowo z domieszkami, radzące sobie z obciążeniem palet cegieł i ruchem wózków widłowych.",
        "ch2_title": "Naturalne oświetlenie",
        "ch2_desc": "Instalacja licznych klap dymowych i naświetli dachowych zapewniających dobre odwzorowanie barw i komfort podczas zakupów.",
        "ch3_title": "Integracja stref zewnętrznych",
        "ch3_desc": "Rozbudowana architektura ogrodowa zewnętrzna: specjalne place sprzedaży krzewów, podgrzewane nawierzchnie, wiaty zacieniające.",
        "ch4_title": "Rozległe strefy dostaw TIR",
        "ch4_desc": "Organizacja dużych powierzchni manewrowych o wytrzymałej nawierzchni zdolnych przyjąć dziesiątki ciężarówek dziennie."
    },
    {
        "slug": "sklepy-stacjonarne",
        "title": "Sklepy stacjonarne",
        "hero_desc": "Atrakcyjne wizualnie pawilony i wolnostojące salony handlowe dla różnorodnych branż i marek.",
        "about_title": "Oryginalny design zachęcający do wejścia",
        "about_desc1": "Nie każda inwestycja handlowa to potężne centrum. Budujemy również reprezentacyjne sklepy wolnostojące, tzw. flagowe salony detaliczne, kładąc szczególny nacisk na estetykę zewnętrzną.",
        "about_desc2": "Projektujemy i montujemy innowacyjne fasady (szkło, klinkier, stal kortenowska, kompozyty alucobond), dążąc do wyróżnienia budynku z miejskiego otoczenia i zbudowania silnej tożsamości wizualnej marki.",
        "ch1_title": "Reprezentacyjne elewacje",
        "ch1_desc": "Wykorzystanie nieszablonowych materiałów wykończeniowych, dużych przeszkleń i innowacyjnego oświetlenia architektonicznego z zewnątrz.",
        "ch2_title": "Wykończenie wnętrz Fit-Out",
        "ch2_desc": "Kompleksowa obsługa wewnątrz: sufity rastrowe, posadzki żywiczne lub wielkoformatowe gresy i precyzyjne instalacje teletechniczne.",
        "ch3_title": "Wymagania miejskie",
        "ch3_desc": "Sprawne prowadzenie budów (tzw. plomby lub gęsta zabudowa miejska) z minimalną uciążliwością dla otoczenia.",
        "ch4_title": "Mała retencja",
        "ch4_desc": "Zagospodarowanie zieleni i wprowadzanie rozwiązań ekologicznych, np. zielone dachy (green roofs), podnoszące rangę obiektu."
    },
    {
        "slug": "galerie-handlowe",
        "title": "Galerie handlowe",
        "hero_desc": "Prestiżowe, wielokondygnacyjne obiekty handlowe o unikalnej architekturze i luksusowym wykończeniu wnętrz.",
        "about_title": "Ikony miejskiej architektury",
        "about_desc1": "Galeria handlowa to obiekt, który na trwale definiuje i ożywia tkankę miejską. To potężne, skomplikowane i najdroższe inwestycje komercyjne, z bogatym programem rozrywkowym (kina, siłownie) obok strefy handlowej.",
        "about_desc2": "Posiadamy doświadczenie w zarządzaniu potężnymi kontraktami. Oferujemy kompleksowe Generalne Wykonawstwo od głębokich wykopów (ściany szczelinowe dla parkingów podziemnych), przez potężną konstrukcję żelbetową ze sprężanymi stropami, po finalne, kunsztowne wykończenia części wspólnych.",
        "ch1_title": "Skomplikowane prace ziemne",
        "ch1_desc": "Budowa w centrach miast wymaga zaawansowanych zabezpieczeń wykopów (pale CFA, ścianki szczelne) dla głębokich garaży podziemnych.",
        "ch2_title": "Zaawansowane instalacje centralne",
        "ch2_desc": "Integracja gigantycznych węzłów chłodu/ciepła, agregatów prądotwórczych, tryskaczy i potężnych szachtów instalacyjnych.",
        "ch3_title": "Atrakcje architektoniczne",
        "ch3_desc": "Realizujemy skomplikowane dachy szklane, przestrzenne atria, reprezentacyjne schody i wodospady wewnętrzne.",
        "ch4_title": "Ewakuacja masowa",
        "ch4_desc": "Najwyższy rygor ppoż., tysiące czujników i systemy aktywnego, wydajnego oddymiania gigantycznych kubatur powietrza."
    },
    {
        "slug": "hipermarkety",
        "title": "Hipermarkety",
        "hero_desc": "Wielkie hale sprzedaży detalicznej z rozbudowaną infrastrukturą towarzyszącą, zapleczem produkcyjnym i usługowym.",
        "about_title": "Wielka skala i optymalizacja",
        "about_desc1": "Hipermarkety (powierzchnie sprzedaży powyżej 2500 mkw) łączą w sobie cechy sklepu detalicznego i małej fabryki żywności z własnymi piekarniami i chłodniami wędzarniczymi na zapleczu.",
        "about_desc2": "Projektujemy sprawną infrastrukturę do zarządzania tysiącami klientów dziennie. Od zoptymalizowanego parkingu z systemem odwodnienia, przez szerokie aleje handlowe, po strefy przykasowe. Dbamy o wyjątkową równość i trwałość polerowanej posadzki betonowej o wielotysięcznym metrażu.",
        "ch1_title": "Technologie chłodnicze i mroźnicze",
        "ch1_desc": "Ogromne zintegrowane układy dla setek metrów ciągów mebli chłodniczych wraz z pompami ciepła na dachu.",
        "ch2_title": "Własna 'produkcja' (piekarnie, wędzarnie)",
        "ch2_desc": "Wymagania sanitarne i wentylacyjne dla gorących procesów obróbki żywności na zapleczu hipermarketu.",
        "ch3_title": "Pola parkingowe",
        "ch3_desc": "Rozległe parkingi i drogi ewakuacyjne. Zabezpieczamy odpowiednie zjazdy z dróg publicznych i rygorystyczne odprowadzanie wód opadowych.",
        "ch4_title": "Płyty posadzkowe o wysokich normach",
        "ch4_desc": "Wykonanie lśniących, niepylących, bezspoinowych posadzek przystosowanych do ruchu ciężkich paleciaków i wózków z zakupami."
    },
    {
        "slug": "nieruchomosci-komercyjne",
        "title": "Nieruchomości komercyjne",
        "hero_desc": "Wielofunkcyjne kompleksy mieszkaniowo-usługowe, inwestycje przeznaczone na wynajem i rozwój działalności biznesowej.",
        "about_title": "Maksymalizacja zwrotu z inwestycji (ROI)",
        "about_desc1": "W budowie budynków mixed-use (np. na parterze sklepy, wyżej biura, a na górze mieszkania lub hotel) najważniejsza jest uniwersalność i opłacalność rozwiązań projektowych.",
        "about_desc2": "Jako Generalny Wykonawca stajemy się dla Inwestora partnerem biznesowym. Prowadzimy inżynierię wartości (Value Engineering), dobierając systemy, które są trwałe, energooszczędne i łatwe w serwisowaniu, co zmniejsza późniejsze koszty zarządzania (Facility Management).",
        "ch1_title": "Inżynieria Wartości (Value Engineering)",
        "ch1_desc": "Optymalizujemy materiały i konstrukcję (np. żelbet vs stal), aby zmaksymalizować zysk Inwestora przy zachowaniu jakości.",
        "ch2_title": "Wielofunkcyjność (Mixed-Use)",
        "ch2_desc": "Rygorystyczne dylatacje akustyczne i niezależne piony instalacyjne dla stref hałaśliwych (usługi) i cichych (hotele/mieszkania).",
        "ch3_title": "Krótki czas zwrotu i najmu",
        "ch3_desc": "Szybkie tempo wznoszenia w technologiach prefabrykowanych, pozwalające Inwestorowi na wczesne rozpoczęcie poboru czynszów.",
        "ch4_title": "Oddzielne strefowanie instalacji",
        "ch4_desc": "Doprowadzenie niezależnych układów opomiarowania energii (subliczniki), wentylacji i ciepła dla poszczególnych komercyjnych najemców."
    },
    {
        "slug": "powierzchnie-uslugowo-handlowe",
        "title": "Powierzchnie usługowo-handlowe",
        "hero_desc": "Nowoczesne obiekty i przestrzenie lokalowe (tzw. convenience), elastycznie dopasowane do potrzeb najemców drobnego formatu.",
        "about_title": "Codzienne zakupy, perfekcyjna infrastruktura",
        "about_desc1": "Pasaże usługowe, strip-malle, małe parki handlowe w mniejszych miejscowościach czy dzielnicach. To obiekty budowane z myślą o szybkich, codziennych zakupach. Wyróżnia je wejście do każdego lokalu bezpośrednio z parkingu.",
        "about_desc2": "Projektujemy je tak, by zoptymalizować do maksimum wskaźnik powierzchni GLA (powierzchni najmu) w stosunku do powierzchni całkowitej, eliminując zbędne korytarze i skomplikowane węzły centralne na rzecz prostoty, modułowości i funkcjonalności.",
        "ch1_title": "Maksymalizacja powierzchni najmu (GLA)",
        "ch1_desc": "Projekty optymalizujące kształt działki bez zbędnych, drogich w utrzymaniu części wspólnych dla klientów wewnątrz.",
        "ch2_title": "Modułowość instalacji",
        "ch2_desc": "Wyposażenie każdego lokalu we własne, dachowe pompy ciepła/klimatyzatory (rooftop) dla łatwego niezależnego rozliczania najemców.",
        "ch3_title": "Atrakcyjny szyld i witryny",
        "ch3_desc": "Rozbudowane, wysunięte dachy i ramy elewacyjne stanowiące idealne miejsce pod ekspozycję banerów reklamowych sieci.",
        "ch4_title": "Ergonomia parkingu",
        "ch4_desc": "Zapewnienie maksymalnej liczby miejsc postojowych przed samymi wejściami (krótki dystans od auta do drzwi)."
    },
    {
        "slug": "fabryki",
        "title": "Fabryki",
        "hero_desc": "Kompleksowe, potężne zakłady produkcyjne z innowacyjnymi procesami dla sektora motoryzacyjnego, elektronicznego i meblowego.",
        "about_title": "Silnik krajowego przemysłu",
        "about_desc1": "Zbudować fabrykę, to zbudować obudowę dla precyzyjnie zsynchronizowanej linii produkcyjnej. Generalny Wykonawca musi głęboko zrozumieć technologię i ciąg produkcyjny (od przyjęcia surowca do ekspedycji).",
        "about_desc2": "Budujemy fabryki dla sektora automotive, FMCG oraz branży maszynowej. Zarządzamy kontraktami wymagającymi integracji z zagranicznymi dostawcami maszyn (tzw. Tooling), dla których przygotowujemy rozbudowane fundamenty, kotwy wklejane oraz kanały technologiczne (technologia pits).",
        "ch1_title": "Fundamenty pod linie technologiczne",
        "ch1_desc": "Realizujemy skomplikowane, pogłębione kanały, tory jazdy AGV i bloki oporowe (prasy 1000-tonowe) osadzone na gęstej siatce pali.",
        "ch2_title": "Potężne przydziały mocy (Trafostacje)",
        "ch2_desc": "Budujemy zaawansowaną infrastrukturę wysokiego napięcia, własne rozdzielnie i szynoprzewody zdolne zasilić setki maszyn CNC.",
        "ch3_title": "Posadzki chemoodporne i antyelektrostatyczne (ESD)",
        "ch3_desc": "Dla branży elektronicznej wykonujemy podłogi nie gromadzące ładunków, chroniące cenne procesory na linii montażowej.",
        "ch4_title": "Wymagania suwnicowe",
        "ch4_desc": "Ciężkie konstrukcje stalowe z belkami podsuwnicowymi do transportu 50-tonowych matryc i elementów składowych."
    },
    {
        "slug": "wytwornie",
        "title": "Wytwórnie",
        "hero_desc": "Specjalistyczne obiekty przetwórstwa oraz małej i średniej produkcji dopasowane do unikalnych procesów Inwestora.",
        "about_title": "Wydajność w każdej branży",
        "about_desc1": "Wytwórnia kosmetyków, stacja mieszania chemii budowlanej czy zakład przetwórstwa drewna – każdy proces wymaga unikalnego podejścia. MBT traktuje te zadania indywidualnie.",
        "about_desc2": "W odróżnieniu od zwykłego 'pudełka' magazynowego, przy wytwórniach mamy do czynienia z wielopoziomowymi konstrukcjami (wieże technologiczne), zbiornikami (silosy) na zewnątrz oraz zaawansowanymi strefami zagrożenia wybuchem (ZGW).",
        "ch1_title": "Strefy Ex (Zagrożenie Wybuchem)",
        "ch1_desc": "Stosowanie specjalnych opraw, instalacji, paneli zrzutowych oraz systemów detekcji przy produkcji z użyciem rozpuszczalników czy pyłów.",
        "ch2_title": "Wielopoziomowe konstrukcje stalowe",
        "ch2_desc": "Budujemy hale ze zintegrowanymi antresolami, pozwalającymi na grawitacyjny zsyp produktów w procesie produkcyjnym.",
        "ch3_title": "Infrastruktura magazynowania surowców",
        "ch3_desc": "Solidne żelbetowe fundamenty pod zewnętrzne stacje silosowe i instalacje rurociągów przesyłowych pneumatycznych do hali.",
        "ch4_title": "Odciągi zapylenia / Filtracja",
        "ch4_desc": "Dla przemysłu ciężkiego, drzewnego oraz chemicznego instalujemy potężne systemy cyklonów odpylających (np. oczyszczanie spalin)."
    },
    {
        "slug": "place-skladowe",
        "title": "Place składowe",
        "hero_desc": "Profesjonalnie utwardzone, zoptymalizowane logistycznie tereny pod wielkogabarytowe i otwarte składowanie materiałów.",
        "about_title": "Logistyka zaczyna się na zewnątrz",
        "about_desc1": "Odpowiednio przygotowany teren wokół hali jest równie ważny co jej wnętrze. Profesjonalny plac składowy to nie po prostu wylany beton. To zaawansowane zadanie inżynieryjne związane z gruntoznawstwem, drenażem i odpowiednim profilem podbudowy.",
        "about_desc2": "Projektujemy nośność nawierzchni pod koła załadowanych naczep, wózków widłowych ciężkich czy sztaplarek kontenerowych (Reach Stackers). Przeprowadzamy zaawansowane procesy stabilizacji gruntu, aby nawierzchnia przetrwała dekady bez koleinowania.",
        "ch1_title": "Stabilizacja gruntów",
        "ch1_desc": "Wymiana gruntów nośnych i wzmocnienie podłoża innowacyjnymi metodami (cementowo-wapiennymi), by uniknąć osiadania i kolein.",
        "ch2_title": "Nawierzchnie z betonu wałowanego (RCC)",
        "ch2_desc": "Dla największych obciążeń stosujemy technologie autostradowe – wytrzymałe płyty betonowe niewrażliwe na naciski osi TIRów.",
        "ch3_title": "Odwodnienia i drenaże",
        "ch3_desc": "Precyzyjne wyprofilowanie spadków, przepompownie, rozległe sieci kanalizacji deszczowej ze zbiornikami retencyjnymi pod placem.",
        "ch4_title": "Strefowanie i oświetlenie",
        "ch4_desc": "Profesjonalne instalacje wysokich masztów oświetleniowych, wygrodzenia, systemy szlabanów i automatyczne wagi najazdowe dla ciężarówek."
    },
    {
        "slug": "centra-biznesowe",
        "title": "Centra Biznesowe",
        "hero_desc": "Inspirujące, innowacyjne kompleksy biurowe i prestiżowe przestrzenie dla korporacji oraz firm IT.",
        "about_title": "Nowoczesne dzielnice biznesu",
        "about_desc1": "Centrum biznesowe, obejmujące zespół biurowców i punktów usługowych, tworzy zintegrowane środowisko pracy dla tysięcy ludzi. Reprezentacyjna, nowoczesna architektura wpływa pozytywnie na wizerunek firm najemców.",
        "about_desc2": "W MBT realizujemy obiekty biznesowe (tzw. Business Parki) stawiając na szkło, fasady wentylowane, systemy rolet zewnętrznych (żaluzje fasadowe redukujące nagrzewanie) i obfitość naturalnej zieleni, która ma kluczowe znaczenie w nowoczesnym standardzie ESG.",
        "ch1_title": "Fasady słupowo-ryglowe",
        "ch1_desc": "Zaawansowane technicznie ściany osłonowe szklane (aluminium/szkło) gwarantujące piękny wygląd i doskonałą izolacyjność.",
        "ch2_title": "Kluczowa rola ESG",
        "ch2_desc": "Zapewnienie infrastruktury dla cyklistów, instalacje OZE oraz rekuperacja na najwyższym światowym poziomie dla certyfikatów WELL i BREEAM.",
        "ch3_title": "Podłogi podniesione w klasie biurowej",
        "ch3_desc": "Instalacja podłóg technicznych umożliwiających ukrycie tysięcy kilometrów okablowania strukturalnego z pełną elastycznością gniazd (floorbox).",
        "ch4_title": "Przyjazne otoczenie (Landscaping)",
        "ch4_desc": "Aranżacja stref odpoczynku (patio, place wodne, ścieżki, parki) wokół obiektów poprawiające dobrostan pracowników i wizerunek najemcy."
    }
]

template_str = """{% extends '../layout/layout.html' %}
{% load i18n %}

{% block title %}{title} - Generalny Wykonawca | MBT{% endblock %}

{% block content %}

<!-- Hero Section -->
<section class="gw-hero" style="background-image:url('{{ photos.gw_hero }}');">
    <div class="gw-hero-kenburns" style="background-image:url('{{ photos.gw_hero }}');"></div>
    <div class="gw-hero-overlay"></div>
    <div class="container">
        <div class="row">
            <div class="col-lg-9 col-xl-8">
                <div class="gw-hero-content">
                    <span class="gw-hero-badge wow animate__animated animate__fadeInDown">{% trans 'Generalny Wykonawca' %}</span>
                    <h1 class="gw-hero-title wow animate__animated animate__fadeInUp">{% blocktranslate %}{title}{% endblocktranslate %}</h1>
                    <p class="gw-hero-text wow animate__animated animate__fadeInUp" data-wow-delay="0.15s">
                        {% blocktranslate %}{hero_desc}{% endblocktranslate %}
                    </p>
                    <div class="gw-hero-actions wow animate__animated animate__fadeInUp" data-wow-delay="0.3s">
                        <a href="#wyzwania" class="btn mbt-cta">{% trans 'Poznaj nasze rozwiązania' %} <i class="ri-arrow-down-line"></i></a>
                        <a href="{% url 'contact' %}" class="btn gw-btn-outline">{% trans 'Skonsultuj projekt' %} <i class="ri-arrow-right-up-line"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Wprowadzenie -->
<section class="gw-about space-top space-extra-bottom">
    <div class="container">
        <div class="row align-items-center gx-60 gy-40">
            <div class="col-lg-6">
                <div class="gw-about-img-wrap wow animate__animated animate__fadeInLeft">
                    <div class="gw-about-img-main">
                        <img src="{{ photos.gw_3 }}" alt="{title}">
                    </div>
                </div>
            </div>
            <div class="col-lg-6">
                <div class="gw-about-content">
                    <span class="sub-title text-theme wow animate__animated animate__fadeInUp">{% trans 'Precyzja i technologia' %}</span>
                    <h2 class="sec-title wow animate__animated animate__fadeInUp" data-wow-delay="0.1s">{% blocktranslate %}{about_title}{% endblocktranslate %}</h2>
                    <p class="wow animate__animated animate__fadeInUp" data-wow-delay="0.2s" style="color:var(--body-color);font-size:16px;line-height:1.8;">
                        {% blocktranslate %}{about_desc1}{% endblocktranslate %}
                    </p>
                    <p class="wow animate__animated animate__fadeInUp" data-wow-delay="0.3s" style="color:var(--body-color);font-size:16px;line-height:1.8;">
                        {% blocktranslate %}{about_desc2}{% endblocktranslate %}
                    </p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Wyzwania inżynieryjne -->
<section id="wyzwania" class="gw-specs space-top space-extra-bottom" style="background:var(--smoke-color);">
    <div class="container">
        <div class="title-area text-center mb-50">
            <span class="sub-title text-theme wow animate__animated animate__fadeInUp">{% trans 'Rozwiązania szyte na miarę' %}</span>
            <h2 class="sec-title wow animate__animated animate__fadeInUp" data-wow-delay="0.1s">{% blocktranslate %}Kluczowe aspekty <strong>naszej realizacji</strong>{% endblocktranslate %}</h2>
        </div>
        <div class="row gy-30 justify-content-center">
            <div class="col-md-6 col-lg-6">
                <div class="gw-spec-card wow animate__animated animate__fadeInUp">
                    <div class="gw-spec-icon"><i class="ri-check-double-line"></i></div>
                    <div class="gw-spec-body">
                        <h3>{% trans '{ch1_title}' %}</h3>
                        <p>{% trans '{ch1_desc}' %}</p>
                    </div>
                </div>
            </div>
            <div class="col-md-6 col-lg-6">
                <div class="gw-spec-card wow animate__animated animate__fadeInUp" data-wow-delay="0.1s">
                    <div class="gw-spec-icon"><i class="ri-check-double-line"></i></div>
                    <div class="gw-spec-body">
                        <h3>{% trans '{ch2_title}' %}</h3>
                        <p>{% trans '{ch2_desc}' %}</p>
                    </div>
                </div>
            </div>
            <div class="col-md-6 col-lg-6">
                <div class="gw-spec-card wow animate__animated animate__fadeInUp" data-wow-delay="0.2s">
                    <div class="gw-spec-icon"><i class="ri-check-double-line"></i></div>
                    <div class="gw-spec-body">
                        <h3>{% trans '{ch3_title}' %}</h3>
                        <p>{% trans '{ch3_desc}' %}</p>
                    </div>
                </div>
            </div>
            <div class="col-md-6 col-lg-6">
                <div class="gw-spec-card wow animate__animated animate__fadeInUp" data-wow-delay="0.3s">
                    <div class="gw-spec-icon"><i class="ri-check-double-line"></i></div>
                    <div class="gw-spec-body">
                        <h3>{% trans '{ch4_title}' %}</h3>
                        <p>{% trans '{ch4_desc}' %}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- CTA -->
<section class="space-top space-extra-bottom overflow-hidden">
    <div class="container text-center">
        <div class="gw-why-card gw-why-card-cta d-inline-block" style="max-width: 800px; padding: 60px;">
            <h3 class="mb-3" style="font-size: 32px;">{% trans 'Gotowy do startu inwestycji?' %}</h3>
            <p style="font-size: 18px; margin-bottom: 30px;">{% trans 'Przejmiemy na siebie cały proces budowlany. Zbudujmy razem Twój nowy obiekt.' %}</p>
            <a href="{% url 'contact' %}" class="btn mbt-cta" style="font-size: 18px; padding: 15px 40px;">
                {% trans 'Skonsultuj swój projekt z inżynierem MBT' %} <i class="ri-arrow-right-up-line"></i>
            </a>
        </div>
    </div>
</section>

<!-- Realizacje -->
<section class="gw-projects space-top space-extra-bottom" style="background:var(--smoke-color);">
    <div class="container">
        <div class="title-area text-center mb-50">
            <span class="sub-title text-theme wow animate__animated animate__fadeInUp">{% trans 'Dowód naszych kompetencji' %}</span>
            <h2 class="sec-title wow animate__animated animate__fadeInUp" data-wow-delay="0.1s">{% blocktranslate %}Ostatnie <strong>realizacje</strong>{% endblocktranslate %}</h2>
        </div>
        <div class="row gy-30">
            {% for p in completed %}
            <div class="col-md-6 col-lg-4">
                <a href="{% url 'realizacjaDetail' p.slug %}" class="gw-project-card wow animate__animated animate__fadeInUp" data-wow-delay="{% cycle '0s' '0.1s' '0.2s' %}">
                    <div class="gw-project-img">
                        <img src="{{ p.hero }}" alt="{{ p.title }}" loading="lazy">
                        <div class="gw-project-overlay">
                            <span class="gw-project-view"><i class="ri-arrow-right-up-line"></i></span>
                        </div>
                    </div>
                    <div class="gw-project-body">
                        <span class="gw-project-tag">{% if p.formula %}{% trans p.formula %}{% else %}{% trans 'Generalne Wykonawstwo' %}{% endif %}</span>
                        <h3>{{ p.title }}</h3>
                    </div>
                </a>
            </div>
            {% endfor %}
        </div>
    </div>
</section>

{% endblock %}
"""

for s in sectors:
    # Safely replace placeholders without messing up django tags
    content = template_str.replace("{title}", s["title"])
    content = content.replace("{hero_desc}", s["hero_desc"])
    content = content.replace("{about_title}", s["about_title"])
    content = content.replace("{about_desc1}", s["about_desc1"])
    content = content.replace("{about_desc2}", s["about_desc2"])
    
    content = content.replace("{ch1_title}", s["ch1_title"])
    content = content.replace("{ch1_desc}", s["ch1_desc"])
    content = content.replace("{ch2_title}", s["ch2_title"])
    content = content.replace("{ch2_desc}", s["ch2_desc"])
    content = content.replace("{ch3_title}", s["ch3_title"])
    content = content.replace("{ch3_desc}", s["ch3_desc"])
    content = content.replace("{ch4_title}", s["ch4_title"])
    content = content.replace("{ch4_desc}", s["ch4_desc"])

    file_path = os.path.join(base_dir, f"{s['slug']}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Wygenerowano {len(sectors)} szablonów.")
