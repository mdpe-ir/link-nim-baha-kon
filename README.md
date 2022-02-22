<div align="center">

# 👀 لینک هات رو نیم بها کن 💡

:) با این اسکریپت خیلی راحت تمام لینک هارو چه خارجی و داخلی میتونی نیم بها کنی ،فقط لازمه نصبش و بعد لینکت رو بهش بدی

</div>
<div dir="rtl">

## فهرست

- [نسخه ی PWA ](https://github.com/mdpe-ir/link-nim-baha-kon#%D9%86%D8%B3%D8%AE%D9%87-%DB%8C-pwa)
  
- [نسخه ی وب (توصیه شده) ](https://github.com/mdpe-ir/link-nim-baha-kon#%D9%86%D8%B3%D8%AE%D9%87-%DB%8C-%D9%88%D8%A8-%D8%AA%D9%88%D8%B5%DB%8C%D9%87-%D8%B4%D8%AF%D9%87)
  
- [اسکریپت](https://github.com/mdpe-ir/link-nim-baha-kon#%D9%86%D8%B5%D8%A8-%D9%88-%D8%A7%D8%AC%D8%B1%D8%A7%DB%8C-%D8%A7%D8%B3%DA%A9%D8%B1%DB%8C%D9%BE%D8%AA-)
   
 - [راهنما](https://github.com/mdpe-ir/link-nim-baha-kon#%D8%B1%D8%A7%D9%87%D9%86%D9%85%D8%A7)
   
- [لیست انجام کار](https://github.com/mdpe-ir/link-nim-baha-kon#%D9%84%DB%8C%D8%B3%D8%AA-%D8%A7%D9%86%D8%AC%D8%A7%D9%85-%DA%A9%D8%A7%D8%B1-)

 - [مشارکت](https://github.com/mdpe-ir/link-nim-baha-kon#%D9%85%D8%B4%D8%A7%D8%B1%DA%A9%D8%AA-)

- [حمایت](https://github.com/mdpe-ir/link-nim-baha-kon#%D8%AD%D9%85%D8%A7%DB%8C%D8%AA)

   
## نسخه ی PWA
  
 ### معرفی


 این نسخه با استفاده از فریم ورک فلاتر توسعه داده شده است و قابلیت نصب بر روی تمام سیستم عامل ها را به صورت وب اپلیکیشن دارد

برای استفاده از این نسخه کافیه وارد لینک زیر شوید :

https://link-nim-baha-kon.pages.dev

[سورس کد نسخه ی PWA](https://github.com/mdpe-ir/link-nim-baha-kon/tree/mdpe-ir-flutter-gui/linknimbahakonFlutterCode)
  
  
 
## نسخه ی وب (توصیه شده)

 ### معرفی


 این نسخه با استفاده از html , css , js توسعه داده شده است و شما میتوانید با استفاده از این سایت بدون محدودیت تعداد لینک های خود را به صورت گروهی و هم زمان در سریع ترین زمان ممکن نیم بها کنید

برای استفاده از این نسخه کافیه وارد لینک زیر شوید :

https://nimbahakon.pages.dev

[سورس کد نسخه ی WEB](https://github.com/mdpe-ir/link-nim-baha-kon/tree/gh-page)
  
  
 
  
## نصب و اجرای اسکریپت 🧰🛠

### پیش نیاز ها 🔌

این اسکریپت برای اجرا نیاز به پیش نیاز هایی دارد..

#### پایتون 🐍

**لینوکس 🐧** پایتون در اکثر توزیع های گنو/لینوکس از پیش نصب است ،اما در صورتی که نصب نبود میتونید با استفاده از پکیج منیجرتون اون رو نصب کنید.

**ویندوز 🖼** در ویندوز برای نصب پایتون لازم است به وبسایت پایتون مراجعه کنید... [python.org](https://python.org)

#### پیش نیاز های داخلی

برای اجرای این اسکریپت نیاز به چند کتابخانه پایتونی است که میتوانید با استفاده از دستورات زیر آنها را نصب کنید :

##### نصب پیش نیاز ها در لینوکس

<div dir="ltr">

```
pip3 install termcolor
pip3 install requests
```

</div>

##### نصب پیش نیاز ها در توزیعات آرچ بیس

<div dir="ltr">

```
sudo pip3 install termcolor
sudo pip3 install requests
```

</div>

##### نصب پیش نیاز ها در ویندوز

<div dir="ltr">

```
pip install termcolor
pip install requests
```

</div>

### اجرا ♨️

1. کلون کردن ریپو
  در اولین مرحله لازم است ریپو پروژه را کلون کنید اما در صورتی که گیت را نصب ندارید میتوانید مستقیما از گیتهاب دانلود کنید... **[دانلود](https://github.com/mdpe-ir/link-nim-baha-kon/archive/refs/heads/main.zip)**
2. اجرای اسکریپت
  در این مرحله وارد پوشه ای که کلون کرده اید شوید و سپس با استفاده از دستور زیر اسکریپت را اجرا کنید :

<div dir="ltr">

```
Linux:
python3 LinkNimbahakon.py
Windows:
python LinkNimbahakon.py
```

</div>

برای راحت تر استفاده کردن از این برنامه در سیستم های لینوکس میتونید از دستورات زیر استفاده کنید:

<div dir="ltr">

```
sudo chmod +x LinkNimbahakon.py 
sudo cp -T  LinkNimbahakon.py  /usr/bin/LinkNimbahakon
# Then run program with:
LinkNimbahakon
```

</div>

## راهنما

شما میتوانید در بخش input یک لینک یا آدرس یک فایل .txt را که در هر خط یک لینک قرار دارد را وارد کنید

## لیست انجام کار ✔

<div dir="ltr">

- [ ] Create gui app
- [x] add bulk links https://github.com/mdpe-ir/link-nim-baha-kon/issues/7

</div>

---

## مشارکت 🤝

این پروژه تحت پروانه GPL نسخه 3 منتشر و نگه‌داری می‌شود و از این‌جهت، هرکسی می‌تواند در صورت نیاز اقدام به مشارکت برای اصلاح یا بهبود یا حتی اضافه کردن ویژگی های جدید به این پروژه کند، همچنین ایجاد فورک های مختلف از پروژه و توسعه پروژه در شاخه‌ای جدا، چه به‌صورت رایگان و چه به‌صورت تجاری، هیچگونه مانعی ندارد.

</div>
<div align="center">

---

## حمایت

<a href="http://www.coffeete.ir/mdpe-ir">
       <img src="http://www.coffeete.ir/images/buttons/lemonchiffon.png" style="width:260px;" />
</a>

---

توسعه داده شده با ❤️ توسط [Mdpe](https://github.com/mdpe-ir) و [مشارکت کنندگان](https://github.com/mdpe-ir/link-nim-baha-kon/graphs/contributors). 1400 ©

💪 قدرت گرفته از [دیجیتال‌بام](https://www.digitalbam.ir)
