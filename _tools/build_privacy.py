"""Builds the four single-language privacy pages: de/, es/, it/ and pt/privacy/.

Run from the site root: python3 _tools/build_privacy.py
French and English stay together in privacy/index.html, which is maintained by hand
and is the design reference: its <style>, theme button icon and script are copied
from it at build time, and each page is one language band of that page (top bar,
contents, cards with stable ids "<lang>-…", footer).

The legal text below is taken as is from the pages published on dartpop-support
(https://hafidnes.github.io/dartpop-support/<lang>/privacy.html, update of
16 November 2026): same sentences, same date. Do not reword or retranslate it here;
change it only together with the French and English text of privacy/index.html.
Interface labels (menus, buttons) are those of the support pages (build_support.py).
"""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
MAIL = "abdelhafid.younes@gmail.com"
STORE = "https://apps.apple.com/app/id6825865334"
# Language menu: French and English share privacy/, the four others have their own page.
MENU = [("fr", "Français", "privacy/"), ("en", "English", "privacy/#en"), ("de", "Deutsch", "de/privacy/"),
        ("es", "Español", "es/privacy/"), ("it", "Italiano", "it/privacy/"), ("pt", "Português", "pt/privacy/")]

T = {}

T["de"] = dict(
    html_lang="de", h1="Datenschutz", updated="Aktualisiert: 16. November 2026",
    home_label="Dartpop, Startseite", theme_label="Zwischen hellem und dunklem Design wechseln", download="Laden",
    home="Startseite", support="Support", toc="Inhalt", links_label="Rechtliche Links",
    sections=[
        ("spiele", "Deine Spiele bleiben auf deinem Gerät",
         "Spielernamen, Würfe, Punkte, Verlauf und Sicherungen werden lokal gespeichert und nicht an unsere Analysedienste gesendet. Du kannst sie in Dateien exportieren oder selbst teilen. Die zweite Punkteanzeige nutzt das lokale Netzwerk."),
        ("einmaliger-kauf", "Einmaliger Kauf",
         "Apple verarbeitet die Zahlung. RevenueCat erhält Transaktionsinformationen und eine pseudonyme Installationskennung, um Käufe zu prüfen und den dauerhaften Zugang wiederherzustellen. Wir erhalten keine Kartendaten. Kein Spielerkonto oder Abo erforderlich."),
        ("analyse-und-diagnose", "Analyse und Diagnose",
         "Freiwillig und standardmäßig deaktiviert. Dartpop fragt dich einmal; du kannst deine Entscheidung jederzeit in den Einstellungen mit dem Schalter „Dartpop verbessern helfen“ ändern. Wenn du zustimmst, erhält PostHog (in der Europäischen Union gehostet) eine feste Liste von Nutzungsereignissen, zusammengefasste Zähler und Regeloptionen mit einer zufälligen Kennung und ohne Personenprofil. Sentry (in der Europäischen Union gehostet) erhält Absturzberichte, die nur aus technischen Informationen neu aufgebaut werden. Spielernamen, Punktestände, Sicherungen, Bildschirmfotos und Sitzungsaufzeichnungen werden nie gesendet. PostHog-Standortbestimmung und Werbetracking sind deaktiviert. Wenn du ablehnst, werden weder PostHog noch Sentry gestartet."),
        ("dienstleister-und-speicherung", "Dienstleister und Speicherung",
         "Technische Daten werden von RevenueCat, PostHog und Sentry gemäß deren Richtlinien und den konfigurierten Speicherfristen verarbeitet, möglicherweise außerhalb deines Landes. Lokale Daten bleiben bis zur Löschung auf dem Gerät. Exportierte Sicherungen liegen in deiner Verantwortung."),
        ("moeglichkeiten-und-rechte", "Deine Möglichkeiten und Rechte",
         "Kontaktiere uns für Auskunft, Zugang oder Löschung technischer Daten zu deiner Person. Sende keine Passwörter oder Zahlungsdaten. Beim Löschen der App werden lokale Dateien entfernt; exportierte Sicherungen müssen separat gelöscht werden. Der Testzähler kann im iOS-Schlüsselbund bleiben und wird durch einen Import nicht zurückgesetzt."),
        ("herausgeber-und-kontakt", "Herausgeber und Kontakt",
         "Dartpop wird von Abdelhafid Younes herausgegeben. Datenschutzfragen und Anfragen an abdelhafid.younes@gmail.com."),
    ])

T["es"] = dict(
    html_lang="es", h1="Privacidad", updated="Actualizado: 16 de noviembre de 2026",
    home_label="Dartpop, inicio", theme_label="Cambiar entre tema claro y oscuro", download="Descargar",
    home="Inicio", support="Ayuda", toc="Contenido", links_label="Enlaces legales",
    sections=[
        ("partidas", "Tus partidas se quedan en el dispositivo",
         "Los nombres, dardos, puntos, historial y copias se guardan localmente y no se envían a nuestros servicios de análisis. Puedes exportarlos a Archivos o compartirlos por tu cuenta. La segunda pantalla usa la red local."),
        ("compra-unica", "Compra única",
         "Apple procesa el pago. RevenueCat recibe datos de la transacción y un identificador seudónimo de instalación para validar la compra y restaurar el acceso permanente. No recibimos datos de tarjeta. Sin cuenta de jugador ni suscripción."),
        ("analisis-y-diagnostico", "Análisis y diagnóstico",
         "Opcional y desactivado por defecto. Dartpop te lo pregunta una vez; puedes cambiar de opinión en cualquier momento en Ajustes con el interruptor Ayudar a mejorar Dartpop. Si aceptas, PostHog (alojado en la Unión Europea) recibe una lista cerrada de eventos de uso, recuentos agregados y opciones de reglas, con un identificador aleatorio y sin perfil de persona. Sentry (alojado en la Unión Europea) recibe informes de fallos reconstruidos solo con información técnica. Nunca se envían nombres, puntuaciones, copias de seguridad, capturas de pantalla ni grabaciones de sesión. La geolocalización de PostHog y el seguimiento publicitario están desactivados. Si lo rechazas, no se inician ni PostHog ni Sentry."),
        ("proveedores-y-conservacion", "Proveedores y conservación",
         "RevenueCat, PostHog y Sentry tratan los datos técnicos según sus políticas y los plazos configurados, posiblemente fuera de tu país. Los datos locales permanecen hasta que los elimines del dispositivo. Las copias exportadas quedan bajo tu control."),
        ("opciones-y-derechos", "Tus opciones y derechos",
         "Contacta para solicitar información, acceso o eliminación de datos técnicos relacionados contigo. No envíes contraseñas ni datos de pago. Eliminar la app borra sus archivos locales; las copias exportadas se eliminan por separado. El contador de prueba puede permanecer en el llavero de iOS y no se reinicia al importar."),
        ("editor-y-contacto", "Editor y contacto",
         "Dartpop está publicada por Abdelhafid Younes. Para cuestiones de privacidad escribe a abdelhafid.younes@gmail.com."),
    ])

T["it"] = dict(
    html_lang="it", h1="Privacy", updated="Aggiornato: 16 novembre 2026",
    home_label="Dartpop, home", theme_label="Alterna tra tema chiaro e scuro", download="Scarica",
    home="Home", support="Assistenza", toc="Sommario", links_label="Link legali",
    sections=[
        ("partite", "Le partite restano sul dispositivo",
         "Nomi, freccette, punteggi, cronologia e backup sono salvati localmente e non vengono inviati ai nostri servizi di analisi. Puoi esportarli in File o condividerli. Il secondo schermo usa la rete locale."),
        ("acquisto-unico", "Acquisto unico",
         "Apple gestisce il pagamento. RevenueCat riceve informazioni sulla transazione e un identificatore pseudonimo di installazione per verificare l’acquisto e ripristinare l’accesso permanente. Non riceviamo i dati della carta. Nessun account giocatore o abbonamento."),
        ("analisi-e-diagnostica", "Analisi e diagnostica",
         "Facoltativo e disattivato per impostazione predefinita. Dartpop te lo chiede una volta; puoi cambiare idea in qualsiasi momento nelle Impostazioni con l’interruttore Aiuta a migliorare Dartpop. Se accetti, PostHog (ospitato nell’Unione europea) riceve un elenco chiuso di eventi d’uso, conteggi aggregati e opzioni delle regole, con un identificativo casuale e senza profilo personale. Sentry (ospitato nell’Unione europea) riceve rapporti sugli arresti anomali ricostruiti solo con informazioni tecniche. Nomi, punteggi, backup, schermate e registrazioni di sessione non vengono mai inviati. La geolocalizzazione PostHog e il tracciamento pubblicitario sono disattivati. Se rifiuti, né PostHog né Sentry vengono avviati."),
        ("fornitori-e-conservazione", "Fornitori e conservazione",
         "RevenueCat, PostHog e Sentry trattano i dati tecnici secondo le loro politiche e i tempi configurati, anche fuori dal tuo Paese. I dati locali restano fino alla rimozione dal dispositivo. I backup esportati restano sotto il tuo controllo."),
        ("scelte-e-diritti", "Scelte e diritti",
         "Contattaci per informazioni, accesso o cancellazione dei dati tecnici che ti riguardano. Non inviare password o dati di pagamento. Eliminare l’app rimuove i file locali; i backup esportati vanno eliminati separatamente. Il contatore di prova può restare nel portachiavi iOS e non viene azzerato da un’importazione."),
        ("editore-e-contatto", "Editore e contatto",
         "Dartpop è pubblicata da Abdelhafid Younes. Per domande sulla privacy scrivi a abdelhafid.younes@gmail.com."),
    ])

T["pt"] = dict(
    html_lang="pt-PT", h1="Privacidade", updated="Atualizado: 16 de novembro de 2026",
    home_label="Dartpop, início", theme_label="Alternar entre tema claro e escuro", download="Descarregar",
    home="Início", support="Apoio", toc="Índice", links_label="Ligações legais",
    sections=[
        ("partidas", "As partidas ficam no dispositivo",
         "Nomes, dardos, pontos, histórico e cópias são guardados localmente e não são enviados aos serviços de análise. Podes exportá-los para Ficheiros ou partilhá-los. O segundo ecrã usa a rede local."),
        ("compra-unica", "Compra única",
         "A Apple processa o pagamento. O RevenueCat recebe informações da transação e um identificador pseudónimo de instalação para validar a compra e restaurar o acesso permanente. Não recebemos dados do cartão. Sem conta de jogador nem subscrição."),
        ("analise-e-diagnostico", "Análise e diagnóstico",
         "Opcional e desativado por predefinição. O Dartpop pergunta uma vez; pode mudar de ideias a qualquer momento nas Definições com o interruptor Ajudar a melhorar o Dartpop. Se aceitar, o PostHog (alojado na União Europeia) recebe uma lista fechada de eventos de utilização, contagens agregadas e opções de regras, com um identificador aleatório e sem perfil de pessoa. O Sentry (alojado na União Europeia) recebe relatórios de falhas reconstruídos apenas com informação técnica. Nomes, pontuações, cópias de segurança, capturas de ecrã e gravações de sessão nunca são enviados. A geolocalização do PostHog e o rastreio publicitário estão desativados. Se recusar, nem o PostHog nem o Sentry são iniciados."),
        ("prestadores-e-conservacao", "Prestadores e conservação",
         "RevenueCat, PostHog e Sentry tratam dados técnicos segundo as suas políticas e prazos configurados, podendo fazê-lo fora do teu país. Os dados locais ficam até serem removidos do dispositivo. As cópias exportadas ficam sob o teu controlo."),
        ("escolhas-e-direitos", "Escolhas e direitos",
         "Contacta-nos para pedir informações, acesso ou eliminação de dados técnicos sobre ti. Não envies palavras-passe nem dados de pagamento. Eliminar a app remove os ficheiros locais; as cópias exportadas devem ser eliminadas separadamente. O contador de experiência pode permanecer no porta-chaves iOS e não é reposto por uma importação."),
        ("editor-e-contacto", "Editor e contacto",
         "O Dartpop é publicado por Abdelhafid Younes. Para questões de privacidade escreve para abdelhafid.younes@gmail.com."),
    ])

reference = (root / "privacy" / "index.html").read_text()
CSS = re.search(r"<style>\n(.*?)\n</style>", reference, re.S).group(1)
SUN = re.search(r'<button class="icon-btn" id="theme"[^>]*>\s*(<svg.*?</svg>)', reference, re.S).group(1)
SCRIPT = re.search(r"<script>\n(.*?)\n</script>", reference, re.S).group(1)


def build(lang):
    t = T[lang]
    up = "../../"                                # site root, seen from <lang>/privacy/
    home, support = "../", "../support/"         # pages of the same language
    title = f"{t['h1']} · Dartpop"
    menu = "".join(
        '<a href="{}" hreflang="{}" lang="{}"{}>{}</a>'.format(
            "./" if l == lang else up + target, l, l, ' aria-current="page"' if l == lang else "", name)
        for l, name, target in MENU)
    toc = "".join(f'<li><a href="#{lang}-{i}">{heading}</a></li>' for i, heading, _ in t["sections"])
    cards = "".join(
        f'\n        <section class="card" id="{lang}-{i}" aria-labelledby="{lang}-{i}-title">\n'
        f'          <h2 id="{lang}-{i}-title">{heading}</h2>\n'
        f'          <p>{body.replace(MAIL, f"""<a href="mailto:{MAIL}">{MAIL}</a>""")}</p>\n        </section>'
        for i, heading, body in t["sections"])
    page = f"""<!doctype html>
<html lang="{t['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{title} · {t['updated']}">
<meta name="theme-color" content="#F3EEE6" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#141210" media="(prefers-color-scheme: dark)">
<link rel="icon" href="{up}assets/icon.png">
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
      <a href="{home}">{t['home']}</a><a href="{support}">{t['support']}</a>
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
<div class="lang" id="{lang}">
  <div class="opening-arc" aria-hidden="true"></div>
  <div class="wrap">
    <div class="opening">
      <div class="kicker">Dartpop</div>
      <h1 class="display">{t['h1']}</h1>
      <p class="small">{t['updated']}</p>
    </div>
    <div class="layout">
      <nav class="toc" aria-label="{t['toc']}">
        <p>{t['toc']}</p>
        <ol>{toc}</ol>
      </nav>
      <div class="cards">{cards}
      </div>
    </div>
  </div>
</div>
</main>

<footer>
  <div class="wrap">
    <span>© 2026 Dartpop · Abdelhafid Younes</span>
    <nav aria-label="{t['links_label']}">
      <a href="{home}">{t['home']}</a>
      <a href="{support}">{t['support']}</a>
    </nav>
  </div>
</footer>

<script>
{SCRIPT}
</script>
</body>
</html>
"""
    out = root / lang / "privacy" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page)
    print("built", out.relative_to(root))


for lang in T:
    build(lang)
