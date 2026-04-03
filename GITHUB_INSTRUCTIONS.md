# Упутство за постављање на GitHub

Ово упутство ће вам помоћи да поставите **АРТ СТУДИО ВАЊА** веб сајт на GitHub и омогућите GitHub Pages за preview.

## 📋 Предуслови

1. GitHub налог (ако немате, направите на [github.com](https://github.com))
2. Git инсталиран на вашем рачунару

### Провера да ли имате Git

Отворите Terminal (Command Prompt на Windows) и откуцајте:

```bash
git --version
```

Ако видите верзију (нпр. `git version 2.x.x`), Git је инсталиран.

Ако није, преузмите са: [https://git-scm.com/downloads](https://git-scm.com/downloads)

## 🚀 Корак по корак упутство

### 1. Креирање новог репозиторијума на GitHub

1. Идите на [github.com](https://github.com) и пријавите се
2. Кликните на "+" икону горе десно → "New repository"
3. Попуните детаље:
   - **Repository name:** `art-studio-vanja`
   - **Description:** "Званични веб сајт АРТ СТУДИО ВАЊА - удружење за визуелне уметности"
   - **Public/Private:** Изаберите **Public** (за GitHub Pages)
   - **НЕ** чекирајте "Initialize with README" (већ имамо README.md)
4. Кликните "Create repository"

### 2. Повезивање локалног пројекта са GitHub-ом

Отворите Terminal/Command Prompt и навигирајте до фолдера пројекта:

```bash
cd "/Users/nemanjakacar/Downloads/Art Studio Vanja"
```

**ВАЖНО:** Пре него што наставите, извршите следеће команде:

#### Иницијализуј Git репозиторијум

```bash
git init
```

#### Додај све фајлове

```bash
git add .
```

#### Направи први commit

```bash
git commit -m "Initial commit: АРТ СТУДИО ВАЊА website preview

- Додате HTML странице (home, about, projects, statute, contact)
- Креиран responsive CSS дизајн
- Имплементиране JavaScript функционалности
- Додате placeholder слике
- Креиран README са документацијом"
```

#### Повежи са GitHub репозиторијумом

**ВАЖНО:** Замените `ваше-корисничко-име` са вашим GitHub корисничким именом!

```bash
git remote add origin https://github.com/ваше-корисничко-име/art-studio-vanja.git
```

#### Пошаљи код на GitHub

За нове верзије Git-а (2.28+):

```bash
git branch -M main
git push -u origin main
```

За старије верзије Git-а:

```bash
git branch -M master
git push -u origin master
```

### 3. Омогућавање GitHub Pages

1. Идите на ваш GitHub репозиторијум
2. Кликните на **Settings** (tab на врху)
3. У левом менију, кликните на **Pages**
4. У секцији **Source**:
   - Изаберите **main** (или **master**) branch
   - Оставите folder на **/ (root)**
5. Кликните **Save**

**Сачекајте 1-2 минута** док GitHub не направи сајт!

### 4. Приступ сајту

Ваш сајт ће бити доступан на:

```
https://ваше-корисничко-име.github.io/art-studio-vanja/
```

GitHub ће вам показати тачну URL адресу у Settings → Pages након што се сајт објави.

## 📝 Како ажурирати сајт

Када направите промене на сајту локално, следите ове кораке:

### 1. Додај измењене фајлове

```bash
git add .
```

### 2. Направи commit са описом измена

```bash
git commit -m "Опис ваших измена"
```

Примери добрих commit порука:
- `"Додате фотографије пројеката из 2025"`
- `"Ажуриран статут удружења"`
- `"Измењена контакт информација"`

### 3. Пошаљи промене на GitHub

```bash
git push
```

Сајт ће се аутоматски ажурирати за 1-2 минута!

## 🔧 Корисне Git команде

### Провера статуса

Види које су датотеке измењене:

```bash
git status
```

### Историја измена

Види све commit-е:

```bash
git log --oneline
```

### Повлачење промена са GitHub-а

Ако радите са другог рачунара или неко други мења сајт:

```bash
git pull
```

## 🌐 Повезивање саCustom доменом (artstudiovanja.com)

Када набавите дomen `artstudiovanja.com`, повежите га са GitHub Pages:

### 1. Подешавање DNS-а на Hostinger-у

1. Пријавите се на Hostinger
2. Идите на DNS/Nameservers управљање за `artstudiovanja.com`
3. Додајте следеће A records:

```
Type: A
Name: @
Value: 185.199.108.153

Type: A
Name: @
Value: 185.199.109.153

Type: A
Name: @
Value: 185.199.110.153

Type: A
Name: @
Value: 185.199.111.153
```

4. Додајте CNAME record за www:

```
Type: CNAME
Name: www
Value: ваше-корисничко-име.github.io
```

### 2. Додавање Custom Domain на GitHub

1. У фолдеру пројекта направите фајл `CNAME` (БЕЗ екстензије):

```bash
echo "artstudiovanja.com" > CNAME
```

2. Commit и push:

```bash
git add CNAME
git commit -m "Add custom domain"
git push
```

3. На GitHub → Settings → Pages → Custom domain:
   - Унесите: `artstudiovanja.com`
   - Кликните **Save**
   - Чекирајте **Enforce HTTPS** (можда ће требати сачекати 24 часа)

**Напомена:** DNS промене могу трајати 24-48 сати да се пропагирају.

## 📧 Потреба за помоћ?

Ако наиђете на проблеме:

1. Проверите да ли сте правилно откуцали команде
2. Уверите се да сте заменили `ваше-корисничко-име` са вашим GitHub корисничким именом
3. Проверите да ли имате интернет конекцију
4. Консултујте се са програмером или IT стручњаком

## ✅ Checklist

- [ ] Git инсталиран
- [ ] GitHub налог креиран
- [ ] Нови репозиторијум направљен на GitHub-у
- [ ] Локални пројекат повезан са GitHub-ом
- [ ] Код послат на GitHub (`git push`)
- [ ] GitHub Pages омогућен
- [ ] Сајт је доступан на `.github.io` адреси
- [ ] Preview послат клијенту

---

**Срећно са постављањем сајта! 🎨**
