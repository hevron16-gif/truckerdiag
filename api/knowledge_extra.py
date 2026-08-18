"""
Дополнительная база кодов Weichai / Howo / Shacman.

Источник таблицы: официальный список ЭБУ Weichai на технике Shacman
(SPN/FMI + внутренний P-код + OBD2). Причины и шаги — полевые,
по частоте с китайских и русских разборов. OEM не выдумывать.
"""

from __future__ import annotations

from typing import Any

EXTRA_KNOWLEDGE: list[dict[str, Any]] = [
    {
        "code": "P0045",
        "aliases": ['SPN 1188 FMI 5', '1188/5', 'SPN 1188 FMI 6', '1188/6'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Незамкнутая цепь турбины",
        "description": (
            "Незамкнутая цепь турбины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1188 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Заклинила геометрия VGT / нагар на лопатках", "probability": 40, "oem_part": None},
            {"cause": "Обрыв или КЗ цепи актуатора турбины", "probability": 30, "oem_part": None},
            {"cause": "Утечка патрубков / интеркулера или врёт датчик наддува", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Сравнить boost desired vs actual.",
            "Проверить разъём и питание актуатора (после мойки мотора часто вода).",
            "Осмотреть патрубки и люфт вала турбины."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P0047",
        "aliases": ['SPN 1188 FMI 4', '1188/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание земли турбины",
        "description": (
            "Короткое замыкание земли турбины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1188 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Заклинила геометрия VGT / нагар на лопатках", "probability": 40, "oem_part": None},
            {"cause": "Обрыв или КЗ цепи актуатора турбины", "probability": 30, "oem_part": None},
            {"cause": "Утечка патрубков / интеркулера или врёт датчик наддува", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Сравнить boost desired vs actual.",
            "Проверить разъём и питание актуатора (после мойки мотора часто вода).",
            "Осмотреть патрубки и люфт вала турбины."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P0048",
        "aliases": ['SPN 1188 FMI 3', '1188/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание источника питания турбины",
        "description": (
            "Короткое замыкание источника питания турбины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1188 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Заклинила геометрия VGT / нагар на лопатках", "probability": 40, "oem_part": None},
            {"cause": "Обрыв или КЗ цепи актуатора турбины", "probability": 30, "oem_part": None},
            {"cause": "Утечка патрубков / интеркулера или врёт датчик наддува", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Сравнить boost desired vs actual.",
            "Проверить разъём и питание актуатора (после мойки мотора часто вода).",
            "Осмотреть патрубки и люфт вала турбины."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P0049",
        "aliases": ['SPN 103 FMI 0', '103/0'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Превышение оборотов турбины",
        "description": (
            "Превышение оборотов турбины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 103 FMI 0). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Заклинила геометрия VGT / нагар на лопатках", "probability": 40, "oem_part": None},
            {"cause": "Обрыв или КЗ цепи актуатора турбины", "probability": 30, "oem_part": None},
            {"cause": "Утечка патрубков / интеркулера или врёт датчик наддува", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Сравнить boost desired vs actual.",
            "Проверить разъём и питание актуатора (после мойки мотора часто вода).",
            "Осмотреть патрубки и люфт вала турбины."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P006D",
        "aliases": ['SPN 102 FMI 0', '102/0', 'SPN 102 FMI 1', '102/1'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Сигнал давления впускаемого воздуха верхнего предела выше максимального значения",
        "description": (
            "Сигнал давления впускаемого воздуха верхнего предела выше максимального значения. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 102 FMI 0). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Неисправен датчик наддува / MAP+IAT", "probability": 40, "oem_part": None},
            {"cause": "Окисление разъёма, нет 5В", "probability": 30, "oem_part": None},
            {"cause": "Реальная утечка во впуске", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "На заглушенном моторе MAP ≈ атмосферному.",
            "Проверить 5В/массу/сигнал.",
            "Искать свист патрубков интеркулера."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0071",
        "aliases": ['SPN 171 FMI 2', '171/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неверный сигнал температуры окружающей среды",
        "description": (
            "Неверный сигнал температуры окружающей среды. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 171 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0072",
        "aliases": ['SPN 171 FMI 4', '171/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение датчика температуры окружающей среды ниже минимального предела",
        "description": (
            "Напряжение датчика температуры окружающей среды ниже минимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 171 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0073",
        "aliases": ['SPN 171 FMI 3', '171/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение датчика температуры окружающей среды выше максимального предела",
        "description": (
            "Напряжение датчика температуры окружающей среды выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 171 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0096",
        "aliases": ['SPN 105 FMI 2', '105/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неверная температура впускного воздуха после охлаждения",
        "description": (
            "Неверная температура впускного воздуха после охлаждения. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 105 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв цепи ДТОЖ / окисление разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен датчик ОЖ", "probability": 35, "oem_part": None},
            {"cause": "Реальный перегрев (уровень, вентилятор, радиатор)", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Сверить сканер с механическим термометром на патрубке.",
            "Прозвонить датчик и провод до ЭБУ.",
            "Параллельно проверить уровень ОЖ и вентилятор."
        ],
        "severity": "limited",
        "estimated_time_min": 25,
    },
    {
        "code": "P0097",
        "aliases": ['SPN 105 FMI 4', '105/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Сигнал напряжения датчика температуры впускного воздуха после охлаждения ниже минимальн…",
        "description": (
            "Сигнал напряжения датчика температуры впускного воздуха после охлаждения ниже минимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 105 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв цепи ДТОЖ / окисление разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен датчик ОЖ", "probability": 35, "oem_part": None},
            {"cause": "Реальный перегрев (уровень, вентилятор, радиатор)", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Сверить сканер с механическим термометром на патрубке.",
            "Прозвонить датчик и провод до ЭБУ.",
            "Параллельно проверить уровень ОЖ и вентилятор."
        ],
        "severity": "limited",
        "estimated_time_min": 25,
    },
    {
        "code": "P0098",
        "aliases": ['SPN 105 FMI 3', '105/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Сигнал напряжения датчика температуры впускного воздуха после охлаждения выше максималь…",
        "description": (
            "Сигнал напряжения датчика температуры впускного воздуха после охлаждения выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 105 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв цепи ДТОЖ / окисление разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен датчик ОЖ", "probability": 35, "oem_part": None},
            {"cause": "Реальный перегрев (уровень, вентилятор, радиатор)", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Сверить сканер с механическим термометром на патрубке.",
            "Прозвонить датчик и провод до ЭБУ.",
            "Параллельно проверить уровень ОЖ и вентилятор."
        ],
        "severity": "limited",
        "estimated_time_min": 25,
    },
    {
        "code": "P0099",
        "aliases": ['SPN 105 FMI 19', '105/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка связи CAN сигнала температуры впускного воздуха после охлаждения",
        "description": (
            "Ошибка связи CAN сигнала температуры впускного воздуха после охлаждения. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 105 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "P0100",
        "aliases": ['SPN 132 FMI 11', '132/11', 'SPN 1241 FMI 11', '1241/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка напряжения в расходомере впускного воздуха",
        "description": (
            "Ошибка напряжения в расходомере впускного воздуха. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 132 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Грязный/замасленный расходомер", "probability": 40, "oem_part": None},
            {"cause": "Подсос воздуха после датчика", "probability": 35, "oem_part": None},
            {"cause": "Обрыв/КЗ цепи MAF", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Осмотреть впуск на подсос, воздушный фильтр.",
            "Проверить разъём и опорное напряжение.",
            "Сравнить расход воздуха с оборотами на холостых."
        ],
        "severity": "can_drive",
        "estimated_time_min": 30,
    },
    {
        "code": "P0101",
        "aliases": ['SPN 1694 FMI 15', '1694/15', 'SPN 1694 FMI 17', '1694/17', 'SPN 1694 FMI 16', '1694/16'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Положительный коэффициент расходомера впускного воздуха выше максимального порогового з…",
        "description": (
            "Положительный коэффициент расходомера впускного воздуха выше максимального порогового значения. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1694 FMI 15). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Грязный/замасленный расходомер", "probability": 40, "oem_part": None},
            {"cause": "Подсос воздуха после датчика", "probability": 35, "oem_part": None},
            {"cause": "Обрыв/КЗ цепи MAF", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Осмотреть впуск на подсос, воздушный фильтр.",
            "Проверить разъём и опорное напряжение.",
            "Сравнить расход воздуха с оборотами на холостых."
        ],
        "severity": "can_drive",
        "estimated_time_min": 30,
    },
    {
        "code": "P0102",
        "aliases": ['SPN 132 FMI 4', '132/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Исходный сигнал расходомера воздуха ниже минимального порогового значения",
        "description": (
            "Исходный сигнал расходомера воздуха ниже минимального порогового значения. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 132 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Грязный/замасленный расходомер", "probability": 40, "oem_part": None},
            {"cause": "Подсос воздуха после датчика", "probability": 35, "oem_part": None},
            {"cause": "Обрыв/КЗ цепи MAF", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Осмотреть впуск на подсос, воздушный фильтр.",
            "Проверить разъём и опорное напряжение.",
            "Сравнить расход воздуха с оборотами на холостых."
        ],
        "severity": "can_drive",
        "estimated_time_min": 30,
    },
    {
        "code": "P0103",
        "aliases": ['SPN 132 FMI 2', '132/2', 'SPN 132 FMI 3', '132/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка сигнала аппаратного оснащения датчика расходомера",
        "description": (
            "Ошибка сигнала аппаратного оснащения датчика расходомера. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 132 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Грязный/замасленный расходомер", "probability": 40, "oem_part": None},
            {"cause": "Подсос воздуха после датчика", "probability": 35, "oem_part": None},
            {"cause": "Обрыв/КЗ цепи MAF", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Осмотреть впуск на подсос, воздушный фильтр.",
            "Проверить разъём и опорное напряжение.",
            "Сравнить расход воздуха с оборотами на холостых."
        ],
        "severity": "can_drive",
        "estimated_time_min": 30,
    },
    {
        "code": "P0110",
        "aliases": ['SPN 2898 FMI 5', '2898/5', 'SPN 2898 FMI 6', '2898/6'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Нет нагрузки подогрева впускного воздуха",
        "description": (
            "Нет нагрузки подогрева впускного воздуха. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 2898 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Неисправен датчик наддува / MAP+IAT", "probability": 40, "oem_part": None},
            {"cause": "Окисление разъёма, нет 5В", "probability": 30, "oem_part": None},
            {"cause": "Реальная утечка во впуске", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "На заглушенном моторе MAP ≈ атмосферному.",
            "Проверить 5В/массу/сигнал.",
            "Искать свист патрубков интеркулера."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0112",
        "aliases": ['SPN 2898 FMI 4', '2898/4', 'SPN 172 FMI 1', '172/1', 'SPN 172 FMI 17', '172/17'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание земли подогрева впускного воздуха",
        "description": (
            "Короткое замыкание земли подогрева впускного воздуха. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 2898 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Неисправен датчик наддува / MAP+IAT", "probability": 40, "oem_part": None},
            {"cause": "Окисление разъёма, нет 5В", "probability": 30, "oem_part": None},
            {"cause": "Реальная утечка во впуске", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "На заглушенном моторе MAP ≈ атмосферному.",
            "Проверить 5В/массу/сигнал.",
            "Искать свист патрубков интеркулера."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0116",
        "aliases": ['SPN 110 FMI 17', '110/17', 'SPN 110 FMI 18', '110/18', 'SPN 110 FMI 2', '110/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неправильный сигнал температуры охлаждающей жидкости двигателя в статическом состоянии",
        "description": (
            "Неправильный сигнал температуры охлаждающей жидкости двигателя в статическом состоянии. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 110 FMI 17). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв цепи ДТОЖ / окисление разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен датчик ОЖ", "probability": 35, "oem_part": None},
            {"cause": "Реальный перегрев (уровень, вентилятор, радиатор)", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Сверить сканер с механическим термометром на патрубке.",
            "Прозвонить датчик и провод до ЭБУ.",
            "Параллельно проверить уровень ОЖ и вентилятор."
        ],
        "severity": "limited",
        "estimated_time_min": 25,
    },
    {
        "code": "P0117",
        "aliases": ['SPN 110 FMI 4', '110/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение исходного сигнала температуры охлаждающей жидкости двигателя ниже минимально…",
        "description": (
            "Напряжение исходного сигнала температуры охлаждающей жидкости двигателя ниже минимального порогового значения. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 110 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв цепи ДТОЖ / окисление разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен датчик ОЖ", "probability": 35, "oem_part": None},
            {"cause": "Реальный перегрев (уровень, вентилятор, радиатор)", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Сверить сканер с механическим термометром на патрубке.",
            "Прозвонить датчик и провод до ЭБУ.",
            "Параллельно проверить уровень ОЖ и вентилятор."
        ],
        "severity": "limited",
        "estimated_time_min": 25,
    },
    {
        "code": "P0122",
        "aliases": ['SPN 91 FMI 4', '91/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение педали 1 ниже минимального предела",
        "description": (
            "Напряжение педали 1 ниже минимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 91 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Коррозия разъёма педали (соль, коврик, вода)", "probability": 45, "oem_part": None},
            {"cause": "Неисправен модуль педали (два канала APP разъехались)", "probability": 40, "oem_part": None},
            {"cause": "Нет опорных 5В с ЭБУ", "probability": 15, "oem_part": None}
        ],
        "check_steps": [
            "Считать оба канала APP % — должны расти синхронно.",
            "Проверить 5В, массы и сигнал на разъёме педали.",
            "Не ставить «неоригинал наугад» без проверки проводки."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0123",
        "aliases": ['SPN 91 FMI 3', '91/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение педали 1 выше максимального предела",
        "description": (
            "Напряжение педали 1 выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 91 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Коррозия разъёма педали (соль, коврик, вода)", "probability": 45, "oem_part": None},
            {"cause": "Неисправен модуль педали (два канала APP разъехались)", "probability": 40, "oem_part": None},
            {"cause": "Нет опорных 5В с ЭБУ", "probability": 15, "oem_part": None}
        ],
        "check_steps": [
            "Считать оба канала APP % — должны расти синхронно.",
            "Проверить 5В, массы и сигнал на разъёме педали.",
            "Не ставить «неоригинал наугад» без проверки проводки."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0181",
        "aliases": ['SPN 174 FMI 2', '174/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неверный сигнал температуры топлива",
        "description": (
            "Неверный сигнал температуры топлива. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 174 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0182",
        "aliases": ['SPN 174 FMI 4', '174/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение сигнала датчика температуры топлива ниже минимального значения",
        "description": (
            "Напряжение сигнала датчика температуры топлива ниже минимального значения. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 174 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0183",
        "aliases": ['SPN 174 FMI 3', '174/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение сигнала датчика температуры топлива выше максимального значения",
        "description": (
            "Напряжение сигнала датчика температуры топлива выше максимального значения. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 174 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0194",
        "aliases": ['SPN 520243 FMI 25', '520243/25'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Изменение давления в топливной рампе превосходит максимальный предел допустимой частоты",
        "description": (
            "Изменение давления в топливной рампе превосходит максимальный предел допустимой частоты. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520243 FMI 25). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Засор фильтра / сепаратора или подсос воздуха на всасывании", "probability": 40, "oem_part": None},
            {"cause": "Износ ТНВД / дозирующего клапана, не держит давление", "probability": 30, "oem_part": None},
            {"cause": "Утечка high-pressure контура или льющая форсунка в обратку", "probability": 20, "oem_part": None},
            {"cause": "Врёт датчик давления рампы или окислен разъём", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Сравнить rail desired vs actual на холостых и под нагрузкой.",
            "Заменить фильтры, слить отстой, прокачать, искать пузырьки.",
            "Проверить питание 5В / массу / сигнал датчика рампы.",
            "Тест обратки форсунок и герметичность рампы."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "P0196",
        "aliases": ['SPN 175 FMI 15', '175/15', 'SPN 175 FMI 2', '175/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Сигнал температуры масла выше максимального предела",
        "description": (
            "Сигнал температуры масла выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 175 FMI 15). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Низкий уровень / разжижение масла топливом", "probability": 40, "oem_part": None},
            {"cause": "Неисправен датчик или проводка", "probability": 30, "oem_part": None},
            {"cause": "Реальная неисправность маслосистемы", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Щуп + механический манометр, не верить только лампе.",
            "Проверить разъём датчика на блоке.",
            "При подтверждении низкого давления — не заводить."
        ],
        "severity": "tow",
        "estimated_time_min": 25,
    },
    {
        "code": "P0197",
        "aliases": ['SPN 175 FMI 4', '175/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение сигнала температуры масла ниже минимального предела",
        "description": (
            "Напряжение сигнала температуры масла ниже минимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 175 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Низкий уровень / разжижение масла топливом", "probability": 40, "oem_part": None},
            {"cause": "Неисправен датчик или проводка", "probability": 30, "oem_part": None},
            {"cause": "Реальная неисправность маслосистемы", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Щуп + механический манометр, не верить только лампе.",
            "Проверить разъём датчика на блоке.",
            "При подтверждении низкого давления — не заводить."
        ],
        "severity": "tow",
        "estimated_time_min": 25,
    },
    {
        "code": "P0198",
        "aliases": ['SPN 175 FMI 3', '175/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение сигнала температуры масла выше максимального предела",
        "description": (
            "Напряжение сигнала температуры масла выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 175 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Низкий уровень / разжижение масла топливом", "probability": 40, "oem_part": None},
            {"cause": "Неисправен датчик или проводка", "probability": 30, "oem_part": None},
            {"cause": "Реальная неисправность маслосистемы", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Щуп + механический манометр, не верить только лампе.",
            "Проверить разъём датчика на блоке.",
            "При подтверждении низкого давления — не заводить."
        ],
        "severity": "tow",
        "estimated_time_min": 25,
    },
    {
        "code": "P0204",
        "aliases": ['SPN 1416 FMI 5', '1416/5'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Незамкнутая цепь форсунки 4",
        "description": (
            "Незамкнутая цепь форсунки 4. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1416 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0205",
        "aliases": ['SPN 1417 FMI 5', '1417/5'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Незамкнутая цепь форсунки 5",
        "description": (
            "Незамкнутая цепь форсунки 5. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1417 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0206",
        "aliases": ['SPN 1418 FMI 5', '1418/5'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Незамкнутая цепь форсунки 6",
        "description": (
            "Незамкнутая цепь форсунки 6. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1418 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0219",
        "aliases": ['SPN 1769 FMI 11', '1769/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Превышение скорости двигателя",
        "description": (
            "Превышение скорости двигателя. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1769 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0222",
        "aliases": ['SPN 29 FMI 4', '29/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение педали 2 ниже минимального предела",
        "description": (
            "Напряжение педали 2 ниже минимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 29 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Коррозия разъёма педали (соль, коврик, вода)", "probability": 45, "oem_part": None},
            {"cause": "Неисправен модуль педали (два канала APP разъехались)", "probability": 40, "oem_part": None},
            {"cause": "Нет опорных 5В с ЭБУ", "probability": 15, "oem_part": None}
        ],
        "check_steps": [
            "Считать оба канала APP % — должны расти синхронно.",
            "Проверить 5В, массы и сигнал на разъёме педали.",
            "Не ставить «неоригинал наугад» без проверки проводки."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0223",
        "aliases": ['SPN 29 FMI 3', '29/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение педали 2 выше максимального предела",
        "description": (
            "Напряжение педали 2 выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 29 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Коррозия разъёма педали (соль, коврик, вода)", "probability": 45, "oem_part": None},
            {"cause": "Неисправен модуль педали (два канала APP разъехались)", "probability": 40, "oem_part": None},
            {"cause": "Нет опорных 5В с ЭБУ", "probability": 15, "oem_part": None}
        ],
        "check_steps": [
            "Считать оба канала APP % — должны расти синхронно.",
            "Проверить 5В, массы и сигнал на разъёме педали.",
            "Не ставить «неоригинал наугад» без проверки проводки."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0237",
        "aliases": ['SPN 102 FMI 4', '102/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Сигнал напряжения давления впускаемого воздуха ниже минимального предела",
        "description": (
            "Сигнал напряжения давления впускаемого воздуха ниже минимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 102 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Неисправен датчик наддува / MAP+IAT", "probability": 40, "oem_part": None},
            {"cause": "Окисление разъёма, нет 5В", "probability": 30, "oem_part": None},
            {"cause": "Реальная утечка во впуске", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "На заглушенном моторе MAP ≈ атмосферному.",
            "Проверить 5В/массу/сигнал.",
            "Искать свист патрубков интеркулера."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0238",
        "aliases": ['SPN 102 FMI 3', '102/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Сигнал напряжения давления впускаемого воздуха выше максимального предела",
        "description": (
            "Сигнал напряжения давления впускаемого воздуха выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 102 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Неисправен датчик наддува / MAP+IAT", "probability": 40, "oem_part": None},
            {"cause": "Окисление разъёма, нет 5В", "probability": 30, "oem_part": None},
            {"cause": "Реальная утечка во впуске", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "На заглушенном моторе MAP ≈ атмосферному.",
            "Проверить 5В/массу/сигнал.",
            "Искать свист патрубков интеркулера."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0251",
        "aliases": ['SPN 1442 FMI 2', '1442/2', 'SPN 1442 FMI 5', '1442/5', 'SPN 520243 FMI 0', '520243/0'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Плохое соединение модуля измерения уровня топлива с ECU",
        "description": (
            "Плохое соединение модуля измерения уровня топлива с ECU. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1442 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0252",
        "aliases": ['SPN 1442 FMI 6', '1442/6'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Перегрев модуля измерения уровня топлива",
        "description": (
            "Перегрев модуля измерения уровня топлива. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1442 FMI 6). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0253",
        "aliases": ['SPN 1442 FMI 17', '1442/17', 'SPN 1442 FMI 18', '1442/18', 'SPN 1442 FMI 4', '1442/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание земли верхнего конца модуля измерения уровня топлива",
        "description": (
            "Короткое замыкание земли верхнего конца модуля измерения уровня топлива. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1442 FMI 17). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0254",
        "aliases": ['SPN 1442 FMI 15', '1442/15', 'SPN 1442 FMI 16', '1442/16', 'SPN 1442 FMI 3', '1442/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание источника питания верхнего конца модуля измерения уровня топлива",
        "description": (
            "Короткое замыкание источника питания верхнего конца модуля измерения уровня топлива. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1442 FMI 15). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0261",
        "aliases": ['SPN 1413 FMI 4', '1413/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание нижнего либо верхнего конца форсунки 1",
        "description": (
            "Короткое замыкание нижнего либо верхнего конца форсунки 1. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1413 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0262",
        "aliases": ['SPN 1413 FMI 3', '1413/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание форсунки 1",
        "description": (
            "Короткое замыкание форсунки 1. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1413 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0263",
        "aliases": ['SPN 1413 FMI 11', '1413/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка форсунки 1 (Без определения, просто сохраняется)",
        "description": (
            "Ошибка форсунки 1 (Без определения, просто сохраняется). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1413 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0264",
        "aliases": ['SPN 1414 FMI 4', '1414/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание нижнего либо верхнего конца форсунки 2",
        "description": (
            "Короткое замыкание нижнего либо верхнего конца форсунки 2. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1414 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0265",
        "aliases": ['SPN 1414 FMI 3', '1414/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание форсунки 2",
        "description": (
            "Короткое замыкание форсунки 2. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1414 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0266",
        "aliases": ['SPN 1414 FMI 11', '1414/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка форсунки 2 (Без определения, просто сохраняется)",
        "description": (
            "Ошибка форсунки 2 (Без определения, просто сохраняется). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1414 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0267",
        "aliases": ['SPN 1415 FMI 4', '1415/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание нижнего либо верхнего конца форсунки 3",
        "description": (
            "Короткое замыкание нижнего либо верхнего конца форсунки 3. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1415 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0268",
        "aliases": ['SPN 1415 FMI 3', '1415/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание форсунки 3",
        "description": (
            "Короткое замыкание форсунки 3. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1415 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0269",
        "aliases": ['SPN 1415 FMI 11', '1415/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка форсунки 3 (Без определения, просто сохраняется)",
        "description": (
            "Ошибка форсунки 3 (Без определения, просто сохраняется). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1415 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0270",
        "aliases": ['SPN 1416 FMI 4', '1416/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание нижнего либо верхнего конца форсунки 4",
        "description": (
            "Короткое замыкание нижнего либо верхнего конца форсунки 4. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1416 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0271",
        "aliases": ['SPN 1416 FMI 3', '1416/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание форсунки 4",
        "description": (
            "Короткое замыкание форсунки 4. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1416 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0272",
        "aliases": ['SPN 1416 FMI 11', '1416/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка форсунки 4 (Без определения, просто сохраняется)",
        "description": (
            "Ошибка форсунки 4 (Без определения, просто сохраняется). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1416 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0273",
        "aliases": ['SPN 1417 FMI 4', '1417/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание нижнего либо верхнего конца форсунки 5",
        "description": (
            "Короткое замыкание нижнего либо верхнего конца форсунки 5. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1417 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0274",
        "aliases": ['SPN 1417 FMI 3', '1417/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание форсунки 5",
        "description": (
            "Короткое замыкание форсунки 5. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1417 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0275",
        "aliases": ['SPN 1417 FMI 11', '1417/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка форсунки 5 (Без определения, просто сохраняется)",
        "description": (
            "Ошибка форсунки 5 (Без определения, просто сохраняется). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1417 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0276",
        "aliases": ['SPN 1418 FMI 4', '1418/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание нижнего либо верхнего конца форсунки 6",
        "description": (
            "Короткое замыкание нижнего либо верхнего конца форсунки 6. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1418 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0277",
        "aliases": ['SPN 1418 FMI 3', '1418/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание форсунки 6",
        "description": (
            "Короткое замыкание форсунки 6. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1418 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0278",
        "aliases": ['SPN 1418 FMI 11', '1418/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка форсунки 6 (Без определения, просто сохраняется)",
        "description": (
            "Ошибка форсунки 6 (Без определения, просто сохраняется). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1418 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0279",
        "aliases": ['SPN 84 FMI 0', '84/0'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Скорость превышает масимальный предел",
        "description": (
            "Скорость превышает масимальный предел. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 84 FMI 0). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0336",
        "aliases": ['SPN 4203 FMI 2', '4203/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка сигнала коленвала",
        "description": (
            "Ошибка сигнала коленвала. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4203 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Неисправен датчик CKP или выбит зазор до венца", "probability": 45, "oem_part": None},
            {"cause": "Обрыв / масло в разъёме на картере маховика", "probability": 35, "oem_part": None},
            {"cause": "Повреждён зубчатый венец", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить зазор и стружку на магните датчика.",
            "Прозвонить экранированный провод.",
            "Снять осциллограмму при прокрутке стартером."
        ],
        "severity": "tow",
        "estimated_time_min": 40,
    },
    {
        "code": "P0341",
        "aliases": ['SPN 4201 FMI 2', '4201/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка сигнала распределительного вала",
        "description": (
            "Ошибка сигнала распределительного вала. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4201 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Неисправен датчик распредвала", "probability": 45, "oem_part": None},
            {"cause": "Разъём в масле у клапанной крышки / насоса", "probability": 35, "oem_part": None},
            {"cause": "Сбиты метки ГРМ (реже)", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание/массу/сигнал CMP.",
            "Сравнить синхрон CKP и CMP.",
            "Метки ГРМ — только если оба датчика живые, а фазы уехали."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0381",
        "aliases": ['SPN 626 FMI 5', '626/5', 'SPN 626 FMI 6', '626/6', 'SPN 626 FMI 3', '626/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Нет нагрузки лампы подогрева впускного воздуха",
        "description": (
            "Нет нагрузки лампы подогрева впускного воздуха. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 626 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Неисправен датчик наддува / MAP+IAT", "probability": 40, "oem_part": None},
            {"cause": "Окисление разъёма, нет 5В", "probability": 30, "oem_part": None},
            {"cause": "Реальная утечка во впуске", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "На заглушенном моторе MAP ≈ атмосферному.",
            "Проверить 5В/массу/сигнал.",
            "Искать свист патрубков интеркулера."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0402",
        "aliases": ['SPN 1241 FMI 0', '1241/0'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Прямое отклонение воздушного контроллера превышает верхнее пороговое значение",
        "description": (
            "Прямое отклонение воздушного контроллера превышает верхнее пороговое значение. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1241 FMI 0). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0420",
        "aliases": ['SPN 523004 FMI 0', '523004/0', 'SPN 523004 FMI 15', '523004/15', 'SPN 523004 FMI 16', '523004/16'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Низкая средняя эффективность фактического преобразования SCR",
        "description": (
            "Низкая средняя эффективность фактического преобразования SCR. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523004 FMI 0). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P0426",
        "aliases": ['SPN 4360 FMI 0', '4360/0', 'SPN 4360 FMI 1', '4360/1', 'SPN 4360 FMI 2', '4360/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "SCR Неверный сигнал превышения максимального предела температуры датчика SCR верхнего у…",
        "description": (
            "SCR Неверный сигнал превышения максимального предела температуры датчика SCR верхнего уровня. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4360 FMI 0). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P0427",
        "aliases": ['SPN 4363 FMI 4', '4363/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Напряжение сигнала датчика температуры нижнего уровня катализатора SCR ниже минимальног…",
        "description": (
            "Напряжение сигнала датчика температуры нижнего уровня катализатора SCR ниже минимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4363 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P0428",
        "aliases": ['SPN 4363 FMI 3', '4363/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Напряжение сигнала датчика температуры нижнего уровня катализатора SCR выше максимально…",
        "description": (
            "Напряжение сигнала датчика температуры нижнего уровня катализатора SCR выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4363 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P042C",
        "aliases": ['SPN 4360 FMI 4', '4360/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Напряжение сигнала датчика температуры верхнего уровня катализатора SCR ниже минимально…",
        "description": (
            "Напряжение сигнала датчика температуры верхнего уровня катализатора SCR ниже минимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4360 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P042D",
        "aliases": ['SPN 4360 FMI 3', '4360/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Напряжение сигнала датчика температуры верхнего уровня катализатора SCR выше максимальн…",
        "description": (
            "Напряжение сигнала датчика температуры верхнего уровня катализатора SCR выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4360 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P0460",
        "aliases": ['SPN 96 FMI 1', '96/1'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Уровень топлива в топливном баке ниже минимального значения, либо воздух в гидравлическ…",
        "description": (
            "Уровень топлива в топливном баке ниже минимального значения, либо воздух в гидравлической системе. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 96 FMI 1). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0475",
        "aliases": ['SPN 571 FMI 5', '571/5', 'SPN 571 FMI 6', '571/6', 'SPN 520208 FMI 5', '520208/5'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Горный тормоз в движении без нагрузки",
        "description": (
            "Горный тормоз в движении без нагрузки. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 571 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Концевик педали тормоза врёт / два сигнала не сходятся", "probability": 50, "oem_part": None},
            {"cause": "Обрыв цепи стоп-сигнала", "probability": 30, "oem_part": None},
            {"cause": "Проблема моторного тормоза / горного тормоза", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Считать статус brake switch 1/2 на сканере.",
            "Проверить лягушку педали и проводку."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0476",
        "aliases": ['SPN 520208 FMI 2', '520208/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неверный сигнал положения реле горного тормоза",
        "description": (
            "Неверный сигнал положения реле горного тормоза. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520208 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Концевик педали тормоза врёт / два сигнала не сходятся", "probability": 50, "oem_part": None},
            {"cause": "Обрыв цепи стоп-сигнала", "probability": 30, "oem_part": None},
            {"cause": "Проблема моторного тормоза / горного тормоза", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Считать статус brake switch 1/2 на сканере.",
            "Проверить лягушку педали и проводку."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0477",
        "aliases": ['SPN 571 FMI 4', '571/4', 'SPN 520208 FMI 4', '520208/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание земли горного тормоза",
        "description": (
            "Короткое замыкание земли горного тормоза. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 571 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Концевик педали тормоза врёт / два сигнала не сходятся", "probability": 50, "oem_part": None},
            {"cause": "Обрыв цепи стоп-сигнала", "probability": 30, "oem_part": None},
            {"cause": "Проблема моторного тормоза / горного тормоза", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Считать статус brake switch 1/2 на сканере.",
            "Проверить лягушку педали и проводку."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0478",
        "aliases": ['SPN 571 FMI 3', '571/3', 'SPN 520208 FMI 3', '520208/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание источника питания горного тормоза",
        "description": (
            "Короткое замыкание источника питания горного тормоза. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 571 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Концевик педали тормоза врёт / два сигнала не сходятся", "probability": 50, "oem_part": None},
            {"cause": "Обрыв цепи стоп-сигнала", "probability": 30, "oem_part": None},
            {"cause": "Проблема моторного тормоза / горного тормоза", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Считать статус brake switch 1/2 на сканере.",
            "Проверить лягушку педали и проводку."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0480",
        "aliases": ['SPN 4815 FMI 5', '4815/5', 'SPN 4815 FMI 20', '4815/20', 'SPN 4815 FMI 6', '4815/6'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Электромагнитный клапан вентилятора 1 без нагрузки",
        "description": (
            "Электромагнитный клапан вентилятора 1 без нагрузки. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4815 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Неисправна вискомуфта / электромагнит вентилятора", "probability": 40, "oem_part": None},
            {"cause": "Обрыв цепи управления вентилятором", "probability": 35, "oem_part": None},
            {"cause": "Врёт датчик оборотов вентилятора", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить включение вентилятора на прогретом моторе.",
            "Разъём муфты и предохранитель.",
            "Не игнорировать летом — риск перегрева."
        ],
        "severity": "limited",
        "estimated_time_min": 35,
    },
    {
        "code": "P0481",
        "aliases": ['SPN 4815 FMI 7', '4815/7', 'SPN 4815 FMI 8', '4815/8'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Нет нагрузки PWM привода вентилятора",
        "description": (
            "Нет нагрузки PWM привода вентилятора. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4815 FMI 7). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Неисправна вискомуфта / электромагнит вентилятора", "probability": 40, "oem_part": None},
            {"cause": "Обрыв цепи управления вентилятором", "probability": 35, "oem_part": None},
            {"cause": "Врёт датчик оборотов вентилятора", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить включение вентилятора на прогретом моторе.",
            "Разъём муфты и предохранитель.",
            "Не игнорировать летом — риск перегрева."
        ],
        "severity": "limited",
        "estimated_time_min": 35,
    },
    {
        "code": "P0494",
        "aliases": ['SPN 1639 FMI 4', '1639/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Обороты вентилятора на рабочих оборотах ниже минимального значения",
        "description": (
            "Обороты вентилятора на рабочих оборотах ниже минимального значения. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1639 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Неисправна вискомуфта / электромагнит вентилятора", "probability": 40, "oem_part": None},
            {"cause": "Обрыв цепи управления вентилятором", "probability": 35, "oem_part": None},
            {"cause": "Врёт датчик оборотов вентилятора", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить включение вентилятора на прогретом моторе.",
            "Разъём муфты и предохранитель.",
            "Не игнорировать летом — риск перегрева."
        ],
        "severity": "limited",
        "estimated_time_min": 35,
    },
    {
        "code": "P0495",
        "aliases": ['SPN 1639 FMI 3', '1639/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Обороты вентилятора на рабочих оборотах превышают максимальное значение",
        "description": (
            "Обороты вентилятора на рабочих оборотах превышают максимальное значение. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1639 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Неисправна вискомуфта / электромагнит вентилятора", "probability": 40, "oem_part": None},
            {"cause": "Обрыв цепи управления вентилятором", "probability": 35, "oem_part": None},
            {"cause": "Врёт датчик оборотов вентилятора", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить включение вентилятора на прогретом моторе.",
            "Разъём муфты и предохранитель.",
            "Не игнорировать летом — риск перегрева."
        ],
        "severity": "limited",
        "estimated_time_min": 35,
    },
    {
        "code": "P0501",
        "aliases": ['SPN 84 FMI 2', '84/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Расхождение скорости автомобиля с оборотами двигателя и крутящим моментом",
        "description": (
            "Расхождение скорости автомобиля с оборотами двигателя и крутящим моментом. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 84 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Нет сигнала скорости с КПП / ABS", "probability": 45, "oem_part": None},
            {"cause": "Обрыв CAN к панели/ABS", "probability": 30, "oem_part": None},
            {"cause": "Неисправен датчик скорости", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Сверить скорость на панели и в сканере.",
            "Проверить, жив ли ABS и сигнал на КПП."
        ],
        "severity": "can_drive",
        "estimated_time_min": 25,
    },
    {
        "code": "P0502",
        "aliases": ['SPN 84 FMI 4', '84/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Сигнал напряжения датчика скорости ниже минимального предела",
        "description": (
            "Сигнал напряжения датчика скорости ниже минимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 84 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0503",
        "aliases": ['SPN 84 FMI 3', '84/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Сигнал напряжения датчика скорости выше максимального предела",
        "description": (
            "Сигнал напряжения датчика скорости выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 84 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0504",
        "aliases": ['SPN 597 FMI 2', '597/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Сигналы основного и вспомогательного тормоза не совпадают",
        "description": (
            "Сигналы основного и вспомогательного тормоза не совпадают. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 597 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Концевик педали тормоза врёт / два сигнала не сходятся", "probability": 50, "oem_part": None},
            {"cause": "Обрыв цепи стоп-сигнала", "probability": 30, "oem_part": None},
            {"cause": "Проблема моторного тормоза / горного тормоза", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Считать статус brake switch 1/2 на сканере.",
            "Проверить лягушку педали и проводку."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0520",
        "aliases": ['SPN 100 FMI 19', '100/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "CAN Ошибка сигнала CAN давления масла в двигателе",
        "description": (
            "CAN Ошибка сигнала CAN давления масла в двигателе. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 100 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "P0521",
        "aliases": ['SPN 100 FMI 2', '100/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неверный сигнал давления масла в двигателе",
        "description": (
            "Неверный сигнал давления масла в двигателе. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 100 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Низкий уровень / разжижение масла топливом", "probability": 40, "oem_part": None},
            {"cause": "Неисправен датчик или проводка", "probability": 30, "oem_part": None},
            {"cause": "Реальная неисправность маслосистемы", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Щуп + механический манометр, не верить только лампе.",
            "Проверить разъём датчика на блоке.",
            "При подтверждении низкого давления — не заводить."
        ],
        "severity": "tow",
        "estimated_time_min": 25,
    },
    {
        "code": "P0522",
        "aliases": ['SPN 100 FMI 18', '100/18'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение сигнала давления масла ниже минимального предела",
        "description": (
            "Напряжение сигнала давления масла ниже минимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 100 FMI 18). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Низкий уровень / разжижение масла топливом", "probability": 40, "oem_part": None},
            {"cause": "Неисправен датчик или проводка", "probability": 30, "oem_part": None},
            {"cause": "Реальная неисправность маслосистемы", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Щуп + механический манометр, не верить только лампе.",
            "Проверить разъём датчика на блоке.",
            "При подтверждении низкого давления — не заводить."
        ],
        "severity": "tow",
        "estimated_time_min": 25,
    },
    {
        "code": "P0523",
        "aliases": ['SPN 100 FMI 15', '100/15', 'SPN 100 FMI 16', '100/16'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Давление масла в двигателе выше максимального предела",
        "description": (
            "Давление масла в двигателе выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 100 FMI 15). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Низкий уровень / разжижение масла топливом", "probability": 40, "oem_part": None},
            {"cause": "Неисправен датчик или проводка", "probability": 30, "oem_part": None},
            {"cause": "Реальная неисправность маслосистемы", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Щуп + механический манометр, не верить только лампе.",
            "Проверить разъём датчика на блоке.",
            "При подтверждении низкого давления — не заводить."
        ],
        "severity": "tow",
        "estimated_time_min": 25,
    },
    {
        "code": "P0571",
        "aliases": ['SPN 597 FMI 19', '597/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка сигнала тормоза",
        "description": (
            "Ошибка сигнала тормоза. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 597 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Концевик педали тормоза врёт / два сигнала не сходятся", "probability": 50, "oem_part": None},
            {"cause": "Обрыв цепи стоп-сигнала", "probability": 30, "oem_part": None},
            {"cause": "Проблема моторного тормоза / горного тормоза", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Считать статус brake switch 1/2 на сканере.",
            "Проверить лягушку педали и проводку."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0575",
        "aliases": ['SPN 596 FMI 2', '596/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка переключателя круиз контроля",
        "description": (
            "Ошибка переключателя круиз контроля. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 596 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0607",
        "aliases": ['SPN 522058 FMI 19', '522058/19', 'SPN 520201 FMI 19', '520201/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка Cy146, связанные с SPI и COM",
        "description": (
            "Ошибка Cy146, связанные с SPI и COM. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 522058 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P060B",
        "aliases": ['SPN 520266 FMI 11', '520266/11', 'SPN 520220 FMI 2', '520220/2', 'SPN 520220 FMI 11', '520220/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Слишком большое отклонение аналого-цифровое преобразование",
        "description": (
            "Слишком большое отклонение аналого-цифровое преобразование. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520266 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P060C",
        "aliases": ['SPN 520221 FMI 11', '520221/11', 'SPN 520222 FMI 11', '520222/11', 'SPN 520223 FMI 11', '520223/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка связи модуля контроля и CPU",
        "description": (
            "Ошибка связи модуля контроля и CPU. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520221 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0611",
        "aliases": ['SPN 520268 FMI 11', '520268/11', 'SPN 520268 FMI 20', '520268/20', 'SPN 520268 FMI 21', '520268/21'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка корекции баланса уровня масла 1",
        "description": (
            "Ошибка корекции баланса уровня масла 1. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520268 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Низкий уровень / разжижение масла топливом", "probability": 40, "oem_part": None},
            {"cause": "Неисправен датчик или проводка", "probability": 30, "oem_part": None},
            {"cause": "Реальная неисправность маслосистемы", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Щуп + механический манометр, не верить только лампе.",
            "Проверить разъём датчика на блоке.",
            "При подтверждении низкого давления — не заводить."
        ],
        "severity": "tow",
        "estimated_time_min": 25,
    },
    {
        "code": "P0615",
        "aliases": ['SPN 1675 FMI 5', '1675/5', 'SPN 1675 FMI 6', '1675/6'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Нет нагрузки стартера",
        "description": (
            "Нет нагрузки стартера. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1675 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/КЗ цепи реле стартера", "probability": 40, "oem_part": None},
            {"cause": "Села АКБ или плохая масса", "probability": 35, "oem_part": None},
            {"cause": "Заклинил втягивающий / сам стартер", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Щёлкает ли реле, есть ли +24В на управляющем проводе.",
            "Напряжение на АКБ при стартере.",
            "Не крутить «до победы» — сядет аккумулятор."
        ],
        "severity": "tow",
        "estimated_time_min": 30,
    },
    {
        "code": "P0616",
        "aliases": ['SPN 1675 FMI 4', '1675/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание земли реле стартера",
        "description": (
            "Короткое замыкание земли реле стартера. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1675 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/КЗ цепи реле стартера", "probability": 40, "oem_part": None},
            {"cause": "Села АКБ или плохая масса", "probability": 35, "oem_part": None},
            {"cause": "Заклинил втягивающий / сам стартер", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Щёлкает ли реле, есть ли +24В на управляющем проводе.",
            "Напряжение на АКБ при стартере.",
            "Не крутить «до победы» — сядет аккумулятор."
        ],
        "severity": "tow",
        "estimated_time_min": 30,
    },
    {
        "code": "P0617",
        "aliases": ['SPN 1675 FMI 3', '1675/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание источника питания реле стартера",
        "description": (
            "Короткое замыкание источника питания реле стартера. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1675 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/КЗ цепи реле стартера", "probability": 40, "oem_part": None},
            {"cause": "Села АКБ или плохая масса", "probability": 35, "oem_part": None},
            {"cause": "Заклинил втягивающий / сам стартер", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Щёлкает ли реле, есть ли +24В на управляющем проводе.",
            "Напряжение на АКБ при стартере.",
            "Не крутить «до победы» — сядет аккумулятор."
        ],
        "severity": "tow",
        "estimated_time_min": 30,
    },
    {
        "code": "P062B",
        "aliases": ['SPN 1413 FMI 14', '1413/14', 'SPN 1414 FMI 14', '1414/14', 'SPN 1415 FMI 14', '1415/14'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка параметра коррекции форсунки 1",
        "description": (
            "Ошибка параметра коррекции форсунки 1. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1413 FMI 14). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P062D",
        "aliases": ['SPN 520214 FMI 3', '520214/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Замыкание конденсатора впрыска 1",
        "description": (
            "Замыкание конденсатора впрыска 1. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520214 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P062E",
        "aliases": ['SPN 520287 FMI 3', '520287/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Замыкание конденсатора впрыска 2",
        "description": (
            "Замыкание конденсатора впрыска 2. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520287 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P062F",
        "aliases": ['SPN 2802 FMI 11', '2802/11', 'SPN 2802 FMI 14', '2802/14', 'SPN 2802 FMI 12', '2802/12'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка стирания EEP",
        "description": (
            "Ошибка стирания EEP. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 2802 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0643",
        "aliases": ['SPN 3509 FMI 2', '3509/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка энергоснабжения датчика 1",
        "description": (
            "Ошибка энергоснабжения датчика 1. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3509 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0645",
        "aliases": ['SPN 1351 FMI 5', '1351/5', 'SPN 1351 FMI 6', '1351/6', 'SPN 2978 FMI 5', '2978/5'],
        "brands": ["Howo", "Shacman"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Компрессор кондиционера работает без нагрузки",
        "description": (
            "Компрессор кондиционера работает без нагрузки. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1351 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/КЗ муфты компрессора кондиционера", "probability": 50, "oem_part": None},
            {"cause": "Нет запроса с панели / CAN климата", "probability": 30, "oem_part": None},
            {"cause": "Сработал датчик давления хладагента", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить предохранитель и разъём муфты.",
            "Считать, видит ли ЭБУ запрос A/C.",
            "На двигатель почти не влияет."
        ],
        "severity": "can_drive",
        "estimated_time_min": 25,
    },
    {
        "code": "P0646",
        "aliases": ['SPN 2978 FMI 4', '2978/4', 'SPN 1351 FMI 4', '1351/4'],
        "brands": ["Howo", "Shacman"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание земли компрессора кондиционера при отключении нагрузки",
        "description": (
            "Короткое замыкание земли компрессора кондиционера при отключении нагрузки. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 2978 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/КЗ муфты компрессора кондиционера", "probability": 50, "oem_part": None},
            {"cause": "Нет запроса с панели / CAN климата", "probability": 30, "oem_part": None},
            {"cause": "Сработал датчик давления хладагента", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить предохранитель и разъём муфты.",
            "Считать, видит ли ЭБУ запрос A/C.",
            "На двигатель почти не влияет."
        ],
        "severity": "can_drive",
        "estimated_time_min": 25,
    },
    {
        "code": "P0647",
        "aliases": ['SPN 2978 FMI 3', '2978/3', 'SPN 1351 FMI 3', '1351/3'],
        "brands": ["Howo", "Shacman"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание источника питания при отключении нагрузки компрессора кондиционера",
        "description": (
            "Короткое замыкание источника питания при отключении нагрузки компрессора кондиционера. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 2978 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/КЗ муфты компрессора кондиционера", "probability": 50, "oem_part": None},
            {"cause": "Нет запроса с панели / CAN климата", "probability": 30, "oem_part": None},
            {"cause": "Сработал датчик давления хладагента", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить предохранитель и разъём муфты.",
            "Считать, видит ли ЭБУ запрос A/C.",
            "На двигатель почти не влияет."
        ],
        "severity": "can_drive",
        "estimated_time_min": 25,
    },
    {
        "code": "P0650",
        "aliases": ['SPN 520219 FMI 5', '520219/5', 'SPN 520219 FMI 6', '520219/6', 'SPN 520219 FMI 3', '520219/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "MIL Лампа MIL без нагрузки",
        "description": (
            "MIL Лампа MIL без нагрузки. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520219 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0653",
        "aliases": ['SPN 3510 FMI 2', '3510/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка энергоснабжения датчика 2",
        "description": (
            "Ошибка энергоснабжения датчика 2. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3510 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0658",
        "aliases": ['SPN 3597 FMI 4', '3597/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Актуатор_0 короткое замыкание земли",
        "description": (
            "Актуатор_0 короткое замыкание земли. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3597 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0659",
        "aliases": ['SPN 3597 FMI 3', '3597/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Актуатор_0 короткое замыкание источника питания",
        "description": (
            "Актуатор_0 короткое замыкание источника питания. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3597 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0667",
        "aliases": ['SPN 523011 FMI 2', '523011/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неверная температура внутреннего блока ECU",
        "description": (
            "Неверная температура внутреннего блока ECU. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523011 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0668",
        "aliases": ['SPN 1136 FMI 4', '1136/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Сигнал напряжения датчика температуры внутренней части ECU ниже минимального предела",
        "description": (
            "Сигнал напряжения датчика температуры внутренней части ECU ниже минимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1136 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0669",
        "aliases": ['SPN 523011 FMI 0', '523011/0', 'SPN 1136 FMI 3', '1136/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Температура внутри ECU выше максимального предела",
        "description": (
            "Температура внутри ECU выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523011 FMI 0). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P068A",
        "aliases": ['SPN 3508 FMI 7', '3508/7'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Раннее включение главного реле после включения ECU",
        "description": (
            "Раннее включение главного реле после включения ECU. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3508 FMI 7). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P068B",
        "aliases": ['SPN 3508 FMI 12', '3508/12'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Позднее включение главного реле",
        "description": (
            "Позднее включение главного реле. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3508 FMI 12). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0691",
        "aliases": ['SPN 4815 FMI 4', '4815/4', 'SPN 4815 FMI 22', '4815/22'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание земли электромагнитного клапана вентилятора 1",
        "description": (
            "Короткое замыкание земли электромагнитного клапана вентилятора 1. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4815 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Неисправна вискомуфта / электромагнит вентилятора", "probability": 40, "oem_part": None},
            {"cause": "Обрыв цепи управления вентилятором", "probability": 35, "oem_part": None},
            {"cause": "Врёт датчик оборотов вентилятора", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить включение вентилятора на прогретом моторе.",
            "Разъём муфты и предохранитель.",
            "Не игнорировать летом — риск перегрева."
        ],
        "severity": "limited",
        "estimated_time_min": 35,
    },
    {
        "code": "P0692",
        "aliases": ['SPN 4815 FMI 3', '4815/3', 'SPN 4815 FMI 21', '4815/21'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание источника питания электромагнитного клапана вентилятора 1",
        "description": (
            "Короткое замыкание источника питания электромагнитного клапана вентилятора 1. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4815 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Неисправна вискомуфта / электромагнит вентилятора", "probability": 40, "oem_part": None},
            {"cause": "Обрыв цепи управления вентилятором", "probability": 35, "oem_part": None},
            {"cause": "Врёт датчик оборотов вентилятора", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить включение вентилятора на прогретом моторе.",
            "Разъём муфты и предохранитель.",
            "Не игнорировать летом — риск перегрева."
        ],
        "severity": "limited",
        "estimated_time_min": 35,
    },
    {
        "code": "P0693",
        "aliases": ['SPN 4815 FMI 10', '4815/10'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание земли привода PWM вентилятора",
        "description": (
            "Короткое замыкание земли привода PWM вентилятора. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4815 FMI 10). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Неисправна вискомуфта / электромагнит вентилятора", "probability": 40, "oem_part": None},
            {"cause": "Обрыв цепи управления вентилятором", "probability": 35, "oem_part": None},
            {"cause": "Врёт датчик оборотов вентилятора", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить включение вентилятора на прогретом моторе.",
            "Разъём муфты и предохранитель.",
            "Не игнорировать летом — риск перегрева."
        ],
        "severity": "limited",
        "estimated_time_min": 35,
    },
    {
        "code": "P0694",
        "aliases": ['SPN 4815 FMI 9', '4815/9'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание источника питания привода PWM вентилятора",
        "description": (
            "Короткое замыкание источника питания привода PWM вентилятора. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4815 FMI 9). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Неисправна вискомуфта / электромагнит вентилятора", "probability": 40, "oem_part": None},
            {"cause": "Обрыв цепи управления вентилятором", "probability": 35, "oem_part": None},
            {"cause": "Врёт датчик оборотов вентилятора", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить включение вентилятора на прогретом моторе.",
            "Разъём муфты и предохранитель.",
            "Не игнорировать летом — риск перегрева."
        ],
        "severity": "limited",
        "estimated_time_min": 35,
    },
    {
        "code": "P0699",
        "aliases": ['SPN 3511 FMI 2', '3511/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка энергоснабжения датчика 3",
        "description": (
            "Ошибка энергоснабжения датчика 3. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3511 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0704",
        "aliases": ['SPN 598 FMI 2', '598/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неверный сигнал сцепления (Передача изменилась, но сигнал сцепления не изменился)",
        "description": (
            "Неверный сигнал сцепления (Передача изменилась, но сигнал сцепления не изменился). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 598 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Нет сигнала сцепления / нейтрали (концевик, CAN)", "probability": 45, "oem_part": None},
            {"cause": "Низкое напряжение на TCM", "probability": 30, "oem_part": None},
            {"cause": "Собственные коды коробки", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Считать коды TCM отдельно от двигателя.",
            "Проверить концевик сцепления и CAN ECM↔TCM."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0A0F",
        "aliases": ['SPN 520211 FMI 11', '520211/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неудачный запуск двигателя",
        "description": (
            "Неудачный запуск двигателя. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520211 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1000",
        "aliases": ['SPN 520195 FMI 2', '520195/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неправильный сигнал холодного пуска при температуре_0",
        "description": (
            "Неправильный сигнал холодного пуска при температуре_0. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520195 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1001",
        "aliases": ['SPN 520254 FMI 2', '520254/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неправильный сигнал холодного пуска при температуре_1",
        "description": (
            "Неправильный сигнал холодного пуска при температуре_1. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520254 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1002",
        "aliases": ['SPN 520255 FMI 2', '520255/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неправильный сигнал холодного пуска при температуре_2",
        "description": (
            "Неправильный сигнал холодного пуска при температуре_2. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520255 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1003",
        "aliases": ['SPN 520256 FMI 2', '520256/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неправильный сигнал холодного пуска при температуре_3",
        "description": (
            "Неправильный сигнал холодного пуска при температуре_3. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520256 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1004",
        "aliases": ['SPN 520257 FMI 2', '520257/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неправильный сигнал холодного пуска при температуре_4",
        "description": (
            "Неправильный сигнал холодного пуска при температуре_4. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520257 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1005",
        "aliases": ['SPN 520258 FMI 2', '520258/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неправильный сигнал холодного пуска множественная температура",
        "description": (
            "Неправильный сигнал холодного пуска множественная температура. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520258 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1006",
        "aliases": ['SPN 520197 FMI 11', '520197/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Превышение объема отчетов о превышении ограничения крутящего момента",
        "description": (
            "Превышение объема отчетов о превышении ограничения крутящего момента. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520197 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1007",
        "aliases": ['SPN 520198 FMI 11', '520198/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка активации ограничения крутящего момента OBD",
        "description": (
            "Ошибка активации ограничения крутящего момента OBD. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520198 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1008",
        "aliases": ['SPN 1109 FMI 11', '1109/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Запрос на отключение двигателя приводит к отключению впрыска топлива",
        "description": (
            "Запрос на отключение двигателя приводит к отключению впрыска топлива. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1109 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1009",
        "aliases": ['SPN 520205 FMI 7', '520205/7'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Активация защиты двигателя",
        "description": (
            "Активация защиты двигателя. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520205 FMI 7). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P100A",
        "aliases": ['SPN 1623 FMI 5', '1623/5'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Двигатель в движении выдает отсутствие нагрузки",
        "description": (
            "Двигатель в движении выдает отсутствие нагрузки. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1623 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P100B",
        "aliases": ['SPN 1623 FMI 6', '1623/6'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Превышение температуры двигателя на рабочих оборотах",
        "description": (
            "Превышение температуры двигателя на рабочих оборотах. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1623 FMI 6). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P100C",
        "aliases": ['SPN 1623 FMI 3', '1623/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание источника питания двигателя на рабочих оборотах",
        "description": (
            "Короткое замыкание источника питания двигателя на рабочих оборотах. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1623 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P100D",
        "aliases": ['SPN 1623 FMI 4', '1623/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание земли двигателя на рабочих оборотах",
        "description": (
            "Короткое замыкание земли двигателя на рабочих оборотах. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1623 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P100E",
        "aliases": ['SPN 520210 FMI 11', '520210/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Частота впрыска превышает ограничение цепи",
        "description": (
            "Частота впрыска превышает ограничение цепи. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520210 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P100F",
        "aliases": ['SPN 520210 FMI 20', '520210/20'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Частота впрыска превышает ограничение максимального давление топливного насоса",
        "description": (
            "Частота впрыска превышает ограничение максимального давление топливного насоса. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520210 FMI 20). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1010",
        "aliases": ['SPN 520210 FMI 21', '520210/21'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Частота впрыска превышает ограничение системы",
        "description": (
            "Частота впрыска превышает ограничение системы. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520210 FMI 21). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1012",
        "aliases": ['SPN 520224 FMI 11', '520224/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Несовместимые 2 напряжения педали акселератора",
        "description": (
            "Несовместимые 2 напряжения педали акселератора. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520224 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Коррозия разъёма педали (соль, коврик, вода)", "probability": 45, "oem_part": None},
            {"cause": "Неисправен модуль педали (два канала APP разъехались)", "probability": 40, "oem_part": None},
            {"cause": "Нет опорных 5В с ЭБУ", "probability": 15, "oem_part": None}
        ],
        "check_steps": [
            "Считать оба канала APP % — должны расти синхронно.",
            "Проверить 5В, массы и сигнал на разъёме педали.",
            "Не ставить «неоригинал наугад» без проверки проводки."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1013",
        "aliases": ['SPN 520225 FMI 11', '520225/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неверный сигнал рабочих оборотов двигателя",
        "description": (
            "Неверный сигнал рабочих оборотов двигателя. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520225 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1014",
        "aliases": ['SPN 520226 FMI 11', '520226/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неверный сигнал форсунки в момент включения питания",
        "description": (
            "Неверный сигнал форсунки в момент включения питания. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520226 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1015",
        "aliases": ['SPN 520227 FMI 11', '520227/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неверный сигнал опережения впрыска",
        "description": (
            "Неверный сигнал опережения впрыска. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520227 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1016",
        "aliases": ['SPN 520228 FMI 11', '520228/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неверный сигнал нулевого уровня топлива в момент включения питания",
        "description": (
            "Неверный сигнал нулевого уровня топлива в момент включения питания. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520228 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1017",
        "aliases": ['SPN 520229 FMI 11', '520229/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неверный сигнал эффективности после впрыска 2",
        "description": (
            "Неверный сигнал эффективности после впрыска 2. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520229 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1018",
        "aliases": ['SPN 520229 FMI 14', '520229/14'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка закрытия 2 после впрыска",
        "description": (
            "Ошибка закрытия 2 после впрыска. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520229 FMI 14). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1019",
        "aliases": ['SPN 520230 FMI 11', '520230/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неверный сигнал эффективности после впрыска 3",
        "description": (
            "Неверный сигнал эффективности после впрыска 3. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520230 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P101A",
        "aliases": ['SPN 1108 FMI 16', '1108/16'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "При Overrun время включения питания превышает максисмальное значение",
        "description": (
            "При Overrun время включения питания превышает максисмальное значение. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1108 FMI 16). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P101B",
        "aliases": ['SPN 520231 FMI 11', '520231/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неверный сигнал коррекции объема впрыска",
        "description": (
            "Неверный сигнал коррекции объема впрыска. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520231 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P101C",
        "aliases": ['SPN 520232 FMI 11', '520232/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка давления в рампе",
        "description": (
            "Ошибка давления в рампе. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520232 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Засор фильтра / сепаратора или подсос воздуха на всасывании", "probability": 40, "oem_part": None},
            {"cause": "Износ ТНВД / дозирующего клапана, не держит давление", "probability": 30, "oem_part": None},
            {"cause": "Утечка high-pressure контура или льющая форсунка в обратку", "probability": 20, "oem_part": None},
            {"cause": "Врёт датчик давления рампы или окислен разъём", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Сравнить rail desired vs actual на холостых и под нагрузкой.",
            "Заменить фильтры, слить отстой, прокачать, искать пузырьки.",
            "Проверить питание 5В / массу / сигнал датчика рампы.",
            "Тест обратки форсунок и герметичность рампы."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "P101D",
        "aliases": ['SPN 520233 FMI 11', '520233/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Несовместимый реальный крутящий момент двигателя с разрешенным",
        "description": (
            "Несовместимый реальный крутящий момент двигателя с разрешенным. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520233 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P101E",
        "aliases": ['SPN 520234 FMI 11', '520234/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Давление в топливной рампе ограничено функцией блока контроля крутящего момента",
        "description": (
            "Давление в топливной рампе ограничено функцией блока контроля крутящего момента. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520234 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Засор фильтра / сепаратора или подсос воздуха на всасывании", "probability": 40, "oem_part": None},
            {"cause": "Износ ТНВД / дозирующего клапана, не держит давление", "probability": 30, "oem_part": None},
            {"cause": "Утечка high-pressure контура или льющая форсунка в обратку", "probability": 20, "oem_part": None},
            {"cause": "Врёт датчик давления рампы или окислен разъём", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Сравнить rail desired vs actual на холостых и под нагрузкой.",
            "Заменить фильтры, слить отстой, прокачать, искать пузырьки.",
            "Проверить питание 5В / массу / сигнал датчика рампы.",
            "Тест обратки форсунок и герметичность рампы."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "P101F",
        "aliases": ['SPN 520234 FMI 20', '520234/20'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Система воздухоподачи ограничена функцией блока контроля крутящего момента",
        "description": (
            "Система воздухоподачи ограничена функцией блока контроля крутящего момента. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520234 FMI 20). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1020",
        "aliases": ['SPN 520234 FMI 21', '520234/21'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Уровень впрыскиваемого топлива ограничен функцией блока контроля крутящего момента",
        "description": (
            "Уровень впрыскиваемого топлива ограничен функцией блока контроля крутящего момента. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520234 FMI 21). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1021",
        "aliases": ['SPN 520237 FMI 11', '520237/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка удаления кода из хранилища",
        "description": (
            "Ошибка удаления кода из хранилища. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520237 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1022",
        "aliases": ['SPN 520237 FMI 28', '520237/28'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка удаления кода из хранилища",
        "description": (
            "Ошибка удаления кода из хранилища. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520237 FMI 28). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1023",
        "aliases": ['SPN 520237 FMI 29', '520237/29'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка удаления кода из хранилища",
        "description": (
            "Ошибка удаления кода из хранилища. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520237 FMI 29). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1024",
        "aliases": ['SPN 520237 FMI 12', '520237/12'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка удаления кода из хранилища",
        "description": (
            "Ошибка удаления кода из хранилища. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520237 FMI 12). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1025",
        "aliases": ['SPN 520237 FMI 13', '520237/13'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка удаления кода из хранилища",
        "description": (
            "Ошибка удаления кода из хранилища. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520237 FMI 13). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1026",
        "aliases": ['SPN 520237 FMI 14', '520237/14'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка удаления кода из хранилища",
        "description": (
            "Ошибка удаления кода из хранилища. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520237 FMI 14). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1027",
        "aliases": ['SPN 520237 FMI 15', '520237/15'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка удаления кода из хранилища",
        "description": (
            "Ошибка удаления кода из хранилища. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520237 FMI 15). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1028",
        "aliases": ['SPN 520237 FMI 16', '520237/16'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка удаления кода из хранилища",
        "description": (
            "Ошибка удаления кода из хранилища. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520237 FMI 16). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1029",
        "aliases": ['SPN 520237 FMI 20', '520237/20'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка удаления кода из хранилища",
        "description": (
            "Ошибка удаления кода из хранилища. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520237 FMI 20). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P102A",
        "aliases": ['SPN 520237 FMI 21', '520237/21'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка удаления кода из хранилища",
        "description": (
            "Ошибка удаления кода из хранилища. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520237 FMI 21). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P102B",
        "aliases": ['SPN 520237 FMI 22', '520237/22'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка удаления кода из хранилища",
        "description": (
            "Ошибка удаления кода из хранилища. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520237 FMI 22). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P102C",
        "aliases": ['SPN 520237 FMI 23', '520237/23'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка удаления кода из хранилища",
        "description": (
            "Ошибка удаления кода из хранилища. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520237 FMI 23). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P102D",
        "aliases": ['SPN 520237 FMI 24', '520237/24'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка удаления кода из хранилища",
        "description": (
            "Ошибка удаления кода из хранилища. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520237 FMI 24). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P102E",
        "aliases": ['SPN 520237 FMI 25', '520237/25'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка удаления кода из хранилища",
        "description": (
            "Ошибка удаления кода из хранилища. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520237 FMI 25). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P102F",
        "aliases": ['SPN 520237 FMI 26', '520237/26'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка удаления кода из хранилища",
        "description": (
            "Ошибка удаления кода из хранилища. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520237 FMI 26). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1030",
        "aliases": ['SPN 520237 FMI 27', '520237/27'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка удаления кода из хранилища",
        "description": (
            "Ошибка удаления кода из хранилища. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520237 FMI 27). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1031",
        "aliases": ['SPN 520240 FMI 13', '520240/13'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неоднородное изменение крутящего момента уровня масла",
        "description": (
            "Неоднородное изменение крутящего момента уровня масла. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520240 FMI 13). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Низкий уровень / разжижение масла топливом", "probability": 40, "oem_part": None},
            {"cause": "Неисправен датчик или проводка", "probability": 30, "oem_part": None},
            {"cause": "Реальная неисправность маслосистемы", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Щуп + механический манометр, не верить только лампе.",
            "Проверить разъём датчика на блоке.",
            "При подтверждении низкого давления — не заводить."
        ],
        "severity": "tow",
        "estimated_time_min": 25,
    },
    {
        "code": "P1032",
        "aliases": ['SPN 520261 FMI 5', '520261/5'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Нет нагрузки на приводе подогрева топлива",
        "description": (
            "Нет нагрузки на приводе подогрева топлива. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520261 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1033",
        "aliases": ['SPN 520261 FMI 6', '520261/6'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Перегрев привода подогрева топлива",
        "description": (
            "Перегрев привода подогрева топлива. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520261 FMI 6). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1034",
        "aliases": ['SPN 520261 FMI 3', '520261/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание источника питания привода обогрева топлива",
        "description": (
            "Короткое замыкание источника питания привода обогрева топлива. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520261 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1035",
        "aliases": ['SPN 520261 FMI 4', '520261/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание земли привода обогрева топлива",
        "description": (
            "Короткое замыкание земли привода обогрева топлива. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520261 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1036",
        "aliases": ['SPN 520241 FMI 22', '520241/22'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка баланса уровня топлива в момент открытия предохранительного клапана",
        "description": (
            "Ошибка баланса уровня топлива в момент открытия предохранительного клапана. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520241 FMI 22). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1037",
        "aliases": ['SPN 520241 FMI 2', '520241/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Среднее давление в рампе превосходит допустимые пределы",
        "description": (
            "Среднее давление в рампе превосходит допустимые пределы. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520241 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Засор фильтра / сепаратора или подсос воздуха на всасывании", "probability": 40, "oem_part": None},
            {"cause": "Износ ТНВД / дозирующего клапана, не держит давление", "probability": 30, "oem_part": None},
            {"cause": "Утечка high-pressure контура или льющая форсунка в обратку", "probability": 20, "oem_part": None},
            {"cause": "Врёт датчик давления рампы или окислен разъём", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Сравнить rail desired vs actual на холостых и под нагрузкой.",
            "Заменить фильтры, слить отстой, прокачать, искать пузырьки.",
            "Проверить питание 5В / массу / сигнал датчика рампы.",
            "Тест обратки форсунок и герметичность рампы."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "P1038",
        "aliases": ['SPN 520269 FMI 14', '520269/14'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Превышение ограничения крутящего момента защиты турбины",
        "description": (
            "Превышение ограничения крутящего момента защиты турбины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520269 FMI 14). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Заклинила геометрия VGT / нагар на лопатках", "probability": 40, "oem_part": None},
            {"cause": "Обрыв или КЗ цепи актуатора турбины", "probability": 30, "oem_part": None},
            {"cause": "Утечка патрубков / интеркулера или врёт датчик наддува", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Сравнить boost desired vs actual.",
            "Проверить разъём и питание актуатора (после мойки мотора часто вода).",
            "Осмотреть патрубки и люфт вала турбины."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P1039",
        "aliases": ['SPN 520270 FMI 14', '520270/14'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Превышение ограничения крутящего момента защиты двигателя",
        "description": (
            "Превышение ограничения крутящего момента защиты двигателя. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520270 FMI 14). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1040",
        "aliases": ['SPN 520271 FMI 14', '520271/14'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Превышение ограничения крутящего момента защиты системы впрыска",
        "description": (
            "Превышение ограничения крутящего момента защиты системы впрыска. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520271 FMI 14). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1041",
        "aliases": ['SPN 520272 FMI 14', '520272/14'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Превышение ограничения крутящего момента горным тормозом",
        "description": (
            "Превышение ограничения крутящего момента горным тормозом. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520272 FMI 14). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Концевик педали тормоза врёт / два сигнала не сходятся", "probability": 50, "oem_part": None},
            {"cause": "Обрыв цепи стоп-сигнала", "probability": 30, "oem_part": None},
            {"cause": "Проблема моторного тормоза / горного тормоза", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Считать статус brake switch 1/2 на сканере.",
            "Проверить лягушку педали и проводку."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1042",
        "aliases": ['SPN 520273 FMI 14', '520273/14'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Превышение ограничения крутящего момента фильтра твердых частиц",
        "description": (
            "Превышение ограничения крутящего момента фильтра твердых частиц. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520273 FMI 14). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Реген не завершается (короткие рейсы, глушат на регене)", "probability": 40, "oem_part": None},
            {"cause": "Врут датчики перепада/температуры DPF", "probability": 30, "oem_part": None},
            {"cause": "Реально забит фильтр (льющая форсунка, масло в выпуске)", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Считать сажевую нагрузку, перепад, статус регена.",
            "Проверить датчики температуры и шланги дифференциала.",
            "Сервисный реген или промывка — не вырезать в поле."
        ],
        "severity": "limited",
        "estimated_time_min": 70,
    },
    {
        "code": "P1043",
        "aliases": ['SPN 520274 FMI 14', '520274/14'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Превышение ограничения крутящего момента ограничителем крутящего момента",
        "description": (
            "Превышение ограничения крутящего момента ограничителем крутящего момента. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520274 FMI 14). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1044",
        "aliases": ['SPN 520275 FMI 14', '520275/14'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Превышение ограничения крутящего момента ограничением уровня дыма",
        "description": (
            "Превышение ограничения крутящего момента ограничением уровня дыма. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520275 FMI 14). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1045",
        "aliases": ['SPN 520276 FMI 11', '520276/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Несовместимые 2 напряжения дальнего хода педали акселератора",
        "description": (
            "Несовместимые 2 напряжения дальнего хода педали акселератора. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520276 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Коррозия разъёма педали (соль, коврик, вода)", "probability": 45, "oem_part": None},
            {"cause": "Неисправен модуль педали (два канала APP разъехались)", "probability": 40, "oem_part": None},
            {"cause": "Нет опорных 5В с ЭБУ", "probability": 15, "oem_part": None}
        ],
        "check_steps": [
            "Считать оба канала APP % — должны расти синхронно.",
            "Проверить 5В, массы и сигнал на разъёме педали.",
            "Не ставить «неоригинал наугад» без проверки проводки."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1046",
        "aliases": ['SPN 520289 FMI 3', '520289/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение сигнала перепада давления топлива выше максимального значения",
        "description": (
            "Напряжение сигнала перепада давления топлива выше максимального значения. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520289 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Засор фильтра / сепаратора или подсос воздуха на всасывании", "probability": 40, "oem_part": None},
            {"cause": "Износ ТНВД / дозирующего клапана, не держит давление", "probability": 30, "oem_part": None},
            {"cause": "Утечка high-pressure контура или льющая форсунка в обратку", "probability": 20, "oem_part": None},
            {"cause": "Врёт датчик давления рампы или окислен разъём", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Сравнить rail desired vs actual на холостых и под нагрузкой.",
            "Заменить фильтры, слить отстой, прокачать, искать пузырьки.",
            "Проверить питание 5В / массу / сигнал датчика рампы.",
            "Тест обратки форсунок и герметичность рампы."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "P1047",
        "aliases": ['SPN 520289 FMI 4', '520289/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение сигнала перепада давления топлива выше максимального значения",
        "description": (
            "Напряжение сигнала перепада давления топлива выше максимального значения. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520289 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Засор фильтра / сепаратора или подсос воздуха на всасывании", "probability": 40, "oem_part": None},
            {"cause": "Износ ТНВД / дозирующего клапана, не держит давление", "probability": 30, "oem_part": None},
            {"cause": "Утечка high-pressure контура или льющая форсунка в обратку", "probability": 20, "oem_part": None},
            {"cause": "Врёт датчик давления рампы или окислен разъём", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Сравнить rail desired vs actual на холостых и под нагрузкой.",
            "Заменить фильтры, слить отстой, прокачать, искать пузырьки.",
            "Проверить питание 5В / массу / сигнал датчика рампы.",
            "Тест обратки форсунок и герметичность рампы."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "P1048",
        "aliases": ['SPN 520289 FMI 7', '520289/7'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Засор топливного фильтра",
        "description": (
            "Засор топливного фильтра. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520289 FMI 7). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1049",
        "aliases": ['SPN 520289 FMI 14', '520289/14'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неверный сигнал засора топливного фильтра",
        "description": (
            "Неверный сигнал засора топливного фильтра. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520289 FMI 14). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1050",
        "aliases": ['SPN 520243 FMI 23', '520243/23'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "В режиме OverRun уровень топлива в ТНВД выше максимального предела",
        "description": (
            "В режиме OverRun уровень топлива в ТНВД выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520243 FMI 23). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1400",
        "aliases": ['SPN 522012 FMI 0', '522012/0'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка SPN1 информации DCU",
        "description": (
            "Ошибка SPN1 информации DCU. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 522012 FMI 0). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1401",
        "aliases": ['SPN 522012 FMI 1', '522012/1'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка SPN2 информации DCU",
        "description": (
            "Ошибка SPN2 информации DCU. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 522012 FMI 1). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1402",
        "aliases": ['SPN 522012 FMI 2', '522012/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка SPN3 информации DCU",
        "description": (
            "Ошибка SPN3 информации DCU. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 522012 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1403",
        "aliases": ['SPN 522012 FMI 3', '522012/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка SPN4 информации DCU",
        "description": (
            "Ошибка SPN4 информации DCU. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 522012 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1404",
        "aliases": ['SPN 522012 FMI 4', '522012/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка SPN5 информации DCU",
        "description": (
            "Ошибка SPN5 информации DCU. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 522012 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1405",
        "aliases": ['SPN 522012 FMI 19', '522012/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Истечение времени ожидания DCU BAM",
        "description": (
            "Истечение времени ожидания DCU BAM. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 522012 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1500",
        "aliases": ['SPN 571 FMI 2', '571/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неверный сигнал горного тормоза",
        "description": (
            "Неверный сигнал горного тормоза. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 571 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Концевик педали тормоза врёт / два сигнала не сходятся", "probability": 50, "oem_part": None},
            {"cause": "Обрыв цепи стоп-сигнала", "probability": 30, "oem_part": None},
            {"cause": "Проблема моторного тормоза / горного тормоза", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Считать статус brake switch 1/2 на сканере.",
            "Проверить лягушку педали и проводку."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1501",
        "aliases": ['SPN 520277 FMI 3', '520277/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение длинного хода педали 1 выше максимального предела",
        "description": (
            "Напряжение длинного хода педали 1 выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520277 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Коррозия разъёма педали (соль, коврик, вода)", "probability": 45, "oem_part": None},
            {"cause": "Неисправен модуль педали (два канала APP разъехались)", "probability": 40, "oem_part": None},
            {"cause": "Нет опорных 5В с ЭБУ", "probability": 15, "oem_part": None}
        ],
        "check_steps": [
            "Считать оба канала APP % — должны расти синхронно.",
            "Проверить 5В, массы и сигнал на разъёме педали.",
            "Не ставить «неоригинал наугад» без проверки проводки."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1502",
        "aliases": ['SPN 520278 FMI 3', '520278/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение длинного хода педали 2 выше максимального предела",
        "description": (
            "Напряжение длинного хода педали 2 выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520278 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Коррозия разъёма педали (соль, коврик, вода)", "probability": 45, "oem_part": None},
            {"cause": "Неисправен модуль педали (два канала APP разъехались)", "probability": 40, "oem_part": None},
            {"cause": "Нет опорных 5В с ЭБУ", "probability": 15, "oem_part": None}
        ],
        "check_steps": [
            "Считать оба канала APP % — должны расти синхронно.",
            "Проверить 5В, массы и сигнал на разъёме педали.",
            "Не ставить «неоригинал наугад» без проверки проводки."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1503",
        "aliases": ['SPN 520277 FMI 4', '520277/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение длинного хода педали 1 ниже минимального предела",
        "description": (
            "Напряжение длинного хода педали 1 ниже минимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520277 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Коррозия разъёма педали (соль, коврик, вода)", "probability": 45, "oem_part": None},
            {"cause": "Неисправен модуль педали (два канала APP разъехались)", "probability": 40, "oem_part": None},
            {"cause": "Нет опорных 5В с ЭБУ", "probability": 15, "oem_part": None}
        ],
        "check_steps": [
            "Считать оба канала APP % — должны расти синхронно.",
            "Проверить 5В, массы и сигнал на разъёме педали.",
            "Не ставить «неоригинал наугад» без проверки проводки."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1504",
        "aliases": ['SPN 520278 FMI 4', '520278/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение длинного хода педали 2 ниже минимального предела",
        "description": (
            "Напряжение длинного хода педали 2 ниже минимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520278 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Коррозия разъёма педали (соль, коврик, вода)", "probability": 45, "oem_part": None},
            {"cause": "Неисправен модуль педали (два канала APP разъехались)", "probability": 40, "oem_part": None},
            {"cause": "Нет опорных 5В с ЭБУ", "probability": 15, "oem_part": None}
        ],
        "check_steps": [
            "Считать оба канала APP % — должны расти синхронно.",
            "Проверить 5В, массы и сигнал на разъёме педали.",
            "Не ставить «неоригинал наугад» без проверки проводки."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1505",
        "aliases": ['SPN 520280 FMI 2', '520280/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Слишком большая разница между сигналами напряжения педали длинного хода 1 и педали длин…",
        "description": (
            "Слишком большая разница между сигналами напряжения педали длинного хода 1 и педали длинного хода 2. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520280 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Коррозия разъёма педали (соль, коврик, вода)", "probability": 45, "oem_part": None},
            {"cause": "Неисправен модуль педали (два канала APP разъехались)", "probability": 40, "oem_part": None},
            {"cause": "Нет опорных 5В с ЭБУ", "probability": 15, "oem_part": None}
        ],
        "check_steps": [
            "Считать оба канала APP % — должны расти синхронно.",
            "Проверить 5В, массы и сигнал на разъёме педали.",
            "Не ставить «неоригинал наугад» без проверки проводки."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1600",
        "aliases": ['SPN 520235 FMI 11', '520235/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение блока электроснабжения 1 превышает максимальное значение",
        "description": (
            "Напряжение блока электроснабжения 1 превышает максимальное значение. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520235 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1601",
        "aliases": ['SPN 520235 FMI 20', '520235/20'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение блока электроснабжения 1 ниже минимального значения",
        "description": (
            "Напряжение блока электроснабжения 1 ниже минимального значения. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520235 FMI 20). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1602",
        "aliases": ['SPN 3512 FMI 3', '3512/3', 'SPN 3513 FMI 3', '3513/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Слишком высокая энергоподача датчика 12V",
        "description": (
            "Слишком высокая энергоподача датчика 12V. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3512 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1603",
        "aliases": ['SPN 3512 FMI 4', '3512/4', 'SPN 3513 FMI 4', '3513/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Слишком низкая энергоподача датчика 12V",
        "description": (
            "Слишком низкая энергоподача датчика 12V. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3512 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1604",
        "aliases": ['SPN 520250 FMI 5', '520250/5'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Нет нагрузки при запуске диагностических индикаторов",
        "description": (
            "Нет нагрузки при запуске диагностических индикаторов. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520250 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1605",
        "aliases": ['SPN 520250 FMI 6', '520250/6'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Превышение температуры пуска диагностических индикаторов",
        "description": (
            "Превышение температуры пуска диагностических индикаторов. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520250 FMI 6). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1606",
        "aliases": ['SPN 520250 FMI 3', '520250/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание источника питания диагностического индикатора",
        "description": (
            "Короткое замыкание источника питания диагностического индикатора. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520250 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1607",
        "aliases": ['SPN 520250 FMI 4', '520250/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание земли диагностического индикатора",
        "description": (
            "Короткое замыкание земли диагностического индикатора. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520250 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1608",
        "aliases": ['SPN 520251 FMI 11', '520251/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Сброс 0 программы диагностики неисправностей",
        "description": (
            "Сброс 0 программы диагностики неисправностей. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520251 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P1609",
        "aliases": ['SPN 520251 FMI 20', '520251/20'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Сброс 1программы диагностики неисправностей",
        "description": (
            "Сброс 1программы диагностики неисправностей. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520251 FMI 20). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P160A",
        "aliases": ['SPN 520251 FMI 21', '520251/21'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Сброс 2 программы диагностики неисправностей",
        "description": (
            "Сброс 2 программы диагностики неисправностей. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520251 FMI 21). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P160B",
        "aliases": ['SPN 100 FMI 5', '100/5'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Открытая цепь индикатора давления масла в двигателе",
        "description": (
            "Открытая цепь индикатора давления масла в двигателе. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 100 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Низкий уровень / разжижение масла топливом", "probability": 40, "oem_part": None},
            {"cause": "Неисправен датчик или проводка", "probability": 30, "oem_part": None},
            {"cause": "Реальная неисправность маслосистемы", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Щуп + механический манометр, не верить только лампе.",
            "Проверить разъём датчика на блоке.",
            "При подтверждении низкого давления — не заводить."
        ],
        "severity": "tow",
        "estimated_time_min": 25,
    },
    {
        "code": "P160C",
        "aliases": ['SPN 100 FMI 6', '100/6'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Температура индикатора давления масла в двигателе выше нормы",
        "description": (
            "Температура индикатора давления масла в двигателе выше нормы. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 100 FMI 6). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Низкий уровень / разжижение масла топливом", "probability": 40, "oem_part": None},
            {"cause": "Неисправен датчик или проводка", "probability": 30, "oem_part": None},
            {"cause": "Реальная неисправность маслосистемы", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Щуп + механический манометр, не верить только лампе.",
            "Проверить разъём датчика на блоке.",
            "При подтверждении низкого давления — не заводить."
        ],
        "severity": "tow",
        "estimated_time_min": 25,
    },
    {
        "code": "P160D",
        "aliases": ['SPN 100 FMI 3', '100/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание источника питания индикатора давления масла в двигателе",
        "description": (
            "Короткое замыкание источника питания индикатора давления масла в двигателе. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 100 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Низкий уровень / разжижение масла топливом", "probability": 40, "oem_part": None},
            {"cause": "Неисправен датчик или проводка", "probability": 30, "oem_part": None},
            {"cause": "Реальная неисправность маслосистемы", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Щуп + механический манометр, не верить только лампе.",
            "Проверить разъём датчика на блоке.",
            "При подтверждении низкого давления — не заводить."
        ],
        "severity": "tow",
        "estimated_time_min": 25,
    },
    {
        "code": "P160E",
        "aliases": ['SPN 100 FMI 4', '100/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание земли индикатора давления масла в двигателе",
        "description": (
            "Короткое замыкание земли индикатора давления масла в двигателе. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 100 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Низкий уровень / разжижение масла топливом", "probability": 40, "oem_part": None},
            {"cause": "Неисправен датчик или проводка", "probability": 30, "oem_part": None},
            {"cause": "Реальная неисправность маслосистемы", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Щуп + механический манометр, не верить только лампе.",
            "Проверить разъём датчика на блоке.",
            "При подтверждении низкого давления — не заводить."
        ],
        "severity": "tow",
        "estimated_time_min": 25,
    },
    {
        "code": "P160F",
        "aliases": ['SPN 520279 FMI 5', '520279/5'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Нет нагрузки индикатора остановки машины",
        "description": (
            "Нет нагрузки индикатора остановки машины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520279 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "P1610",
        "aliases": ['SPN 520279 FMI 6', '520279/6'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Превышение температуры индикатора остановки машины",
        "description": (
            "Превышение температуры индикатора остановки машины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520279 FMI 6). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "P1611",
        "aliases": ['SPN 520279 FMI 3', '520279/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание источника питания индикатора остановки машины",
        "description": (
            "Короткое замыкание источника питания индикатора остановки машины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520279 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "P1612",
        "aliases": ['SPN 520279 FMI 4', '520279/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание земли индикатора остановки машины",
        "description": (
            "Короткое замыкание земли индикатора остановки машины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520279 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "P1613",
        "aliases": ['SPN 520281 FMI 5', '520281/5'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Незамкнутая цепь сигнальной лампы",
        "description": (
            "Незамкнутая цепь сигнальной лампы. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520281 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1614",
        "aliases": ['SPN 520281 FMI 6', '520281/6'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Перегрев сигнальной лампы",
        "description": (
            "Перегрев сигнальной лампы. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520281 FMI 6). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1615",
        "aliases": ['SPN 520281 FMI 3', '520281/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание источника питания сигнальной лампы",
        "description": (
            "Короткое замыкание источника питания сигнальной лампы. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520281 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P1616",
        "aliases": ['SPN 520281 FMI 4', '520281/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание земли сигнальной лампы",
        "description": (
            "Короткое замыкание земли сигнальной лампы. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520281 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P203B",
        "aliases": ['SPN 3516 FMI 2', '3516/2', 'SPN 3031 FMI 2', '3031/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Ошибка регулировки уровня мочевины в впрыскиваемом объеме топлива",
        "description": (
            "Ошибка регулировки уровня мочевины в впрыскиваемом объеме топлива. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3516 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P203C",
        "aliases": ['SPN 1761 FMI 4', '1761/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Напряжение датчика уровня мочевины ниже минимального значения",
        "description": (
            "Напряжение датчика уровня мочевины ниже минимального значения. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1761 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P203D",
        "aliases": ['SPN 1761 FMI 3', '1761/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Напряжение датчика уровня мочевины выше максимального значения",
        "description": (
            "Напряжение датчика уровня мочевины выше максимального значения. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1761 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P203F",
        "aliases": ['SPN 1761 FMI 2', '1761/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Низкий уровень мочевины",
        "description": (
            "Низкий уровень мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1761 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P2043",
        "aliases": ['SPN 3031 FMI 14', '3031/14'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Перегрев бака мочевины",
        "description": (
            "Перегрев бака мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3031 FMI 14). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P2047",
        "aliases": ['SPN 3361 FMI 2', '3361/2', 'SPN 3361 FMI 17', '3361/17'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Засор распылителя форсунки мочевины SCR",
        "description": (
            "Засор распылителя форсунки мочевины SCR. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3361 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P2048",
        "aliases": ['SPN 3361 FMI 4', '3361/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание земли актуатора распылителя форсунки мочевины SCR",
        "description": (
            "Короткое замыкание земли актуатора распылителя форсунки мочевины SCR. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3361 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P2049",
        "aliases": ['SPN 3361 FMI 5', '3361/5', 'SPN 3361 FMI 15', '3361/15', 'SPN 3361 FMI 3', '3361/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Электроток распылителя форсунки мочевины SCR выше максимального предела",
        "description": (
            "Электроток распылителя форсунки мочевины SCR выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3361 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P204C",
        "aliases": ['SPN 1387 FMI 4', '1387/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Сигнал напряжения датчика напряжения насоса мочевины ниже минимального предела",
        "description": (
            "Сигнал напряжения датчика напряжения насоса мочевины ниже минимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1387 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P204D",
        "aliases": ['SPN 1387 FMI 3', '1387/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Сигнал напряжения датчика напряжения насоса мочевины выше максимального предела",
        "description": (
            "Сигнал напряжения датчика напряжения насоса мочевины выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1387 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P204E",
        "aliases": ['SPN 1387 FMI 19', '1387/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка связи CAN сигнала напряжения насоса мочевины",
        "description": (
            "Ошибка связи CAN сигнала напряжения насоса мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1387 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "P205A",
        "aliases": ['SPN 3031 FMI 19', '3031/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка информации CAN температуры бака мочевины",
        "description": (
            "Ошибка информации CAN температуры бака мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3031 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "P205B",
        "aliases": ['SPN 3031 FMI 0', '3031/0', 'SPN 3031 FMI 1', '3031/1'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Сигнал датчика температуры бака мочевины выше максимального предела",
        "description": (
            "Сигнал датчика температуры бака мочевины выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3031 FMI 0). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P205C",
        "aliases": ['SPN 3031 FMI 4', '3031/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Сигнал напряжения датчика температуры бака мочевины ниже минимального предела",
        "description": (
            "Сигнал напряжения датчика температуры бака мочевины ниже минимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3031 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P205D",
        "aliases": ['SPN 3031 FMI 3', '3031/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Сигнал напряжения датчика температуры бака мочевины выше максимального предела",
        "description": (
            "Сигнал напряжения датчика температуры бака мочевины выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3031 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P2062",
        "aliases": ['SPN 523017 FMI 21', '523017/21', 'SPN 523017 FMI 8', '523017/8'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "PWM Принимаемый SCR насос мочевины PWM цикл находится в недопустимом диапазоне",
        "description": (
            "PWM Принимаемый SCR насос мочевины PWM цикл находится в недопустимом диапазоне. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523017 FMI 21). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P2068",
        "aliases": ['SPN 532103 FMI 11', '532103/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Количество повторных запусков SCR превышает допустимый предел",
        "description": (
            "Количество повторных запусков SCR превышает допустимый предел. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 532103 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P2135",
        "aliases": ['SPN 520252 FMI 2', '520252/2', 'SPN 558 FMI 2', '558/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Слишком большая разница между сигналами напряжения педали 1 и педали 2",
        "description": (
            "Слишком большая разница между сигналами напряжения педали 1 и педали 2. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520252 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Коррозия разъёма педали (соль, коврик, вода)", "probability": 45, "oem_part": None},
            {"cause": "Неисправен модуль педали (два канала APP разъехались)", "probability": 40, "oem_part": None},
            {"cause": "Нет опорных 5В с ЭБУ", "probability": 15, "oem_part": None}
        ],
        "check_steps": [
            "Считать оба канала APP % — должны расти синхронно.",
            "Проверить 5В, массы и сигнал на разъёме педали.",
            "Не ставить «неоригинал наугад» без проверки проводки."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P2158",
        "aliases": ['SPN 1624 FMI 3', '1624/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ширина импульса датчика скорости выше максимального предела",
        "description": (
            "Ширина импульса датчика скорости выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1624 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P2160",
        "aliases": ['SPN 1624 FMI 4', '1624/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ширина импульса датчика скорости ниже минимального предела",
        "description": (
            "Ширина импульса датчика скорости ниже минимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1624 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P2161",
        "aliases": ['SPN 1624 FMI 8', '1624/8'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Цикл сигнала датчика датчика скорости ниже минимального предела",
        "description": (
            "Цикл сигнала датчика датчика скорости ниже минимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1624 FMI 8). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P2162",
        "aliases": ['SPN 84 FMI 14', '84/14'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неверный сигнал напряжения датчика скорости",
        "description": (
            "Неверный сигнал напряжения датчика скорости. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 84 FMI 14). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P2200",
        "aliases": ['SPN 3220 FMI 5', '3220/5', 'SPN 3217 FMI 15', '3217/15', 'SPN 3217 FMI 17', '3217/17'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка подачи электроэнергии датчика нижнее положение",
        "description": (
            "Ошибка подачи электроэнергии датчика нижнее положение. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3220 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P2201",
        "aliases": ['SPN 3217 FMI 2', '3217/2', 'SPN 3220 FMI 0', '3220/0', 'SPN 3220 FMI 1', '3220/1'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неверная компенсация сигнала датчика нижнее положение нижнее положение",
        "description": (
            "Неверная компенсация сигнала датчика нижнее положение нижнее положение. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3217 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P2204",
        "aliases": ['SPN 3216 FMI 11', '3216/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неверный сигнал датчика нижнее положение",
        "description": (
            "Неверный сигнал датчика нижнее положение. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3216 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P2214",
        "aliases": ['SPN 3216 FMI 2', '3216/2', 'SPN 3216 FMI 15', '3216/15', 'SPN 3216 FMI 17', '3216/17'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Неверный сигнал проверки пика сигнала датчика нижнего уровня SCR",
        "description": (
            "Неверный сигнал проверки пика сигнала датчика нижнего уровня SCR. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3216 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P2228",
        "aliases": ['SPN 108 FMI 4', '108/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение датчика давления окружающей среды ниже минимального предела",
        "description": (
            "Напряжение датчика давления окружающей среды ниже минимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 108 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P2229",
        "aliases": ['SPN 108 FMI 3', '108/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение датчика давления окружающей среды выше максимального предела",
        "description": (
            "Напряжение датчика давления окружающей среды выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 108 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P2266",
        "aliases": ['SPN 520264 FMI 4', '520264/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение сигнала датчика воды в топливе выше максимального значения",
        "description": (
            "Напряжение сигнала датчика воды в топливе выше максимального значения. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520264 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P2267",
        "aliases": ['SPN 520264 FMI 3', '520264/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение сигнала датчика воды в топливе выше максимального значения",
        "description": (
            "Напряжение сигнала датчика воды в топливе выше максимального значения. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520264 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P250B",
        "aliases": ['SPN 98 FMI 2', '98/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неверный сигнал напряжения уровня масла в двигателе",
        "description": (
            "Неверный сигнал напряжения уровня масла в двигателе. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 98 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Низкий уровень / разжижение масла топливом", "probability": 40, "oem_part": None},
            {"cause": "Неисправен датчик или проводка", "probability": 30, "oem_part": None},
            {"cause": "Реальная неисправность маслосистемы", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Щуп + механический манометр, не верить только лампе.",
            "Проверить разъём датчика на блоке.",
            "При подтверждении низкого давления — не заводить."
        ],
        "severity": "tow",
        "estimated_time_min": 25,
    },
    {
        "code": "P250C",
        "aliases": ['SPN 98 FMI 4', '98/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение сигнала уровня масла ниже минимального предела",
        "description": (
            "Напряжение сигнала уровня масла ниже минимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 98 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Низкий уровень / разжижение масла топливом", "probability": 40, "oem_part": None},
            {"cause": "Неисправен датчик или проводка", "probability": 30, "oem_part": None},
            {"cause": "Реальная неисправность маслосистемы", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Щуп + механический манометр, не верить только лампе.",
            "Проверить разъём датчика на блоке.",
            "При подтверждении низкого давления — не заводить."
        ],
        "severity": "tow",
        "estimated_time_min": 25,
    },
    {
        "code": "P250D",
        "aliases": ['SPN 98 FMI 3', '98/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение сигнала уровня масла выше максимального предела",
        "description": (
            "Напряжение сигнала уровня масла выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 98 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Низкий уровень / разжижение масла топливом", "probability": 40, "oem_part": None},
            {"cause": "Неисправен датчик или проводка", "probability": 30, "oem_part": None},
            {"cause": "Реальная неисправность маслосистемы", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Щуп + механический манометр, не верить только лампе.",
            "Проверить разъём датчика на блоке.",
            "При подтверждении низкого давления — не заводить."
        ],
        "severity": "tow",
        "estimated_time_min": 25,
    },
    {
        "code": "P250F",
        "aliases": ['SPN 98 FMI 1', '98/1'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Сигнал уровня масла ниже минимального значения",
        "description": (
            "Сигнал уровня масла ниже минимального значения. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 98 FMI 1). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Низкий уровень / разжижение масла топливом", "probability": 40, "oem_part": None},
            {"cause": "Неисправен датчик или проводка", "probability": 30, "oem_part": None},
            {"cause": "Реальная неисправность маслосистемы", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Щуп + механический манометр, не верить только лампе.",
            "Проверить разъём датчика на блоке.",
            "При подтверждении низкого давления — не заводить."
        ],
        "severity": "tow",
        "estimated_time_min": 25,
    },
    {
        "code": "P251B",
        "aliases": ['SPN 976 FMI 4', '976/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Напряжение на Переключателе PTO ниже минимального предела",
        "description": (
            "Напряжение на Переключателе PTO ниже минимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 976 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P251C",
        "aliases": ['SPN 976 FMI 3', '976/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "PTO Напряжение на переключателе PTO выше максимального предела",
        "description": (
            "PTO Напряжение на переключателе PTO выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 976 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P252F",
        "aliases": ['SPN 98 FMI 0', '98/0'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Сигнал уровня масла выше максимального значения",
        "description": (
            "Сигнал уровня масла выше максимального значения. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 98 FMI 0). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Низкий уровень / разжижение масла топливом", "probability": 40, "oem_part": None},
            {"cause": "Неисправен датчик или проводка", "probability": 30, "oem_part": None},
            {"cause": "Реальная неисправность маслосистемы", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Щуп + механический манометр, не верить только лампе.",
            "Проверить разъём датчика на блоке.",
            "При подтверждении низкого давления — не заводить."
        ],
        "severity": "tow",
        "estimated_time_min": 25,
    },
    {
        "code": "P2530",
        "aliases": ['SPN 520253 FMI 11', '520253/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "T50 Ошибка переключателя Т50",
        "description": (
            "T50 Ошибка переключателя Т50. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520253 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P2536",
        "aliases": ['SPN 520203 FMI 2', '520203/2', 'SPN 520203 FMI 5', '520203/5'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неверный сигнал переключателя остановки машины",
        "description": (
            "Неверный сигнал переключателя остановки машины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 520203 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "P253E",
        "aliases": ['SPN 976 FMI 19', '976/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "PTO Неверное напряжение переключателя PTO",
        "description": (
            "PTO Неверное напряжение переключателя PTO. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 976 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P2609",
        "aliases": ['SPN 2898 FMI 16', '2898/16', 'SPN 2898 FMI 18', '2898/18', 'SPN 2898 FMI 15', '2898/15'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Сигнал высокого напряжения в выключенном состоянии сетки обогрева впускного воздуха",
        "description": (
            "Сигнал высокого напряжения в выключенном состоянии сетки обогрева впускного воздуха. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 2898 FMI 16). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Неисправен датчик наддува / MAP+IAT", "probability": 40, "oem_part": None},
            {"cause": "Окисление разъёма, нет 5В", "probability": 30, "oem_part": None},
            {"cause": "Реальная утечка во впуске", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "На заглушенном моторе MAP ≈ атмосферному.",
            "Проверить 5В/массу/сигнал.",
            "Искать свист патрубков интеркулера."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P2670",
        "aliases": ['SPN 3598 FMI 4', '3598/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Актуатор_1 короткое замыкание земли",
        "description": (
            "Актуатор_1 короткое замыкание земли. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3598 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P2671",
        "aliases": ['SPN 3598 FMI 3', '3598/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Актуатор_1 короткое замыкание источника питания",
        "description": (
            "Актуатор_1 короткое замыкание источника питания. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3598 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P2685",
        "aliases": ['SPN 3599 FMI 4', '3599/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Актуатор_2 короткое замыкание земли",
        "description": (
            "Актуатор_2 короткое замыкание земли. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3599 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P2686",
        "aliases": ['SPN 3599 FMI 3', '3599/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Актуатор_2 короткое замыкание источника питания",
        "description": (
            "Актуатор_2 короткое замыкание источника питания. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3599 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / КЗ цепи указанного узла", "probability": 40, "oem_part": None},
            {"cause": "Неисправен сам исполнитель или датчик", "probability": 35, "oem_part": None},
            {"cause": "Просадка питания ЭБУ, плохой контакт разъёма", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Проверить питание и массы ЭБУ при стартере.",
            "Осмотреть разъём указанного узла.",
            "Сверить живые данные с ожидаемыми."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P3000",
        "aliases": ['SPN 523015 FMI 2', '523015/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Ошибка функции PUQP системы SCR",
        "description": (
            "Ошибка функции PUQP системы SCR. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523015 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3001",
        "aliases": ['SPN 4375 FMI 2', '4375/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Ошибка отклонения оборотов двигателя насоса мочевины",
        "description": (
            "Ошибка отклонения оборотов двигателя насоса мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4375 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3002",
        "aliases": ['SPN 4375 FMI 11', '4375/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Отказ двигателя насоса мочевины",
        "description": (
            "Отказ двигателя насоса мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4375 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3003",
        "aliases": ['SPN 4375 FMI 6', '4375/6'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Перегрев актуатора двигателя насоса мочевины",
        "description": (
            "Перегрев актуатора двигателя насоса мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4375 FMI 6). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3004",
        "aliases": ['SPN 4375 FMI 3', '4375/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Короткое замыкание источник питания актуатора двигателя насоса мочевины",
        "description": (
            "Короткое замыкание источник питания актуатора двигателя насоса мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4375 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3005",
        "aliases": ['SPN 4375 FMI 4', '4375/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Короткое замыкание земли актуатора двигателя насоса мочевины",
        "description": (
            "Короткое замыкание земли актуатора двигателя насоса мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4375 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3006",
        "aliases": ['SPN 4375 FMI 5', '4375/5'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Незамкнутая цепь актуатора двигателя насоса мочевины",
        "description": (
            "Незамкнутая цепь актуатора двигателя насоса мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4375 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3007",
        "aliases": ['SPN 1387 FMI 15', '1387/15', 'SPN 1387 FMI 17', '1387/17'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Напряжение насоса мочевины выше максимального предела",
        "description": (
            "Напряжение насоса мочевины выше максимального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1387 FMI 15). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3009",
        "aliases": ['SPN 3361 FMI 6', '3361/6'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Перегрев распылителя форсунки мочевины SCR",
        "description": (
            "Перегрев распылителя форсунки мочевины SCR. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3361 FMI 6). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P3010",
        "aliases": ['SPN 4376 FMI 5', '4376/5'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Незамкнутая цепь актуатора реверсивного клапана мочевины",
        "description": (
            "Незамкнутая цепь актуатора реверсивного клапана мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4376 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3011",
        "aliases": ['SPN 4376 FMI 6', '4376/6'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Перегрев актатора реверсивного клапана мочевины",
        "description": (
            "Перегрев актатора реверсивного клапана мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4376 FMI 6). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3012",
        "aliases": ['SPN 4376 FMI 4', '4376/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Короткое замыкание земли актуатора реверсивного клапана мочевины",
        "description": (
            "Короткое замыкание земли актуатора реверсивного клапана мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4376 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3013",
        "aliases": ['SPN 4376 FMI 3', '4376/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Короткое замыкание источника питания актуатора реверсивного клапана мочевины",
        "description": (
            "Короткое замыкание источника питания актуатора реверсивного клапана мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4376 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3014",
        "aliases": ['SPN 523014 FMI 2', '523014/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Засор обратного клапана насоса мочевины SCR",
        "description": (
            "Засор обратного клапана насоса мочевины SCR. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523014 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3015",
        "aliases": ['SPN 523009 FMI 0', '523009/0'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Отсутсвие опорожнения системы SCR в конце ездового цикла",
        "description": (
            "Отсутсвие опорожнения системы SCR в конце ездового цикла. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523009 FMI 0). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3016",
        "aliases": ['SPN 3363 FMI 5', '3363/5'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Незамкнутая цепь электромагнитного клапана обогрева бака мочевины",
        "description": (
            "Незамкнутая цепь электромагнитного клапана обогрева бака мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3363 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3018",
        "aliases": ['SPN 3363 FMI 0', '3363/0'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Перегрев электромагнитного клапана обогрева бака мочевины",
        "description": (
            "Перегрев электромагнитного клапана обогрева бака мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3363 FMI 0). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3019",
        "aliases": ['SPN 3363 FMI 4', '3363/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Короткое замыкание земли электромагнитного клапана обогрева бака мочевины",
        "description": (
            "Короткое замыкание земли электромагнитного клапана обогрева бака мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3363 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3020",
        "aliases": ['SPN 3363 FMI 3', '3363/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Короткое замыкание источника питания электромагнитного клапана обогрева бака мочевины",
        "description": (
            "Короткое замыкание источника питания электромагнитного клапана обогрева бака мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 3363 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3021",
        "aliases": ['SPN 4346 FMI 5', '4346/5'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Незамкнутая цепь реле обогрева трубопровода мочевины (от насоса к баку)",
        "description": (
            "Незамкнутая цепь реле обогрева трубопровода мочевины (от насоса к баку). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4346 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3022",
        "aliases": ['SPN 4346 FMI 4', '4346/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Короткое замыкание земли реле обогрева трубопровода мочевины (от насоса к баку)",
        "description": (
            "Короткое замыкание земли реле обогрева трубопровода мочевины (от насоса к баку). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4346 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3023",
        "aliases": ['SPN 4346 FMI 3', '4346/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Короткое замыкание источника питания реле обогрева трубопровода мочевины (от насоса к б…",
        "description": (
            "Короткое замыкание источника питания реле обогрева трубопровода мочевины (от насоса к баку). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4346 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3024",
        "aliases": ['SPN 4344 FMI 5', '4344/5'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Незамкнутая цепь реле обогрева трубопровода мочевины (от насоса к форсунке)",
        "description": (
            "Незамкнутая цепь реле обогрева трубопровода мочевины (от насоса к форсунке). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4344 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P3025",
        "aliases": ['SPN 523019 FMI 11', '523019/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Ошибка обогрева мочевины",
        "description": (
            "Ошибка обогрева мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523019 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3026",
        "aliases": ['SPN 4344 FMI 4', '4344/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание земли реле обогрева трубопровода мочевины (от насоса к форсунке)",
        "description": (
            "Короткое замыкание земли реле обогрева трубопровода мочевины (от насоса к форсунке). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4344 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P3027",
        "aliases": ['SPN 4344 FMI 3', '4344/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание иточника питания реле обогрева трубопровода мочевины (от насоса к фо…",
        "description": (
            "Короткое замыкание иточника питания реле обогрева трубопровода мочевины (от насоса к форсунке). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4344 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P3028",
        "aliases": ['SPN 4340 FMI 5', '4340/5'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Незамкнутая цепь реле обогрева трубопровода мочевины (от бака к насосу)",
        "description": (
            "Незамкнутая цепь реле обогрева трубопровода мочевины (от бака к насосу). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4340 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3029",
        "aliases": ['SPN 4355 FMI 9', '4355/9', 'SPN 4355 FMI 8', '4355/8', 'SPN 523017 FMI 9', '523017/9'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Продолжительность включения обогревателя насоса мочевины SCR в диапазоне ошибок",
        "description": (
            "Продолжительность включения обогревателя насоса мочевины SCR в диапазоне ошибок. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4355 FMI 9). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3031",
        "aliases": ['SPN 4340 FMI 4', '4340/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Короткое замыкание земли реле обогрева трубопровода мочевины (от бака к насосу)",
        "description": (
            "Короткое замыкание земли реле обогрева трубопровода мочевины (от бака к насосу). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4340 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3032",
        "aliases": ['SPN 4340 FMI 3', '4340/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Короткое замыкание источника питания реле обогрева трубопровода мочевины (от бака к нас…",
        "description": (
            "Короткое замыкание источника питания реле обогрева трубопровода мочевины (от бака к насосу). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4340 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3033",
        "aliases": ['SPN 4355 FMI 2', '4355/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Незамкнутая цепь реле обогрева насоса мочевины",
        "description": (
            "Незамкнутая цепь реле обогрева насоса мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4355 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3036",
        "aliases": ['SPN 4355 FMI 4', '4355/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Короткое замыкание земли реле обгрева трубопровода насоса мочевины",
        "description": (
            "Короткое замыкание земли реле обгрева трубопровода насоса мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4355 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3037",
        "aliases": ['SPN 4355 FMI 3', '4355/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Короткое замыкание источника питания реле обогрева трубопровода насоса мочевины",
        "description": (
            "Короткое замыкание источника питания реле обогрева трубопровода насоса мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4355 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3038",
        "aliases": ['SPN 523017 FMI 11', '523017/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Отказ модуля измерения температуры мочевины насоса SCR",
        "description": (
            "Отказ модуля измерения температуры мочевины насоса SCR. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523017 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3039",
        "aliases": ['SPN 523010 FMI 0', '523010/0', 'SPN 1387 FMI 0', '1387/0'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Превышение давления впрыска мочевины в блоке управления уровня мочевины SCR",
        "description": (
            "Превышение давления впрыска мочевины в блоке управления уровня мочевины SCR. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523010 FMI 0). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3040",
        "aliases": ['SPN 1387 FMI 2', '1387/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Ошибка давления мочевины SCR",
        "description": (
            "Ошибка давления мочевины SCR. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1387 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3041",
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "SCRПосле понижения давления, давление мочевины в системе SCR ниже минмального предела",
        "description": (
            "SCRПосле понижения давления, давление мочевины в системе SCR ниже минмального предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1387 FMI 0). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3042",
        "aliases": ['SPN 523006 FMI 11', '523006/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Мочевина не поступает в впрыскиваемое топливо",
        "description": (
            "Мочевина не поступает в впрыскиваемое топливо. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523006 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3043",
        "aliases": ['SPN 523003 FMI 5', '523003/5'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Незамкнутая цепь главного реле обогрева мочевины",
        "description": (
            "Незамкнутая цепь главного реле обогрева мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523003 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3044",
        "aliases": ['SPN 523003 FMI 6', '523003/6'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Перегрев главного реле обогрева мочевины",
        "description": (
            "Перегрев главного реле обогрева мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523003 FMI 6). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3045",
        "aliases": ['SPN 523003 FMI 3', '523003/3'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Короткое замыкание источника питания главного реле обогрева мочевины",
        "description": (
            "Короткое замыкание источника питания главного реле обогрева мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523003 FMI 3). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3046",
        "aliases": ['SPN 523003 FMI 4', '523003/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Короткое замыкание земли главного реле обогрева мочевины",
        "description": (
            "Короткое замыкание земли главного реле обогрева мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523003 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3047",
        "aliases": ['SPN 4376 FMI 20', '4376/20'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Незамкнутая цепь верхнего конца актуатора реверсивного клапана мочевины",
        "description": (
            "Незамкнутая цепь верхнего конца актуатора реверсивного клапана мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4376 FMI 20). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3048",
        "aliases": ['SPN 4376 FMI 21', '4376/21'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Перегрев верхнего конца актуатора реверсивного клапана мочевины",
        "description": (
            "Перегрев верхнего конца актуатора реверсивного клапана мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4376 FMI 21). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3049",
        "aliases": ['SPN 523025 FMI 2', '523025/2', 'SPN 4376 FMI 15', '4376/15'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Ошибка понижения давления SCR",
        "description": (
            "Ошибка понижения давления SCR. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523025 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3050",
        "aliases": ['SPN 523007 FMI 2', '523007/2', 'SPN 4376 FMI 17', '4376/17'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Ошибка обратного трубопровода мочевины SCR",
        "description": (
            "Ошибка обратного трубопровода мочевины SCR. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523007 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3051",
        "aliases": ['SPN 523026 FMI 0', '523026/0'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Период самоадаптации SCR превосходит предел",
        "description": (
            "Период самоадаптации SCR превосходит предел. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523026 FMI 0). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3052",
        "aliases": ['SPN 523026 FMI 1', '523026/1'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Период самоадаптации SCR ниже установленного предела",
        "description": (
            "Период самоадаптации SCR ниже установленного предела. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523026 FMI 1). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3053",
        "aliases": ['SPN 523007 FMI 20', '523007/20'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Ошибка падения давления впрыска мочевины SCR",
        "description": (
            "Ошибка падения давления впрыска мочевины SCR. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523007 FMI 20). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3054",
        "aliases": ['SPN 523007 FMI 21', '523007/21'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "SCRОшибка давления впрыска мочевины SCR",
        "description": (
            "SCRОшибка давления впрыска мочевины SCR. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523007 FMI 21). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3056",
        "aliases": ['SPN 523010 FMI 1', '523010/1'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Низкое давление впрыска мочевины в блоке управления уровня мочевины SCR",
        "description": (
            "Низкое давление впрыска мочевины в блоке управления уровня мочевины SCR. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523010 FMI 1). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3057",
        "aliases": ['SPN 4355 FMI 20', '4355/20'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "SCR Неверный обогрев насоса мочевины SCR",
        "description": (
            "SCR Неверный обогрев насоса мочевины SCR. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4355 FMI 20). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3058",
        "aliases": ['SPN 4355 FMI 21', '4355/21'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "SCR Неверное положение датчика температуры обогрева насоса мочевины SCR",
        "description": (
            "SCR Неверное положение датчика температуры обогрева насоса мочевины SCR. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4355 FMI 21). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3059",
        "aliases": ['SPN 4355 FMI 22', '4355/22'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "SCR неверный сигнал датчика температуры обогрева насоса мочевины во время холодного пуска",
        "description": (
            "SCR неверный сигнал датчика температуры обогрева насоса мочевины во время холодного пуска. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4355 FMI 22). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3060",
        "aliases": ['SPN 523017 FMI 2', '523017/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "SCR Неверное состояние датчика температуры мочевины SCR",
        "description": (
            "SCR Неверное состояние датчика температуры мочевины SCR. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523017 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3061",
        "aliases": ['SPN 523017 FMI 20', '523017/20'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "SCR Неверный сигнал датчика температуры мочевины SCR во время холодного пуска",
        "description": (
            "SCR Неверный сигнал датчика температуры мочевины SCR во время холодного пуска. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523017 FMI 20). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3062",
        "aliases": ['SPN 1761 FMI 11', '1761/11'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Остатка уровня мочевины недостаточно",
        "description": (
            "Остатка уровня мочевины недостаточно. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1761 FMI 11). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3063",
        "aliases": ['SPN 1761 FMI 20', '1761/20'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Остаточный уровень мочевины ниже уровня предостережения 1",
        "description": (
            "Остаточный уровень мочевины ниже уровня предостережения 1. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1761 FMI 20). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3064",
        "aliases": ['SPN 1761 FMI 21', '1761/21'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Остаточный уровень мочевины ниже уровня предостережения 2",
        "description": (
            "Остаточный уровень мочевины ниже уровня предостережения 2. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1761 FMI 21). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3065",
        "aliases": ['SPN 532104 FMI 2', '532104/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Ошибка контроля хранения аммиака SCR",
        "description": (
            "Ошибка контроля хранения аммиака SCR. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 532104 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3066",
        "aliases": ['SPN 1761 FMI 0', '1761/0'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Слишком большой расход мочевины",
        "description": (
            "Слишком большой расход мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1761 FMI 0). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3067",
        "aliases": ['SPN 1761 FMI 1', '1761/1'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Слишком малый расход мочевины",
        "description": (
            "Слишком малый расход мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 1761 FMI 1). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3069",
        "aliases": ['SPN 4357 FMI 2', '4357/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Неверная обратная связь сопротивления провода обогрева трубопровода мочевины (от насоса…",
        "description": (
            "Неверная обратная связь сопротивления провода обогрева трубопровода мочевины (от насоса к баку). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4357 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3070",
        "aliases": ['SPN 4357 FMI 5', '4357/5'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Незамкнутая цепь сопротивления провода обогрева трубопровода мочевины (от насоса к баку)",
        "description": (
            "Незамкнутая цепь сопротивления провода обогрева трубопровода мочевины (от насоса к баку). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4357 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3071",
        "aliases": ['SPN 4357 FMI 6', '4357/6'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Короткое замыкание земли сопротивления провода обогрева трубопровода мочевины (от насос…",
        "description": (
            "Короткое замыкание земли сопротивления провода обогрева трубопровода мочевины (от насоса к баку). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4357 FMI 6). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3072",
        "aliases": ['SPN 4346 FMI 6', '4346/6'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Перегрев реле обогрева трубопровода мочевины (от насоса к баку)",
        "description": (
            "Перегрев реле обогрева трубопровода мочевины (от насоса к баку). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4346 FMI 6). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3073",
        "aliases": ['SPN 4356 FMI 2', '4356/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неверная обратная связь сопротивления провода обогрева трубопровода мочевины (от насоса…",
        "description": (
            "Неверная обратная связь сопротивления провода обогрева трубопровода мочевины (от насоса с форсунке). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4356 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P3074",
        "aliases": ['SPN 4356 FMI 5', '4356/5'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Незамкнутая цепь сопротивления провода обогрева трубопровода мочевины (от насоса к форс…",
        "description": (
            "Незамкнутая цепь сопротивления провода обогрева трубопровода мочевины (от насоса к форсунке). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4356 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P3075",
        "aliases": ['SPN 4356 FMI 6', '4356/6'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Короткое замыкание земли сопротивления провода обогрева трубопровода мочевины (от насос…",
        "description": (
            "Короткое замыкание земли сопротивления провода обогрева трубопровода мочевины (от насоса к форсунке). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4356 FMI 6). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P3076",
        "aliases": ['SPN 4344 FMI 6', '4344/6'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Перегрев реле обогрева трубопровода мочевины (от насоса к форсунке)",
        "description": (
            "Перегрев реле обогрева трубопровода мочевины (от насоса к форсунке). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4344 FMI 6). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P3077",
        "aliases": ['SPN 523003 FMI 20', '523003/20'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Короткое замыкание источника питания главного реле обогрева мочевины",
        "description": (
            "Короткое замыкание источника питания главного реле обогрева мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 523003 FMI 20). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3078",
        "aliases": ['SPN 4354 FMI 2', '4354/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Неверная обратная связь сопротивления провода обогрева трубопровода мочевины (от бака к…",
        "description": (
            "Неверная обратная связь сопротивления провода обогрева трубопровода мочевины (от бака к насосу). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4354 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3079",
        "aliases": ['SPN 4354 FMI 5', '4354/5'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Незамкнутая цепь сопротивления провода обогрева трубопровода мочевины (от бака к насосу)",
        "description": (
            "Незамкнутая цепь сопротивления провода обогрева трубопровода мочевины (от бака к насосу). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4354 FMI 5). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3080",
        "aliases": ['SPN 4354 FMI 6', '4354/6'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Короткое замыкание земли провода сопротивления обогрева трубопровода мочевины (от бака …",
        "description": (
            "Короткое замыкание земли провода сопротивления обогрева трубопровода мочевины (от бака к насосу). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4354 FMI 6). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3081",
        "aliases": ['SPN 4340 FMI 6', '4340/6'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Перегрев реле обогрева трубопровода мочевины (от бака к насосу)",
        "description": (
            "Перегрев реле обогрева трубопровода мочевины (от бака к насосу). "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4340 FMI 6). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3082",
        "aliases": ['SPN 4342 FMI 14', '4342/14'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Неверная обратная связь сопротивления провода обогрева насоса мочевины",
        "description": (
            "Неверная обратная связь сопротивления провода обогрева насоса мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4342 FMI 14). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3083",
        "aliases": ['SPN 4342 FMI 2', '4342/2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Незамкнутая цепь провода сопротивления обогрева насоса мочевины",
        "description": (
            "Незамкнутая цепь провода сопротивления обогрева насоса мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4342 FMI 2). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3084",
        "aliases": ['SPN 4342 FMI 4', '4342/4'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Короткое замыкание земли провода сопротивления обогрева насоса мочевины",
        "description": (
            "Короткое замыкание земли провода сопротивления обогрева насоса мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4342 FMI 4). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3085",
        "aliases": ['SPN 4355 FMI 6', '4355/6'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Перегрев реле обогрева трубопровода насоса мочевины",
        "description": (
            "Перегрев реле обогрева трубопровода насоса мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4355 FMI 6). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P3086",
        "aliases": ['SPN 4375 FMI 14', '4375/14'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11", "MC13"],
        "title": "Ошибка отклонения оборотов двигателя на продолжительное время двигателя насоса мочевины",
        "description": (
            "Ошибка отклонения оборотов двигателя на продолжительное время двигателя насоса мочевины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 4375 FMI 14). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Кристаллы мочевины в магистрали / форсунке / насосе", "probability": 40, "oem_part": None},
            {"cause": "Обрыв/КЗ обогрева труб или насоса зимой", "probability": 30, "oem_part": None},
            {"cause": "Пустой бак AdBlue, датчик уровня или насос мёртвый", "probability": 20, "oem_part": None},
            {"cause": "Неисправен NOx-датчик до/после катализатора", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Считать уровень, температуру, давление мочевины и статус дозирования.",
            "Проверить предохранители обогрева и разъёмы насоса/форсунки.",
            "Прокачать/промыть магистраль, не лить воду в бак."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "U0073",
        "aliases": ['SPN 522000 FMI 14', '522000/14', 'SPN 522001 FMI 14', '522001/14', 'SPN 522002 FMI 14', '522002/14'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка главного провода А CAN шины",
        "description": (
            "Ошибка главного провода А CAN шины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 522000 FMI 14). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "U0103",
        "aliases": ['SPN 522022 FMI 19', '522022/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка времени ожидания ETC1, посылаемой CAN",
        "description": (
            "Ошибка времени ожидания ETC1, посылаемой CAN. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 522022 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "U0104",
        "aliases": ['SPN 522030 FMI 19', '522030/19', 'SPN 522044 FMI 19', '522044/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка времени ожидания ETC1, посылаемой CAN",
        "description": (
            "Ошибка времени ожидания ETC1, посылаемой CAN. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 522030 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "U0113",
        "aliases": ['SPN 522006 FMI 14', '522006/14', 'SPN 522006 FMI 19', '522006/19', 'SPN 522007 FMI 19', '522007/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка длины данных AT1IG1 получаемых CAN",
        "description": (
            "Ошибка длины данных AT1IG1 получаемых CAN. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 522006 FMI 14). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "U0116",
        "aliases": ['SPN 110 FMI 19', '110/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка температуры охлаждающей жидкости двигателя, идет от сигнала CAN шины",
        "description": (
            "Ошибка температуры охлаждающей жидкости двигателя, идет от сигнала CAN шины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 110 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "U0129",
        "aliases": ['SPN 522013 FMI 19', '522013/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка времени ожидания получения CAN информации EBC1",
        "description": (
            "Ошибка времени ожидания получения CAN информации EBC1. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 522013 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "U0291",
        "aliases": ['SPN 522023 FMI 19', '522023/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка времени ожидания ETC2, посылаемой CAN",
        "description": (
            "Ошибка времени ожидания ETC2, посылаемой CAN. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 522023 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "U0424",
        "aliases": ['SPN 985 FMI 14', '985/14'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Неисправность входного сигнала CAN шины переключателя кондиционера",
        "description": (
            "Неисправность входного сигнала CAN шины переключателя кондиционера. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 985 FMI 14). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "U0466",
        "aliases": ['SPN 985 FMI 19', '985/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Истечение времени ожидания входного сигнала CAN шины переключателя кондиционера",
        "description": (
            "Истечение времени ожидания входного сигнала CAN шины переключателя кондиционера. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 985 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "U1100",
        "aliases": ['SPN 522018 FMI 19', '522018/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка запроса на остановку двигателя, посылаемого CAN",
        "description": (
            "Ошибка запроса на остановку двигателя, посылаемого CAN. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 522018 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "U1101",
        "aliases": ['SPN 522034 FMI 19', '522034/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка времени ожидания TimeDate, получаемой CAN",
        "description": (
            "Ошибка времени ожидания TimeDate, получаемой CAN. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 522034 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "U1103",
        "aliases": ['SPN 522033 FMI 19', '522033/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка времени ожидания TI1, получаемой CAN",
        "description": (
            "Ошибка времени ожидания TI1, получаемой CAN. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 522033 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "U1105",
        "aliases": ['SPN 522045 FMI 19', '522045/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка информации CAN температура датчика концентрации кислорода",
        "description": (
            "Ошибка информации CAN температура датчика концентрации кислорода. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 522045 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "U1106",
        "aliases": ['SPN 522057 FMI 19', '522057/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "CANWFI Ошибка времени ожидания WFI, посылаемой CAN",
        "description": (
            "CANWFI Ошибка времени ожидания WFI, посылаемой CAN. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 522057 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "U1400",
        "aliases": ['SPN 598 FMI 19', '598/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка сигнала сцепления, идет от CAN шины",
        "description": (
            "Ошибка сигнала сцепления, идет от CAN шины. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 598 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "U1401",
        "aliases": ['SPN 108 FMI 19', '108/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка информации CAN давления окружающей среды",
        "description": (
            "Ошибка информации CAN давления окружающей среды. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 108 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "U1402",
        "aliases": ['SPN 59 FMI 19', '59/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "CAN Ошибка сигнала CAN нейтральной передачи",
        "description": (
            "CAN Ошибка сигнала CAN нейтральной передачи. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 59 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "U1403",
        "aliases": ['SPN 175 FMI 19', '175/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "CAN Ошибка сигнала CAN температуры масла в двигателе",
        "description": (
            "CAN Ошибка сигнала CAN температуры масла в двигателе. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 175 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "U1404",
        "aliases": ['SPN 976 FMI 20', '976/20'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка сообщения CAN переключателя PTO",
        "description": (
            "Ошибка сообщения CAN переключателя PTO. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 976 FMI 20). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "U1405",
        "aliases": ['SPN 84 FMI 19', '84/19'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "WP7", "WP6"],
        "title": "Ошибка связи сигнала скорости CAN",
        "description": (
            "Ошибка связи сигнала скорости CAN. "
            "Код из таблицы ЭБУ Weichai/Shacman (SPN 84 FMI 19). "
            "На Howo и Sitrak тот же мотор и те же причины."
        ),
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "SPN789_FMI5",
        "aliases": ['SPN 789 FMI 5', '789/5'],
        "brands": ["Howo", "Shacman"],
        "engines": ["WD615", "WP10", "WP12", "WP13", "MC11"],
        "title": "Датчик ABS переднего левого колеса — обрыв",
        "description": "Howo/Shacman WABCO: нет сигнала датчика FL. Обычно зазор, оборванный провод в гофре на балке или грязь на венце.",
        "causes": [
            {"cause": "Оборван/перетёрт жгут датчика на балке или у ступицы", "probability": 45, "oem_part": None},
            {"cause": "Большой зазор датчика до венца, грязь, сбитый венец", "probability": 35, "oem_part": None},
            {"cause": "Неисправен сам датчик ABS", "probability": 20, "oem_part": None},
        ],
        "check_steps": [
            "Прозвонить датчик (обычно 1–2 кОм) и провод до блока ABS.",
            "Проверить зазор до венца и целостность зубьев.",
            "Осмотреть гофру на балке — типичное место обрыва Howo/Shacman.",
        ],
        "severity": "limited",
        "estimated_time_min": 35,
    },
    {
        "code": "SPN790_FMI5",
        "aliases": ['SPN 790 FMI 5', '790/5'],
        "brands": ["Howo", "Shacman"],
        "engines": ["WD615", "WP10", "WP12", "WP13", "MC11"],
        "title": "Датчик ABS переднего правого колеса — обрыв",
        "description": "Нет сигнала FR. Смотреть разъём в ступице и жгут по балке.",
        "causes": [
            {"cause": "Оборван/перетёрт жгут датчика на балке или у ступицы", "probability": 45, "oem_part": None},
            {"cause": "Большой зазор датчика до венца, грязь, сбитый венец", "probability": 35, "oem_part": None},
            {"cause": "Неисправен сам датчик ABS", "probability": 20, "oem_part": None},
        ],
        "check_steps": [
            "Прозвонить датчик (обычно 1–2 кОм) и провод до блока ABS.",
            "Проверить зазор до венца и целостность зубьев.",
            "Осмотреть гофру на балке — типичное место обрыва Howo/Shacman.",
        ],
        "severity": "limited",
        "estimated_time_min": 35,
    },
    {
        "code": "SPN791_FMI5",
        "aliases": ['SPN 791 FMI 5', '791/5'],
        "brands": ["Howo", "Shacman"],
        "engines": ["WD615", "WP10", "WP12", "WP13", "MC11"],
        "title": "Датчик ABS заднего левого колеса — обрыв",
        "description": "Нет сигнала RL. На самосвалах часто рвётся жгут у рессоры.",
        "causes": [
            {"cause": "Оборван/перетёрт жгут датчика на балке или у ступицы", "probability": 45, "oem_part": None},
            {"cause": "Большой зазор датчика до венца, грязь, сбитый венец", "probability": 35, "oem_part": None},
            {"cause": "Неисправен сам датчик ABS", "probability": 20, "oem_part": None},
        ],
        "check_steps": [
            "Прозвонить датчик (обычно 1–2 кОм) и провод до блока ABS.",
            "Проверить зазор до венца и целостность зубьев.",
            "Осмотреть гофру на балке — типичное место обрыва Howo/Shacman.",
        ],
        "severity": "limited",
        "estimated_time_min": 35,
    },
    {
        "code": "SPN792_FMI5",
        "aliases": ['SPN 792 FMI 5', '792/5'],
        "brands": ["Howo", "Shacman"],
        "engines": ["WD615", "WP10", "WP12", "WP13", "MC11"],
        "title": "Датчик ABS заднего правого колеса — обрыв",
        "description": "Нет сигнала RR. Проверить венец ступицы и зазор датчика.",
        "causes": [
            {"cause": "Оборван/перетёрт жгут датчика на балке или у ступицы", "probability": 45, "oem_part": None},
            {"cause": "Большой зазор датчика до венца, грязь, сбитый венец", "probability": 35, "oem_part": None},
            {"cause": "Неисправен сам датчик ABS", "probability": 20, "oem_part": None},
        ],
        "check_steps": [
            "Прозвонить датчик (обычно 1–2 кОм) и провод до блока ABS.",
            "Проверить зазор до венца и целостность зубьев.",
            "Осмотреть гофру на балке — типичное место обрыва Howo/Shacman.",
        ],
        "severity": "limited",
        "estimated_time_min": 35,
    },
    {
        "code": "SPN789_FMI1",
        "aliases": ['SPN 789 FMI 1', '789/1'],
        "brands": ["Howo", "Shacman"],
        "engines": ["WD615", "WP10", "WP12", "WP13", "MC11"],
        "title": "Датчик ABS FL — слишком большой зазор",
        "description": "Сигнал слабый. Подвинуть датчик к венцу, проверить зубья подшипника.",
        "causes": [
            {"cause": "Оборван/перетёрт жгут датчика на балке или у ступицы", "probability": 45, "oem_part": None},
            {"cause": "Большой зазор датчика до венца, грязь, сбитый венец", "probability": 35, "oem_part": None},
            {"cause": "Неисправен сам датчик ABS", "probability": 20, "oem_part": None},
        ],
        "check_steps": [
            "Прозвонить датчик (обычно 1–2 кОм) и провод до блока ABS.",
            "Проверить зазор до венца и целостность зубьев.",
            "Осмотреть гофру на балке — типичное место обрыва Howo/Shacman.",
        ],
        "severity": "limited",
        "estimated_time_min": 35,
    },
    {
        "code": "C0035",
        "aliases": ['C0035'],
        "brands": ["Howo", "Shacman"],
        "engines": ["WD615", "WP10", "WP12", "WP13", "MC11"],
        "title": "Цепь датчика ABS левого переднего колеса",
        "description": "Типичный OBD-код WABCO на Howo/Shacman: датчик или проводка FL.",
        "causes": [
            {"cause": "Оборван/перетёрт жгут датчика на балке или у ступицы", "probability": 45, "oem_part": None},
            {"cause": "Большой зазор датчика до венца, грязь, сбитый венец", "probability": 35, "oem_part": None},
            {"cause": "Неисправен сам датчик ABS", "probability": 20, "oem_part": None},
        ],
        "check_steps": [
            "Прозвонить датчик (обычно 1–2 кОм) и провод до блока ABS.",
            "Проверить зазор до венца и целостность зубьев.",
            "Осмотреть гофру на балке — типичное место обрыва Howo/Shacman.",
        ],
        "severity": "limited",
        "estimated_time_min": 35,
    },
    {
        "code": "C0040",
        "aliases": ['C0040'],
        "brands": ["Howo", "Shacman"],
        "engines": ["WD615", "WP10", "WP12", "WP13", "MC11"],
        "title": "Цепь датчика ABS правого переднего колеса",
        "description": "Датчик или проводка FR.",
        "causes": [
            {"cause": "Оборван/перетёрт жгут датчика на балке или у ступицы", "probability": 45, "oem_part": None},
            {"cause": "Большой зазор датчика до венца, грязь, сбитый венец", "probability": 35, "oem_part": None},
            {"cause": "Неисправен сам датчик ABS", "probability": 20, "oem_part": None},
        ],
        "check_steps": [
            "Прозвонить датчик (обычно 1–2 кОм) и провод до блока ABS.",
            "Проверить зазор до венца и целостность зубьев.",
            "Осмотреть гофру на балке — типичное место обрыва Howo/Shacman.",
        ],
        "severity": "limited",
        "estimated_time_min": 35,
    },
    {
        "code": "P2562",
        "aliases": ['SPN 2791 FMI 2'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11"],
        "title": "Датчик положения актуатора VGT — неверный сигнал",
        "description": "На WP10/WP12/WP13 и MC11 ЭБУ не видит правдоподобное положение геометрии турбины. Поле: после мойки мотора вода в разъёме, либо закисла геометрия.",
        "causes": [
            {"cause": "Заклинила геометрия VGT / нагар на лопатках", "probability": 40, "oem_part": None},
            {"cause": "Обрыв или КЗ цепи актуатора турбины", "probability": 30, "oem_part": None},
            {"cause": "Утечка патрубков / интеркулера или врёт датчик наддува", "probability": 30, "oem_part": None}
        ],
        "check_steps": [
            "Сравнить boost desired vs actual.",
            "Проверить разъём и питание актуатора (после мойки мотора часто вода).",
            "Осмотреть патрубки и люфт вала турбины."
        ],
        "severity": "limited",
        "estimated_time_min": 50,
    },
    {
        "code": "P0403",
        "aliases": ['SPN 2791 FMI 5'],
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11"],
        "title": "Цепь управления клапаном EGR",
        "description": "Обрыв или КЗ актуатора EGR. На Weichai Euro 4/5 клапан часто закисает, ЭБУ видит обрыв при попытке открыть.",
        "causes": [
            {"cause": "Закоксован клапан EGR, не открывается/не закрывается", "probability": 50, "oem_part": None},
            {"cause": "Обрыв или КЗ актуатора / датчика положения EGR", "probability": 30, "oem_part": None},
            {"cause": "Забит охладитель EGR", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Тест клапана сканером Weichai: открыть/закрыть, смотреть позицию.",
            "Проверить разъём и сопротивление актуатора.",
            "Снять клапан, оценить нагар."
        ],
        "severity": "can_drive",
        "estimated_time_min": 55,
    },
    {
        "code": "P0404",
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11"],
        "title": "Клапан EGR — диапазон / производительность",
        "description": "Положение EGR не совпадает с командой. Классика закоксованной тарелки на WP12/WP13.",
        "causes": [
            {"cause": "Закоксован клапан EGR, не открывается/не закрывается", "probability": 50, "oem_part": None},
            {"cause": "Обрыв или КЗ актуатора / датчика положения EGR", "probability": 30, "oem_part": None},
            {"cause": "Забит охладитель EGR", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Тест клапана сканером Weichai: открыть/закрыть, смотреть позицию.",
            "Проверить разъём и сопротивление актуатора.",
            "Снять клапан, оценить нагар."
        ],
        "severity": "can_drive",
        "estimated_time_min": 55,
    },
    {
        "code": "P0090",
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11"],
        "title": "Цепь регулятора давления топлива",
        "description": "Нет управления дозирующим/регулятором на ТНВД. Часто обрыв у блока насоса или сам IMV.",
        "causes": [
            {"cause": "Засор фильтра / сепаратора или подсос воздуха на всасывании", "probability": 40, "oem_part": None},
            {"cause": "Износ ТНВД / дозирующего клапана, не держит давление", "probability": 30, "oem_part": None},
            {"cause": "Утечка high-pressure контура или льющая форсунка в обратку", "probability": 20, "oem_part": None},
            {"cause": "Врёт датчик давления рампы или окислен разъём", "probability": 10, "oem_part": None}
        ],
        "check_steps": [
            "Сравнить rail desired vs actual на холостых и под нагрузкой.",
            "Заменить фильтры, слить отстой, прокачать, искать пузырьки.",
            "Проверить питание 5В / массу / сигнал датчика рампы.",
            "Тест обратки форсунок и герметичность рампы."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "P2146",
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11"],
        "title": "Группа форсунок A — напряжение питания",
        "description": "Питание банка форсунок 1-2-3. На Weichai часто жгут у ГБЦ или конденсатор драйвера.",
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P2149",
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11"],
        "title": "Группа форсунок B — напряжение питания",
        "description": "Питание банка форсунок 4-5-6. Симметрично P2146.",
        "causes": [
            {"cause": "Обрыв / перетирание жгута у ГБЦ или разъёма форсунки", "probability": 45, "oem_part": None},
            {"cause": "Неисправна сама форсунка (обмотка, КЗ на корпус)", "probability": 35, "oem_part": None},
            {"cause": "Отказ канала драйвера в ЭБУ Weichai", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Переставить разъёмы с соседней форсункой — уходит ли код за цилиндром.",
            "Измерить сопротивление обмотки и изоляцию на корпус.",
            "Осмотреть гофру жгута у клапанной крышки Howo/Shacman.",
            "Не менять ЭБУ, пока не исключён жгут."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    },
    {
        "code": "P0472",
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11"],
        "title": "Датчик давления выпуска — низкий сигнал",
        "description": "Обрыв или КЗ на массу датчика давления ОГ / импульсной трубки. Часто забита трубка нагаром.",
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "P0473",
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11"],
        "title": "Датчик давления выпуска — высокий сигнал",
        "description": "КЗ сигнала на питание или забитая импульсная трубка даёт ложный высокий сигнал.",
        "causes": [
            {"cause": "Обрыв или КЗ сигнального провода / разъёма", "probability": 45, "oem_part": None},
            {"cause": "Неисправен сам датчик", "probability": 35, "oem_part": None},
            {"cause": "Нет опорных 5В или плохая масса", "probability": 20, "oem_part": None}
        ],
        "check_steps": [
            "Проверить 5В, массу и сигнал на разъёме при включённом зажигании.",
            "Осмотреть жгут в зоне вибрации и температуры.",
            "Сверить показание с ожидаемым на холодном моторе."
        ],
        "severity": "limited",
        "estimated_time_min": 30,
    },
    {
        "code": "U0102",
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11"],
        "title": "Потеря связи с блоком раздатки / ретардера",
        "description": "На Howo/Shacman с ретардером или раздаткой: нет питания блока или обрыв CAN на раме.",
        "causes": [
            {"cause": "Обрыв/плохой контакт CAN или сопротивление ≠ 60 Ом", "probability": 40, "oem_part": None},
            {"cause": "Нет питания / массы у блока, который должен отвечать", "probability": 35, "oem_part": None},
            {"cause": "Блок вешает шину (вода, КЗ)", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "60 Ом на диагностическом разъёме, зажигание выкл.",
            "Проверить питание и массы целевого блока.",
            "Осмотреть гофру кабины–рамы Howo/Shacman."
        ],
        "severity": "limited",
        "estimated_time_min": 45,
    },
    {
        "code": "P0705",
        "brands": ["Howo", "Shacman", "Weichai"],
        "engines": ["WP10", "WP12", "WP13", "MC11"],
        "title": "Датчик положения селектора КПП (PRNDL)",
        "description": "ЭБУ не видит достоверное положение селектора. Концевики кулисы, разъём на КПП, CAN TCM.",
        "causes": [
            {"cause": "Нет сигнала сцепления / нейтрали (концевик, CAN)", "probability": 45, "oem_part": None},
            {"cause": "Низкое напряжение на TCM", "probability": 30, "oem_part": None},
            {"cause": "Собственные коды коробки", "probability": 25, "oem_part": None}
        ],
        "check_steps": [
            "Считать коды TCM отдельно от двигателя.",
            "Проверить концевик сцепления и CAN ECM↔TCM."
        ],
        "severity": "limited",
        "estimated_time_min": 40,
    }
]
