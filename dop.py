import sqlite3
conn = sqlite3.connect('links.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS links(
    name TEXT PRIMORY KEY,
    link TEXT
    );
""")
conn.commit()
cur.execute("""INSERT INTO links(name, link)
    VALUES('История','Книги:Верт Н. История советского государства, Александров В. Н. История русского искусства, Кириллов В. В. Отечественная история в схемах и таблицах. Аудиолекции: Аудиоверсия «История государства Российского» Н. М. Карамзина. ');""")
cur.execute("""INSERT INTO links(name, link)
    VALUES('Математика','Книги: Агаханов Н. Х., Богданов И. И., Кожевников П. А., Подлипский О. К., Терешин Д. А. Всероссийская олимпиада школьников по математике 1993-2009, Кохась К. П., Берлов С. Л., Власова Н.Ю., Петров Ф. В., Солынин А. А., Храбров А. И. Задачи Санкт-Петербургской олимпиады школьников, Акопян А. В. Геометрия в картинках, Прасолов В. В. Задачи по планиметрии. Интернет-ресурсы: https://artofproblemsolving.com/ , https://problems.ru/');""")
conn.commit()
cur.execute("""INSERT INTO links(name, link)
    VALUES('Биология','Книги:Гайтон А., Холл Дж., Медицинская физиология, Рупперт Э. Э. Зоология беспозвоночных. В 4 томах, Ромер А., Парсонс Т. Анатомия позвоночных, Льюин Б. Гены, Клетки. Интернет-ресурсы:https://biomolecula.ru/ ,https://elementy.ru/ ');""")
conn.commit()
cur.execute("""INSERT INTO links(name, link)
    VALUES('География','Книги:Михайлов В. Н., Добровольский А. Д., Добролюбов С. А. Гидрология, Хромов С. П., Петросянц М. А. Метеорология и климатология. Интернет-ресурсы: https://vk.com/geolibrary');""")
conn.commit()



conn = sqlite3.connect('event.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS event(
    event_id INTENGER PRIMORY KEY,
    name TEXT,
    date_begin DATE,
    date_last DATE,
    whre TEXT,
    about TEXT,
    ssilka TEXT
    );
""")
conn.commit()
cur.execute("""INSERT INTO event(event_id,name,date_begin,date_last,whre,about,ssilka)
    VALUES(1,'«Ёлка Победы — 2021»','2021-10-13','2022-05-31','г.Москва','«Елка Победы» – это не просто новогоднее представление в Музее Победы на Поклонной горе, а интерактивная и увлекательная командная игра-квест, во время которой участникам предстоит выполнить секретную миссию и разгадать военные тайны, чтобы оказаться на праздновании победного 1945 года. Это возможность погрузиться в историю, узнать о традициях встречи Нового года в середине ХХ века','https://dobro.ru/event/10099191');""")
conn.commit()
cur.execute("""INSERT INTO event(event_id,name,date_begin,date_last,whre,about,ssilka)
    VALUES(2,'Фестиваль семейного отдыха «Фактория Маркет»','2021-11-27','2021-11-28','г.Москва','пространстве «Бойлерная» арт-квартала «Хлебозавод 9» соберутся небольшие семейные мастерские, которые представят изделия ручной работы: домашний декор, одежду, косметику, украшения, предметы повседневной необходимости и многое другое, в том числе необычные сладости и полезные продукты. Гости фестиваля смогут принять участие в мастер-классах по росписи ткани и лепке из глины, создать собственный флорариум или японскую кокедаму — шарик из мха, на котором растут растения. А маленьких посетителей фестиваля ждёт отдельная увлекательная программа.','https://kudago.com/msk/event/festival-faktoriya-market/');""")
conn.commit()
cur.execute("""INSERT INTO event(event_id,name,date_begin,date_last,whre,about,ssilka)
    VALUES(3,'Фестиваль Matrëshka-Market Fest','2021-12-11','2021-12-12','г.Москва','Ароматные свечи, уютные вязаные вещи, необычные украшения, стильная посуда и элементы декора, милые детские вещи ждут вас на фестивале Matrëshka-Market Fest. Все вещи, которые выставят на продажу на ярмарке, созданы творческими людьми, настоящими мастерами своего дела.','https://kudago.com/msk/event/festival-matrshka-market-fest/');""")
conn.commit()
cur.execute("""INSERT INTO event(event_id,name,date_begin,date_last,whre,about,ssilka)
    VALUES(4,'XV Большой фестиваль мультфильмов','2021-10-28','2021-11-08','г.Москва','Многие помнят, какими яркими и душевными были советские мультфильмы. Но что актуально в данный момент, какие новые работы выпускают ведущие анимационные студии и художники? Посмотреть лучшие работы отечественных и зарубежных авторов можно будет на XV фестивале мультфильмов.','https://kudago.com/msk/event/festival-bolshoj-festival-multfilmov/');""")
conn.commit()


conn = sqlite3.connect('konkyrs.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS konkyrs(
    konkurs_id INTENGER PRIMORY KEY,
    gifts TEXT,
    ssilka TEXT,
    object TEXT,
    name TEXT,
    reg_begin DATE,
    reg_last DATE,
    who INT,
    about TEXT,
    team TEXT
    );
""")
conn.commit()


cur.execute("""INSERT INTO konkyrs(konkurs_id,gifts,ssilka,object,name,reg_begin,reg_last,who,about,team)
    VALUES(1,'Победители и призеры будут награждены дипломами и призами','https://olymp.mephi.ru/junior','Естественная наука','Конкурс научных работ «Юниор»','2021-11-13','2021-12-20',10,'Конкурс проводится ежегодно в два этапа: отборочный и заключительный. Для участия в отборочном этапе необходимо представить жюри тезисы своего исследовательского проекта. Авторы лучших работ объявляются победителями и призерами первого этапа и приглашаются на финал. Он проходит очно в Москве в НИЯУ МИФИ и на региональных площадках. Из числа победителей организаторы формируют команду на конкурс научного и инженерного творчества школьников Intel ISEF.','индивидуальное');""")
conn.commit()

cur.execute("""INSERT INTO konkyrs(konkurs_id,gifts,ssilka,object,name,reg_begin,reg_last,who,about,team)
    VALUES(2,'Победители и призеры будут награждены дипломами и призами','https://olymp.mephi.ru/junior','ИНженерная наука','Конкурс научных работ «Юниор»','2021-11-13','2021-12-20',10,'Конкурс проводится ежегодно в два этапа: отборочный и заключительный. Для участия в отборочном этапе необходимо представить жюри тезисы своего исследовательского проекта. Авторы лучших работ объявляются победителями и призерами первого этапа и приглашаются на финал. Он проходит очно в Москве в НИЯУ МИФИ и на региональных площадках. Из числа победителей организаторы формируют команду на конкурс научного и инженерного творчества школьников Intel ISEF.','индивидуальное');""")
conn.commit()

cur.execute("""INSERT INTO konkyrs(konkurs_id,gifts,ssilka,object,name,reg_begin,reg_last,who,about,team)
    VALUES(3,'Победители и призеры будут награждены дипломами и призами','https://xn--80aaaadhd9alvnnfid3a3d1hrd.xn--p1ai/','Для предпринимателей','Конкурс «Флагман России»','2021-10-07','2021-11-30',30,'Это площадка для обмена опытом и распространения лучших практик, на которой управленцы в сфере образования могут заявить о себе и найти единомышленников. Целью конкурса является выявление и поддержка талантливых управленцев системы образования, обладающих высоким уровнем лидерских качеств. В конкурсе нет ограничений: участвовать в нем могут как опытные сотрудники образовательных организаций, так и имеющие небольшой стаж.','командное');""")
conn.commit()

cur.execute("""INSERT INTO konkyrs(konkurs_id,gifts,ssilka,object,name,reg_begin,reg_last,who,about,team)
    VALUES(4,'Награды для победителей и финалистов: грант на обучение 1 млн рублей, год консультаций топ-менеджеров крупнейших компаний и выдающихся государственных деятелей, возможность стать участником специальной программы развития кадрового управленческого резерва.','https://xn--d1achcanypala0j.xn--p1ai/','Для предпринимателей','Конкурс «Лидеры России»','2021-12-07','2022-01-30',30,'«Лидеры России» — флагманский проект президентской платформы и самый масштабный конкурс для управленцев, не имеющий аналогов в мире. Участники получают возможность пройти комплексную оценку профессиональных компетенций, получить индивидуальный план развития, познакомиться лично с руководителями крупных компаний и вступить в сообщество лучших управленцев.','индивидуальное');""")
conn.commit()

cur.execute("""INSERT INTO konkyrs(konkurs_id,gifts,ssilka,object,name,reg_begin,reg_last,who,about,team)
    VALUES(5,'1 место — 500 долларов, 2 место — 350 долларов, 3 место — 200 долларов. Все участники получат сертификат (электронный).','https://www.livingoceansfoundation.org/education/science-without-borders-challenge/','Творчество','Конкурс рисунка «Наука без границ»','2021-10-31','2022-03-07',10,'К участию приглашаются школьники в возрасте от 11 до 19 лет со всего мира. Принимаются оригинальные художественные работы школьников на тему «От хребта до рифа».','индивидуальное');""")
conn.commit()

cur.execute("""INSERT INTO konkyrs(konkurs_id,gifts,ssilka,object,name,reg_begin,reg_last,who,about,team)
    VALUES(6,'Победители получат дипломы и призы. Активные участники получат сертификаты.','https://alt.ranepa.ru/pressroom/news/startoval_priem_zayavok_na_konkurs_tvorcheskih_rabot_n_6373.html','Творчество','Конкурс творческих работ «На страже закона»','2021-10-30','2022-02-02',10,'Принимаются видеофильмы, плакаты, эссе и научные работы, посвященные:истории образования и развития прокуратуры России в разные исторические периоды, героическим поступкам, совершенным сотрудниками прокуратуры, важным деятелям прокуратуры России','индивидуальное');""")
conn.commit()

cur.execute("""INSERT INTO konkyrs(konkurs_id,gifts,ssilka,object,name,reg_begin,reg_last,who,about,team)
    VALUES(7,'Главный приз — стереомикроскоп SZX7 с цифровой камерой DP27. Приз за лучшую региональную фотографию — вертикальный микроскоп CX23.','https://www.olympus-lifescience.com/en/landing/ioty-2021/','Творчество','Конкурс «Olympus Image of the Year 2021»','2021-10-28','2021-01-31',20,'К участию приглашаются все желающие в возрасте от 18 лет. Принимаются фотографии, сделанные с помощью светового микроскопа на любую тему. Каждый участник может представить до 3 фото.','индивидуальное');""")
conn.commit()

cur.execute("""INSERT INTO konkyrs(konkurs_id,gifts,ssilka,object,name,reg_begin,reg_last,who,about,team)
    VALUES(8,'Победители и призеры будут награждены дипломами и призами','http://www.rgpbz.ru/press-czentr/akczii-i-meropriyatiya/konkursa-tvorcheskix-reshenij-%C2%ABluchshij-art-obekt%C2%BB','Творчество','Конкурс творческих решений для экологических троп','2021-11-1','2022-02-10',10,'Организатор: Государственный природный биосферный заповедник «Ростовский».К участию приглашаются все желающие в возрасте от 12 лет.Принимаются эскизы арт-объектов для обустройства экологических троп «Загадки Манычской долины» и «Лазоревый цветок»','индивидуальное');""")
conn.commit()

cur.execute("""INSERT INTO konkyrs(konkurs_id,gifts,ssilka,object,name,reg_begin,reg_last,who,about,team)
    VALUES(9,'Авторам 12-ти лучших работ получат грамоты и ценные подарки','http://contest.primepress.ru/','Творчество','Конкурс студенческих работ «Сытинское дело»','2021-09-15','2021-12-01',10,'Конкурс посвящен основателю «Первой Образцовой типографии» И. Д. Сытину.','индивидуальное');""")
conn.commit()

cur.execute("""INSERT INTO konkyrs(konkurs_id,gifts,ssilka,object,name,reg_begin,reg_last,who,about,team)
    VALUES(10,'Победитель получит 3 000 евро на производство нового короткометражного фильма.','https://www.max3min.com/','Творчество','Конкурс видеороликов MAX3MIN','2021-10-31','2021-12-13',10,'','индивидуальное');""")
conn.commit()


conn = sqlite3.connect('users.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
    ID INTENGER PRIMORY KEY,
    firstname TEXT,
    surname TEXT,
    age INT,
    class INT
    );
""")
conn.commit()

for value in cur.execute("SELECT * FROM users"):
    print(value)
conn = sqlite3.connect('volonters.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS volonters(
    volonter_id INTENGER PRIMORY KEY,
    object TEXT,
    name TEXT,
    date_begin DATE,
    date_last DATE,
    whre TEXT,
    about TXT,
    ssilka TEXT
    );
""")
conn.commit()
cur.execute("""INSERT INTO volonters(volonter_id,object,name,date_begin,date_last,whre,about,ssilka)
    VALUES(1,'Помощь детям','Волонтёр на очные занятия с ребятами с cиндромом Дауна','2021-10-13','2022-05-31','г.Москва','Дорогие волонтёры, в нашем фонде регулярно проходят занятия очно и на занятиях очень нужны волонтёры, которые смогут помогать педагогам и коммуницировать с ребятами. Нам очень нужны волонтеры, которые смогут приходить регулярно, так будет легче для наших педагогов, да и для подопечных нашего фонда частая смена лиц — это большой стресс. На группы для детей от 7 до 12 лет: По средам с 15:00 до 17:00 — нужно 2 волонтёра, по пятницам с 15:00 до 17:00 — нужно 2 волонтера. На группы для ребят 14+: по вторникам с 16:00 до 18:00 — нужно 2 волонтёра','https://volonter.ru/events/volontyor-na-ochnye-zanyatiya-s-rebyatami-s-cindromom-dauna/');""")
conn.commit()
cur.execute("""INSERT INTO volonters(volonter_id,object,name,date_begin,date_last,whre,about,ssilka)
    VALUES(2,'Помощь детям','Волонтёр-психолог','2020-07-01','2022-07-01','Москва, ул.Клязьминская д.6 к.1','Наш Благотворительный Фонд нуждается в волонтёрах-психологах, для проведения занятий с детьми из неблагополучных семей, и для поддержки людей, попавших в трудную жизненную ситуацию.','https://volonter.ru/events/volontyor-psiholog/');""")
conn.commit()
cur.execute("""INSERT INTO volonters(volonter_id,object,name,date_begin,date_last, whre,about,ssilka)
    VALUES(3,'Помощь детям','Занятия с детьми “Школа Мира”','2021-09-26','2022-03-06','г.Москва, м. Проспект мира','Школа мира — это занятия с детьми из разных стран, которые мы уже три года проводим каждое воскресенье. В Школе мира ребята учатся дружить и помогать друг другу, узнавать больше о городе, в котором живут, и о других странах и культурах, участвуют в праздниках, экскурсиях и в благотворительных проектах.','https://volonter.ru/events/zanyatiya-s-detmi-shkola-mira/');""")
conn.commit()
cur.execute("""INSERT INTO volonters(volonter_id,object,name,date_begin,date_last,whre,about,ssilka)
    VALUES(4,'Помощь взрослым','Волонтёр-психолог','2020-07-01','2022-07-01','Москва, ул.Клязьминская д.6 к.1','Наш Благотворительный Фонд нуждается в волонтёрах-психологах, для проведения занятий с детьми из неблагополучных семей, и для поддержки людей, попавших в трудную жизненную ситуацию.','https://volonter.ru/events/volontyor-psiholog/');""")
conn.commit()
cur.execute("""INSERT INTO volonters(volonter_id,object,name,date_begin,date_last,whre,about,ssilka)
    VALUES(5,'Помощь взрослым','Помочь бедным и бездомным людям','26.09.2021','06.03.2022','Москва, м. Проспект мира и м. Пушкинская','Помочь бездомному человеку может каждый, для этого необязательно быть социальным работником, можно быть просто другом. Приготовить горячую еду и чай для бездомных, угостить ею людей, познакомиться и узнать больше о мире бездомности из первых уст — не так сложно, как может показаться.  Присоединяйтесь!','https://volonter.ru/events/alternativnaya-subbota/');""")
conn.commit()
cur.execute("""INSERT INTO volonters(volonter_id,object,name,date_begin,date_last,whre,about,ssilka)
    VALUES(6,'Помощь взрослым','Помочь в центре социальной поддержки для бездомных людей','2021-09-06','2022-03-06','Москва, метро Цветной бульвар','Дом «Друзей на улице» — первый в России многофункциональный центр для бездомных людей. Здесь можно постирать и высушить одежду, воспользоваться интернетом и телефоном, поискать работу, получить консультацию соцработника и юриста, починить одежду. А главное — это место, где можно отдохнуть, прийти в себя, где каждого ждут, уважают, относятся по-дружески. Трудные ситуации, проблемы, сложности — всего этого много в жизни бездомного человека. Но есть и место, где можно подумать о жизни, отдохнуть, сделать несколько шагов к выходу из сложной ситуации.','https://volonter.ru/events/dom-druzey-na-ulitse/');""")
conn.commit()
cur.execute("""INSERT INTO volonters(volonter_id,object,name,date_begin,date_last,whre,about,ssilka)
    VALUES(7,'Помощь взрослым','Помочь в Центре гуманитарной помощи','2021-09-26','2022-03-06','Москва, м. Проспект Мира','«Человек в Центре» — так называется наш новый проект. Благодаря гранту Президента РФ мы открыли место, где нуждающиеся ЛЮДИ могут как ЛЮДИ выбрать себе одежду. В спокойной обстановке, в тепле и с дружеской помощью, сохранить своё достоинство и выглядеть прилично в повседневной жизни, которая часто меняется в лучшую сторону вслед за внешним видом. Каждому гостю мы даём набор продуктов и гигиенические принадлежности, которых хватит на первое время. В нашем центре есть много работы, которая приносит радость и чувство нужности.','https://volonter.ru/events/chelovek-v-czentre/');""")
conn.commit()
cur.execute("""INSERT INTO volonters(volonter_id,object,name,date_begin,date_last,whre,about,ssilka)
    VALUES(8,'Помощь пожилым','Волонтёр-психолог','2020-07-01','2022-07-01','Москва, ул.Клязьминская д.6 к.1','Наш Благотворительный Фонд нуждается в волонтёрах-психологах, для проведения занятий с детьми из неблагополучных семей, и для поддержки людей, попавших в трудную жизненную ситуацию.','https://volonter.ru/events/volontyor-psiholog/');""")
conn.commit()
cur.execute("""INSERT INTO volonters(volonter_id,object,name,date_begin,date_last,whre,about,ssilka)
    VALUES(9,'Помощь пожилым','Помочь в Центре гуманитарной помощи','2021-09-26','2022-03-06','Москва, м. Проспект Мира','«Человек в Центре» — так называется наш новый проект. Благодаря гранту Президента РФ мы открыли место, где нуждающиеся ЛЮДИ могут как ЛЮДИ выбрать себе одежду. В спокойной обстановке, в тепле и с дружеской помощью, сохранить своё достоинство и выглядеть прилично в повседневной жизни, которая часто меняется в лучшую сторону вслед за внешним видом. Каждому гостю мы даём набор продуктов и гигиенические принадлежности, которых хватит на первое время. В нашем центре есть много работы, которая приносит радость и чувство нужности.','https://volonter.ru/events/chelovek-v-czentre/');""")
conn.commit()
cur.execute("""INSERT INTO volonters(volonter_id,object,name,date_begin,date_last,whre,about,ssilka)
    VALUES(10,'Помощь в защите культурного наследия','Творческий Фестиваль «Парк Тенишевых и Классика»','2021-10-22','2023-07-15','Брянск, Брянская обл., село Хотылёво, парк Усадьбы Тенишевых','Инициативной группой волонтеров Фонда начата работа по изучению и возрождению культурного наследия, связанного с историческим местом «Парком Усадьбы Тенишевых».  В планах группы разработка материалов по объединению исторических фактов связанных с культурой жизнью этих мест с XVII-XX  вв., а также подготовка базового уровня  для возможности проведения  Творческого фестиваля «Парк Тенишевых и Классика».','https://volonter.ru/events/tvorcheskij-festival-park-tenishivyh-i-klassika/');""")
conn.commit()
cur.execute("""INSERT INTO volonters(volonter_id,object,name,date_begin,date_last,whre,about,ssilka)
    VALUES(11,'Помощь в проведении патриотических мероприятий','Волонтеры Службы Розыска','2021-02-22','2025-02-22','Санкт-Петербург, СПб. 4 линия ВО, д.41','Служба Розыска ИНФОРМБЮРО осуществляет поиск родственников солдат, чьи останки найдены поисковыми отрядами.  Нам необходима помощь в поисковой архивной работе.','https://volonter.ru/events/vedenie-sajta-sluzhby-rozyska/');""")
conn.commit()
cur.execute("""INSERT INTO volonters(volonter_id,object,name,date_begin,date_last,whre,about,ssilka)
    VALUES(12,'Помощь в чрезвычайных ситуациях','Короновирус:помощь бездомным людям','2021-09-26','2022-03-06','г. Москва','Во время коронавируса особенно страдают бездомные люди. Мы призваны не проходить мимо и помочь людям в это непростое время. Присоединяйся и ты!','https://volonter.ru/events/koronavirus-2-pomoch-bezdomnym-lyudyam/');""")
conn.commit()
cur.execute("""INSERT INTO volonters(volonter_id,object,name,date_begin,date_last,whre,about,ssilka)
    VALUES(13,'Помощь пожилым','Короновирус:помощь бездомным людям','2021-09-26','2022-03-06','г. Москва','Во время коронавируса особенно страдают бездомные люди. Мы призваны не проходить мимо и помочь людям в это непростое время. Присоединяйся и ты!','https://volonter.ru/events/koronavirus-2-pomoch-bezdomnym-lyudyam/');""")
conn.commit()
cur.execute("""INSERT INTO volonters(volonter_id,object,name,date_begin,date_last,whre,about,ssilka)
    VALUES(14,'Помощь взрослым','Короновирус:помощь бездомным людям','2021-09-26','2022-03-06','г. Москва','Во время коронавируса особенно страдают бездомные люди. Мы призваны не проходить мимо и помочь людям в это непростое время. Присоединяйся и ты!','https://volonter.ru/events/koronavirus-2-pomoch-bezdomnym-lyudyam/');""")
conn.commit()

conn = sqlite3.connect('olimpss.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS olimpss(
    olimp_id INTEGER PRIMORY KEY,
    object TEXT,
    name TEXT,
    level INT,
    reg_begin DATE,
    reg_last DATE,
    class_begin INT,
    class_last INT
    );
""")
conn.commit()
n = 1
b = ['Олимпиада НТО - программная инженерия финансовых технологий',' Олимпиада НТО - умный город','Олимпиада НТО - большие данные и машинное обучение ','Олимпиада НТО - аэрокосмические системы','Олимпиада НТО - интеллектуальные робототехнические системы','Олимпиада НТО - беспилотные авиационные системы','Олимпиада НТО - технологии беспроводной связи','Олимпиада НТО - интеллектуальные энергетические системы','Олимпиада НТО - искусственный интеллект','Олимпиада НТО - информационная безопасность','Олимпиада НТО - автоматизация бизнес-процессов','Олимпиада НТО - композитные технологии','Олимпиада НТО - анализ космических снимков и геопространственных данных','Олимпиада НТО - водные робототехнические системы','Олимпиада НТО - нейротехнологии и когнитивные науки','Олимпиада НТО - передовые производственные технологии','Олимпиада НТО - спутниковые системы','Олимпиада НТО - автономные транспортные системы','Олимпиада НТО - летающая робототехника']
c = [3,3,2,3,1,2,2,3,3,3,2,3,3,2,2,2,3,3,3]
for i in range(19):
    query = 'INSERT INTO olimpss (olimp_id,object,name, level,reg_begin,reg_last,class_begin,class_last) VALUES (?,?,?,?,?,?,?,?);'
    cur.execute(query, [n,'Инженерные науки',b[i],c[i],'2021-10-06','202-11-10',5,11]);
    n+=1
conn.commit()
b = ['Олимпиада НТО - геномное редактирование','Олимпиада НТО - наносистемы и наноинженерия','Олимпиада НТО - инженерные биологические системы: агробиотехнологии']
c = [3,2,3]
for i in range(3):
    query = 'INSERT INTO olimpss (olimp_id,object,name, level,reg_begin,reg_last,class_begin,class_last) VALUES (?,?,?,?,?,?,?,?);'
    cur.execute(query, [n,'Естественная наука',b[i],c[i],'2021-10-06','2021-11-10',5,11]);
    n+=1
conn.commit()
b = [2,1,1,2]
a = ['История','Математика','Биология','География']
for i in range(4):
    query = 'INSERT INTO olimpss (olimp_id,object,name, level,reg_begin,reg_last,class_begin,class_last) VALUES (?,?,?,?,?,?,?,?);'
    cur.execute(query, [n,a[i],'Олимпиада «Покори Воробьевы горы!»',b[i],'2021-11-16','2021-12-21',5,11]);
    n+=1
conn.commit()
a = ['История','Математика','Обществознание','Биология','География','Информатика','Химия','Физика']
b = [1,1,1,1,1,1,1,2]
for i in range(8):
    query = 'INSERT INTO olimpss (olimp_id,object,name, level,reg_begin,reg_last,class_begin,class_last) VALUES (?,?,?,?,?,?,?,?);'
    cur.execute(query, [n,a[i],'Олимпиада «Ломоносов»',b[i],'2021-10-05','2021-11-09',5,11]);
    n+=1
conn.commit()
a = ['История','Математика','Обществознание']
b = [3,3,3]
for i in range(3):
    query = 'INSERT INTO olimpss (olimp_id,object,name, level,reg_begin,reg_last,class_begin,class_last) VALUES (?,?,?,?,?,?,?,?);'
    cur.execute(query, [n,a[i],'Олимпиада «Миссия выполнима. Твое призвание-финансист»',b[i],'2021-10-05','2021-11-09',5,11]);
    n+=1
conn.commit()
a = ['Биология','Информатика','История','Математика','Обществознание','Русский язык','Физика','Химия']
b = [2,1,1,1,1,1,3,2]
for i in range(8):
    query = 'INSERT INTO olimpss (olimp_id,object,name, level,reg_begin,reg_last,class_begin,class_last) VALUES (?,?,?,?,?,?,?,?);'
    cur.execute(query, [n,a[i],'Олимпиада «Высшая проба»',b[i],'2021-10-01','2021-11-09',7,11]);
    n+=1
conn.commit()
a = ['Информатика','Естественная наука','Химия']
b = [3,3,2]
for i in range(3):
    query = 'INSERT INTO olimpss (olimp_id,object,name, level,reg_begin,reg_last,class_begin,class_last) VALUES (?,?,?,?,?,?,?,?);'
    cur.execute(query, [n,a[i],'Олимпиада «Гранит науки»',b[i],'2021-11-26','2022-02-24',5,11]);
    n+=1
conn.commit()
cur.execute("""INSERT INTO olimpss(olimp_id,object,name,level,reg_begin,reg_last,class_begin,class_last)
    VALUES(49,'Химия','Юные таланты',1,'2021-10-15','2021-11-16',9,11);""")
conn.commit()
cur.execute("""INSERT INTO olimpss(olimp_id,object,name,level,reg_begin,reg_last,class_begin,class_last)
    VALUES(50,'История','Океан знаний',3,'2021-11-1','2022-01-10',10,11);""")
conn.commit()
cur.execute("""INSERT INTO olimpss(olimp_id,object,name,level,reg_begin,reg_last,class_begin,class_last)
    VALUES(51,'Физика','Наследники Левши','3','2021-12-29','2022-01-24',7,11);""")
conn.commit()
cur.execute("""INSERT INTO olimpss(olimp_id,object,name,level,reg_begin,reg_last,class_begin,class_last)
    VALUES(52,'География','Юные таланты',1,'2021-11-01','2022-02-02',5,11);""")
conn.commit()


conn = sqlite3.connect('olymp_subjects.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS olymp_subjects(
    olimp_id INTEGER PRIMORY KEY,
    subject_id INTEGER PRIMORY KEY
    );
""")

  
