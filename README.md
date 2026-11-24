# dartpop-site

Page commerciale de Dartpop (GitHub Pages, racine du dépôt) : français à la racine, anglais, allemand, espagnol, italien et portugais dans `en/`, `de/`, `es/`, `it/`, `pt/`, page d'assistance `support/` dans chaque langue (`support/`, `en/support/`, …) page `privacy/` bilingue français / anglais et une page `<langue>/privacy/` par autre langue (`de/`, `es/`, `it/`, `pt/`).

- `index.html` : page autonome (CSS et JS en ligne, police Archivo via Google Fonts). Ouverture avec une cible jouable (301 ou 501, fin libre comme le réglage par défaut de l'app), thèmes clair et sombre, mise en page mobile, respect de « Réduire les animations ».
- `assets/shots/` (français) et `assets/shots/<langue>/` : captures de l'iPhone 18 Pro Max issues de `DartPop/store/release-next/screenshots/iphone-island/raw/fr-FR` et `raw/en-US`, présentées dans un cadre CSS avec l'îlot.
- `privacy/` : reprise des textes publiés sur dartpop-support (mise à jour du 16 novembre 2026), qui nomment Apple, RevenueCat, PostHog et Sentry. Même design que la page commerciale, un sommaire par langue, rubriques avec `id` stables (`fr-…`, `en-…`).
- `de/privacy/`, `es/privacy/`, `it/privacy/`, `pt/privacy/` : une langue par page, produites par `python3 _tools/build_privacy.py` ; le style et le script sont copiés de `privacy/index.html`, le texte est repris tel quel des pages de dartpop-support de la même langue (même date), `id` stables `<langue>-…`. Les pages commerciales et d'assistance de chaque langue y renvoient par un lien relatif.
- `support/` et `<langue>/support/` : questions d'assistance et contact, produits par `python3 _tools/build_support.py` (textes et libellés de menus tirés du code et du catalogue de chaînes de l'app). L'app ne nomme pas les prestataires de mesure ; cette page non plus.

Chaque affirmation de la page est tirée du code de l'app ou de sa fiche App Store vérifiée. Aucun prix n'est écrit : il varie selon le pays.
Aucune mesure d'audience sur le site, donc aucun bandeau de cookies.

Aperçu local : `python3 -m http.server 8742` dans ce dossier, puis http://127.0.0.1:8742/.

Les pages `de/`, `es/`, `it/`, `pt/` et le menu des langues sont produits par `python3 _tools/build_languages.py` à partir de la page française ; la page anglaise `en/` est maintenue à la main.
