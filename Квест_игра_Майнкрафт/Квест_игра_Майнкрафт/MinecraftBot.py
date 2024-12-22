import telebot
from telebot import types # для указание типов
import config

# Создание экземпляра бота
bot = telebot.TeleBot("7828391225:AAHnjdqUlNDNJF06ffo2hHbqLO8Xcl0pweg") #в скобках токен(ключ) бота

user_data = {}

# Функция, которая вызывается при первом сообщении
@bot.message_handler(commands=['start']) #ОБРАБОТЧИК СООБЩЕНИЯ /START
def start(message):
    if message.chat.id not in user_data:
        user_data[message.chat.id] = {"runZombie": False} # Добавляем пользователя в словарь
    # Отправляем приветственное сообщение и список функций
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #СОЗДАЁМ КЛАВИАТУРУ
    btn1 = types.KeyboardButton("НАЧАТЬ ИГРУ") #так создаются кнопки (в скобках текст)
    markup.add(btn1) #добавляем кнопки на клавиатуру
    bot.send_photo(message.chat.id, open('./images/10.jpeg', 'rb'), caption="""Привет, игрок. Ты попал в квест-игру «Приключение Мистика в Майнкрафте»,
пройдя её ты узнаешь одну интересную и захватывающую историю (а может и нет, никто не знает, ахах).
Нажмите начать игру и скорее в путь.""".format(message.from_user), reply_markup=markup);

@bot.message_handler(content_types=['text']) #ТУТ ОБРАБАТЫВАЕМ СООБЩЕНИЯ ВСЕ КРОМЕ СТАРТА
def func(message):
    if(message.text == "НАЧАТЬ ИГРУ" or message.text == "НАЧАТЬ ИГРУ СНАЧАЛА" or message.text == "НАЧАТЬ ИГРУ СНАЧАЛА"): #обработка когда пишут "НАЧАТЬ ИГРУ"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("ПОЙТИ ИСКАТЬ ДЕРЕВНЮ")
        btn2 = types.KeyboardButton("ДОБЫВАТЬ ДЕРЕВО")
        markup.add(btn1, btn2)
        bot.send_photo(message.chat.id, open('./images/2.jpeg', 'rb'), caption="""Мистик только заспавнивался в этом неизвестном мире. У него нет совершенно никаких вещей,\
он беззащитен перед этим миром. Тебе скорее надо решить его проблему и найти первые вещи для выживания.""".format(message.from_user), reply_markup=markup);


    elif(message.text == "ДОБЫВАТЬ ДЕРЕВО"): #обработка когда пишут "ДОБЫВАТЬ ДЕРЕВО"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("ИДЁМ ДАЛЬШЕ")
        markup.add(btn1)
        bot.send_photo(message.chat.id, open('./images/13.jpeg', 'rb'), caption="""Мистик спокойно добыл дерево и скрафтил первоначальную деревянную броню.""".format(message.from_user), reply_markup=markup);


    elif(message.text == "ПОЙТИ ИСКАТЬ ДЕРЕВНЮ"): #обработка когда пишут "ПОЙТИ ИСКАТЬ ДЕРЕВНЮ"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("УБИТЬ ЗОМБИ")
        btn2 = types.KeyboardButton("УБЕЖАТЬ ОТ ЗОМБИ")
        markup.add(btn1,btn2)
        bot.send_photo(message.chat.id, open('./images/7.jpeg', 'rb'), caption="""Мистик отправился искать деревню через темный лес поблизости
и встретил зомби. Он движется прямого на него, желая съесть мозги. Что ты будешь делать?""".format(message.from_user), reply_markup=markup);


    elif(message.text == "УБЕЖАТЬ ОТ ЗОМБИ"): #обработка когда пишут "УБЕЖАТЬ ОТ ЗОМБИ"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("ИДЁМ ДАЛЬШЕ")
        markup.add(btn1)
        user_data[message.chat.id]["runZombie"] = False
        bot.send_photo(message.chat.id, open('./images/3.jpeg', 'rb'), caption="""Мистик убежал от зомби, нашел деревню и забрал много лута. Теперь у вас есть
каменная броня, железный меч и иглобрюх.""".format(message.from_user), reply_markup=markup);


    elif(message.text == "УБИТЬ ЗОМБИ"): #обработка когда пишут "УБИТЬ ЗОМБИ"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("НАЧАТЬ ИГРУ СНАЧАЛА")
        markup.add(btn1)
        bot.send_photo(message.chat.id, open('./images/4.jpeg', 'rb'), caption="""Мистик полез на зомби без брони и оружия и конечно же погиб.
            Жители деревни нашли его тело без мозгов и создали надгробие подписав «Здесь лежит неизвестный безголовик».""".format(message.from_user), reply_markup=markup);


    elif(message.text == "ИДЁМ ДАЛЬШЕ" or message.text == "ВОЗВРАТ К НАЧАЛУ ВТОРОЙ СЦЕНЫ"): #обработка когда пишут "ИДЁМ ДАЛЬШЕ" (ПЕРЕХОД НА ВТОРУЮ СЦЕНУ)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("ПОЙТИ НАЛЕВО")
        btn2 = types.KeyboardButton("ПОЙТИ НАПРАВО")
        btn3 = types.KeyboardButton("ПОЙТИ ПРЯМО")
        markup.add(btn1, btn2, btn3)
        bot.send_photo(message.chat.id, open('./images/6.jpeg', 'rb'), caption="""Поздравляю, теперь Мистик немного приоделся и готов продолжить свое путешествие.
Ну и конечно он не справился бы без тебя. А ты не так плох как кажешься. Далее вы увидели шахту и 
отправились к ней за драгоценными рудами. Спустившись в нее, вы наткнулись на два туннеля. Один ведет направо, другой налево.""".format(message.from_user), reply_markup=markup);



    elif(message.text == "ПОЙТИ НАЛЕВО"): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("НАЧАТЬ ИГРУ СНАЧАЛА")
        markup.add(btn1)
        bot.send_photo(message.chat.id, open('./images/8.jpeg', 'rb'), caption="""Ты проиграл ведь там были криперы и взорвали Мистика. Так как их было много, а у тебя слабый ПК,
то эта игра глюкнула и тебе надо начать с самого начало игры, 
ахаха!""".format(message.from_user), reply_markup=markup);


    elif(message.text == "ПОЙТИ ПРЯМО"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("ВОЗВРАТ К НАЧАЛУ ВТОРОЙ СЦЕНЫ")
        markup.add(btn1)
        bot.send_photo(message.chat.id, open('./images/12.jpeg', 'rb'), caption="""Ты что дурак?! Я же написал тут два туннеля налево направо. Ты раздражаешь
я отбираю у Мистика железный меч. Выбирай из двух вариантов""".format(message.from_user), reply_markup=markup);


    elif(message.text == "ПОЙТИ НАПРАВО"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("ПРОДОЛЖИТЬ")
        markup.add(btn1)
        bot.send_photo(message.chat.id, open('./images/14.jpg', 'rb'), caption="""Ура, вы нашли кладку алмазов и куча других драгоценных руд.
Теперь мы ультра мега супер БОГАТЫ! Мы продадим алмазы и купим все что захотим! Что же нам делать дальше?""".format(message.from_user), reply_markup=markup);



    
        '''СЦЕНА 3'''

    elif(message.text == "ПРОДОЛЖИТЬ" or message.text == "ВОЗВРАТ К 3 СЦЕНЕ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("ПОЙТИ СНАЧАЛА УБИВАТЬ СКИЛЕТОВ")
        btn2 = types.KeyboardButton("ПОЙТИ СНАЧАЛА ДОБЫВАТЬ НЕЗЕРИТ")
        markup.add(btn1,btn2)
        bot.send_photo(message.chat.id, open('./images/9.jpeg', 'rb'), caption="""После кучи добытых ресурсов ты выгодно вложился в майнкойн и вовремя его продал. Мистик купил алмазную броню,
нужное оружие и решил отправится в АД в крепость за головами визерскилетов и за самой драгоценной
и крепкой рудой – незеритом""".format(message.from_user), reply_markup=markup);


    elif(message.text =="ПОЙТИ СНАЧАЛА УБИВАТЬ СКИЛЕТОВ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("ВОЗВРАТ К 3 СЦЕНЕ")
        markup.add(btn1)
        bot.send_photo(message.chat.id, open('./images/4.jpeg', 'rb'), caption="""Митстик проиграл без незеритовой брони, хахаха""".format(message.from_user), reply_markup=markup);



    elif(message.text =="ПОЙТИ СНАЧАЛА ДОБЫВАТЬ НЕЗЕРИТ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("ПОГНАЛИ ДАЛЬШЕ")
        markup.add(btn1)
        bot.send_photo(message.chat.id, open('./images/15.jpg', 'rb'), caption="""Мистик спокойно добыл незерит, скрафтил незеритовую броню и добыл головы визер скилетов. Поздравляю!""".format(message.from_user), reply_markup=markup);
    

    elif(message.text =="ПОГНАЛИ ДАЛЬШЕ" or message.text == "ВОЗВРАТ К НАЧАЛУ 4 СЦЕНЫ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("АЛМАЗНЫЙ БЛОК")
        btn2 = types.KeyboardButton("НЕЗЕРИТОВЫЙ БЛОК")
        btn3 = types.KeyboardButton("ЗЕМЛЯНОЙ БЛОК")
        markup.add(btn1,btn2,btn3)
        media = [
            types.InputMediaPhoto(open('./images/16.jpg', 'rb'), caption="Алмазный блок"),
            types.InputMediaPhoto(open('./images/17.jpg', 'rb'), caption="Незеритовый блок"),
            types.InputMediaPhoto(open('./images/18.png', 'rb'), caption="Земляной блок"),
        ]
        bot.send_media_group(message.chat.id, media)
        bot.send_message(message.chat.id, text="""Мистик вышел из ада добыв все необходимое для того что бы сделать боса визера
для того что бы добыть звезду энда чтобы он тебя не убил надо закрыть его в коробке какой блок для этого ты выберешь?""", reply_markup=markup) #ДОПИСАТЬ ТЕКСТ




    elif(message.text =="АЛМАЗНЫЙ БЛОК"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("ВОЗВРАТ К НАЧАЛУ 4 СЦЕНЫ")
        markup.add(btn1)
        bot.send_photo(message.chat.id, open('./images/4.jpeg', 'rb'), caption="""Мистик умер ведь Визер его сломал""".format(message.from_user), reply_markup=markup);
     

    elif(message.text =="НЕЗЕРИТОВЫЙ БЛОК"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("ИДЕМ ДАЛЬШЕ")
        markup.add(btn1)
        bot.send_photo(message.chat.id, open('./images/19.jpg', 'rb'), caption="""Мистик убил Визера и добыл звезду Энда. Поздравляю!!!""".format(message.from_user), reply_markup=markup);


    elif(message.text =="ЗЕМЛЯНОЙ БЛОК"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("ВОЗВРАТ К НАЧАЛУ 4 СЦЕНЫ")
        markup.add(btn1)
        bot.send_photo(message.chat.id, open('./images/4.jpeg', 'rb'), caption="""Земляной блок появился у тебя надо головой, а в нем было
250 тысяч тон тротила и ты вместе с Мистиком взлетел на реактивной тяге в небо. Просто начни занаво""".format(message.from_user), reply_markup=markup);


    elif(message.text =="ИДЕМ ДАЛЬШЕ"):
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("НЕЗЕРИТОВУЮ БРОНЮ, НЕЗЕРИТОВЫЙ МЕЧ, ЛУК ЗОЛОТЫЕ ЗАЧАРОВАННЫЕ ЯБЛОКИ И ЩИТ")
        btn2 = types.KeyboardButton("ИЗУМРУДНУЮ БРОНЮ, РУЖЬЁ, ЗОЛОТОЙ ИГЛОБРЮХ")
        markup.add(btn1,btn2)
        bot.send_photo(message.chat.id, open('./images/5.jpeg', 'rb'), caption="""Поздравляем, вы дошли до финала, но сможет ли Мистик одолеть главного босса? Итак, Мистик под твоим руководством,
добыв звезду Энда, подумал, что надо отправляться
в Эндер-мир и убить Эндер-дракона «главного босса игры» и закончить квест-игру. Какой сет брони и оружия возьмешь с собой?""".format(message.from_user), reply_markup=markup);

    elif(message.text =="НЕЗЕРИТОВУЮ БРОНЮ, НЕЗЕРИТОВЫЙ МЕЧ, ЛУК ЗОЛОТЫЕ ЗАЧАРОВАННЫЕ ЯБЛОКИ И ЩИТ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("ВЫБРАТЬ ДОБИВАНИЕ")
        markup.add(btn1)
        bot.send_photo(message.chat.id, open('./images/11.jpeg', 'rb'), caption="""Ты выбрал верно! Дракон не смог пробить незеритовую броню, с помощью лука Мистик взрывал кристалы Энда
и с помощью золотых яблок хорошо восстанавливал хп и вот, дракон пал на землю. Осталось его только добить. Как же ты это сделаешь?""".format(message.from_user), reply_markup=markup);

    elif(message.text =="ИЗУМРУДНУЮ БРОНЮ, РУЖЬЁ, ЗОЛОТОЙ ИГЛОБРЮХ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("НАЧАТЬ ИГРУ СНАЧАЛА")
        markup.add(btn1)
        bot.send_photo(message.chat.id, open('./foto1.jpg', 'rb'), caption="Ты что с ума сошёл? Ты где в майнкрафте видел такое? Ты походу интернет пират. Лови!»".format(message.from_user), reply_markup=markup);

    elif(message.text =="ВЫБРАТЬ ДОБИВАНИЕ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("ФАТАЛИТИ В СТИЛЕ САБЗИРО")
        btn2 = types.KeyboardButton("МОЛИТЬ О ПОЩАДЕ")
        btn3 = types.KeyboardButton("ПРЫГНУТЬ И В ПОЛЕТЕ ВЫСТРЕЛИТЬ ИЗ ЛУКА")
        btn4 = types.KeyboardButton("ВОНЗИТЬ МЕЧ В ЕГО БРЮХО")
        markup.add(btn1,btn2,btn3,btn4)
        bot.send_message(message.chat.id, text="Выбери нужное тебе добивание.", reply_markup=markup)



    elif(message.text =="ФАТАЛИТИ В СТИЛЕ САБЗИРО"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("МОЛИТЬ О ПОЩАДЕ")
        if(user_data[message.chat.id]["runZombie"] == True):
            btn2 = types.KeyboardButton("ВОНЗИТЬ МЕЧ В ЕГО БРЮХО")
            markup.add(btn2)
        markup.add(btn1)
        bot.send_message(message.chat.id, text="""Мистик сколдовал дорожку из-за льда, поскользнулся на ней, выронил все оружие и упал прямо к ногам
вот-вот вставшего на ноги дракона. Твои действия?""", reply_markup=markup)



    elif(message.text =="МОЛИТЬ О ПОЩАДЕ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("СМОТРЕТЬ ВИДЕО")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="""Дракон не стал слушать и съел Мистика выпленув броню, ведь он не переваривает алмазы. Бесславный конец для тебя.
Попробуй начать с начала, ты явно пропустил один судьбоносный предмет, чтобы победить дракона. Ну и зарядись мотивацией, посмотри видео!""", reply_markup=markup)

   

    
    elif(message.text =="СМОТРЕТЬ ВИДЕО"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("ПОЛУЧИТЬ ОТВЕТ")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="https://vk.com/video-11254710_456241594", reply_markup=markup)
        bot.send_message(message.chat.id, text="""УРА. Мистик понимая, что убил главного боса в игре спокойно выдыхает и вы вместе смотрите титры
окончания игры. Молодец, вы прошли этот квест. У тебя вопрос, что же вам будет за это. Вот ответ.""", reply_markup=markup)
        
    elif(message.text =="ВОНЗИТЬ МЕЧ В ЕГО БРЮХО"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("ПОЛУЧИТЬ ОТВЕТ")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Мистик вспомнил, что за пазухой было зелье суперуспеха. Он выпивает его и замечает рядом тот самый железный меч. Он смог отвлечь дракона фразой «Смотри, курица», допрыгнул до меча и вонзил МЕЧ В ЕГО РАНУ В БРЮХО.", reply_markup=markup)
        bot.send_message(message.chat.id, text="УРА. Мистик понимая, что убил главного боса в игре спокойно выдыхает и вы вместе смотрите титры окончания игры. Молодец, вы прошли этот квест. У тебя вопрос, что же вам будет за это. Вот ответ.»", reply_markup=markup)
  
    elif(message.text =="СМОТРЕТЬ ВИДЕО"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("ПОЛУЧИТЬ ОТВЕТ")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="https://vk.com/video585026734_456239589", reply_markup=markup)

    

    
    elif(message.text =="ПРЫГНУТЬ И В ПОЛЕТЕ ВЫСТРЕЛИТЬ ИЗ ЛУКА"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("СПЕТЬ ПЕСЕНКУ, АВОСЬ ПРОСТИТ")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Ты как Джекичан исполнил крутой трюк с криками «ЙА-ЙА-ЙА» и в полете запустил в него стрелу. Но ты не учел, что у Мистика зрение -10 и конечно же он промазал. Дракон успел встать и ударил Мистика хвостом, и тот выронил все оружие. Твои действия?", reply_markup=markup)


    elif(message.text =="СПЕТЬ ПЕСЕНКУ, АВОСЬ ПРОСТИТ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("СМОТРЕТЬ ВИДЕО")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Дракона не впечатлили хриплые потуги мистика спеть песенку. Он съел Мистика, а промазанную стрелу использовал как зубочистку. Мистик стал в ряд с теми, кого победил дракон. Попробуй начать с начала, ты явно пропустил один судьбоносный предмет, чтобы победить дракона. Ну и зарядись мотивацией, посмотри видео!", reply_markup=markup)



    else:
        bot.send_message(message.chat.id, text="На такую команду меня не запрограммировали..")


bot.polling()

