# E-fill Privacy

Il 3 gennaio 2021 Michele Pinassi [segnala](https://twitter.com/michele_pinassi/status/1477920944169656320) che il portale dei pagamenti del suo comune utilizza il servizio ReCaptcha di Google senza riportarno nella privacy policy.

<blockquote class="twitter-tweet"><p lang="it" dir="ltr">Il portale dei pagamenti del mio comune, nella <a href="https://twitter.com/hashtag/privacypolicy?src=hash&amp;ref_src=twsrc%5Etfw">#privacypolicy</a>, non indica che nel codice del portare stesso è incluso lo strumento recaptcha di Google che, incorporato tramite js, acquisisce alcune informazioni relative agli utenti.<br><br>Che faccio? Segnalo? <a href="https://t.co/ACdylGOFvk">pic.twitter.com/ACdylGOFvk</a></p>&mdash; Mic Pin ☄ (@michele_pinassi) <a href="https://twitter.com/michele_pinassi/status/1477920944169656320?ref_src=twsrc%5Etfw">January 3, 2022</a></blockquote>

La stessa piattaforma di pagamento è utilizzata da moltissimi enti, ho quindi pensato di approfondire quanti sono e di che tipo sono.

In questo documento trovi i risultati della mia analisi e il proceso che ho seguito per arrivarci.

## Risultati

Ho individuato **1421 possibili piattaforme di pagamento**.

Di queste:

| Risultato | Quantità |
| --------- | -------- |
| Piattaforme di pagamento che **usano ReCaptcha** | 1272 |
| Siti che non sono piattaforme di pagamento | 15 |
| Siti che danno risposte HTTP != 200 | 34 | 
| DNS non esistente | 45 | 
| Siti che danno errore | 54 | 

Per ogni sito web che usano ReCaptcha ho provato a classificare l'ente che lo utilizza:

| Tipologia ente | Quantità |
| -------------- | -------- |
| Comuni/unione di comuni | 911 |
| Oridini professionali | 206 |
| Aziende (pubbliche e private) | 48 |
| Altro | 25 |
| Non classificate | 82 |

## Analisi

### 1. Ricerca sottodomini

Le piattaforme di pagamento sono hostate nel dominio plugandpay.it, per ricercare i sottodomini ho utilizzato il sito web [nmmapper.com](https://www.nmmapper.com/sys/tools/subdomainfinder/).

L'output è stato di 1421 sottodomini.

Ho pulito l'output con lo script `script.py`

### 2. Controllo contenuto

Per tutti i domini ho provato a connettermi, in base all'output assegno uno stato.

Procedura:

1. Se non viene trovato un record DNS per quel dominio lo scarto.
2. Non tutti i siti web contengono piattaforme di pagamento, alcuni sono domini utili per altre funzionalità. Questi vengono scartati.
3. Alcuni sottodomini rispondono con pagine di errore, quindi scarto tutte le pagine con stato HTTP diverso da 200.
4. Provo a capire se il sito web è effettivamente una piattaforma di pagamento controllando se la pagina contine il testo `Benvenuto nel portale dei pagamenti`
5. Infine controllo se la pagina contiene lo script a Google ReCaptcha.

Ho impostato un timeout di 15 secondi per ogni dominio, se non ricevo una risposta in tempo lo scarto.

Script: [`check.py`](check.py)

### 3. Classificazione

Dei domini che usano ReCaptcha ho provato a classificare la tipologia di ente che utilizza la piattaforma di pagamento.

Questa classificazione è basata su keyword, **quindi potrebbe non essere precisa.**

Script per pulire l'output: [`filter.py`](filter.py)

Script per classificare gli enti: [`classify.py`](classify.py)

### 4. Analisi

Ho creato una panoramica dei dati aggregandoli per

- contenuto dei sottodomini
- classificazione degli enti

Script: [`analytics.py`](analytics.py)

## Licenza

Il contenuto di questa repository è fornita secondo le seguente licenze:

- Codice: [MIT License](LICENSE)
- Testo: [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/)

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
