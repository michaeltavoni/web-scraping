# Web scraping - clothing website

**Progetto**
- **Descrizione:** Progetto di web-scraping per un piccolo sito di abbigliamento italiano, con l'obiettivo di raccogliere dati su brand, categoria, descrizione e prezzo degli articoli.
- **Obiettivo:** Generare un dataset pulito pronto per analisi esplorative e visualizzazioni.

**Requisiti**
- **Python:** 3.8+ consigliato.
- **Dipendenze:** installare con `pip install -r requirements.txt`.
- **File principali:** - notebook.ipynb - htmlContent.json - collectionsData.csv - htmlGrabber.py

**Installazione**
- **Clona repo:** usa il tuo metodo preferito.
- **Installa dipendenze:** `pip install -r requirements.txt`
- **Apri il notebook:** avvia `jupyter notebook` o apri notebook.ipynb in un ambiente compatibile.

**Uso del pacchetto htmlGrabber**
- **Scopo:** htmlGrabber è un piccolo modulo per scaricare e serializzare pagine web in oggetti Python (es. dizionari) e salvarle localmente per lo scraping offline.
- **Output tipico:** oggetti contenenti almeno `url`, `html` (contenuto), `timestamp` e `status_code` oppure un file JSON aggregato in htmlContent.json.
- **Esempio d'uso (generico):**
  - Import: `from htmlGrabber import htmlGrabber`
  - Scarico singolo/pulled list: creare una lista di URL e passarla alla funzione di grab; i risultati vengono salvati in raw.
  - Nota: consultare htmlGrabber.py per l'API esatta del pacchetto.

**Cosa fa il notebook**
- **Caricamento dati:** legge il file grezzo delle pagine scaricate (htmlContent.json).
- **Parsing HTML:** usa BeautifulSoup (o simili) per estrarre i campi rilevanti: **Brand**, **Categoria**, **Descrizione**, **Prezzo**.
- **Pulizia dati:** normalizza stringhe, rimuove valori mancanti o duplicati, converte prezzi in formato numerico.
- **Output:** salva il dataset pulito in collectionsData.csv.
- **Riproducibilità:** il notebook è organizzato in celle per ciascuna fase (caricamento → parsing → pulizia → esportazione) per facilità di riproduzione e debug.

**Esempio di estrazione (snippet concettuale)**
- Legge: `data = json.load(open('data/raw/htmlContent.json'))`
- Per ogni pagina: usare BeautifulSoup per trovare selettori CSS/XML corrispondenti a brand, descrizione e prezzo.
- Compone DataFrame con `pandas` e salva: `df.to_csv('data/final/collectionsData.csv', index=False)`

**Struttura della repository**
- **notebook.ipynb**: notebook principale con pipeline di scraping->parsing->cleaning.
- **htmlGrabber**: modulo per il download delle pagine.
- **raw**: contenuto HTML grezzo (`htmlContent.json`).
- **final**: dataset finale esportato (`collectionsData.csv`).
- **requirements.txt**: dipendenze del progetto.

**Prossimi passi (analisi futura)**

- **Analisi esplorativa:** distribuzioni dei prezzi, frequenza per brand, percentuale per categoria.
- **Visualizzazioni:** istogrammi, boxplot prezzi per brand, heatmap disponibilità/variazioni.
- **Arricchimenti:** normalizzazione brand, estrazione di taglia/colore se presenti, deduplica avanzata.
- **Automazione:** trasformare htmlGrabber in CLI o job schedulato per aggiornamenti periodici.

**Contribuire**
- **Segnala issue:** apri un issue per bug o feature.
- **Pull request:** descrivi chiaramente le modifiche e aggiorna requirements.txt se serve.
- **Stile codice:** mantieni coerenza con lo stile Python del progetto.