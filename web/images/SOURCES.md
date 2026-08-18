# Reference images — только расположение узлов

Старые крупные планы деталей перенесены в `old/`.
В галерее остаются только схемы и фото, где видно МЕСТО узла
на двигателе или в системе.

Привязка: `api/knowledge.py` → `CODE_IMAGES`.

## Файлы

| File | Что видно | Источник |
|------|-----------|----------|
| `weichai-wp12-engine-outline.jpg` | Официальный чертёж Weichai WP12 Euro V: рампа на ГБЦ, два фильтра на блоке, турбина, маховик. | Weichai WP12 CR Euro V Maintenance Manual (demo, krutilvertel) |
| `weichai-wp10-cmp-on-engine.jpg` | WP10: датчик распредвала на блоке рядом с топливным фильтром (обведён). | Weichai WP10 National IV O&M, Fig. 4-6, ManualsLib |
| `weichai-wp10-ckp-on-flywheel-housing.jpg` | WP10: датчик коленвала на картере маховика (обведён). | Weichai WP10 National IV O&M, Fig. 4-7, ManualsLib |
| `weichai-wp10-fuel-filter-on-engine.jpg` | Фильтр тонкой очистки на корпусе двигателя Weichai, штуцеры магистрали. | Weichai WP10 National IV O&M, ManualsLib |
| `bosch-cp3-assembly-rails-injectors.jpg` | Сборка CR: ТНВД с дозирующим клапаном, две рампы, датчики на торцах, форсунки. | MotorTrend / Bosch CP3 system photo |
| `bosch-cp3-pump-labeled-diagram.jpg` | Разрез CP3: где на насосе metering / overflow / HP-выход. | Bosch CP3 training diagram |
| `bosch-cp3-metering-on-pump-circuit.jpg` | Схема низкого давления CP3, положение дозирующего клапана. | Bosch CP3 low-pressure circuit |
| `common-rail-on-engine.jpg` | Рампа на моторе: трубы к форсункам, разъём датчика на торце, фильтр ниже. | Учебный разбор (ориентир узлов, не Howo) |
| `common-rail-system-overview.jpg` | Подписанная схема Bosch CR: фильтр, ТНВД, рампа, датчик, форсунки, CKP, CMP. | JYHY Diesel / Bosch training |
| `common-rail-system-layout.png` | Немецкая схема CR с подписями узлов. | Wikimedia Commons |
| `ckp-at-flywheel-ring.jpg` | CKP напротив зубчатого венца маховика. | Autoditex CKP guide |

Отдельного открытого фото Racor Howo A7 «на раме шасси» не нашлось.
На Howo/Shacman с Weichai тонкая очистка стоит на двигателе — это закрыто
фото WP10 и чертежом WP12.

## Коды

| Коды | Набор |
|------|--------|
| P1011 | дозирующий клапан на ТНВД + чертёж WP12 |
| P0087, SPN157, SPN94, P2269 | фильтр на двигателе + схемы CR |
| P0088, P0089, P0093, P0191–P0193 | рампа / датчик на торце рампы |
| P0201–P0203, SPN651 | форсунки на рампе + чертёж WP12 |
| P0335 | CKP на картере маховика WP10 |
| P0340 | CMP на блоке WP10 рядом с фильтром |
