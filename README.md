# 🚀 Telethon Telegram Webhook Service

خدمة احترافية وجاهزة للاستخدام الفوري - اسحب، اعدّ، وشغّل!

![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ⚡ البدء السريع (10 دقايق)

### الخطوة 1️⃣: استنساخ المشروع

```bash
git clone https://github.com/e48981652-hash/telethon-webhook-service.git
cd telethon-webhook-service
```

### الخطوة 2️⃣: إنشاء ملف البيانات

```bash
cat > .env << 'EOF'
TELEGRAM_API_ID=your_api_id_here
TELEGRAM_API_HASH=your_api_hash_here
TELEGRAM_PHONE=+20xxxxxxxxx
SESSION_NAME=sessions/telethon_session
SERVER_PORT=8000
SERVER_HOST=0.0.0.0
WEBHOOK_URL=http://localhost:8000/webhook/telegram
N8N_WEBHOOK_URL=
EOF
```

### الخطوة 3️⃣: الحصول على بيانات Telegram

1. اذهب إلى https://my.telegram.org
2. ادخل بحسابك
3. اختر "API development tools"
4. انسخ:
   - `api_id` → ضعه في `TELEGRAM_API_ID`
   - `api_hash` → ضعه في `TELEGRAM_API_HASH`
5. رقمك (مع +): `+20xxxxxxxxx` → ضعه في `TELEGRAM_PHONE`

**مثال:**
```env
TELEGRAM_API_ID=123456789
TELEGRAM_API_HASH=abcdef1234567890abcdef1234567890
TELEGRAM_PHONE=+201001234567
```

---

## 🔐 إنشاء Session (خطوة مهمة جداً!)

هذه الخطوة **إلزامية** للمرة الأولى فقط - تفعيل الحساب على Telegram:

### الخطوة 1️⃣: شغّل برنامج الـ Setup

```bash
docker run --rm -it \
  -v $(pwd):/app \
  --env-file .env \
  drhema9/telethon-webhook-service:latest \
  python3 setup_session.py
```

### الخطوة 2️⃣: ادخل البيانات

تشوف:
```
============================================================
🔐 Telethon Session Setup
============================================================
📱 Phone: +201001234567
📁 Session: sessions/telethon_session.session
============================================================

🔗 جاري الاتصال بـ Telegram...
⏳ برجاء الانتظار...

الرجاء إدخال رقم الهاتف:
```

**اكتب رقمك (موجود بالفعل، بس أكدّ):**
```
+201001234567
```

### الخطوة 3️⃣: ادخل الكود

تشوف:
```
تحقق من حسابك على Telegram وأرسل الكود بهنا
الرجاء إدخال الكود:
```

**روح على Telegram واسحب الكود:**
- فتح Telegram
- ابحث عن "Telegram" من الحسابات الرسمية
- خذ الكود (6 أرقام)
- أرجع للـ Terminal واكتبه:
```
123456
```

### الخطوة 4️⃣: النجاح! ✅

تشوف:
```
============================================================
✅ تم التفعيل بنجاح!
============================================================

👤 User ID: 123456789
👤 User Name: Your Name
📁 Session File: sessions/telethon_session.session

✨ الخدمة جاهزة للاستخدام!
```

### الخطوة 5️⃣: تأكد من الملف

```bash
ls -la sessions/
```

تشوف:
```
telethon_session.session
telethon_session.session-journal
```

---

## 🚀 بدء الخدمة

الآن بعد إنشاء الـ Session، شغّل الخدمة:

```bash
docker-compose up -d
```

### التحقق

```bash
curl http://localhost:8000/health
```

**تشوف:**
```json
{
  "status": "healthy",
  "telethon_ready": true,
  "server": "0.0.0.0:8000"
}
```

**يعني كل حاجة تمام ✅**

---

## 📚 استخدام الخدمة

### إرسال رسالة لـ Telegram

```bash
curl -X POST http://localhost:8000/send-message \
  -H "Content-Type: application/json" \
  -d '{
    "chat_id": 123456789,
    "message": "مرحبا من الخدمة!"
  }'
```

**ملاحظة:** استبدل `123456789` برقم Chat ID بتاعك

### الحصول على Chat ID

1. ابعت رسالة لـ بوت: https://t.me/userinfobot
2. البوت بيبعت لك الـ ID

### الحصول على سجل الرسائل

```bash
curl http://localhost:8000/messages/log
```

### عرض الإعدادات

```bash
curl http://localhost:8000/config
```

### عرض الـ API Documentation

```
http://localhost:8000/docs
```

(Swagger UI - اضغط على الرابط في المتصفح)

---

## 🔗 الربط مع n8n

### في n8n:

1. **New Workflow**
2. **أضف Webhook node:**
   - Method: POST
   - Path: `/telegram`
3. **أضف HTTP Request node:**
   - Method: POST
   - URL: `http://your-server-ip:8000/send-message`
   - Headers: `Content-Type: application/json`
   - Body:
   ```json
   {
     "chat_id": "{{ $json.chat_id }}",
     "message": "{{ $json.message }}"
   }
   ```
4. **Save وفعّل الـ Webhook**

### Test من n8n:

اضغط "Send test data":
```json
{
  "chat_id": 123456789,
  "message": "رسالة من n8n"
}
```

---

## 📝 أوامر مهمة

### شغّل الخدمة

```bash
docker-compose up -d
```

### أوقف الخدمة

```bash
docker-compose down
```

### شوف السجلات

```bash
docker-compose logs -f
```

### إعادة تشغيل

```bash
docker-compose restart
```

### دخول الـ Container

```bash
docker-compose exec telethon-webhook bash
```

### حذف البيانات وإعادة البدء

```bash
docker-compose down
rm -rf sessions/*.session*
docker run --rm -it \
  -v $(pwd):/app \
  --env-file .env \
  YOUR-USERNAME/telethon-webhook-service:latest \
  python3 setup_session.py
docker-compose up -d
```

---

## 🧪 اختبارات سريعة

### فحص الصحة

```bash
curl http://localhost:8000/health
```

### إرسال رسالة اختبار

```bash
curl -X POST http://localhost:8000/send-message \
  -H "Content-Type: application/json" \
  -d '{"chat_id": YOUR_CHAT_ID, "message": "اختبار"}'
```

### شوف كل الرسائل المستقبلة

```bash
curl http://localhost:8000/messages/log
```

### شوف رسائل من chat معين

```bash
curl http://localhost:8000/messages/log/123456789
```

---

## 📁 هيكل المشروع

```
telethon-webhook-service/
├── docker-compose.yml         # تشغيل الخدمة
├── setup_session.py           # إنشاء Session (مهم جداً)
├── README.md                  # هذا الملف
├── LICENSE                    # الترخيص (MIT)
├── sessions/                  # مجلد السيشن
│   └── telethon_session.session    # ملف السيشن (بعد الإنشاء)
└── logs/                      # مجلد السجلات
```

---

## 🐛 استكشاف الأخطاء

### المشكلة: "Telethon client not ready"

**الحل:**
```bash
# شوف السجلات
docker-compose logs

# انتظر 30 ثانية بعد البدء

# أعد التشغيل
docker-compose restart
```

### المشكلة: "python3: can't find setup_session.py"

**الحل:**
```bash
# تأكد إن الملف موجود
ls setup_session.py

# استخدم الأمر الصحيح
docker run --rm -it \
  -v $(pwd):/app \
  --env-file .env \
  YOUR-USERNAME/telethon-webhook-service:latest \
  python3 setup_session.py
```

### المشكلة: خطأ في البيانات

**الحل:**
```bash
# تأكد من البيانات صحيحة
cat .env

# جرّب إعادة البدء
docker-compose down
docker-compose up -d
```

### المشكلة: Port 8000 مشغول

**الحل:**
اعمل `.env` وغيّر:
```env
SERVER_PORT=9000
```

بعدين:
```bash
docker-compose up -d
```

### المشكلة: "could not find Docker image"

**الحل:**
```bash
# pull الـ Image أولاً
docker pull YOUR-USERNAME/telethon-webhook-service:latest

# بعدين
docker-compose up -d
```

---

## ✨ الميزات

✅ **سهلة جداً** - اسحب، اعدّ، وشغّل
✅ **آمنة** - بيانات محلية بس
✅ **سريعة** - Image خفيف ومستقر
✅ **API كاملة** - الإرسال والاستقبال والسجلات
✅ **n8n Compatible** - ربط كامل مع n8n
✅ **Health Checks** - مراقبة تلقائية
✅ **Setup بسيط** - ملف واحد للإعداد

---

## 📚 الـ API الكاملة

### الـ Endpoints

| الـ Method | الـ URL | الوصف |
|-----------|--------|-------|
| GET | `/health` | فحص الصحة |
| GET | `/` | الصفحة الرئيسية |
| GET | `/config` | الإعدادات |
| GET | `/status` | حالة الخدمة |
| POST | `/send-message` | إرسال رسالة |
| POST | `/webhook/telegram` | استقبال من n8n |
| GET | `/messages/log` | السجلات |
| GET | `/messages/log/{chat_id}` | رسائل من chat |
| DELETE | `/messages/log` | مسح السجل |
| GET | `/docs` | Swagger Documentation |

---

## 🔒 الأمان

⚠️ **تحذيرات مهمة:**

✅ **لا تشارك `.env`** - يحتوي على بيانات حساسة
✅ **لا تشارك `sessions/` folder** - بيانات التسجيل
✅ **استخدم HTTPS** في الإنتاج
✅ **قيّد الـ Access** بـ firewall

---

## 💾 حفظ البيانات

البيانات محفوظة في:

```
sessions/telethon_session.session    # بيانات Telegram
logs/                                 # السجلات
```

**لو حذفت `sessions/`:** بتحتاج تشغّل `setup_session.py` تاني

---

## 🚀 التحديثات

لو عاوز آخر نسخة:

```bash
docker pull drhema9/telethon-webhook-service:latest
docker-compose up -d
```

---

## 📞 الدعم

### شوف السجلات

```bash
docker-compose logs -f
```

### دخول الـ Container

```bash
docker-compose exec telethon-webhook bash
```

---

## 🔧 متطلبات التشغيل

- **Docker** (20.10+)
- **Docker Compose** (1.29+)
- **حساب Telegram** (نشط)
- **رقم هاتفك** (لـ التفعيل الأول)

### التثبيت

**Windows/Mac:**
- https://www.docker.com/products/docker-desktop

**Linux:**
```bash
curl -fsSL https://get.docker.com | sh
```

---

## 📄 الترخيص

MIT License - استخدم بحرية!

---

## 💡 نصائح

1. **احفظ `.env` محليك** - ما تشاركه
2. **استخدم `curl` للتجربة** - سهل وسريع
3. **فعّل `docker-compose logs -f`** - للمراقبة
4. **شوف `/docs` endpoint** - للـ API documentation
5. **الـ Setup مرة واحدة** - بعدها خدمة مستقرة 24/7

---

## 🎯 الخطوات التفصيلية

### أول مرة (Setup كامل)

```bash
# 1. اسحب الريبو
git clone https://github.com/YOUR-USERNAME/telethon-webhook-service.git

# 2. ادخل الفولدر
cd telethon-webhook-service

# 3. اعمل .env وملي البيانات
nano .env

# 4. إنشاء Session (مهم جداً!)
docker run --rm -it \
  -v $(pwd):/app \
  --env-file .env \
  YOUR-USERNAME/telethon-webhook-service:latest \
  python3 setup_session.py

# 5. شغّل الخدمة
docker-compose up -d

# 6. اختبر
curl http://localhost:8000/health
```

### الاستخدام اليومي

```bash
# شغّل
docker-compose up -d

# اسحب الرسائل
curl http://localhost:8000/messages/log

# أرسل رسالة
curl -X POST http://localhost:8000/send-message \
  -H "Content-Type: application/json" \
  -d '{"chat_id": 123, "message": "مرحبا"}'

# أيقف
docker-compose down
```

---

## 🎉 الآن جاهز!

الخدمة شغّالة واستعملها مع n8n أو أي تطبيق!

---

**آخر تحديث:** 11/2025
**النسخة:** 2.0.0
**المصدر:** https://github.com/e48981652-hash/telethon-webhook-service
