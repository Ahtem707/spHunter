"""
Файл - для общей замены сообщений в боте
"""

INCORRECT_INPUT = 'Ошибка ввода! Данной команды не существует!'
START_COMMAND = 'Привет! Это твой персональный помощник чат-бот, по поиску практики, стажировки или работы.' \
                ' Но если ты человек-идеи, то можешь также обращаться ко мне,' \
                ' я помогу найти единомышленников для получения опыта, или давай свою крутую идею, найдем для нее команду.' \

CURRENT_VACANCIES = 'Раздел «Вакансии» содержит информацию о Практиках, Стажировках,' \
                    'и поиска Работы от работодателей-партнеров КИПУ, а также внутренних вакансиях КИПУ.' \
                    'Выберите тип подходящей услуги'

DETAILED = '<b>{}</b> \n\n<b>Тип: </b> {}\n<b>Статус: </b> {}\n<b>Автор: </b> {}\n<b>Команда: </b> {}\n' \
           '<b>Описание: </b> {}\n'
CURRENT_PROJECTS = 'Раздел «Проекты» содержит актуальные проекты КИПУ.'
SUPPORT = 'Перейдите в чат тех. поддержки'
PROFILE = 'Ваш профиль'
PRACTICE_TEMPLATE = '<b>{}</b>\n\n<b>Тип вакансии:</b> {}\n\n<b>Форма занятности:</b> {}\n\n'\
                   '<b>График работы:</b> {}\n\n<b>Адресс вакансии:</b> {}\n\n<b>Описание:</b> {}'

PRACTICES_TEMPLATE = '<b>{}</b>\n{}<b>Форма занятности:</b> {}\n\n'\
                   '<b>Описание:</b> {}'

AUTOMATIC_DISTRIBUTION = 'Что вы хотите сделать? Выберите нужный пункт'

NO_VACANCIES = 'На данный момент вакансий нет.'
NO_PRACTICES = 'На данный момент вакансий на практику нет.'

EDUCTION = 'Укажите уровень получаемого образования, отправив соответствующую кнопку'


COURSES_EDIT = 'Укажите курс обучения, отправив соответствующую цифру' \
          '\n\n' \
          '<b>Нужно выбрать обязатьльно один из курсов</b>'

COURSES = 'Укажите курс обучения, отправив соответствующую цифру'

SPECIALIZATION = '\nУкажите интересующую специализацию, отправив соответствующую цифру/цифры' \
                 ' в случае множественного выбора (1,2,3 и т.п.)'

SPECIALIZATION_TEMPLATE = '{} - {}\n'

SPECIFY = 'Укажите форму занятости'
LIST_PROVEN_PRACTICE = 'Укажите сроки практики'

ERROR_SPECIALIZATION = 'Ошибка ввода!\nНеобходимо вводить числа осуществлять через запятую.' \
                       '\nВведите числа заново!'

ERROR_NUMBER = 'Одно из чисел  выходит за диапозон специализаций'

CANCEL = 'К сожалению, в настоящий момент нет активных вакансий, соответствующих запросу'

MAILING = 'Присылать список открытых вакансий по заданным параметрам'

SAVE_MAILING = 'Рассылка сохранена'

NO_LINK = 'К сожалению, в настоящий момент нет активных вакансий на практику, соответствующих  параметрам  рассылки'

EDIT_MAILING = 'Интервал установлен'

EMPTY_MAILING = 'К сожалению в настоящий момент у вас не установлена рассылка'

DELETE_MAILING = 'Рассылка отменена'

AVAILABLE_MAILING = 'У вас уже имеется рассылка'

NEWSLETTER_OF_VACANCIES = '<b>Рассылка вакансий</b>'

COMPETENCE_ASSESSMENT_MES = 'Оценка компетенций обучающихся проводиться в сотрудничестве с порталом' \
                        ' «Россия – страна возможностей». Чтобы пройти оценку компетенций, необходимо:\n\n -' \
                        ' В своем личном кабинете на портале «Портфолио РГСУ» https://portfolio.rgsu.net/ ' \
                        'нажать «Оценить компетенции», войти в личный кабинет «Россия - страна возможностей».\n\n ' \
                        'По итогам оценки каждый участник получит результаты с расшифровкой, ' \
                        'а также индивидуальные рекомендации по развитию навыков, ' \
                        'которые требуют дополнительного развития в соответствии с профилем обучения.» '

INFO_PORTAL = 't.me/cstrssu'

CALENDAR_INFO = 'Раздел «Карьерные мероприятия» содержит актуальную информацию о мероприятиях' \
                ' с участием работодателей-партнеров РГСУ, а также внутренних карьерных мероприятиях РГСУ.' \
                ' Выберите тип услуги, отправив соответствующую цифру'


TEMPLATES = 'Уровень: {}\n\n Курсы: {}\n\n Специализация: {}\n\n Форма занятности: {}\n\n'

EVENT_TEMP = '<b>{}\n\n{}</b>\n\n{}'
NO_EVENT_TEMP = 'На текущую дату не запланировано мероприятий'

TEMPLATE = '<b>{}</b>\n\n<b>Автор: </b> {}\n<b>Команда: </b> {}\n'
MY_PROFILE = '<b>Имя пользователя:</b> {}\n<b>Логин: </b> {}\n <b>Пол: </b> {}\n<b>Телефон: </b> {}\n' \
             '<b>Дата рождения пользователя: </b> {}\n<b>Валюта: </b> {}'