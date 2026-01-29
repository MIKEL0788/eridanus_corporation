# Eridanus Corporation

## 👥 Équipe

- **Mike** → `branch_mike`
- **Komoé** → `branch_komoe`
- **Yakoub** → `branch_yacoub`
- **Sery** → `branch_sery`

---

## 📋 Qui fait quoi ?

| Page/Composant | Développeur | Branche |
|----------------|-------------|---------|
| **Accueil** | Mike | `branch_mike` |
| **Portfolio** | Mike | `branch_mike` |
| **À propos** | Komoé | `branch_komoe` |
| **Contact** (page) | Komoé | `branch_komoe` |
| **Contact** (formulaire) | Yakoub | `branch_yacoub` |
| **Navbar** | Yakoub | `branch_yacoub` |
| **Services** | Sery | `branch_sery` |
| **Footer** | Sery | `branch_sery` |

> 💡 **Backend** : Chacun fait le backend de ses pages (views, models, urls)

---

📁 Structure du Projet
eridanus-corporation/
│
├── 📂 main_app/                    # Application principale Django
│   ├── 📂 templates/
│   │   ├── 📂 pages/
│   │   │   ├── index.html          (Mike)
│   │   │   ├── about.html          (Komoé)
│   │   │   ├── contact.html        (Yacoub)
│   │   │   ├── services.html       (Sery)
│   │   │   └── portfolio.html      (Mike)
│   │   │
│   │   ├── 📂 includes/
│   │   │   ├── navbar.html         (Yacoub)
│   │   │   └── footer.html         (Sery)
│   │   │
│   │   └── base.html               (Template de base - commun)
│   │
│   ├── 📂 static/
│   │   ├── 📂 css/
│   │   │   ├── index.css           (Mike)
│   │   │   ├── about.css           (Komoé)
│   │   │   ├── contact.css         (Yacoub)
│   │   │   ├── services.css        (Sery)
│   │   │   ├── portfolio.css       (Mike)
│   │   │   └── style.css           (Styles communs)
│   │   │
│   │   ├── 📂 js/
│   │   │   ├── index.js            (Mike)
│   │   │   ├── about.js            (Komoé)
│   │   │   ├── contact.js          (Yacoub)
│   │   │   ├── services.js         (Sery)
│   │   │   └── main.js             (JS commun)
│   │   │
│   │   └── 📂 images/
│   │
│   ├── views.py                    (Tous - chacun ses vues)
│   ├── models.py                   (Tous - chacun ses modèles)
│   ├── urls.py                     (Tous - chacun ses routes)
│   └── forms.py                    (Si formulaires nécessaires)
│
├── 📂 config/                      # Configuration Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔧 Installation et Configuration

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/VOTRE-USERNAME/VOTRE-REPO.git
cd VOTRE-REPO
```

### 2️⃣ Créer un environnement virtuel

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4️⃣ Lancer le serveur

```bash
python manage.py migrate
python manage.py runserver
```

Ouvrir : http://127.0.0.1:8000/

---

## 🌿 Workflow Git

### ✅ Les branches sont déjà créées !

Chacun travaille sur sa branche :
- Mike → `branch_mike`
- Komoé → `branch_komoe`
- Yakoub → `branch_yakou`
- Sery → `branch_sery`

### Comment travailler ?

#### 1️⃣ Aller sur votre branche

```bash
# Mike
git checkout branch_mike

# Komoé
git checkout branch_komoe

# Yakoub
git checkout branch_yakou

# Sery
git checkout branch_sery
```

#### 2️⃣ Travailler et sauvegarder

```bash
# Faites vos modifications, puis :
git add .
git commit -m "Description de ce que vous avez fait"
git push origin VOTRE_BRANCHE
```

#### 3️⃣ Fusionner votre travail

1. Allez sur GitHub
2. Cliquez **"Compare & pull request"**
3. Demandez à un ami de vérifier
4. Cliquez **"Merge"**

#### 4️⃣ Récupérer le travail des autres

```bash
git checkout main
git pull origin main
git checkout VOTRE_BRANCHE
git merge main
```

---

## 📝 Règles Importantes

1. **Ne supprimez jamais** le code d'un autre
2. **Communiquez** avant de modifier un fichier partagé
3. **Testez** votre code avant de pusher
4. **Commitez régulièrement** (pas tout à la fin)
5. **Demandez de l'aide** si vous bloquez

---


Voici comment envoyer ton travail de branch_mike vers main :
🚀 Méthode Recommandée (avec Pull Request)
bash# 1. Assure-toi d'être sur ta branche
git checkout branch_mike

# 2. Sauvegarde ton travail
git add .
git commit -m "Ajout pages accueil et portfolio"

# 3. Envoie sur GitHub
git push origin branch_mike
Ensuite sur GitHub :

Va sur ton repo GitHub
Tu verras un bouton "Compare & pull request" (jaune)
Clique dessus
Ajoute une description (ex: "Pages accueil et portfolio terminées")
Clique "Create pull request"
Clique "Merge pull request"
Clique "Confirm merge"

✅ C'est fait ! Ton code est maintenant dans main

⚡ Méthode Rapide (directement)
Si tu veux faire ça direct sans passer par GitHub :
bash# 1. Va sur main
git checkout main

# 2. Récupère les dernières mises à jour
git pull origin main

# 3. Fusionne ta branche
git merge branch_mike

# 4. Envoie sur GitHub
git push origin main

# 5. Retourne sur ta branche
git checkout branch_mike

💡 Quelle méthode choisir ?

Pull Request (1ère méthode) → Meilleure pour travailler en équipe, les autres peuvent vérifier ton code
Merge direct (2ème méthode) → Plus rapide mais risque de conflits




## 🆘 Commandes Git Essentielles

```bash
# Voir où vous êtes
git status

# Aller sur votre branche
git checkout VOTRE_BRANCHE

# Sauvegarder votre travail
git add .
git commit -m "Message"
git push origin VOTRE_BRANCHE

# Récupérer les mises à jour
git pull origin main
```

---

**🎉 Bon code à tous ! L'équipe Eridanus Corporation 🚀**
