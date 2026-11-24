"""Builds the six support pages: support/ (French) and <lang>/support/.

Run from the site root: python3 _tools/build_support.py
Same look as the commercial page: the colour tokens, fonts, top bar, theme button
(localStorage key "dartpop-theme") and footer are copied from index.html.
Every statement comes from the app's code; menu names are the exact labels of
Dartpop's String Catalog (Cible/Localizable.xcstrings) in each language.
No price is written: it varies by country.
"""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
MAIL = "abdelhafid.younes@gmail.com"
STORE = "https://apps.apple.com/app/id6825865334"
BASE = "https://hafidnes.github.io/dartpop-site/"
LANGS = [("fr", "Français", ""), ("en", "English", "en/"), ("de", "Deutsch", "de/"),
         ("es", "Español", "es/"), ("it", "Italiano", "it/"), ("pt", "Português", "pt/")]


def path(*steps):
    return '<span class="path">' + " › ".join(steps) + "</span>"


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def ol(*items):
    return '<ol class="steps">' + "".join(f"<li><span>{i}</span></li>" for i in items) + "</ol>"


def p(*paragraphs):
    return "".join(f"<p>{t}</p>" for t in paragraphs)


T = {}

# ---------------------------------------------------------------- Français
T["fr"] = dict(
    html_lang="fr", title="Assistance · Dartpop",
    description="Assistance Dartpop : saisir les scores, les jeux, l’essai gratuit, restaurer l’achat, changer d’appareil, sons et vibrations, contact.",
    home_label="Dartpop, accueil", theme_label="Changer le thème clair ou sombre", download="Télécharger",
    nav=("Accueil", "Confidentialité", "Contact"), kicker="Assistance",
    h1=("Besoin", "d’aide&nbsp;?"),
    lede="Saisir les scores, débloquer Dartpop, retrouver vos parties sur un nouvel appareil&nbsp;: les réponses sont ici. Sinon, écrivez-nous.",
    updated="Mise à jour&nbsp;: 24 novembre 2026", toc="Sommaire",
    footer=("Accueil", "Confidentialité · Privacy", "Assistance"), legal_label="Liens légaux",
    sections=[
        ("scores", "Saisir les scores",
         p("Dartpop accompagne une vraie cible&nbsp;: vous saisissez chaque fléchette à la main et l’app fait les comptes. Pendant la partie, passez à tout moment de la <b>Cible tactile</b> au <b>Pavé rapide</b>.")
         + ul("<b>Cible tactile.</b> Touchez la zone atteinte, ou glissez le doigt&nbsp;: une loupe montre la zone visée avant de relâcher. Autour de la cible, c’est un raté.",
              "<b>Pavé rapide.</b> Touchez un nombre. Pour un double ou un triple, choisissez <b>Double</b> ou <b>Triple</b> avant le nombre&nbsp;; en ’01, vous pouvez aussi glisser sur la touche vers le haut (double) ou vers le bas (triple). Les touches <b>25</b> et <b>Bull 50</b> complètent le pavé.",
              "<b>Raté.</b> Une fléchette hors cible se saisit avec le bouton <b>Raté</b>.",
              "<b>Valider.</b> Une volée compte jusqu’à trois fléchettes&nbsp;; validez-la pour passer au joueur suivant. En ’01, avec <b>Passage automatique</b> (" + path("Réglages", "À votre rythme") + "), la volée est validée après un court délai dès la troisième fléchette.",
              "<b>Corriger.</b> Le bouton d’annulation (flèche de retour) efface la dernière saisie. En ’01, il peut aussi revenir au passage précédent, et toucher une fléchette déjà saisie permet de la reprendre avec les suivantes.")
         + p("Les règles de chaque jeu sont expliquées dans " + path("Réglages", "À votre rythme", "Comprendre les règles") + ".")),
        ("jeux", "Les jeux",
         p("Dans l’onglet <b>Jouer</b>, choisissez un jeu, puis les joueurs&nbsp;: de 2 à 8 (3 au minimum pour Killer).")
         + ul("<b>301 · 501.</b> Départ à 301, 501, 701, 901 ou 1001. Départ libre ou Double In, fin libre ou sur un double. En individuel, en doublettes (2 contre 2) ou en équipes (4 contre 4) à score partagé. En une manche, ou au premier à 2, 3 ou 5 victoires.",
              "<b>Cricket.</b> Fermez les 15 à 20 et le Bull.",
              "<b>Tour du monde.</b> Touchez les numéros de 1 à 20 dans l’ordre, puis le centre selon l’option choisie.",
              "<b>Killer.</b> Chaque joueur a son numéro et des vies&nbsp;; le dernier survivant gagne.",
              "<b>Shanghai.</b> Chaque tour vise son numéro, en 7 ou 20 tours. Un simple, un double et un triple dans la même volée donnent la victoire immédiate.",
              "<b>Halve-It.</b> Atteignez l’objectif de chaque tour&nbsp;; si vos trois fléchettes le manquent, votre total est divisé par deux.")
         + p("L’onglet <b>S’entraîner</b> propose des exercices en solo.")),
        ("essai", "L’essai gratuit",
         p("<b>Trois rencontres complètes sont gratuites.</b> Une rencontre comprend toutes ses manches, et seules les rencontres terminées sont décomptées. Le nombre de rencontres gratuites restantes s’affiche dans " + path("Réglages", "Achats") + ".",
           "Ensuite, un achat unique et permanent permet de lancer de nouvelles rencontres sans limite. Aucun abonnement. Le prix s’affiche dans l’App Store, dans votre devise, avant l’achat.",
           "Sans achat, vos résultats restent accessibles, et l’entraînement en solo, l’historique, les statistiques, les sauvegardes, le partage et le second écran restent gratuits.")),
        ("restaurer", "Restaurer l’achat",
         ol("Utilisez le même compte Apple que lors de l’achat.",
            "Ouvrez " + path("Réglages", "Achats") + ".",
            "Touchez <b>Restaurer les achats</b>.")
         + p("L’app affiche «&nbsp;Achats restaurés&nbsp;» quand l’accès est retrouvé, ou «&nbsp;Aucun achat à restaurer&nbsp;» si elle n’en trouve pas. Une connexion Internet peut être nécessaire&nbsp;: si vous lisez «&nbsp;Service indisponible. Réessayez plus tard.&nbsp;», vérifiez votre connexion et recommencez.")),
        ("appareil", "Changer d’appareil",
         ol("Sur l’ancien appareil, ouvrez " + path("Réglages", "Sauvegarde et restauration") + ", puis touchez <b>Exporter une sauvegarde</b>. Enregistrez le fichier dans Fichiers, sur iCloud Drive, ou partagez-le avec votre nouvel appareil.",
            "Sur le nouvel appareil, ouvrez le même écran, touchez <b>Importer une sauvegarde</b> et choisissez le fichier.",
            "Restaurez séparément votre achat avec le même compte Apple&nbsp;: " + path("Réglages", "Achats", "Restaurer les achats") + ".")
         + p("La sauvegarde contient vos amis mémorisés, la rencontre en cours et les résultats. L’import remplace la rencontre active et les réglages&nbsp;; les résultats déjà présents sont conservés. Une copie de récupération est créée avant l’import&nbsp;: <b>Récupérer la version avant import</b> permet de revenir en arrière.",
             "Le compteur de rencontres gratuites n’est pas remis à zéro par un import.")),
        ("sons", "Sons et vibrations",
         p("Les deux se règlent dans " + path("Réglages", "À votre rythme") + " et sont activés par défaut.")
         + ul("<b>Sons.</b> Petits sons à la validation d’une volée, à la victoire et à l’achat. Ils sont muets en mode silencieux et ne coupent pas votre musique.",
              "<b>Retour haptique.</b> Vibrations à la saisie et à la fin du tour.")
         + p("Vous n’entendez rien&nbsp;? Vérifiez le mode silencieux de l’appareil, puis l’interrupteur <b>Sons</b>.")),
        ("donnees", "Partage de données facultatif",
         p("Dartpop vous pose une fois la question «&nbsp;Aider à améliorer Dartpop&nbsp;?&nbsp;». Le partage est facultatif et reste désactivé tant que vous n’avez pas répondu «&nbsp;Partager&nbsp;».",
           "Si vous acceptez, l’app envoie des statistiques d’utilisation et des diagnostics de plantage, avec un identifiant aléatoire. Jamais les prénoms, les scores ni vos sauvegardes.",
           "Vous pouvez changer d’avis à tout moment avec l’interrupteur " + path("Réglages", "À propos", "Aider à améliorer Dartpop") + ". Tous les détails sont dans la page <a href=\"{privacy}\">Confidentialité</a>.")),
        ("probleme", "Signaler un problème",
         p("Écrivez-nous en indiquant&nbsp;:")
         + ul("le modèle de votre appareil et la version d’iOS ou d’iPadOS&nbsp;;",
              "la version de Dartpop, visible dans " + path("Réglages", "À propos", "Version") + "&nbsp;;",
              "le jeu concerné et les étapes qui mènent au problème.")
         + p("Ne transmettez aucun mot de passe ni information bancaire.")),
    ],
    contact=("contact", "Contact", "Une question ou un souci&nbsp;? Écrivez-nous."),
)

# ---------------------------------------------------------------- English
T["en"] = dict(
    html_lang="en", title="Support · Dartpop",
    description="Dartpop support: entering scores, the games, the free trial, restoring your purchase, moving to another device, sounds and haptics, contact.",
    home_label="Dartpop, home", theme_label="Switch between light and dark theme", download="Download",
    nav=("Home", "Privacy", "Contact"), kicker="Support",
    h1=("Need", "a hand?"),
    lede="Entering scores, unlocking Dartpop, moving your games to a new device: the answers are here. If not, email us.",
    updated="Updated: 24 November 2026", toc="Contents",
    footer=("Home", "Privacy", "Support"), legal_label="Legal links",
    sections=[
        ("scores", "Entering scores",
         p("Dartpop works alongside a real dartboard: you enter each dart by hand and the app does the math. During a game you can switch between the <b>Touch dartboard</b> and the <b>Quick keypad</b> at any time.")
         + ul("<b>Touch dartboard.</b> Tap the segment you hit, or drag your finger: a magnifier shows the segment before you let go. Around the board is a miss.",
              "<b>Quick keypad.</b> Tap a number. For a double or a treble, select <b>Double</b> or <b>Treble</b> first; in ’01 you can also swipe up on the key for a double and down for a treble. The <b>25</b> and <b>Bull 50</b> keys complete the keypad.",
              "<b>Miss.</b> A dart off the board is entered with the <b>Miss</b> button.",
              "<b>Confirm.</b> A turn is up to three darts; confirm it to move on to the next player. In ’01, with <b>Automatic next player</b> (" + path("Settings", "At your pace") + "), the turn is confirmed after a short delay once the third dart is in.",
              "<b>Correct.</b> The undo button (the back arrow) removes the last entry. In ’01 it can also return to the previous turn, and tapping a dart you already entered lets you re-enter it and the later darts.")
         + p("The rules of each game are explained in " + path("Settings", "At your pace", "Understand the rules") + ".")),
        ("games", "The games",
         p("In the <b>Play</b> tab, choose a game, then the players: 2 to 8 (at least 3 for Killer).")
         + ul("<b>301 · 501.</b> Start from 301, 501, 701, 901 or 1001. Straight in or double in, straight out or double out. Individual, pairs (2 vs 2) or teams (4 vs 4) with a shared score. One leg, or first to 2, 3 or 5 wins.",
              "<b>Cricket.</b> Close 15 to 20 and the bull.",
              "<b>Around the Clock.</b> Hit the numbers 1 to 20 in order, then the bull if that option is on.",
              "<b>Killer.</b> Each player has a number and lives; the last player standing wins.",
              "<b>Shanghai.</b> Each round aims at its own number, over 7 or 20 rounds. A single, a double and a treble in the same turn win at once.",
              "<b>Halve-It.</b> Hit the target of each round; if all three darts miss it, your total is halved.")
         + p("The <b>Practice</b> tab offers solo drills.")),
        ("trial", "The free trial",
         p("<b>Three full matches are free.</b> A match includes all its legs, and only completed matches count. The number of free matches remaining is shown in " + path("Settings", "Purchases") + ".",
           "After that, one permanent purchase lets you start new matches without limit. There is no subscription. The price is shown on the App Store, in your currency, before you buy.",
           "Without buying, your results remain available, and solo practice, history, statistics, backups, sharing and the second screen stay free.")),
        ("restore", "Restoring your purchase",
         ol("Use the same Apple Account as for the purchase.",
            "Open " + path("Settings", "Purchases") + ".",
            "Tap <b>Restore purchases</b>.")
         + p("The app shows “Purchases restored” once access is back, or “No purchases to restore” if it finds none. Internet access may be required: if you read “Service unavailable. Try again later.”, check your connection and try again.")),
        ("device", "Moving to another device",
         ol("On the old device, open " + path("Settings", "Backup and restore") + ", then tap <b>Export backup</b>. Save the file to Files or iCloud Drive, or share it with your new device.",
            "On the new device, open the same screen, tap <b>Import backup</b> and pick the file.",
            "Restore your purchase separately with the same Apple Account: " + path("Settings", "Purchases", "Restore purchases") + ".")
         + p("The backup holds your saved friends, the current match and the results. Import replaces the active match and settings; existing results are kept. A recovery copy is created first: <b>Recover the version before import</b> takes you back.",
             "The free-match counter is not reset by importing a backup.")),
        ("sounds", "Sounds and haptics",
         p("Both are set in " + path("Settings", "At your pace") + " and are on by default.")
         + ul("<b>Sounds.</b> Small sounds when a turn is confirmed, on a win and after a purchase. They are silent when the device is in silent mode and do not interrupt your music.",
              "<b>Haptic feedback.</b> Vibrations when entering darts and ending the turn.")
         + p("No sound? Check the device’s silent mode, then the <b>Sounds</b> switch.")),
        ("data", "Optional data sharing",
         p("Dartpop asks you once: “Help improve Dartpop?”. Sharing is optional and stays off unless you answer “Share”.",
           "If you agree, the app sends usage statistics and crash diagnostics, with a random identifier. Never player names, scores or your backups.",
           "You can change your mind at any time with the " + path("Settings", "About", "Help improve Dartpop") + " switch. All the details are on the <a href=\"{privacy}\">Privacy</a> page.")),
        ("problem", "Reporting a problem",
         p("Email us with:")
         + ul("your device model and iOS or iPadOS version;",
              "your Dartpop version, shown in " + path("Settings", "About", "Version") + ";",
              "the game involved and the steps that lead to the problem.")
         + p("Never send passwords or bank information.")),
    ],
    contact=("contact", "Contact", "A question or a problem? Email us."),
)

# ---------------------------------------------------------------- Deutsch
T["de"] = dict(
    html_lang="de", title="Support · Dartpop",
    description="Dartpop-Support: Punkte eingeben, die Spiele, die Gratis-Matches, Kauf wiederherstellen, Gerät wechseln, Töne und Vibrationen, Kontakt.",
    home_label="Dartpop, Startseite", theme_label="Zwischen hellem und dunklem Design wechseln", download="Laden",
    nav=("Startseite", "Datenschutz", "Kontakt"), kicker="Support",
    h1=("Brauchst du", "Hilfe?"),
    lede="Punkte eingeben, Dartpop freischalten, Spiele auf ein neues Gerät mitnehmen: Hier findest du die Antworten. Sonst schreib uns.",
    updated="Stand: 24. November 2026", toc="Inhalt",
    footer=("Startseite", "Datenschutz", "Support"), legal_label="Rechtliche Links",
    sections=[
        ("punkte", "Punkte eingeben",
         p("Dartpop ergänzt eine echte Dartscheibe: Du erfasst jeden Dart von Hand, die App rechnet. Während des Spiels kannst du jederzeit zwischen <b>Touch-Dartscheibe</b> und <b>Schnelleingabe</b> wechseln.")
         + ul("<b>Touch-Dartscheibe.</b> Tippe das getroffene Feld an oder ziehe den Finger: Eine Lupe zeigt das Feld, bevor du loslässt. Außerhalb der Scheibe zählt als Fehlwurf.",
              "<b>Schnelleingabe.</b> Tippe eine Zahl an. Für ein Doppel oder Triple wählst du vorher <b>Doppel</b> oder <b>Triple</b>; bei ’01 kannst du auf der Taste auch nach oben (Doppel) oder nach unten (Triple) wischen. Die Tasten <b>25</b> und <b>Bull 50</b> ergänzen das Tastenfeld.",
              "<b>Fehlwurf.</b> Einen Dart neben die Scheibe erfasst du mit der Taste <b>Fehlwurf</b>.",
              "<b>Bestätigen.</b> Eine Aufnahme umfasst bis zu drei Darts; bestätige sie, um zum nächsten Spieler zu wechseln. Bei ’01 wird die Aufnahme mit <b>Automatischer Spielerwechsel</b> (" + path("Einstellungen", "In deinem Tempo") + ") nach dem dritten Dart nach kurzer Pause bestätigt.",
              "<b>Korrigieren.</b> Die Rückgängig-Taste (Pfeil zurück) löscht die letzte Eingabe. Bei ’01 kann sie auch zur vorherigen Aufnahme zurückkehren, und wenn du einen bereits erfassten Dart antippst, gibst du ihn und die folgenden neu ein.")
         + p("Die Regeln jedes Spiels findest du unter " + path("Einstellungen", "In deinem Tempo", "Regeln verstehen") + ".")),
        ("spiele", "Die Spiele",
         p("Wähle im Tab <b>Spielen</b> ein Spiel, dann die Spieler: 2 bis 8 (bei Killer mindestens 3).")
         + ul("<b>301 · 501.</b> Start bei 301, 501, 701, 901 oder 1001. Straight-in oder Double-in, Straight-out oder Double-out. Einzel, Doppel (2 gegen 2) oder Teams (4 gegen 4) mit gemeinsamem Punktestand. Ein Leg, oder wer zuerst 2, 3 oder 5 Siege hat.",
              "<b>Cricket.</b> Schließe 15 bis 20 und das Bull.",
              "<b>Rund um die Uhr.</b> Triff die Zahlen 1 bis 20 der Reihe nach, je nach Option danach das Bull.",
              "<b>Killer.</b> Jeder Spieler hat eine Zahl und Leben; der letzte Überlebende gewinnt.",
              "<b>Shanghai.</b> Jede Runde hat ihre Zahl, über 7 oder 20 Runden. Einfach, Doppel und Triple in derselben Aufnahme bedeuten den sofortigen Sieg.",
              "<b>Halve-It.</b> Triff das Ziel jeder Runde; verfehlen es alle drei Darts, wird dein Punktestand halbiert.")
         + p("Der Tab <b>Trainieren</b> bietet Solo-Übungen.")),
        ("gratis", "Die Gratis-Matches",
         p("<b>Drei vollständige Matches sind kostenlos.</b> Ein Match umfasst alle Legs, und nur beendete Matches werden gezählt. Die Zahl der verbleibenden kostenlosen Matches steht unter " + path("Einstellungen", "Käufe") + ".",
           "Danach schaltet ein einmaliger, dauerhafter Kauf unbegrenzt neue Matches frei. Kein Abo. Der Preis wird vor dem Kauf im App Store in deiner Währung angezeigt.",
           "Ohne Kauf bleiben deine Ergebnisse verfügbar, und Solo-Training, Verlauf, Statistiken, Sicherungen, Teilen und zweiter Bildschirm bleiben kostenlos.")),
        ("wiederherstellen", "Kauf wiederherstellen",
         ol("Verwende denselben Apple Account wie beim Kauf.",
            "Öffne " + path("Einstellungen", "Käufe") + ".",
            "Tippe auf <b>Käufe wiederherstellen</b>.")
         + p("Die App zeigt „Käufe wiederhergestellt“, sobald der Zugang wieder da ist, oder „Keine Käufe zum Wiederherstellen“, wenn sie keinen findet. Eine Internetverbindung kann nötig sein: Steht dort „Dienst nicht verfügbar. Versuche es später erneut.“, prüfe deine Verbindung und versuche es noch einmal.")),
        ("geraet", "Gerät wechseln",
         ol("Öffne auf dem alten Gerät " + path("Einstellungen", "Sichern und wiederherstellen") + " und tippe auf <b>Sicherung exportieren</b>. Speichere die Datei in Dateien oder iCloud Drive, oder teile sie mit deinem neuen Gerät.",
            "Öffne auf dem neuen Gerät denselben Bildschirm, tippe auf <b>Sicherung importieren</b> und wähle die Datei.",
            "Stelle deinen Kauf separat mit demselben Apple Account wieder her: " + path("Einstellungen", "Käufe", "Käufe wiederherstellen") + ".")
         + p("Die Sicherung enthält deine gespeicherten Freunde, das aktuelle Match und die Ergebnisse. Der Import ersetzt das aktive Match und die Einstellungen; vorhandene Ergebnisse bleiben erhalten. Zuvor wird eine Wiederherstellungskopie erstellt: Mit <b>Version vor dem Import wiederherstellen</b> kommst du zurück.",
             "Der Zähler der kostenlosen Matches wird durch einen Import nicht zurückgesetzt.")),
        ("toene", "Töne und Vibrationen",
         p("Beides stellst du unter " + path("Einstellungen", "In deinem Tempo") + " ein; beides ist standardmäßig aktiviert.")
         + ul("<b>Töne.</b> Kurze Töne beim Bestätigen einer Aufnahme, beim Sieg und nach dem Kauf. Im Stumm-Modus bleiben sie still, und deine Musik läuft weiter.",
              "<b>Haptisches Feedback.</b> Vibrationen bei der Eingabe und am Ende des Zugs.")
         + p("Du hörst nichts? Prüfe den Stumm-Modus des Geräts und dann den Schalter <b>Töne</b>.")),
        ("daten", "Freiwilliges Teilen von Daten",
         p("Dartpop fragt dich einmal: „Dartpop verbessern helfen?“. Das Teilen ist freiwillig und bleibt aus, solange du nicht mit „Teilen“ antwortest.",
           "Wenn du zustimmst, sendet die App Nutzungsstatistiken und Absturzdiagnosen mit einer zufälligen Kennung. Niemals Spielernamen, Punktestände oder deine Sicherungen.",
           "Du kannst deine Entscheidung jederzeit mit dem Schalter " + path("Einstellungen", "Über Dartpop", "Dartpop verbessern helfen") + " ändern. Alle Details findest du unter <a href=\"{privacy}\">Datenschutz</a>.")),
        ("problem", "Ein Problem melden",
         p("Schreib uns und nenne:")
         + ul("dein Gerätemodell und die iOS- oder iPadOS-Version;",
              "deine Dartpop-Version, zu finden unter " + path("Einstellungen", "Über Dartpop", "Version") + ";",
              "das betroffene Spiel und die Schritte, die zum Problem führen.")
         + p("Sende niemals Passwörter oder Bankdaten.")),
    ],
    contact=("kontakt", "Kontakt", "Eine Frage oder ein Problem? Schreib uns."),
)

# ---------------------------------------------------------------- Español
T["es"] = dict(
    html_lang="es", title="Ayuda · Dartpop",
    description="Ayuda de Dartpop: anotar los puntos, los juegos, las partidas gratis, restaurar la compra, cambiar de dispositivo, sonidos y vibraciones, contacto.",
    home_label="Dartpop, inicio", theme_label="Cambiar entre tema claro y oscuro", download="Descargar",
    nav=("Inicio", "Privacidad", "Contacto"), kicker="Ayuda",
    h1=("¿Necesitas", "ayuda?"),
    lede="Anotar los puntos, desbloquear Dartpop, llevar tus partidas a un dispositivo nuevo: aquí están las respuestas. Si no, escríbenos.",
    updated="Actualizado: 24 de noviembre de 2026", toc="Contenido",
    footer=("Inicio", "Privacidad", "Ayuda"), legal_label="Enlaces legales",
    sections=[
        ("puntos", "Anotar los puntos",
         p("Dartpop se usa junto a una diana de verdad: introduces cada dardo a mano y la app hace las cuentas. Durante la partida puedes pasar en cualquier momento de la <b>Diana táctil</b> al <b>Teclado rápido</b>.")
         + ul("<b>Diana táctil.</b> Toca la zona alcanzada o desliza el dedo: una lupa muestra la zona antes de soltar. Fuera de la diana cuenta como fallo.",
              "<b>Teclado rápido.</b> Toca un número. Para un doble o un triple, elige antes <b>Doble</b> o <b>Triple</b>; en ’01 también puedes deslizar la tecla hacia arriba (doble) o hacia abajo (triple). Las teclas <b>25</b> y <b>Diana 50</b> completan el teclado.",
              "<b>Fallo.</b> Un dardo fuera de la diana se anota con el botón <b>Fallo</b>.",
              "<b>Confirmar.</b> Una tirada tiene hasta tres dardos; confírmala para pasar al siguiente jugador. En ’01, con <b>Cambio automático de jugador</b> (" + path("Ajustes", "A tu ritmo") + "), la tirada se confirma tras una breve pausa después del tercer dardo.",
              "<b>Corregir.</b> El botón de deshacer (flecha hacia atrás) borra la última entrada. En ’01 también puede volver al turno anterior, y si tocas un dardo ya anotado puedes repetir su entrada y las siguientes.")
         + p("Las reglas de cada juego se explican en " + path("Ajustes", "A tu ritmo", "Entender las reglas") + ".")),
        ("juegos", "Los juegos",
         p("En la pestaña <b>Jugar</b>, elige un juego y luego los jugadores: de 2 a 8 (al menos 3 en Killer).")
         + ul("<b>301 · 501.</b> Puntuación inicial de 301, 501, 701, 901 o 1001. Inicio libre o con doble, cierre libre o con doble. Individual, por parejas (2 contra 2) o en equipos (4 contra 4) con puntuación compartida. A una manga, o gana el primero en lograr 2, 3 o 5 victorias.",
              "<b>Cricket.</b> Cierra del 15 al 20 y el bull.",
              "<b>La vuelta al mundo.</b> Acierta los números del 1 al 20 en orden y, según la opción elegida, después el centro.",
              "<b>Killer.</b> Cada jugador tiene su número y sus vidas; gana el último superviviente.",
              "<b>Shanghai.</b> Cada ronda apunta a su número, en 7 o 20 rondas. Un simple, un doble y un triple en la misma tirada dan la victoria inmediata.",
              "<b>Halve-It.</b> Acierta el objetivo de cada ronda; si fallas los tres dardos, tu total se divide entre dos.")
         + p("La pestaña <b>Entrenar</b> ofrece ejercicios en solitario.")),
        ("gratis", "Las partidas gratis",
         p("<b>Tres partidas completas son gratis.</b> Una partida incluye todas sus mangas y solo cuentan las partidas terminadas. El número de partidas gratuitas restantes aparece en " + path("Ajustes", "Compras") + ".",
           "Después, una compra única y permanente permite iniciar nuevas partidas sin límite. Sin suscripción. El precio aparece en el App Store, en tu moneda, antes de comprar.",
           "Sin comprar, tus resultados siguen disponibles, y el entrenamiento en solitario, el historial, las estadísticas, las copias, compartir y la segunda pantalla siguen siendo gratis.")),
        ("restaurar", "Restaurar la compra",
         ol("Usa la misma cuenta de Apple con la que compraste.",
            "Abre " + path("Ajustes", "Compras") + ".",
            "Toca <b>Restaurar compras</b>.")
         + p("La app muestra «Compras restauradas» cuando recuperas el acceso, o «No hay compras que restaurar» si no encuentra ninguna. Puede hacer falta conexión a internet: si lees «Servicio no disponible. Inténtalo más tarde.», comprueba tu conexión y vuelve a intentarlo.")),
        ("dispositivo", "Cambiar de dispositivo",
         ol("En el dispositivo antiguo, abre " + path("Ajustes", "Copia y restauración") + " y toca <b>Exportar copia</b>. Guarda el archivo en Archivos o en iCloud Drive, o compártelo con tu nuevo dispositivo.",
            "En el dispositivo nuevo, abre la misma pantalla, toca <b>Importar copia</b> y elige el archivo.",
            "Restaura la compra por separado con la misma cuenta de Apple: " + path("Ajustes", "Compras", "Restaurar compras") + ".")
         + p("La copia contiene tus amigos guardados, la partida actual y los resultados. La importación sustituye la partida activa y los ajustes; se conservan los resultados existentes. Antes se crea una copia de recuperación: <b>Recuperar la versión anterior a la importación</b> te permite volver atrás.",
             "El contador de partidas gratuitas no se reinicia al importar una copia.")),
        ("sonidos", "Sonidos y vibraciones",
         p("Los dos se ajustan en " + path("Ajustes", "A tu ritmo") + " y están activados por defecto.")
         + ul("<b>Sonidos.</b> Sonidos breves al validar una tirada, al ganar y tras la compra. No suenan en modo silencio y no cortan tu música.",
              "<b>Respuesta háptica.</b> Vibraciones al registrar dardos y al terminar el turno.")
         + p("¿No oyes nada? Comprueba el modo silencio del dispositivo y luego el interruptor <b>Sonidos</b>.")),
        ("datos", "Compartir datos, opcional",
         p("Dartpop te pregunta una sola vez: «¿Ayudar a mejorar Dartpop?». Compartir es opcional y sigue desactivado mientras no respondas «Compartir».",
           "Si aceptas, la app envía estadísticas de uso y diagnósticos de fallos, con un identificador aleatorio. Nunca nombres, puntuaciones ni tus copias de seguridad.",
           "Puedes cambiar de opinión en cualquier momento con el interruptor " + path("Ajustes", "Acerca de", "Ayudar a mejorar Dartpop") + ". Todos los detalles en <a href=\"{privacy}\">Privacidad</a>.")),
        ("problema", "Informar de un problema",
         p("Escríbenos indicando:")
         + ul("el modelo de tu dispositivo y la versión de iOS o iPadOS;",
              "tu versión de Dartpop, visible en " + path("Ajustes", "Acerca de", "Versión") + ";",
              "el juego afectado y los pasos que llevan al problema.")
         + p("No envíes nunca contraseñas ni datos bancarios.")),
    ],
    contact=("contacto", "Contacto", "¿Una pregunta o un problema? Escríbenos."),
)

# ---------------------------------------------------------------- Italiano
T["it"] = dict(
    html_lang="it", title="Assistenza · Dartpop",
    description="Assistenza Dartpop: inserire i punteggi, i giochi, le partite gratis, ripristinare l’acquisto, cambiare dispositivo, suoni e vibrazioni, contatti.",
    home_label="Dartpop, home", theme_label="Alterna tra tema chiaro e scuro", download="Scarica",
    nav=("Home", "Privacy", "Contatti"), kicker="Assistenza",
    h1=("Serve", "aiuto?"),
    lede="Inserire i punteggi, sbloccare Dartpop, portare le partite su un nuovo dispositivo: le risposte sono qui. Altrimenti, scrivici.",
    updated="Aggiornamento: 24 novembre 2026", toc="Sommario",
    footer=("Home", "Privacy", "Assistenza"), legal_label="Link legali",
    sections=[
        ("punteggi", "Inserire i punteggi",
         p("Dartpop si usa insieme a un vero bersaglio: inserisci ogni freccetta a mano e l’app fa i calcoli. Durante la partita puoi passare in qualsiasi momento dal <b>Bersaglio touch</b> al <b>Tastierino rapido</b>.")
         + ul("<b>Bersaglio touch.</b> Tocca la zona colpita, oppure trascina il dito: una lente mostra la zona prima di rilasciare. Fuori dal bersaglio vale come mancato.",
              "<b>Tastierino rapido.</b> Tocca un numero. Per un doppio o un triplo, scegli prima <b>Doppio</b> o <b>Triplo</b>; nel ’01 puoi anche scorrere sul tasto verso l’alto (doppio) o verso il basso (triplo). I tasti <b>25</b> e <b>Centro 50</b> completano il tastierino.",
              "<b>Mancato.</b> Una freccetta fuori bersaglio si inserisce con il pulsante <b>Mancato</b>.",
              "<b>Confermare.</b> Un turno conta fino a tre freccette; confermalo per passare al giocatore successivo. Nel ’01, con <b>Cambio automatico del giocatore</b> (" + path("Impostazioni", "Al tuo ritmo") + "), il turno viene confermato dopo una breve pausa dalla terza freccetta.",
              "<b>Correggere.</b> Il pulsante di annullamento (freccia indietro) cancella l’ultimo inserimento. Nel ’01 può anche tornare al turno precedente, e toccando una freccetta già inserita puoi reinserirla insieme alle successive.")
         + p("Le regole di ogni gioco sono spiegate in " + path("Impostazioni", "Al tuo ritmo", "Capire le regole") + ".")),
        ("giochi", "I giochi",
         p("Nella scheda <b>Gioca</b>, scegli un gioco, poi i giocatori: da 2 a 8 (almeno 3 per Killer).")
         + ul("<b>301 · 501.</b> Punteggio iniziale di 301, 501, 701, 901 o 1001. Inizio libero o con doppio, chiusura libera o con doppio. Individuale, a coppie (2 contro 2) o a squadre (4 contro 4) con punteggio condiviso. In una manche, oppure vince il primo a 2, 3 o 5 vittorie.",
              "<b>Cricket.</b> Chiudi dal 15 al 20 e il bull.",
              "<b>Giro del mondo.</b> Colpisci i numeri da 1 a 20 in ordine, poi il centro secondo l’opzione scelta.",
              "<b>Killer.</b> Ogni giocatore ha il suo numero e le sue vite; vince l’ultimo sopravvissuto.",
              "<b>Shanghai.</b> Ogni turno ha il suo numero, in 7 o 20 turni. Un singolo, un doppio e un triplo nello stesso turno danno la vittoria immediata.",
              "<b>Halve-It.</b> Colpisci l’obiettivo di ogni turno; se lo manchi con tutte e tre le freccette, il tuo totale viene dimezzato.")
         + p("La scheda <b>Allenati</b> propone esercizi in solitaria.")),
        ("gratis", "Le partite gratis",
         p("<b>Tre partite complete sono gratis.</b> Una partita comprende tutte le sue manche e vengono conteggiate solo le partite terminate. Il numero di partite gratuite rimaste appare in " + path("Impostazioni", "Acquisti") + ".",
           "Poi, un acquisto unico e permanente permette di iniziare nuove partite senza limiti. Nessun abbonamento. Il prezzo appare nell’App Store, nella tua valuta, prima dell’acquisto.",
           "Senza acquisto, i tuoi risultati restano disponibili, e allenamento in solitaria, cronologia, statistiche, backup, condivisione e secondo schermo restano gratis.")),
        ("ripristino", "Ripristinare l’acquisto",
         ol("Usa lo stesso Apple Account dell’acquisto.",
            "Apri " + path("Impostazioni", "Acquisti") + ".",
            "Tocca <b>Ripristina acquisti</b>.")
         + p("L’app mostra «Acquisti ripristinati» quando l’accesso è tornato, oppure «Nessun acquisto da ripristinare» se non ne trova. Può servire una connessione a internet: se leggi «Servizio non disponibile. Riprova più tardi.», controlla la connessione e riprova.")),
        ("dispositivo", "Cambiare dispositivo",
         ol("Sul vecchio dispositivo, apri " + path("Impostazioni", "Backup e ripristino") + " e tocca <b>Esporta backup</b>. Salva il file in File o su iCloud Drive, oppure condividilo con il nuovo dispositivo.",
            "Sul nuovo dispositivo, apri la stessa schermata, tocca <b>Importa backup</b> e scegli il file.",
            "Ripristina l’acquisto separatamente con lo stesso Apple Account: " + path("Impostazioni", "Acquisti", "Ripristina acquisti") + ".")
         + p("Il backup contiene gli amici salvati, la partita in corso e i risultati. L’importazione sostituisce la partita attiva e le impostazioni; i risultati esistenti vengono conservati. Prima viene creata una copia di recupero: <b>Recupera la versione precedente all’importazione</b> ti permette di tornare indietro.",
             "Il contatore delle partite gratuite non viene azzerato da un’importazione.")),
        ("suoni", "Suoni e vibrazioni",
         p("Entrambi si regolano in " + path("Impostazioni", "Al tuo ritmo") + " e sono attivi per impostazione predefinita.")
         + ul("<b>Suoni.</b> Brevi suoni alla conferma di un turno, alla vittoria e dopo l’acquisto. Sono muti in modalità silenziosa e non interrompono la tua musica.",
              "<b>Feedback aptico.</b> Vibrazioni durante l’inserimento delle freccette e alla fine del turno.")
         + p("Non senti nulla? Controlla la modalità silenziosa del dispositivo, poi l’interruttore <b>Suoni</b>.")),
        ("dati", "Condivisione dei dati facoltativa",
         p("Dartpop ti chiede una sola volta: «Aiutare a migliorare Dartpop?». La condivisione è facoltativa e resta disattivata finché non rispondi «Condividi».",
           "Se accetti, l’app invia statistiche d’uso e diagnostica dei crash, con un identificativo casuale. Mai nomi, punteggi o i tuoi backup.",
           "Puoi cambiare idea in qualsiasi momento con l’interruttore " + path("Impostazioni", "Informazioni", "Aiuta a migliorare Dartpop") + ". Tutti i dettagli nella pagina <a href=\"{privacy}\">Privacy</a>.")),
        ("problema", "Segnalare un problema",
         p("Scrivici indicando:")
         + ul("il modello del dispositivo e la versione di iOS o iPadOS;",
              "la tua versione di Dartpop, visibile in " + path("Impostazioni", "Informazioni", "Versione") + ";",
              "il gioco interessato e i passaggi che portano al problema.")
         + p("Non inviare mai password o dati bancari.")),
    ],
    contact=("contatti", "Contatti", "Una domanda o un problema? Scrivici."),
)

# ---------------------------------------------------------------- Português
T["pt"] = dict(
    html_lang="pt-PT", title="Apoio · Dartpop",
    description="Apoio do Dartpop: registar os pontos, os jogos, as partidas grátis, restaurar a compra, mudar de dispositivo, sons e vibrações, contacto.",
    home_label="Dartpop, início", theme_label="Alternar entre tema claro e escuro", download="Descarregar",
    nav=("Início", "Privacidade", "Contacto"), kicker="Apoio",
    h1=("Precisas", "de ajuda?"),
    lede="Registar os pontos, desbloquear o Dartpop, levar as partidas para um novo dispositivo: as respostas estão aqui. Se não, escreve-nos.",
    updated="Atualizado: 24 de novembro de 2026", toc="Índice",
    footer=("Início", "Privacidade", "Apoio"), legal_label="Ligações legais",
    sections=[
        ("pontos", "Registar os pontos",
         p("O Dartpop usa-se com um alvo verdadeiro: introduzes cada dardo à mão e a app faz as contas. Durante a partida podes passar a qualquer momento do <b>Alvo tátil</b> para o <b>Teclado rápido</b>.")
         + ul("<b>Alvo tátil.</b> Toca na zona atingida ou arrasta o dedo: uma lupa mostra a zona antes de largares. Fora do alvo conta como falha.",
              "<b>Teclado rápido.</b> Toca num número. Para um duplo ou um triplo, escolhe primeiro <b>Duplo</b> ou <b>Triplo</b>; no ’01 também podes deslizar a tecla para cima (duplo) ou para baixo (triplo). As teclas <b>25</b> e <b>Centro 50</b> completam o teclado.",
              "<b>Falhou.</b> Um dardo fora do alvo regista-se com o botão <b>Falhou</b>.",
              "<b>Confirmar.</b> Uma jogada tem até três dardos; confirma-a para passar ao jogador seguinte. No ’01, com <b>Mudança automática de jogador</b> (" + path("Definições", "Ao teu ritmo") + "), a jogada é confirmada após uma breve pausa a seguir ao terceiro dardo.",
              "<b>Corrigir.</b> O botão de anular (seta para trás) apaga a última entrada. No ’01 também permite voltar ao turno anterior, e ao tocares num dardo já registado podes introduzi-lo novamente com os seguintes.")
         + p("As regras de cada jogo estão explicadas em " + path("Definições", "Ao teu ritmo", "Compreender as regras") + ".")),
        ("jogos", "Os jogos",
         p("No separador <b>Jogar</b>, escolhe um jogo e depois os jogadores: de 2 a 8 (pelo menos 3 no Killer).")
         + ul("<b>301 · 501.</b> Pontuação inicial de 301, 501, 701, 901 ou 1001. Início livre ou com duplo, fecho livre ou com duplo. Individual, em duplas (2 contra 2) ou em equipas (4 contra 4) com pontuação partilhada. Numa só manga, ou ganha o primeiro a chegar a 2, 3 ou 5 vitórias.",
              "<b>Cricket.</b> Fecha do 15 ao 20 e o bull.",
              "<b>Volta ao mundo.</b> Acerta nos números de 1 a 20 por ordem e, consoante a opção escolhida, depois no centro.",
              "<b>Killer.</b> Cada jogador tem o seu número e as suas vidas; ganha o último sobrevivente.",
              "<b>Shanghai.</b> Cada ronda aponta ao seu número, em 7 ou 20 rondas. Um simples, um duplo e um triplo na mesma jogada dão a vitória imediata.",
              "<b>Halve-It.</b> Acerta no objetivo de cada ronda; se os três dardos falharem, o teu total é dividido por dois.")
         + p("O separador <b>Treinar</b> propõe exercícios a solo.")),
        ("gratis", "As partidas grátis",
         p("<b>Três partidas completas são grátis.</b> Uma partida inclui todas as suas mangas e só as partidas terminadas são contabilizadas. O número de partidas gratuitas restantes aparece em " + path("Definições", "Compras") + ".",
           "Depois, uma compra única e permanente permite iniciar novas partidas sem limite. Sem subscrição. O preço aparece na App Store, na tua moeda, antes da compra.",
           "Sem compra, os teus resultados continuam disponíveis, e o treino a solo, o histórico, as estatísticas, as cópias, a partilha e o segundo ecrã continuam grátis.")),
        ("restaurar", "Restaurar a compra",
         ol("Usa a mesma conta Apple com que compraste.",
            "Abre " + path("Definições", "Compras") + ".",
            "Toca em <b>Restaurar compras</b>.")
         + p("A app mostra «Compras restauradas» quando o acesso é recuperado, ou «Sem compras para restaurar» se não encontrar nenhuma. Pode ser necessária uma ligação à internet: se leres «Serviço indisponível. Tenta mais tarde.», verifica a ligação e tenta de novo.")),
        ("dispositivo", "Mudar de dispositivo",
         ol("No dispositivo antigo, abre " + path("Definições", "Cópia e restauro") + " e toca em <b>Exportar cópia</b>. Guarda o ficheiro em Ficheiros ou no iCloud Drive, ou partilha-o com o novo dispositivo.",
            "No novo dispositivo, abre o mesmo ecrã, toca em <b>Importar cópia</b> e escolhe o ficheiro.",
            "Restaura a compra em separado com a mesma conta Apple: " + path("Definições", "Compras", "Restaurar compras") + ".")
         + p("A cópia contém os teus amigos guardados, a partida atual e os resultados. A importação substitui a partida ativa e as definições; os resultados existentes são mantidos. Antes é criada uma cópia de recuperação: <b>Recuperar a versão anterior à importação</b> permite voltar atrás.",
             "O contador de partidas gratuitas não é reposto por uma importação.")),
        ("sons", "Sons e vibrações",
         p("Ambos se ajustam em " + path("Definições", "Ao teu ritmo") + " e estão ativos por predefinição.")
         + ul("<b>Sons.</b> Sons curtos ao validar uma jogada, na vitória e após a compra. Ficam mudos no modo silencioso e não interrompem a tua música.",
              "<b>Resposta háptica.</b> Vibrações ao registar dardos e no fim do turno.")
         + p("Não ouves nada? Verifica o modo silencioso do dispositivo e depois o interruptor <b>Sons</b>.")),
        ("dados", "Partilha de dados opcional",
         p("O Dartpop pergunta-te uma só vez: «Ajudar a melhorar o Dartpop?». A partilha é opcional e fica desativada enquanto não responderes «Partilhar».",
           "Se aceitares, a app envia estatísticas de utilização e diagnósticos de falhas, com um identificador aleatório. Nunca nomes, pontuações nem as tuas cópias de segurança.",
           "Podes mudar de ideias a qualquer momento com o interruptor " + path("Definições", "Sobre", "Ajudar a melhorar o Dartpop") + ". Todos os detalhes em <a href=\"{privacy}\">Privacidade</a>.")),
        ("problema", "Comunicar um problema",
         p("Escreve-nos indicando:")
         + ul("o modelo do teu dispositivo e a versão do iOS ou iPadOS;",
              "a tua versão do Dartpop, visível em " + path("Definições", "Sobre", "Versão") + ";",
              "o jogo em causa e os passos que levam ao problema.")
         + p("Nunca envies palavras-passe nem dados bancários.")),
    ],
    contact=("contacto", "Contacto", "Uma pergunta ou um problema? Escreve-nos."),
)

# Design tokens, base, top bar, buttons, footer and language menu: identical to index.html.
CSS = """:root{
  --bg:#F3EEE6;--bg2:#EBE4D9;--card:#FFFDF9;--ink:#17130F;--muted:#6B635B;--line:#DDD3C5;
  --red:#E30E1C;--red-ink:#B30A16;--green:#1E8A4C;--cream:#F4ECDC;--board:#17130F;
  --shadow:0 30px 60px -30px rgba(40,20,10,.35);
  --display:"Archivo",system-ui,sans-serif;--text:-apple-system,BlinkMacSystemFont,"SF Pro Text",system-ui,sans-serif;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --bg:#141210;--bg2:#1D1A17;--card:#221E1B;--ink:#F3EEE6;--muted:#A99F94;--line:#3A342E;--red:#FF3B47;--red-ink:#FF6B73;
  --shadow:0 30px 60px -30px rgba(0,0,0,.8)}}
:root[data-theme="dark"]{
  --bg:#141210;--bg2:#1D1A17;--card:#221E1B;--ink:#F3EEE6;--muted:#A99F94;--line:#3A342E;--red:#FF3B47;--red-ink:#FF6B73;
  --shadow:0 30px 60px -30px rgba(0,0,0,.8)}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:84px;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.55 var(--text);-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit}
img{max-width:100%;height:auto;display:block}
.wrap{max-width:1180px;margin:0 auto;padding:0 24px}
.display{font-family:var(--display);font-weight:900;font-variation-settings:"wdth" 68;letter-spacing:-.02em;line-height:.88;text-transform:uppercase}
.kicker{font-size:13px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--red-ink);display:flex;align-items:center;gap:10px}
.kicker::before{content:"";width:10px;height:10px;border-radius:50%;background:var(--red)}
.btn{display:inline-flex;align-items:center;gap:10px;padding:16px 22px;border-radius:16px;font-weight:700;text-decoration:none;border:0;cursor:pointer;font-size:16px}
.btn-red{background:var(--red);color:#fff}
.btn-red:hover{filter:brightness(1.07)}
.wordmark{font-family:var(--display);font-weight:900;font-variation-settings:"wdth" 80;font-size:26px;letter-spacing:-.03em;text-decoration:none}
.wordmark b{color:var(--red);font-weight:900}

/* Header */
header.site{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--bg) 82%,transparent);backdrop-filter:saturate(1.4) blur(14px);-webkit-backdrop-filter:saturate(1.4) blur(14px);border-bottom:1px solid transparent;transition:border-color .3s}
header.site.scrolled{border-color:var(--line)}
.bar{display:flex;align-items:center;justify-content:space-between;height:64px;gap:16px}
nav{display:flex;gap:22px;font-size:15px;color:var(--muted)}
nav a{text-decoration:none}nav a:hover{color:var(--ink)}
.icon-btn{width:40px;height:40px;border-radius:12px;border:1.5px solid var(--line);background:transparent;color:var(--ink);cursor:pointer;display:grid;place-items:center}
.right{display:flex;align-items:center;gap:10px}
.right .btn{padding:10px 16px;border-radius:12px;font-size:14px}

/* Page opening */
.opening{position:relative;padding:48px 0 8px;overflow:hidden}
.opening-arc{position:absolute;right:-180px;top:-200px;width:620px;height:620px;border-radius:50%;border:90px solid color-mix(in srgb,var(--red) 14%,transparent);pointer-events:none}
.opening .wrap{position:relative}
.opening h1{font-size:clamp(56px,8.4vw,128px);margin:18px 0 18px}
.opening h1 span{display:block}
.opening h1 .r{color:var(--red)}
.lede{font-size:21px;color:var(--muted);max-width:46ch;margin:0 0 14px}
.small{font-size:14px;color:var(--muted);margin:0}

/* Contents and cards */
.layout{display:grid;grid-template-columns:250px minmax(0,1fr);gap:40px;align-items:start;padding:44px 0 100px}
.toc{display:block;position:sticky;top:88px}
.toc p{margin:0 0 10px;font-size:13px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}
.toc ol{list-style:none;margin:0;padding:0;display:grid;gap:2px}
.toc a{display:block;padding:8px 12px;border-radius:12px;color:var(--muted);text-decoration:none;font-size:15px;line-height:1.35}
.toc a:hover{background:var(--card);color:var(--ink)}
.cards{display:grid;gap:16px;min-width:0;max-width:820px}
.card{background:var(--card);border:1px solid var(--line);border-radius:24px;padding:28px;min-width:0}
.card h2{font-family:var(--display);font-weight:900;font-variation-settings:"wdth" 75;font-size:clamp(30px,4vw,40px);text-transform:uppercase;letter-spacing:-.01em;line-height:.95;margin:0 0 16px;overflow-wrap:break-word;hyphens:auto}
.card p{margin:0 0 14px;color:var(--muted);overflow-wrap:break-word}
.card>:last-child{margin-bottom:0}
.card b{color:var(--ink)}
.card a{color:var(--red-ink);font-weight:700}
.path{color:var(--ink);font-weight:700}
.card ul{list-style:none;padding:0;margin:0 0 14px;display:grid;gap:12px}
.card ul li{position:relative;padding-left:22px;color:var(--muted);overflow-wrap:break-word}
.card ul li::before{content:"";position:absolute;left:2px;top:.62em;width:8px;height:8px;border-radius:50%;background:var(--red)}
.steps{list-style:none;counter-reset:step;padding:0;margin:0 0 16px;display:grid;gap:12px}
.steps li{counter-increment:step;display:flex;gap:12px;align-items:flex-start;color:var(--muted)}
.steps li>span{min-width:0;overflow-wrap:break-word}
.steps li::before{content:counter(step);flex:none;width:26px;height:26px;margin-top:1px;border-radius:50%;background:var(--red);color:#fff;font-weight:800;font-size:14px;display:grid;place-items:center;font-variant-numeric:tabular-nums}
.card.contact{background:var(--red);color:#fff;border-color:var(--red);position:relative;overflow:hidden}
.card.contact::after{content:"";position:absolute;right:-90px;bottom:-90px;width:260px;height:260px;border-radius:50%;border:44px solid rgba(255,255,255,.12);pointer-events:none}
.card.contact p{color:#ffe6e8}
.card.contact .btn{position:relative;z-index:1;background:#fff;color:#B30A16;max-width:100%;overflow-wrap:anywhere;font-weight:700}

footer{border-top:1px solid var(--line);padding:30px 0 50px;font-size:14px;color:var(--muted)}
footer .wrap{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}
footer nav{gap:18px;display:flex;flex-wrap:wrap}

@media (max-width:980px){
  .layout{grid-template-columns:minmax(0,1fr);gap:20px;padding-top:28px}
  .toc{position:static;background:var(--card);border:1px solid var(--line);border-radius:20px;padding:16px}
  .toc p{padding-left:12px}
  .cards{max-width:none}
  header.site nav{display:none}
}
@media (max-width:640px){
  .wrap{padding:0 16px}
  .opening{padding-top:32px}
  .lede{font-size:19px}
  .layout{padding-bottom:70px}
  .card{padding:22px 18px;border-radius:22px}
  .right .btn{display:none}
  .card.contact .btn{font-size:15px;padding:14px 16px}
}
@media (prefers-reduced-motion:reduce){
  *{animation:none!important;transition:none!important;scroll-behavior:auto!important}
}
.langs{position:relative;border:0;padding:0}.langs summary{list-style:none;cursor:pointer;font-weight:800;font-size:13px;padding:0;display:flex;align-items:center;justify-content:center;width:40px}.langs summary::-webkit-details-marker{display:none}.langs summary::after{content:none}.langs div{position:absolute;right:0;top:46px;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:6px;display:grid;min-width:150px;box-shadow:var(--shadow);z-index:30}.langs a{padding:8px 12px;border-radius:9px;text-decoration:none;font-size:15px}.langs a:hover,.langs a[aria-current]{background:var(--bg2)}"""

SUN = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'

SCRIPT = """(() => {
  const root = document.documentElement;
  const store = { get(k){ try { return localStorage.getItem(k) } catch { return null } }, set(k,v){ try { localStorage.setItem(k,v) } catch {} } };
  const saved = store.get("dartpop-theme"); if (saved) root.dataset.theme = saved;
  document.getElementById("theme").addEventListener("click", () => {
    const dark = root.dataset.theme ? root.dataset.theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
    root.dataset.theme = dark ? "light" : "dark"; store.set("dartpop-theme", root.dataset.theme);
  });
  const header = document.querySelector("header.site");
  addEventListener("scroll", () => header.classList.toggle("scrolled", scrollY > 8), { passive: true });
})();"""


def build(lang, folder):
    t = T[lang]
    up = "../../" if folder else "../"          # site root, seen from this page
    home = "../"                                 # commercial page of the same language
    if lang == "fr":
        privacy = up + "privacy/"
    elif lang == "en":
        privacy = up + "privacy/#en"
    else:
        privacy = "../privacy/"                  # that language's own page (_tools/build_privacy.py)
    menu = "".join(
        '<a href="{}" hreflang="{}" lang="{}"{}>{}</a>'.format(
            "./" if l == lang else f"{up}{p}support/", l, l, ' aria-current="page"' if l == lang else "", name)
        for l, name, p in LANGS)
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{BASE}{p}support/">\n' for l, _, p in LANGS)
    alts += f'<link rel="alternate" hreflang="x-default" href="{BASE}en/support/">\n'
    contact_id, contact_title, contact_text = t["contact"]
    entries = [(i, title) for i, title, _ in t["sections"]] + [(contact_id, contact_title)]
    toc = "".join(f'<li><a href="#{i}">{title}</a></li>' for i, title in entries)
    cards = "".join(
        f'\n      <section class="card" id="{i}" aria-labelledby="{i}-title">\n        <h2 id="{i}-title">{title}</h2>\n        {body.replace("{privacy}", privacy)}\n      </section>'
        for i, title, body in t["sections"])
    cards += (f'\n      <section class="card contact" id="{contact_id}" aria-labelledby="{contact_id}-title">\n'
              f'        <h2 id="{contact_id}-title">{contact_title}</h2>\n        <p>{contact_text}</p>\n'
              f'        <a class="btn" href="mailto:{MAIL}">{MAIL}</a>\n      </section>')
    nav_home, nav_privacy, nav_contact = t["nav"]
    foot_home, foot_privacy, foot_support = t["footer"]
    page = f"""<!doctype html>
<html lang="{t['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{t['title']}</title>
<meta name="description" content="{t['description']}">
<meta property="og:title" content="{t['title']}">
<meta property="og:image" content="{up}assets/icon.png">
<meta name="theme-color" content="#F3EEE6" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#141210" media="(prefers-color-scheme: dark)">
{alts}<link rel="icon" href="{up}assets/icon.png">
<link rel="apple-touch-icon" href="{up}assets/touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>
<header class="site" id="top">
  <div class="wrap bar">
    <a class="wordmark" href="{home}" aria-label="{t['home_label']}">dart<b>pop</b></a>
    <nav aria-label="Sections">
      <a href="{home}">{nav_home}</a><a href="{privacy}">{nav_privacy}</a><a href="#{contact_id}">{nav_contact}</a>
    </nav>
    <div class="right">
      <details class="langs"><summary class="icon-btn" aria-label="Language">{lang.upper()}</summary><div>{menu}</div></details>
      <button class="icon-btn" id="theme" aria-label="{t['theme_label']}">
        {SUN}
      </button>
      <a class="btn btn-red" href="{STORE}">{t['download']}</a>
    </div>
  </div>
</header>

<main>
<div class="opening">
  <div class="opening-arc" aria-hidden="true"></div>
  <div class="wrap">
    <div class="kicker">{t['kicker']}</div>
    <h1 class="display"><span>{t['h1'][0]}</span><span class="r">{t['h1'][1]}</span></h1>
    <p class="lede">{t['lede']}</p>
    <p class="small">{t['updated']}</p>
  </div>
</div>

<div class="wrap layout">
  <nav class="toc" aria-label="{t['toc']}">
    <p>{t['toc']}</p>
    <ol>{toc}</ol>
  </nav>
  <div class="cards">{cards}
  </div>
</div>
</main>

<footer>
  <div class="wrap">
    <span>© 2026 Dartpop · Abdelhafid Younes</span>
    <nav aria-label="{t['legal_label']}">
      <a href="{home}">{foot_home}</a>
      <a href="{privacy}">{foot_privacy}</a>
      <a href="./" aria-current="page">{foot_support}</a>
    </nav>
  </div>
</footer>

<script>
{SCRIPT}
</script>
</body>
</html>
"""
    out = root / folder / "support" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page)
    print("built", out.relative_to(root))


for lang, _, folder in LANGS:
    build(lang, folder)
