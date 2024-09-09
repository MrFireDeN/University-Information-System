#  Информационная система Вуза

## Описание проекта

Студенты, организованные в группы, учатся на одном из факультетов, возглавляемом деканатом, в функции которого входит контроль за учебным процессом. В учебном процессе участвуют преподаватели кафедр, административно относящиеся к одному из факультетов. Преподаватели подразделяются на следующие категории: ассистенты, преподаватели, старшие преподаватели, доценты, профессора. Ассистенты и преподаватели могут обучаться в аспирантуре, ст. преподаватели, доценты, могут возглавлять научные темы, профессора - научные направления. Преподаватели любой из категории в свое время могли защитить кандидатскую, а доценты и профессора и докторскую диссертацию, при этом преподаватели могут занимать должности доцента и профессора только, если они имеют соответственно звания доцента и профессора. 
Учебный процесс регламентируется учебным планом, в котором указывается, какие учебные дисциплины на каких курсах и в каких семестрах читаются для студентов каждого года набора, с указанием количества часов на каждый вид занятий по дисциплине (виды занятий: лекции, семинары, лабораторные работы, консультации, курсовые работы, ИР и т.д.) и формы контроля (зачет, экзамен). Перед началом учебного семестра деканаты раздают на кафедры учебные поручения, в которых указываются какие кафедры (не обязательно относящиеся к данному факультету), какие дисциплины и для каких групп должны вести в очередном семестре. Руководствуясь ими, на кафедрах осуществляется распределение нагрузки, при этом по одной дисциплине в одной группе разные виды занятий могут вести один или несколько разных преподавателей кафедры (с учетом категории преподавателей, например, ассистент не может читать лекции, а профессор никогда не будет проводить лабораторные работы). Преподаватель может вести занятия по одной или нескольким дисциплинам для студентов как своего, так и других факультетов. Сведения о проведенных экзаменах и зачетах собираются деканатом.
По окончании обучения студент выполняет дипломную работу, руководителем которой является преподаватель с кафедры, относящейся к тому же факультету, где обучается студент, при этом преподаватель может руководить несколькими студентами.
Виды запросов в информационной системе:
1.	Получить перечень и общее число студентов указанных групп либо указанного курса (курсов) факультета полностью, по половому признаку, году рождения, возрасту, признаку наличия детей, по признаку получения и размеру стипендии.
2.	Получить список и общее число преподавателей указанных кафедр либо указанного факультета полностью либо указанных категорий (ассистенты, доценты, профессора и т.д.) по половому признаку, году рождения, возрасту, признаку наличия и количеству детей, размеру заработной платы, являющихся аспирантами, защитивших кандидатские, докторские диссертации в указанный период.
3.	Получить перечень и общее число тем кандидатских и докторских диссертаций, защитивших сотрудниками указанной кафедры либо указанного факультета.
4.	Получить перечень кафедр, проводящих занятия в указанной группе либо на указанном курсе указанного факультета в указанном семестре, либо за указанный период.
5.	Получить список и общее число преподавателей, проводивших (проводящих) занятия по указанной дисциплине в указанной группе либо на указанном курсе указанного факультета.
6.	Получить перечень и общее число преподавателей проводивших (проводящих) лекционные, семинарские и другие виды занятий в указанной группе либо на указанном курсе указанного факультета в указанном семестре, либо за указанный период.
7.	Получить список и общее число студентов указанных групп, сдавших зачет либо экзамен по указанной дисциплине с указанной оценкой.
8.	Получить список и общее число студентов указанных групп или указанного курса указанного факультета, сдавших указанную сессию на отлично, без троек, без двоек.
9.	Получить перечень преподавателей, принимающих (принимавших) экзамены в указанных группах, по указанным дисциплинам, в указанном семестре.
10.	Получить список студентов указанных групп, либо которым заданный преподаватель поставил некоторую оценку за экзамен по определенным дисциплинам, в указанных семестрах, за некоторый период.
11.	Получить список студентов и тем дипломных работ, выполняемых ими на указанной кафедре либо у указанного преподавателя.
12.	Получить список руководителей дипломных работ с указанной кафедры, либо факультета полностью и раздельно по некоторым категориям преподавателей.
13.	Получить нагрузку преподавателей (название дисциплины, количество часов), ее объем по отдельным видам занятий и общую нагрузку в указанном семестре для конкретного преподавателя либо для преподавателей указанной кафедры.

## Описание команды

| Член команды | Свиридов Денис | Чекашов Матвей | Сытников Олег |
| ------------ | -------------- | -------------- | ------------- |
| Основые задачи | Документация | Проектирование | Тестирование |
| Опыт | Знания правил оформления документации | Знание шаблонов проектирования | Умеет писать unit тесты |
| Языки Программирования | Python - хорошо, Django - мало | Python - отлично, Django - отлично | Python - хорошо, Django text - хорошо |

## Описание модели программного процесса

Проект, который предстоит реализовать, имеет ограниченный объем, а команда разработки небольшая и прозрачная. В связи с этим было принято решение использовать гибкую модель процесса разработки вместо более жесткой модели, управляемой планами. Команда выбрала Scrum в качестве основной модели для структурирования разработки программного обеспечения.

Scrum не требует полной документации на начальном этапе разработки, поскольку многие детали проявляются по мере выполнения работы. Учитывая размер проекта и команды, каждый участник может иметь полное представление о ходе проекта благодаря эффективной коммуникации. Это обеспечивается короткими ежедневными неформальными встречами (Daily Scrum), где обсуждается прогресс каждого члена команды.

Все встречи организует и проводит Scrum-мастер, который выполняет роль координатора и помогает команде работать эффективно. Задачи для выполнения выбираются из документа, называемого «product backlog» (список требований), где приоритеты устанавливаются владельцем продукта (в данном случае — командой на встречах по планированию спринта).

Спринты длятся от 14 до 30 дней, что позволяет каждому члену команды примерить на себя разные роли в Scrum с ротацией в начале каждого спринта. Каждый спринт разбивает продукт на функциональные блоки, которые могут быть завершены и протестированы по окончании каждой итерации. После каждого спринта команда собирается на встречу по обзору спринта (Sprint Review), чтобы обсудить выполненные задачи. Перед началом следующего спринта также проводится ретроспектива спринта, где обсуждаются успехи и возможные улучшения процесса работы.
