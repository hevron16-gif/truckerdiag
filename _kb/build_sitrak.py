"""Build knowledge_sitrak.json + knowledge_more.py from extra sources."""
from __future__ import annotations

import json
import re
import sys
from html import unescape
from pathlib import Path

sys.path.insert(0, r"C:\Users\User\source\repos\truckerdiag\api")
from knowledge import lookup, normalize_code  # noqa: E402

KB = Path(r"C:\Users\User\source\repos\truckerdiag\_kb")
API = Path(r"C:\Users\User\source\repos\truckerdiag\api")

FMI_CAUSE = {
    "0": "Значение выше нормы (реальная величина или врёт датчик)",
    "1": "Значение ниже нормы (реальная величина или врёт датчик)",
    "2": "Сигнал прерывистый / недостоверный",
    "3": "КЗ сигнала на питание",
    "4": "КЗ сигнала на массу",
    "5": "Обрыв цепи",
    "6": "Ток выше нормы, КЗ или заклинивший актуатор",
    "7": "Механический отказ узла",
    "8": "Неверная частота / период сигнала",
    "9": "Нет обновления по сети (таймаут CAN)",
    "11": "Неизвестная причина, смотреть сопутствующие коды",
    "12": "Отказ интеллектуального блока",
    "13": "Нет калибровки / конфигурации",
    "14": "Особая неисправность узла",
    "15": "Выше нормального диапазона (слабо)",
    "16": "Выше нормального диапазона (средне)",
    "17": "Ниже нормального диапазона (слабо)",
    "18": "Ниже нормального диапазона (средне)",
    "19": "Ошибка сети / CAN к этому узлу",
}

SYS_BRANDS = {
    "Bosch": (["Howo", "Sitrak", "Weichai"], ["MC11", "MC13", "WP10", "WP12"]),
    "EDC17": (["Howo", "Sitrak", "Weichai"], ["MC11", "MC13"]),
    "EDC17/SCR": (["Howo", "Sitrak"], ["MC11", "MC13"]),
    "CFV/EGR": (["Howo", "Sitrak", "Weichai"], ["MC11", "MC13", "WP13"]),
    "SCR": (["Howo", "Sitrak", "Shacman"], ["MC11", "MC13", "WP12", "WP13"]),
    "SCR_DOSING": (["Howo", "Sitrak", "Shacman"], ["MC11", "MC13", "WP13"]),
    "HH_SCR": (["Howo", "Sitrak"], ["MC11", "MC13"]),
    "AMT": (["Howo", "Sitrak"], ["MC11", "MC13", "WP12"]),
    "AMT_ZF_DTCs": (["Sitrak", "Howo"], ["MC11", "MC13"]),
    "ZF_GearBox": (["Sitrak", "Howo", "Shacman"], ["MC11", "MC13"]),
    "HW-AMT": (["Howo", "Sitrak"], ["MC11", "MC13"]),
    "ABS": (["Howo", "Sitrak", "Shacman"], ["WD615", "WP10", "WP12", "MC11"]),
    "KNORRABS8": (["Howo", "Sitrak"], ["MC11", "MC13"]),
    "ESCABS": (["Howo", "Sitrak"], ["MC11", "MC13"]),
    "KNORREBS": (["Howo", "Sitrak"], ["MC11", "MC13"]),
    "EBS": (["Howo", "Sitrak", "Shacman"], ["MC11", "MC13"]),
    "WABCO_EBS31": (["Howo", "Shacman"], ["WP12", "WP13", "MC11"]),
    "KMAEBS": (["Howo", "Sitrak"], ["MC11", "MC13"]),
    "ZF_Retarder": (["Sitrak", "Howo"], ["MC11", "MC13"]),
    "Voith Retarder": (["Howo", "Sitrak", "Shacman"], ["WP12", "WP13", "MC11"]),
    "FST_Retarder": (["Howo", "Sitrak"], ["MC11", "MC13"]),
    "ECAS": (["Howo", "Sitrak"], ["MC11", "MC13"]),
    "ECAS4PLUS": (["Howo", "Sitrak"], ["MC11", "MC13"]),
    "ECAS_KNORR": (["Howo", "Sitrak"], ["MC11", "MC13"]),
    "BCU": (["Howo", "Sitrak"], ["MC11", "MC13"]),
    "BCM": (["Howo", "Sitrak"], ["MC11", "MC13"]),
    "BCM_HR": (["Howo", "Sitrak"], ["MC11", "MC13"]),
    "NanoBCU": (["Howo", "Sitrak"], ["MC11", "MC13"]),
    "NewBCU": (["Howo", "Sitrak"], ["MC11", "MC13"]),
    "CBCU": (["Howo", "Sitrak"], ["MC11", "MC13"]),
    "VCU": (["Howo", "Sitrak"], ["MC11", "MC13"]),
    "PCU": (["Howo", "Sitrak"], ["MC11", "MC13"]),
    "GatewayBosch": (["Howo", "Sitrak"], ["MC11", "MC13"]),
    "OGP": (["Howo", "Sitrak"], ["MC11", "MC13"]),
    "OGP2": (["Howo", "Sitrak"], ["MC11", "MC13"]),
}


def clean(s: str) -> str:
    s = unescape(s or "")
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\s+", " ", s).strip(" .;")
    s = re.sub(r"^[\d#]+\s*", "", s)
    return s


def taken(raw: str) -> bool:
    return lookup(raw) is not None


def family_of(system: str, desc: str) -> str:
    s = (system + " " + desc).lower()
    if "форсун" in s or "инжектор" in s:
        return "injector"
    if "рамп" in s or "топлив" in s:
        return "rail"
    if "турбин" in s or "наддув" in s or "vgt" in s:
        return "turbo"
    if "egr" in s:
        return "egr"
    if "scr" in s or "мочев" in s or "nox" in s or "adblue" in s:
        return "scr"
    if "can" in s or "шин" in s or "таймаут" in s:
        return "can"
    if "ретардер" in s or "retarder" in s:
        return "retarder"
    if "кпп" in s or "amt" in s or "сцеплен" in s or "передач" in s or "traxon" in s:
        return "trans"
    if "abs" in s or "ebs" in s or "тормоз" in s:
        return "brake"
    if "ecas" in s or "пневмоподвеск" in s or "высот" in s:
        return "air"
    if "масл" in s:
        return "oil"
    if "охлажд" in s or "антифриз" in s:
        return "coolant"
    if "педал" in s:
        return "pedal"
    return "generic"


SEV = {
    "oil": "tow",
    "ckp": "tow",
    "starter": "tow",
    "rail": "limited",
    "injector": "limited",
    "turbo": "limited",
    "can": "limited",
    "trans": "limited",
    "brake": "limited",
    "scr": "limited",
    "egr": "can_drive",
    "air": "limited",
    "retarder": "can_drive",
    "pedal": "limited",
    "coolant": "limited",
    "generic": "limited",
}


def card(code, title, desc, system, fmi, aliases=None, brands=None, engines=None):
    fam = family_of(system or "", desc + " " + title)
    fmi_s = FMI_CAUSE.get(str(fmi), "Неисправность цепи или самого узла")
    brands = brands or ["Howo", "Sitrak", "Shacman"]
    engines = engines or ["MC11", "MC13", "WP12", "WP13"]
    return {
        "code": code,
        "aliases": aliases or [],
        "brands": brands,
        "engines": engines,
        "title": title[:110],
        "description": desc,
        "causes": [
            {"cause": fmi_s, "probability": 45, "oem_part": None},
            {
                "cause": "Обрыв / коррозия разъёма или жгута указанного узла",
                "probability": 35,
                "oem_part": None,
            },
            {
                "cause": "Неисправен сам датчик / клапан / блок",
                "probability": 20,
                "oem_part": None,
            },
        ],
        "check_steps": [
            f"Считать живые данные узла «{title[:60]}».",
            "Проверить питание, массу и разъём, осмотреть жгут.",
            "Сверить с сопутствующими кодами той же системы (сканер Sitrak/Howo).",
        ],
        "severity": SEV.get(fam, "limited"),
        "estimated_time_min": 40,
        "source_system": system or "",
    }


def from_sitrak():
    data = json.loads((KB / "sitrak.json").read_text(encoding="utf-8"))
    out = []
    seen = set()
    for x in data:
        spn = str(x.get("spn") or "").strip()
        fmi = str(x.get("fmi") or "").strip()
        if not spn or not fmi:
            continue
        # skip hex-looking that aren't digits
        if not re.fullmatch(r"\d+", spn.replace("0x", ""), re.I) and not re.fullmatch(r"\d+", spn):
            # allow 0x01
            hx = re.fullmatch(r"0x([0-9a-f]+)", spn, re.I)
            if hx:
                spn = str(int(hx.group(1), 16))
            else:
                continue
        if not re.fullmatch(r"\d+", fmi.replace("0x", ""), re.I):
            hx = re.fullmatch(r"0x([0-9a-f]+)", fmi, re.I)
            if hx:
                fmi = str(int(hx.group(1), 16))
            else:
                continue
        key = f"SPN{spn}_FMI{fmi}"
        if key in seen:
            continue
        seen.add(key)
        if taken(key) or taken(f"SPN {spn} FMI {fmi}") or taken(f"{spn}/{fmi}"):
            continue
        desc = clean(x.get("description_ru") or "")
        if len(desc) < 8 or desc.startswith("Данные действительны"):
            continue
        if desc.lower().startswith("fmi "):
            # description is just FMI text — still usable with system
            desc = f"{x.get('system')}: {desc}"
        sysname = x.get("system") or "Sitrak"
        brands, engines = SYS_BRANDS.get(sysname, (["Howo", "Sitrak"], ["MC11", "MC13"]))
        dtc = clean(str(x.get("dtc") or ""))
        aliases = [f"SPN {spn} FMI {fmi}", f"{spn}/{fmi}"]
        if dtc and dtc not in {"0", "-", "0+0"} and not taken(dtc):
            aliases.append(f"DTC {dtc}")
        title = desc if len(desc) < 90 else desc[:87] + "…"
        title = f"{sysname}: {title}"
        full = (
            f"{desc}. Sitrak/Howo, система {sysname}, SPN {spn} FMI {fmi}. "
            f"Типично на C7H/C9H/T7H с MC11/MC13 и на Howo с тем же блоком."
        )
        out.append(card(key, title, full, sysname, fmi, aliases, brands, engines))
    return out


def from_mega_m():
    html = (KB / "mega-m.html").read_text(encoding="utf-8", errors="ignore")
    text = unescape(re.sub(r"<br\s*/?>", "\n", html, flags=re.I))
    text = re.sub(r"<[^>]+>", "\n", text)
    text = re.sub(r"&nbsp;", " ", text)
    out = []
    # description then P-code
    for m in re.finditer(
        r"([А-Яа-яA-Za-z][^P\n]{12,140}?)\s*\n\s*(P[0-9A-F]{4})\s*\n\s*(\d{1,6})\s*\n\s*(\d{1,2})",
        text,
    ):
        desc, pcode, spn, fmi = m.group(1).strip(), m.group(2), m.group(3), m.group(4)
        desc = clean(desc)
        if taken(pcode):
            continue
        if any(e["code"] == pcode for e in out):
            continue
        aliases = [f"SPN {spn} FMI {fmi}", f"{spn}/{fmi}"]
        out.append(
            card(
                pcode,
                desc[:110],
                f"{desc}. Код Bosch EDC17 на MC11/MC13 (Sitrak/Howo T7H). SPN {spn} FMI {fmi}.",
                "Bosch",
                fmi,
                aliases,
                ["Howo", "Sitrak", "Weichai"],
                ["MC11", "MC13"],
            )
        )
    return out


def from_remont():
    html = (KB / "remontgruz.html").read_text(encoding="utf-8", errors="ignore")
    html = unescape(html.replace("<br />", "\n").replace("<br/>", "\n"))
    out = []
    for m in re.finditer(
        r"SPN\s+(\d+)\s+FMI\s+(\d+)\s*[–—-]\s*([^;<\n]{8,160})",
        html,
        flags=re.I,
    ):
        spn, fmi, desc = m.group(1), m.group(2), clean(m.group(3))
        key = f"SPN{spn}_FMI{fmi}"
        if taken(key) or taken(f"SPN {spn} FMI {fmi}"):
            continue
        if any(e["code"] == key for e in out):
            continue
        out.append(
            card(
                key,
                desc[:110],
                f"{desc}. J1939 SPN {spn} FMI {fmi} — встречается на Howo/Shacman/Weichai и Cummins ISM11.",
                "J1939",
                fmi,
                [f"SPN {spn} FMI {fmi}", f"{spn}/{fmi}"],
                ["Howo", "Shacman", "Weichai"],
                ["WP10", "WP12", "WP13", "ISM11"],
            )
        )
    return out


def from_howo_official():
    extras = [
        (
            "P0227",
            "Сигнал педали ВОМ/PTO слишком высокий",
            "Howo: цепь педали/потенциометра PTO коротнула на питание (23AD10 на 65A-VCC5). ВОМ отключается.",
            "5",
        ),
        (
            "P0228",
            "Сигнал педали ВОМ/PTO слишком низкий",
            "Howo: обрыв цепи педали PTO (23AD10). Функция ВОМ не работает.",
            "5",
        ),
        (
            "P0236",
            "Датчик давления наддува — недостоверный сигнал",
            "Howo: MAP не меняется при изменении нагрузки. ЭБУ глушит круиз. Часто сам датчик или подсос после него.",
            "2",
        ),
        (
            "P1266",
            "Нет нагрузки на подкачивающий насос",
            "Howo common-rail: ЭБУ не видит ток насоса подкачки. Лампа, стоп круиз, лимит топлива 70%. Белая дымка, нет тяги.",
            "5",
        ),
        (
            "P0182",
            "Датчик температуры топлива — низкий сигнал",
            "Howo: обрыв ДТ топлива. На холодную пуск тяжелее, смесь может быть богатой.",
            "4",
        ),
        (
            "P0183",
            "Датчик температуры топлива — высокий сигнал",
            "Howo: КЗ или обрыв NTC топлива (высокое сопротивление = высокая температура).",
            "3",
        ),
    ]
    out = []
    for code, title, desc, fmi in extras:
        if taken(code):
            continue
        out.append(
            card(
                code,
                title,
                desc,
                "Howo",
                fmi,
                [],
                ["Howo", "Sitrak"],
                ["WD615", "WP10", "WP12", "MC11"],
            )
        )
    return out


def from_cummins_ism():
    """Частые Cummins-коды на Shacman ISM11 / ISB."""
    rows = [
        ("CUMMINS_111", ["111"], "Cummins: критическая внутренняя ошибка ЭБУ", "SPN 629 FMI 12 — ECM. Часто после просадки питания или «прикуривания».", "12"),
        ("CUMMINS_115", ["115"], "Cummins: нет сигнала датчика коленвала", "SPN 190. Не заводится. Датчик на картере маховика / венец.", "12"),
        ("CUMMINS_122", ["122"], "Cummins: MAP — высокий сигнал", "Наддув/MAP выше порога. Датчик или КЗ на питание.", "3"),
        ("CUMMINS_123", ["123"], "Cummins: MAP — низкий сигнал", "Обрыв MAP или реальный underboost.", "4"),
        ("CUMMINS_135", ["135"], "Cummins: давление масла — высокий сигнал", "Датчик масла или КЗ.", "3"),
        ("CUMMINS_141", ["141"], "Cummins: давление масла — низкий сигнал", "Обрыв датчика или реально низкое давление — проверить манометром.", "4"),
        ("CUMMINS_143", ["143"], "Cummins: давление масла ниже нормы", "Реальное низкое давление или датчик. Глушить, мерить механикой.", "1"),
        ("CUMMINS_144", ["144"], "Cummins: ДТОЖ — высокий сигнал", "Обрыв NTC ОЖ.", "3"),
        ("CUMMINS_145", ["145"], "Cummins: ДТОЖ — низкий сигнал", "КЗ ДТОЖ на массу.", "4"),
        ("CUMMINS_146", ["146"], "Cummins: перегрев ОЖ", "Реальный перегрев. Уровень, вентилятор, радиатор.", "0"),
        ("CUMMINS_151", ["151"], "Cummins: критический перегрев ОЖ", "Аварийно. Немедленно остановиться.", "0"),
        ("CUMMINS_153", ["153"], "Cummins: IAT — высокий сигнал", "Обрыв датчика воздуха на впуске.", "3"),
        ("CUMMINS_154", ["154"], "Cummins: IAT — низкий сигнал", "КЗ датчика воздуха.", "4"),
        ("CUMMINS_187", ["187"], "Cummins: сенсорное питание 5В низкое", "КЗ 5В на массу, тянет все датчики.", "4"),
        ("CUMMINS_227", ["227"], "Cummins: сенсорное питание 5В высокое", "КЗ 5В на 12/24В.", "3"),
        ("CUMMINS_234", ["234"], "Cummins: превышение оборотов", "Спуск на передаче или ложный CKP.", "0"),
        ("CUMMINS_235", ["235"], "Cummins: низкий уровень ОЖ", "Датчик уровня в расширительном или реальная течь.", "1"),
        ("CUMMINS_415", ["415"], "Cummins: давление масла критически низкое", "Глушить. Манометр, щуп, не ехать.", "1"),
        ("CUMMINS_441", ["441"], "Cummins: напряжение батареи низкое", "АКБ, генератор, массы. 24В система.", "4"),
        ("CUMMINS_442", ["442"], "Cummins: напряжение батареи высокое", "Регулятор генератора.", "3"),
        ("CUMMINS_449", ["449"], "Cummins: давление рампы слишком высокое", "Регулятор / IMV залип, риск трубок.", "0"),
        ("CUMMINS_451", ["451"], "Cummins: датчик рампы — высокий сигнал", "КЗ сигнала датчика rail pressure.", "3"),
        ("CUMMINS_452", ["452"], "Cummins: датчик рампы — низкий сигнал", "Обрыв датчика рампы.", "4"),
        ("CUMMINS_553", ["553"], "Cummins: давление рампы выше нормы", "Регулятор не сбрасывает.", "0"),
        ("CUMMINS_559", ["559"], "Cummins: давление рампы ниже команды", "Фильтры, подсос, ТНВД, IMV. Самый частый на ISM11/ISB Shacman.", "18"),
        ("CUMMINS_1117", ["1117"], "Cummins: просадка питания ЭБУ при стартере", "АКБ, массы, клеммы. Куча ложных кодов следом.", "4"),
        ("CUMMINS_1139", ["1139"], "Cummins: форсунка цилиндра 1 — механическая", "Льёт / не открывается. Тест вкладов.", "7"),
        ("CUMMINS_1141", ["1141"], "Cummins: форсунка цилиндра 2 — механическая", "Аналогично цил. 2.", "7"),
        ("CUMMINS_1142", ["1142"], "Cummins: форсунка цилиндра 3 — механическая", "Аналогично цил. 3.", "7"),
        ("CUMMINS_1143", ["1143"], "Cummins: форсунка цилиндра 4 — механическая", "Аналогично цил. 4.", "7"),
        ("CUMMINS_1144", ["1144"], "Cummins: форсунка цилиндра 5 — механическая", "Аналогично цил. 5.", "7"),
        ("CUMMINS_1145", ["1145"], "Cummins: форсунка цилиндра 6 — механическая", "Аналогично цил. 6.", "7"),
        ("CUMMINS_2215", ["2215"], "Cummins: топливный насос не держит давление", "ТНВД / IMV / питание насоса.", "18"),
        ("CUMMINS_2249", ["2249"], "Cummins: давление рампы ниже минимума", "Как 559, но жёстче. Фильтры и подсос в первую очередь.", "1"),
        ("CUMMINS_2265", ["2265"], "Cummins: датчик топлива в сепараторе — высокий", "Вода в топливе или КЗ датчика воды.", "3"),
        ("CUMMINS_2266", ["2266"], "Cummins: датчик топлива в сепараторе — низкий", "Обрыв датчика воды.", "4"),
        ("CUMMINS_2311", ["2311"], "Cummins: IMV / дозирующий клапан ТНВД", "Цепь или сам клапан. Пара к 559.", "5"),
        ("CUMMINS_2372", ["2372"], "Cummins: фильтр топлива забит (перепад)", "Менять фильтры, слить отстой.", "0"),
        ("CUMMINS_2554", ["2554"], "Cummins: давление картера высокое", "Вентиляция картера / кольца / льющая форсунка.", "0"),
        ("CUMMINS_2771", ["2771"], "Cummins: нет связи с Aftertreatment", "CAN к блоку мочевины/SCR.", "9"),
        ("CUMMINS_2973", ["2973"], "Cummins: MAP недостоверен", "Датчик наддува не соответствует режиму.", "2"),
        ("CUMMINS_3361", ["3361"], "Cummins: форсунка мочевины — цепь", "Обрыв/КЗ дозирующего модуля SCR.", "5"),
        ("CUMMINS_3532", ["3532"], "Cummins: качество мочевины", "Пустой бак, вода, плохой AdBlue, датчик качества.", "2"),
        ("CUMMINS_3597", ["3597"], "Cummins: питание Aftertreatment высокое", "Питание блока SCR.", "3"),
        ("CUMMINS_3616", ["3616"], "Cummins: питание Aftertreatment низкое", "Предохранитель / масса блока SCR.", "4"),
        ("CUMMINS_3714", ["3714"], "Cummins: крутящий момент ограничен (защита)", "Вторичный код — искать первопричину (рампa, наддув, SCR).", "14"),
        ("CUMMINS_3727", ["3727"], "Cummins: DPF — высокое ограничение", "Сажевый забит, реген не идёт.", "0"),
        ("CUMMINS_4152", ["4152"], "Cummins: NOx после катализатора высокий", "SCR не работает: мочевина, форсунка, катализатор.", "0"),
        ("CUMMINS_4677", ["4677"], "Cummins: реагент SCR — уровень низкий", "Заправить AdBlue, проверить датчик уровня.", "1"),
    ]
    out = []
    for code, aliases, title, desc, fmi in rows:
        if taken(code) or any(taken(a) for a in aliases if not a.isdigit()):
            continue
        # numeric alias 111 might be ok
        safe_aliases = [a for a in aliases if not taken(a)]
        out.append(
            card(
                code,
                title,
                desc + " На Shacman X3000 с ISM11 / ISB читается как числовой код Cummins.",
                "Cummins",
                fmi,
                safe_aliases,
                ["Shacman"],
                ["ISM11", "ISB", "ISDe"],
            )
        )
    return out


def main():
    packs = [
        ("sitrak", from_sitrak),
        ("mega-m", from_mega_m),
        ("remontgruz", from_remont),
        ("howo", from_howo_official),
        ("cummins", from_cummins_ism),
    ]
    all_items = []
    seen_codes = set()
    stats = {}
    for name, fn in packs:
        items = fn()
        kept = []
        for e in items:
            c = e["code"]
            if c in seen_codes or taken(c):
                continue
            # drop empty aliases that collide
            e["aliases"] = [a for a in (e.get("aliases") or []) if not taken(a) and a not in seen_codes]
            seen_codes.add(c)
            kept.append(e)
        stats[name] = len(kept)
        all_items.extend(kept)
        print(f"{name}: {len(kept)}")

    out = API / "knowledge_sitrak.json"
    out.write_text(json.dumps(all_items, ensure_ascii=False, indent=None), encoding="utf-8")
    print("wrote", out, "total", len(all_items), "bytes", out.stat().st_size)
    print("stats", stats)


if __name__ == "__main__":
    main()
