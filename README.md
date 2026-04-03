# ART STUDIO VANJA - Zvanični Veb Sajt

Dobrodošli na repozitorijum zvaničnog veb sajta udruženja **ART STUDIO VANJA** - udruženja za vizuelne umetnosti i kulturni razvoj.

## 📋 O projektu

ART STUDIO VANJA je udruženje posvećeno razvoju vizuelnih umetnosti kroz edukativne programe, umetničke projekte i kulturne aktivnosti. Naš fokus je na:

- 🎨 Osnaživanje žena umetnica
- 🌈 Inkluzija osetljivih grupa
- 👶 Umetnički rad sa decom
- 🌿 Očuvanje životne sredine kroz kreativnost
- 🎓 Edukativne radionice (fotografija, crtanje, slikanje, vajanje, keramika)

## 🌐 Struktura sajta

Sajt sadrži sledeće stranice:

- **index.html** - Početna strana (hero, misija, izdvojeni projekti)
- **about.html** - O nama (informacije o udruženju, vizija, misija)
- **founder.html** - Osnivač (biografija, vizija, radovi)
- **team.html** - Naš tim (članovi, saradnici)
- **workshops.html** - Edukativne radionice (crtanje, slikanje, vajanje, keramika, fotografija)
- **projects.html** - Realizovani projekti (sa filterom po godinama, galerija sa lightbox-om)
- **statute.html** - Statut udruženja (sa PDF za preuzimanje)
- **contact.html** - Kontakt (forma, info, Instagram)

## 🛠️ Tehnologije

- **HTML5** - Semantički markup
- **CSS3** - Moderni stilovi (CSS Grid, Flexbox, CSS Variables)
- **JavaScript (Vanilla)** - Interaktivne funkcionalnosti
- **Responsive Design** - Potpuno prilagođen za sve uređaje (mobile-first)
- **Google Fonts** - Playfair Display, Poppins, Kalam

## 🎨 Dizajn

### Glavne boje:
- 🟡 Žuta (#FFD700) - Fotografija
- 🟢 Zelena (#7CB342) - Rad u prirodi
- 🔴 Crvena (#E53935) - Umetnost i slikarstvo
- 🔵 Plava (#1E88E5) - Edukacija
- 🟣 Ljubičasta (#7B1FA2) - Kreativnost
- 🌸 Roze (#C5A5A5) - Glavna brand boja
- 🎨 Peach (#F5E6D3) - Pozadina

### Vizuelni elementi:
- Watercolor gradient pozadine
- Smooth animacije i hover efekti
- Lightbox galerije za fotografije
- Responsive grid layout

## 📁 Struktura fajlova za upload

```
art-studio-vanja/
├── index.html
├── about.html
├── founder.html
├── team.html
├── workshops.html
├── projects.html
├── statute.html
├── contact.html
├── .gitignore
├── README.md
│
├── css/
│   └── style.css
│
├── js/
│   └── main.js
│
├── images/
│   ├── logo.svg
│   ├── hero-placeholder.svg
│   ├── about-image.jpg
│   ├── projects/
│   │   ├── vizantija/          (27 slika, kompresovane ~600KB svaka)
│   │   ├── ples-zivota/        (17 slika, ~200KB svaka)
│   │   ├── reljefi-secesije/   (22 slike, ~230KB svaka)
│   │   └── deciji-svet/        (6 slika, ~200KB svaka)
│   ├── workshops/
│   │   └── (18 kompresovanih fotografija, 500-800KB svaka)
│   └── team/
│       └── (fotografije članova tima)
│
└── documents/
    └── statut.pdf (166KB)
```

## 🚀 Kako uploadovati na GitHub

### 1. Inicijalizuj Git repozitorijum (ako već nije):
```bash
cd "/path/to/Art Studio Vanja"
git init
```

### 2. Dodaj sve fajlove:
```bash
git add .
```

### 3. Kreiraj commit:
```bash
git commit -m "Initial commit - ART STUDIO VANJA website"
```

### 4. Poveži sa GitHub repozitorijumom:
```bash
git remote add origin https://github.com/USERNAME/art-studio-vanja.git
git branch -M main
git push -u origin main
```

## 🌐 Kako postaviti na hosting (Hostinger)

### 1. Fajlovi za upload:
Uploadujte **SVE** fajlove i foldere sa liste iznad **OSIM**:
- ❌ `Info Projekti/` (source fajlovi)
- ❌ `Fotografije/` (source fajlovi)
- ❌ `.claude/` (Claude Code cache)
- ❌ Root `.pdf`, `.doc`, `.docx`, `.png`, `.jpg` fajlovi (screenshots, originalni dokumenti)

### 2. Upload putem FTP/SFTP:
- Konektuj se na Hostinger preko FTP klijenta (FileZilla, Cyberduck)
- Uploaduj sve fajlove u `public_html` folder
- Proveri da struktura foldera ostane ista

### 3. Provera:
- Otvori `yourdomain.com` u browseru
- Testiraj sve stranice
- Proveri da slike i PDF-ovi rade

## ✨ Glavne funkcionalnosti

### Navigacija:
- ✅ Sticky navbar sa scroll efektom
- ✅ Mobile hamburger menu
- ✅ Smooth scrolling

### Projekti:
- ✅ Filter po godinama (2025, 2024, 2020, Sve godine)
- ✅ Modal prozor sa detaljima projekta
- ✅ Galerije sa lightbox-om (klik na sliku → fullscreen prikaz)
- ✅ Navigacija strelicama, tastaturom (← →), swipe na mobilnom

### Radionice:
- ✅ Galerija umetničkih fotografija polaznika
- ✅ Lightbox sa navigacijom
- ✅ "Prikaži sve" dugme (prikazuje skrivene slike)

### Kontakt:
- ✅ Kontakt forma (ime, email, telefon, tema, poruka)
- ✅ Instagram dugme sa linkdirectom
- ✅ Email i telefon info

### Statut:
- ✅ Preuzimanje PDF-a (166KB)
- ✅ Pregled online u browseru

### Lightbox galerija:
- ✅ Fullscreen prikaz fotografija
- ✅ Navigacija: strelice, tastatura, swipe
- ✅ Brojač slika (npr. "5 / 27")
- ✅ ESC za zatvaranje
- ✅ Mobile friendly

## 📊 Optimizacije

### Slike:
- ✅ Sve slike kompresovane (JPEG 75-85%, max 1400-1920px)
- ✅ Projekat Vizantija: smanjen sa ~240MB na 16MB (93% smanjenje)
- ✅ Radionice: slike 500-800KB (sa originalno do 13MB)
- ✅ Lazy loading za brže učitavanje

### Performance:
- ✅ CSS minifikacija moguća
- ✅ JavaScript vanilla (bez biblioteka, brzo)
- ✅ Responsive images
- ✅ SEO optimizovano

## 📱 Responsive Design

Sajt je potpuno responsivan:
- 💻 Desktop (1200px+) - 3 kolone u grid-ovima
- 📱 Tablet (768-992px) - 2 kolone
- 📱 Mobile (< 768px) - 1 kolona, hamburger menu

## 📧 Kontakt Informacije

**Email:** vignjac@gmail.com
**Telefon:** 062 829 56 96
**Web:** [artstudiovanja.com](https://artstudiovanja.com)
**Instagram:** [@art_studio_vanja](https://www.instagram.com/art_studio_vanja)

## 📄 Licenca

© 2026 ART STUDIO VANJA. Sva prava zadržana.

---

## 🔧 Buduća unapređenja (opciono)

- [ ] Google Analytics
- [ ] GDPR Cookie Consent
- [ ] Backend za kontakt formu (PHP/Node.js)
- [ ] Više projekata
- [ ] Blog sekcija
- [ ] Newsletter
- [ ] Multilingualnost (EN/SR)

---

**Verzija:** 1.0
**Datum:** April 2026
**Developed with:** Claude Code by Anthropic
