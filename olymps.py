import sqlite3
conn = sqlite3.connect('olimps.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS olimps(
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

b = ['Олимпиада НТО - программная инженерия финансовых технологий',' Олимпиада НТО - умный город','Олимпиада НТО - большие данные и машинное обучение ','Олимпиада НТО - аэрокосмические системы','Олимпиада НТО - интеллектуальные робототехнические системы','Олимпиада НТО - беспилотные авиационные системы','Олимпиада НТО - технологии беспроводной связи','Олимпиада НТО - интеллектуальные энергетические системы','Олимпиада НТО - искусственный интеллект','Олимпиада НТО - информационная безопасность','Олимпиада НТО - автоматизация бизнес-процессов','Олимпиада НТО - композитные технологии','Олимпиада НТО - анализ космических снимков и геопространственных данных','Олимпиада НТО - водные робототехнические системы','Олимпиада НТО - нейротехнологии и когнитивные науки','Олимпиада НТО - передовые производственные технологии','Олимпиада НТО - спутниковые системы','Олимпиада НТО - автономные транспортные системы','Олимпиада НТО - летающая робототехника']
c = [3,3,2,3,1,2,2,3,3,3,2,3,3,2,2,2,3,3,3]
for i in range(19):
    query = 'INSERT INTO olimps (object,name, level,reg_begin,reg_last,class_begin,class_last) VALUES (?,?,?,?,?,?,?);'
    cur.execute(query, ['Инженерные науки',b[i],c[i],'2021-10-06','202-11-10',5,11]);
b = ['Олимпиада НТО - геномное редактирование','Олимпиада НТО - наносистемы и наноинженерия','Олимпиада НТО - инженерные биологические системы: агробиотехнологии']
c = [3,2,3]
for i in range(3):
    query = 'INSERT INTO olimps (object,name, level,reg_begin,reg_last,class_begin,class_last) VALUES (?,?,?,?,?,?,?);'
    cur.execute(query, ['Естественная наука',b[i],c[i],'2021-10-06','2021-11-10',5,11]);
b = [2,1,1,1,2,1]
a = ['История','Литература','Математика','Биология','Геогрфия','Иностранные языки']
for i in range(6):
    query = 'INSERT INTO olimps (object,name, level,reg_begin,reg_last,class_begin,class_last) VALUES (?,?,?,?,?,?,?);'
    cur.execute(query, [a[i],'Олимпиада «Покори Воробьевы горы!»',b[i],'2021-11-16','2021-12-21',5,11]);

a = ['История','Литература','Математика','Обществознание','Биология','Геогрфия','Право','Информатика','Русский язык','Химия','Физика']
b = [1,1,1,1,1,1,1,1,1,1,2]
for i in range(11):
    query = 'INSERT INTO olimps (object,name, level,reg_begin,reg_last,class_begin,class_last) VALUES (?,?,?,?,?,?,?);'
    cur.execute(query, [a[i],'Олимпиада «Ломоносов»',b[i],'2021-10-05','2021-11-09',5,11]);

a = ['История','Математика','Обществознание','Экономика']
b = [3,3,3,3]
for i in range(4):
    query = 'INSERT INTO olimps (object,name, level,reg_begin,reg_last,class_begin,class_last) VALUES (?,?,?,?,?,?,?);'
    cur.execute(query, [a[i],'Олимпиада «Миссия выполнима. Твое призвание-финансист»',b[i],'2021-10-05','2021-11-09',5,11]);

a = ['Биология','Дизайн','Журналистика','Иностранные языки','Информатика','История','Математика','Обществознание','Право','Русский язык','Физика','Химия','Экономика']
b = [2,1,1,1,1,1,1,1,1,1,3,2,1]
for i in range(13):
    query = 'INSERT INTO olimps (object,name, level,reg_begin,reg_last,class_begin,class_last) VALUES (?,?,?,?,?,?,?);'
    cur.execute(query, [a[i],'Олимпиада «Высшая проба»',b[i],'2021-10-01','2021-11-09',7,11]);

a = ['Информатика','Естественная наука','Химия']
b = [3,3,2]
for i in range(3):
    query = 'INSERT INTO olimps (object,name, level,reg_begin,reg_last,class_begin,class_last) VALUES (?,?,?,?,?,?,?);'
    cur.execute(query, [a[i],'Олимпиада «Гранит науки»',b[i],'2021-11-26','2022-02-24',5,11]);


cur.execute("""INSERT INTO olimps(object,name,level,reg_begin,reg_last,class_begin,class_last)
    VALUES('Химия','Юные таланты',1,'2021-10-15','2021-11-16',9,11);""")
cur.execute("""INSERT INTO olimps(object,name,level,reg_begin,reg_last,class_begin,class_last)
    VALUES('История','Океан знаний',3,'2021-11-1','2022-01-10',10,11);""")
cur.execute("""INSERT INTO olimps(object,name,level,reg_begin,reg_last,class_begin,class_last)
    VALUES('Физика','Наследники Левши','3','2021-12-29','2022-01-24',7,11);""")
cur.execute("""INSERT INTO olimps(object,name,level,reg_begin,reg_last,class_begin,class_last)
    VALUES('География','Юные таланты',1,'2021-11-01','2022-02-02',5,11);""")
for value in cur.execute("SELECT * FROM olimps"):
    print(value)
