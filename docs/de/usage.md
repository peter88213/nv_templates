[Projekt-Homepage](https://peter88213.github.io/nv_templates) > Gebrauchsanleitung

--- 

Ein [noveltree](https://peter88213.github.io/noveltree/)-Plugin zur Verwaltung von "Erzählstruktur-Vorlagen" im Markdown-Format. 

---

# Installation

Wenn [noveltree](https://peter88213.github.io/noveltree/) installiert ist, installiert das Setup-Skript automatisch das*nv_templates*-Plugin im *noveltree* Plugin-Verzeichnis.

Das Plugin hängt einen **Erzählstruktur-Vorlagen**-Eintrag an das *noveltree* **Extras**-Menü, und einen **Template plugin Online Hilfe**-Eintrag an das **Hilfe**-Menü an. 

---

# Befelhlsreferenz

Das Untermenü mit **Extras > Erzählstruktur-Vorlagen** öffnen.

---

## Laden

Das lädt die Erzählstruktur aus einer Markdown-Vorlagendatei.

---

## Speichern

Das speichert die Erzählstruktur in eine Markdown-Vorlagendatei.

---

## Ordner öffnen

Das öffnet den Vorlagenordner mit dem Dateimanager des Betriebssystems, um die Vorlagen zu verwalten und zu bearbeiten.

---

# Konventionen

In *noveltree* kann man eine Erzählstruktur im "Planung"-Zweig, mit Kapiteln uns Abschnitten definieren. Siehe [Bögen](https://peter88213.github.io/noveltree/de/help/arcs). *nv_templates* erleichtert die Wiederverwendung solcher Erzählstrukturen.

## Struktur der Markdown-Datei

Die Markdown-*Erzählstruktur-Vorlage* definiert seine solche Struktur mit Überschriften und gewöhnlichem Text..

---

### Überschrift erster Ordnung

Die Überschrift erster Ordnung beginnt mit `#`, gefolgt von einem Leerzeichen und einem Titel. 

Two titles are allowed:
- `nv` for the "Planung" chapters in the *Narrative* tree, signifying e.g. acts.
- `pl` for the "Planung" parts, chapters, and scenes in the *Planung* tree, signifying story arcs and arc points.

---

### Überschrift zweiter Ordnung

Die Überschrift zweiter Ordnung beginnt mit  `##`, gefolgt von einem Leerzeichen und einem Teil-Titel.  

- One second level heading is required for creating the "Bögen" part in the *Planung* tree.

---

### Überschrift dritter Ordnung

Die Überschrift dritter Ordnung beginnt mit `###`, gefolgt von einem Leerzeichen und einem Kapiteltitel. 

- In the *Narrative* tree, a chapter signifying a story phase such as an act is created. 
- In the *Planung* tree, a chapter is created. If the heading contains a hyphen (`-`), the chapter defines an arc. Then the arc name will be the part of the chapter title that comes before the hyphen.

---

### Überschrift vierter Ordnung

Die Überschrift vierter Ordnung beginnt mit `####`, gefolgt von einem Leerzeichen und einem Abschnittstitel. 

- Under a chapter in the *Planung* tree, a scene signifying an arc point is created.

---

### Ordinary text

Any text under a heading is used as a description for the element generated from the heading.

---

### Example

```
# nv

### ACT 1

Setup

### ACT 2

Confrontation

### ACT 3

Resolution

# pl

## Bögen

### A-Storyline

Anwendening a three-act structure.

#### Inciting Incident

#### Plot Point 1

#### Midpoint

#### Plot Point 2

#### Climax

```

This file generates the following structure:

![Screenshot](Screenshots/structure01.png)

---

# Lizenz

Dies ist quelloffene Software, und das *nv_templates*-Plugin steht unter der GPLv3-Lizenz. Für mehr Details besuchen Sie die[Website der GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.de.html), oder schauen Sie sich die [LICENSE](https://github.com/peter88213/nv_templates/blob/main/LICENSE)-Datei an.
