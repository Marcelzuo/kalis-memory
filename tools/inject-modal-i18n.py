#!/usr/bin/env python3
"""Inject 20 modal i18n keys into fr/de/it/es blocks in index.html __LANGS__."""

import json
import sys
from pathlib import Path

INDEX = Path(__file__).resolve().parent.parent / "index.html"

TRANSLATIONS = {
    "fr": {
        "qm_title": "Inspection Qualité",
        "qm_subtitle": "Photos et vidéos avant le paiement du solde. Chaque pièce vérifiée.",
        "qm_card1_title": "Échantillon Pré-Production",
        "qm_card1_text": "Nous partageons des photos et une courte vidéo de la première pièce avant le début de la production en série.",
        "qm_card2_title": "Contrôle Intermédiaire",
        "qm_card2_text": "À environ 30% d'achèvement, nous inspectons à nouveau. Cela détecte la plupart des problèmes avant qu'ils ne se propagent.",
        "qm_card3_title": "Rapport Pré-Expédition",
        "qm_card3_text": "Avant le paiement du solde, vous recevez un rapport complet avec photos et vidéo. Vous décidez.",
        "promo_title": "Promotions en Cours",
        "promo_countdown": "La vente se termine dans 3 jours · 12:34:56",
        "promo_total": "Total",
        "promo_cta": "Envoyer la Demande",
        "inq_name_label": "Nom *",
        "inq_name_placeholder": "Votre nom",
        "inq_email_label": "E-mail *",
        "inq_email_placeholder": "votre@email.com",
        "inq_message_label": "Message",
        "inq_message_placeholder": "Ce produit m'intéresse. Veuillez établir un devis.",
        "inq_submit": "Envoyer",
        "inq_success": "Demande envoyée ! Nous répondrons dès que possible.",
    },
    "de": {
        "qm_title": "Qualitätskontrolle",
        "qm_subtitle": "Fotos und Videos vor der Restzahlung. Jedes Stück wird geprüft.",
        "qm_card1_title": "Vorproduktionsmuster",
        "qm_card1_text": "Wir teilen Fotos und ein kurzes Video des ersten Stücks, bevor die Serienproduktion beginnt.",
        "qm_card2_title": "Zwischenkontrolle",
        "qm_card2_text": "Bei etwa 30 % Fertigstellung prüfen wir erneut. Das erkennt die meisten Probleme, bevor sie sich ausbreiten.",
        "qm_card3_title": "Vorversandbericht",
        "qm_card3_text": "Vor der Restzahlung erhalten Sie einen vollständigen Bericht mit Fotos und Video. Sie entscheiden.",
        "promo_title": "Aktuelle Aktionen",
        "promo_countdown": "Angebot endet in 3 Tagen · 12:34:56",
        "promo_total": "Gesamt",
        "promo_cta": "Anfrage Senden",
        "inq_name_label": "Name *",
        "inq_name_placeholder": "Ihr Name",
        "inq_email_label": "E-Mail *",
        "inq_email_placeholder": "ihre@email.com",
        "inq_message_label": "Nachricht",
        "inq_message_placeholder": "Ich interessiere mich für dieses Produkt. Bitte erstellen Sie ein Angebot.",
        "inq_submit": "Senden",
        "inq_success": "Anfrage gesendet! Wir antworten so schnell wie möglich.",
    },
    "it": {
        "qm_title": "Ispezione Qualità",
        "qm_subtitle": "Foto e video prima del pagamento del saldo. Ogni pezzo verificato.",
        "qm_card1_title": "Campione di Pre-Produzione",
        "qm_card1_text": "Condividiamo foto e un breve video del primo pezzo prima dell'inizio della produzione in serie.",
        "qm_card2_title": "Controllo Intermedio",
        "qm_card2_text": "A circa il 30% del completamento, ispezioniamo di nuovo. Questo rileva la maggior parte dei problemi prima che si diffondano.",
        "qm_card3_title": "Rapporto Pre-Spedizione",
        "qm_card3_text": "Prima del pagamento del saldo, ricevi un rapporto completo con foto e video. Decidi tu.",
        "promo_title": "Promozioni in Corso",
        "promo_countdown": "La vendita termina tra 3 giorni · 12:34:56",
        "promo_total": "Totale",
        "promo_cta": "Invia Richiesta",
        "inq_name_label": "Nome *",
        "inq_name_placeholder": "Il tuo nome",
        "inq_email_label": "Email *",
        "inq_email_placeholder": "tua@email.com",
        "inq_message_label": "Messaggio",
        "inq_message_placeholder": "Sono interessato a questo prodotto. Per favore, inviate un preventivo.",
        "inq_submit": "Invia",
        "inq_success": "Richiesta inviata! Ti risponderemo il prima possibile.",
    },
    "es": {
        "qm_title": "Inspección de Calidad",
        "qm_subtitle": "Fotos y videos antes del pago del saldo. Cada pieza verificada.",
        "qm_card1_title": "Muestra de Preproducción",
        "qm_card1_text": "Compartimos fotos y un breve video de la primera pieza antes de que comience la producción en serie.",
        "qm_card2_title": "Control Intermedio",
        "qm_card2_text": "Aproximadamente al 30% de finalización, inspeccionamos de nuevo. Esto detecta la mayoría de los problemas antes de que se extiendan.",
        "qm_card3_title": "Informe Pre-Envío",
        "qm_card3_text": "Antes del pago del saldo, recibe un informe completo con fotos y video. Usted decide.",
        "promo_title": "Promociones Actuales",
        "promo_countdown": "La oferta termina en 3 días · 12:34:56",
        "promo_total": "Total",
        "promo_cta": "Enviar Consulta",
        "inq_name_label": "Nombre *",
        "inq_name_placeholder": "Su nombre",
        "inq_email_label": "Correo Electrónico *",
        "inq_email_placeholder": "su@email.com",
        "inq_message_label": "Mensaje",
        "inq_message_placeholder": "Me interesa este producto. Por favor, envíe una cotización.",
        "inq_submit": "Enviar",
        "inq_success": "¡Consulta enviada! Le responderemos lo antes posible.",
    },
}

# Boundary markers: lang block ends right before the next lang starts
NEXT_LANG = {"fr": "de", "de": "it", "it": "es", "es": "pt"}


def build_pairs(trans: dict) -> str:
    """Build JSON key:value pairs string from translations dict."""
    parts = []
    for k, v in trans.items():
        parts.append(f'"{k}":"{v}"')
    return ",".join(parts)


def inject_lang(html: str, lang: str) -> tuple[str, bool]:
    """Inject TRANSLATIONS[lang] before the closing } of the lang block.
    Returns (new_html, changed)."""
    trans = TRANSLATIONS[lang]
    pairs = build_pairs(trans)

    next_lang = NEXT_LANG[lang]
    # The closing } is right before ,"<next_lang>":
    marker = f'}},"{next_lang}":'
    idx = html.find(marker)
    if idx == -1:
        print(f"  [WARN] marker not found for {lang}: {marker}")
        return html, False

    # Check if already injected
    first_key = list(trans.keys())[0]
    # Find the lang block start to limit our search scope
    block_start = html.find(f',"{lang}":')
    if block_start == -1:
        block_start = html.find(f'"{lang}":')
    block_before_marker = html[block_start:idx]

    if f'"{first_key}"' in block_before_marker:
        print(f"  [SKIP] {lang}: keys already present")
        return html, False

    # Insert pairs, before the closing }
    # marker = '},"<next_lang>":' -> we want to insert before the }
    # So replace '},"<next_lang>":' with ',' + pairs + '},"<next_lang>":'
    new_marker = f',{pairs}{marker}'
    html = html[:idx] + new_marker + html[idx + len(marker):]
    return html, True


def main():
    print(f"Reading {INDEX}")
    html = INDEX.read_text(encoding="utf-8")

    changed = False
    for lang in ["fr", "de", "it", "es"]:
        new_html, did_change = inject_lang(html, lang)
        if did_change:
            html = new_html
            changed = True
            print(f"  [OK] injected {len(TRANSLATIONS[lang])} keys into {lang}")
        if new_html != html and not did_change:
            pass  # html was not updated, skip case handled inside inject_lang

    if changed:
        INDEX.write_text(html, encoding="utf-8")
        print(f"Written: {INDEX}")
    else:
        print("No changes needed.")

    # Verify
    from subprocess import run
    result = run(["grep", "-c", "qm_title", str(INDEX)], capture_output=True, text=True)
    count = result.stdout.strip()
    print(f"grep -c qm_title: {count}")

    result2 = run(["grep", "-o", '"qm_title"', str(INDEX)], capture_output=True, text=True)
    matches = result2.stdout.strip().split("\n") if result2.stdout.strip() else []
    print(f"Total qm_title occurrences: {len(matches)}")


if __name__ == "__main__":
    main()
