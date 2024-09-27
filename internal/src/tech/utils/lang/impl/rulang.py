from tech.utils.lang.langmodel import LanguageModel


class RuLanguageModel(LanguageModel):
    not_owner_error = 'Текущий пользователь не владеет выбранным животным'
    not_judge_error = 'Текущий пользователь не является судьей на выбранной выставке'
    show_result_status_error = 'Нельзя посмотреть результаты: выставка не завершена'
    no_empty_field = 'Ввод не может быть пустым'
    yes = 'Да'
    no = 'Нет'
    out_login = 'Логин (почта): '
    out_password = 'Пароль: '
    role_register_error = 'Пользователь должен быть судьей'
    already_registered_error = 'Запись на выставку уже существует (нельзя записаться дважды)'
    not_registered_error = 'Записи на выбранную выставку не было'
    duplicate_error = 'Джекпот 777: найдет дупликат (ОШИБКА)'
    foreign_keys_error = 'Ошибка создания (проверьте существование сущностей, на которые введены ссылки)'
    out_deleted_success = 'Запись успешно удалена'
    out_deleted_error = 'Запись не может быть удалена'
    out_deleted_animal_active_shows_error = 'Животное не может быть удалено (есть запись на запущенные выставки)'
    input_invalid = 'Некорректный ввод'
    question_year = '[Ввод даты рождения] Введите год: '
    show_start_success = 'Выставка успешно запущена'
    show_stop_success = 'Выставка успешно завершена'
    unregister_animal_success = 'Животное успешно отписано от выставки'
    register_animal_success = 'Животное успешно записано на выставку'
    unregister_user_success = 'Судья успешно отписан от выставки'
    register_user_success = 'Судья успешно записан на выставку'
    show_start_error_status = 'Выставка не может быть запущена: неподходящий статус'
    show_start_error_no_records_user = 'Выставка не может быть запущена: нет записанных судей'
    show_stop_error_status = 'Выставка не может быть завершена: неподходящий статус'
    show_register_status_error = 'Невозможна запись на выставку: она должна быть в состоянии \'создана\''
    show_unregister_status_error = 'Невозможна отписка от выставки: она должна быть в состоянии \'создана\''
    show_stop_error_not_all_users_scored = 'Выставка не может быть завершена: не все судьи завершили оценивание'
    show_start_error_no_records_animal = 'Выставка не может быть запущена: нет записанных животных'
    question_month = '[Ввод даты рождения] Введите месяц: '
    question_day = '[Ввод даты рождения] Введите день: '
    auth_token_expired = 'Время сессии истекло'
    get_empty_result = 'Нет результатов'
    out_question_name = 'Завершить ввод имени? '
    out_question_animal_id = 'Завершить ввод ID животного? '
    out_question_show_id = 'Завершить ввод ID выставки? '
    out_question_breed_id = 'Завершить ввод ID породы? '
    out_question_species_id = 'Завершить ввод ID вида? '
    out_question_standard_id = 'Завершить ввод ID стандарта? '
    out_question_show_class = 'Завершить ввод класса? '
    out_question_country = 'Завершить ввод страны? '
    out_question_user_id = 'Завершить ввод ID пользователя? '
    out_question_length = 'Завершить ввод длины? '
    out_question_weight = 'Завершить ввод веса? '
    out_question_height = 'Завершить ввод роста? '
    out_question_sex = 'Завершить ввод пола? '
    out_question_has_defects = 'Завершить ввод признака дефектов? '
    out_question_is_multicolor = 'Завершить ввод признака многоцветности? '
    out_question_is_multi_breed = 'Завершить ввод признака мультипородности? '
    question_name = 'Введите имя: '
    question_breed_id = 'Введите ID породы: '
    question_show_id = 'Введите ID выставки: '
    question_animal_id = 'Введите ID животного: '
    question_species_id = 'Введите ID вида: '
    question_standard_id = 'Введите ID стандарта: '
    question_country = 'Введите страну (англ.): '
    question_show_class = 'Введите класс: '
    question_user_id = 'Введите ID пользователя: '
    question_length = 'Введите длину (см): '
    question_weight = 'Введите вес (кг): '
    question_height = 'Введите высоту (см): '
    question_status = 'Введите статус: '
    question_sex = 'Введите пол: '
    question_has_defects = 'Введите признак наличия дефектов (да/нет): '
    question_is_multicolor = 'Введите признак многоцветности (да/нет): '
    question_is_multi_breed = 'Является ли выставка мультипородной? (да/нет): '
    cancel_input = 'Ввод отменен'
    out_id = 'ID'
    out_rank = 'Место'
    question_score_value = 'Введите оценку (1-5): '
    out_question_score_value = 'Завершить ввод оценки? '
    question_animalshow_id = 'Введите ID записи животного на выставку: '
    question_usershow_id = 'Введите ID записи судьи на выставку: '
    out_question_animalshow_id = 'Завершить ввод ID записи животного на выставку? '
    out_question_usershow_id = 'Завершить ввод ID записи судьи на выставку? '
    out_animal_id = 'ID животного'
    out_show_id = 'ID выставки'
    out_breed_id = 'ID породы'
    out_species_id = 'ID вида'
    out_animalshow_id = 'ID записи судьи на выставку: '
    out_usershow_id = 'ID записи животного на выставку: '
    out_standard_id = 'ID стандарта'
    out_name = 'Имя'
    out_is_archived = 'В архиве'
    out_dt_created = 'Дата создания'
    score_create_success = 'Оценка успешно создана'
    user_not_found = 'Пользователь не найден'
    invalid_password = 'Неправильный пароль'
    animal_standard_error = 'Животное не соответствует стандарту выставки'
    animal_not_found = 'Животное не найдено'
    show_not_found = 'Выставка не найдена'
    out_score_value = 'Значение оценки'
    out_show_name = 'Название'
    out_birth_dt = 'Дата рождения'
    out_question_birth_dt = 'Завершить ввод даты рождения? '
    out_user_id = 'ID пользователя'
    out_length = 'Длина'
    out_show_class = 'Класс'
    out_status = 'Статус'
    out_country = 'Страна'
    out_weight = 'Вес'
    out_height = 'Рост'
    out_length_unit = 'см'
    out_weight_unit = 'кг'
    out_height_unit = 'см'
    out_has_defects = 'Наличие дефектов'
    out_is_multicolor = 'Многоцветность'
    out_is_multi_breed = 'Мультипородность'
    out_sex = 'Пол'
    out_sex_female = 'женский'
    out_sex_male = 'мужской'
    out_sex_female_short = 'ж'
    out_sex_male_short = 'м'