# quiz_data.py
# Senior darajadagi informatika fani bo'yicha test savollari bazasi.
# Har bir mavzu bo'yicha savollar ro'yxati: matn, variantlar, to'g'ri javob indeksi, tushuntirish.

QUIZ_TOPICS = {
    "algoritmlar": {
        "title": "🧮 Algoritmlar va murakkablik",
        "questions": [
            {
                "question": "Ikkilik qidiruv (binary search) algoritmining vaqt murakkabligi qanday?",
                "options": ["O(n)", "O(log n)", "O(n log n)", "O(n^2)"],
                "correct": 1,
                "explanation": "Har bir qadamda qidiruv maydoni 2 marta qisqaradi, shu sabab O(log n)."
            },
            {
                "question": "Quicksort algoritmining eng yomon holatdagi murakkabligi?",
                "options": ["O(n log n)", "O(n)", "O(n^2)", "O(log n)"],
                "correct": 2,
                "explanation": "Agar pivot har doim noto'g'ri tanlansa (masalan, tartiblangan massivda), murakkablik O(n^2) bo'ladi."
            },
            {
                "question": "Dynamic programming (dinamik dasturlash) qaysi xususiyatga ega masalalarda qo'llaniladi?",
                "options": [
                    "Faqat grafik masalalarida",
                    "Optimal substruktura va bir-biriga bog'liq qism-masalalarda",
                    "Faqat sortirovka masalalarida",
                    "Faqat rekursiv bo'lmagan masalalarda"
                ],
                "correct": 1,
                "explanation": "DP optimal substruktura va overlapping subproblems (takrorlanuvchi qism-masalalar) mavjud bo'lganda samarali."
            },
            {
                "question": "Greedy (ochko'z) algoritmlar har doim optimal yechim beradimi?",
                "options": [
                    "Ha, har doim",
                    "Yo'q, faqat ma'lum shartlar (greedy choice property) bajarilganda",
                    "Faqat grafiklarda",
                    "Faqat kichik massivlarda"
                ],
                "correct": 1,
                "explanation": "Greedy algoritm faqat greedy-choice property va optimal substruktura mavjud bo'lgan masalalarda optimal natija beradi."
            },
            {
                "question": "BFS (Breadth-First Search) qaysi ma'lumotlar tuzilmasidan foydalanadi?",
                "options": ["Stack", "Queue", "Heap", "Hash-jadval"],
                "correct": 1,
                "explanation": "BFS navbat (queue) yordamida daraja bo'yicha (level by level) grafni aylanib chiqadi."
            },
        ]
    },
    "malumotlar_tuzilmalari": {
        "title": "🗂 Ma'lumotlar tuzilmalari",
        "questions": [
            {
                "question": "Bog'langan ro'yxatda (linked list) elementni boshiga qo'shish murakkabligi qanday?",
                "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
                "correct": 0,
                "explanation": "Bosh elementga ishorachini o'zgartirish yetarli, shu sabab O(1)."
            },
            {
                "question": "Stack (steak) ma'lumotlar tuzilmasi qaysi prinsip asosida ishlaydi?",
                "options": ["FIFO", "LIFO", "Random access", "Priority based"],
                "correct": 1,
                "explanation": "Stack — Last In First Out (LIFO) prinsipi asosida ishlaydi."
            },
            {
                "question": "Hash-jadvalda (hash table) collision (to'qnashuv) yuzaga kelganda qanday usullar qo'llaniladi?",
                "options": [
                    "Faqat o'chirish",
                    "Chaining va open addressing",
                    "Faqat qayta hashlash",
                    "Hech qanday usul kerak emas"
                ],
                "correct": 1,
                "explanation": "Chaining (bog'langan ro'yxat orqali) va open addressing (bo'sh joy qidirish) eng ko'p qo'llaniladigan usullar."
            },
            {
                "question": "Ikkilik qidiruv daraxti (BST) da o'rtacha qidiruv murakkabligi qanday?",
                "options": ["O(1)", "O(n)", "O(log n)", "O(n log n)"],
                "correct": 2,
                "explanation": "Muvozanatlashgan BST da har bir qadam daraxt balandligini yarmiga qisqartiradi — O(log n)."
            },
            {
                "question": "Heap (uyum) ma'lumotlar tuzilmasi asosan qaysi masalada ishlatiladi?",
                "options": [
                    "Matnni qidirishda",
                    "Priority queue (ustuvorlik navbati) va sortirovkada",
                    "Faqat grafiklarni saqlashda",
                    "Faqat fayl tizimida"
                ],
                "correct": 1,
                "explanation": "Heap eng katta/eng kichik elementni tez topish kerak bo'lgan priority queue va heap sort kabi masalalarda ishlatiladi."
            },
        ]
    },
    "oop": {
        "title": "🧩 Obyektga yo'naltirilgan dasturlash (OOP)",
        "questions": [
            {
                "question": "Inkapsulyatsiya (encapsulation) tushunchasi nimani anglatadi?",
                "options": [
                    "Bir nechta klassni birlashtirish",
                    "Ma'lumot va metodlarni bitta birlikka joylab, tashqi ta'sirdan himoyalash",
                    "Klasslarni meros qilib olish",
                    "Kodni bir necha faylga bo'lish"
                ],
                "correct": 1,
                "explanation": "Inkapsulyatsiya — ma'lumotlarni yashirish va ularga faqat metodlar orqali kirish imkonini beradi."
            },
            {
                "question": "Polimorfizm (polymorphism) nima uchun kerak?",
                "options": [
                    "Xotira tejash uchun",
                    "Bitta interfeys orqali turli klass obyektlari bilan ishlash uchun",
                    "Kodni tezroq kompilyatsiya qilish uchun",
                    "Faqat konstruktorlar uchun"
                ],
                "correct": 1,
                "explanation": "Polimorfizm bir xil metod nomi orqali turli obyektlarda turlicha xatti-harakatni amalga oshirish imkonini beradi."
            },
            {
                "question": "Meros olish (inheritance) va kompozitsiya (composition) o'rtasidagi asosiy farq nima?",
                "options": [
                    "Farqi yo'q",
                    "Meros — 'is-a', kompozitsiya — 'has-a' munosabat",
                    "Meros faqat interfeyslarda ishlatiladi",
                    "Kompozitsiya faqat statik metodlarda ishlatiladi"
                ],
                "correct": 1,
                "explanation": "Inheritance 'is-a' (masalan, it — hayvon), composition esa 'has-a' (masalan, mashina — motorga ega) munosabatni ifodalaydi."
            },
            {
                "question": "Abstrakt klass va interfeys o'rtasidagi asosiy farq (ko'p tillarda)?",
                "options": [
                    "Abstrakt klass metod implementatsiyasiga ega bo'lishi mumkin, interfeys esa an'anaviy ravishda yo'q",
                    "Interfeys obyekt yarata oladi",
                    "Abstrakt klassdan meros olib bo'lmaydi",
                    "Farqi yo'q, ular bir xil"
                ],
                "correct": 0,
                "explanation": "Abstrakt klasslar qisman implementatsiyaga ega bo'lishi mumkin, interfeyslar odatda faqat metod imzolarini belgilaydi."
            },
            {
                "question": "SOLID prinsiplaridan 'S' harfi nimani anglatadi?",
                "options": [
                    "Single Responsibility Principle",
                    "Simple System Principle",
                    "Static Structure Principle",
                    "Shared State Principle"
                ],
                "correct": 0,
                "explanation": "S — Single Responsibility Principle: har bir klass faqat bitta vazifaga javobgar bo'lishi kerak."
            },
        ]
    },
    "malumotlar_bazasi": {
        "title": "🗄 Ma'lumotlar bazalari",
        "questions": [
            {
                "question": "Normalizatsiya (normalization) nima maqsadda qilinadi?",
                "options": [
                    "Ma'lumotlar bazasini tezlashtirish uchun",
                    "Ma'lumotlar takrorlanishini kamaytirish va yaxlitlikni ta'minlash uchun",
                    "Faqat zaxira nusxa olish uchun",
                    "Faqat foydalanuvchi interfeysini yaxshilash uchun"
                ],
                "correct": 1,
                "explanation": "Normalizatsiya ma'lumotlar takrorlanishini kamaytirib, anomaliyalarning oldini oladi."
            },
            {
                "question": "SQL da PRIMARY KEY va FOREIGN KEY o'rtasidagi farq?",
                "options": [
                    "Farqi yo'q",
                    "PRIMARY KEY jadvalning noyob identifikatori, FOREIGN KEY boshqa jadvalga bog'lanish uchun ishlatiladi",
                    "FOREIGN KEY faqat NULL qiymat qabul qilmaydi",
                    "PRIMARY KEY faqat matn turida bo'ladi"
                ],
                "correct": 1,
                "explanation": "PRIMARY KEY jadvaldagi har bir qatorni noyob aniqlaydi, FOREIGN KEY esa boshqa jadval bilan bog'liqlikni ta'minlaydi."
            },
            {
                "question": "ACID xususiyatlaridan 'I' nimani anglatadi?",
                "options": ["Integration", "Isolation", "Indexing", "Interaction"],
                "correct": 1,
                "explanation": "Isolation — bir vaqtning o'zida bajarilayotgan tranzaksiyalar bir-biriga ta'sir qilmasligini ta'minlaydi."
            },
            {
                "question": "INNER JOIN va LEFT JOIN o'rtasidagi asosiy farq?",
                "options": [
                    "INNER JOIN faqat mos keluvchi qatorlarni qaytaradi, LEFT JOIN chap jadvaldagi barcha qatorlarni qaytaradi",
                    "Farqi yo'q",
                    "LEFT JOIN faqat raqamli ustunlarda ishlaydi",
                    "INNER JOIN faqat bitta jadvalda ishlaydi"
                ],
                "correct": 0,
                "explanation": "LEFT JOIN chap jadvaldagi barcha qatorlarni, mos kelmasa NULL bilan birga qaytaradi."
            },
            {
                "question": "NoSQL ma'lumotlar bazalari qaysi holatlarda afzal hisoblanadi?",
                "options": [
                    "Qat'iy sxema va murakkab tranzaksiyalar kerak bo'lganda",
                    "Katta hajmdagi tuzilmasi o'zgaruvchan ma'lumotlar va gorizontal masshtablash kerak bo'lganda",
                    "Faqat kichik loyihalarda",
                    "Faqat moliyaviy tizimlarda"
                ],
                "correct": 1,
                "explanation": "NoSQL tez o'zgaruvchan sxema, katta hajm va gorizontal masshtablash talab qilinganda qulay."
            },
        ]
    },
    "tarmoqlar_va_os": {
        "title": "🌐 Tarmoqlar va operatsion tizimlar",
        "questions": [
            {
                "question": "TCP va UDP o'rtasidagi asosiy farq nima?",
                "options": [
                    "TCP ulanishga asoslangan va ishonchli, UDP tezroq lekin kafolatsiz",
                    "UDP har doim TCP dan xavfsizroq",
                    "Farqi yo'q",
                    "TCP faqat elektron pochtada ishlatiladi"
                ],
                "correct": 0,
                "explanation": "TCP paketlarni tartib bilan va kafolatlangan holda yetkazadi, UDP esa tezroq, lekin yetkazilishga kafolat bermaydi."
            },
            {
                "question": "OSI modelida nechta qatlam (layer) mavjud?",
                "options": ["5", "6", "7", "8"],
                "correct": 2,
                "explanation": "OSI modeli 7 ta qatlamdan iborat: fizik, kanal, tarmoq, transport, seans, taqdimot, ilova."
            },
            {
                "question": "Operatsion tizimda 'deadlock' (o'lik holat) nima?",
                "options": [
                    "Dastur ishlamay qolishi",
                    "Ikki yoki undan ortiq jarayon bir-birining resursini kutib, hech biri ilgarilay olmasligi",
                    "Xotira to'lib qolishi",
                    "Protsessor haddan tashqari qizib ketishi"
                ],
                "correct": 1,
                "explanation": "Deadlock — jarayonlar bir-birining egallagan resursini kutib, doiraviy bog'liqlik natijasida to'xtab qolishi."
            },
            {
                "question": "Virtual xotira (virtual memory) nima maqsadda ishlatiladi?",
                "options": [
                    "Protsessorni tezlashtirish uchun",
                    "Fizik xotiradan katta manzil maydonini dasturlarga taqdim etish uchun",
                    "Fayllarni siqish uchun",
                    "Tarmoq tezligini oshirish uchun"
                ],
                "correct": 1,
                "explanation": "Virtual xotira disk va RAM yordamida dasturlarga fizik xotiradan kattaroq manzil maydonini taqdim etadi."
            },
            {
                "question": "HTTPS protokoli HTTP dan nimasi bilan farq qiladi?",
                "options": [
                    "Tezroq ishlaydi, lekin xavfsiz emas",
                    "TLS/SSL orqali shifrlangan va xavfsiz aloqa ta'minlaydi",
                    "Faqat rasm yuklashda ishlatiladi",
                    "Farqi yo'q"
                ],
                "correct": 1,
                "explanation": "HTTPS — HTTP protokolining TLS/SSL yordamida shifrlangan xavfsiz versiyasi."
            },
        ]
    },
}
