import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

col1,col2 = st.columns(2)

st.write('# DASHBOARD ESBORSI PREVISTI')

costo_ora = st.number_input("Costo orario server", value = 0.78, step = 0.01, min_value = 0.00)
costo_mensile_fisso = 1000

st.write('### Imposta il numero di ore')

luned = st.slider("Lunedì",value=(0,0),max_value=24)
marted = st.slider("Martedì",value=(0,0),max_value=24)
mercoled = st.slider("Mercoledì",value=(0,0),max_value=24)
gioved = st.slider("Giovedì",value=(0,0),max_value=24)
venerd = st.slider("Venerdì",value=(0,0),max_value=24)
sabat = st.slider("Sabato",value=(0,0),max_value=24)
domenic = st.slider("Domenica",value=(0,0),max_value=24)

lunedi = luned[1]-luned[0]
martedi = marted[1]-marted[0]
mercoledi = mercoled[1]-mercoled[0]
giovedi = gioved[1]-gioved[0]
venerdi = venerd[1]-venerd[0]
sabato = sabat[1]-sabat[0]
domenica = domenic[1]-domenic[0]

def Consumo(giorno):
  return (giorno * costo_ora)

# Creazione del grafico a barre con Streamlit

ArrayCost = pd.DataFrame({
'Giorni': ['1 - Lunedì','2 - Martedì','3 - Mercoledì','4 - Giovedì','5 - Venerdì','6 - Sabato','7 - Domenica'],
'Euro': [Consumo(lunedi),Consumo(martedi),Consumo(mercoledi),Consumo(giovedi),Consumo(venerdi),Consumo(sabato),Consumo(domenica)]
})

# Costo totale settimanale e mensile del server
costo = 0
for i in ArrayCost['Euro']:
  costo += i

cost = round(costo,2)

st.write('# COSTI TOTALI INFRASTRUTTURA')

st.write('### Costo totale SETTIMANALE:',
cost,'euro')

st.write('### Costo totale MENSILE:',
cost*4,'euro')

# Costo del nostro servizio

st.write("#")

Abbonamento = st.sidebar.radio(
  "Seleziona il tipo di servizio:",
  ["Basic","Avanzato","Completo"]
)
def Scritte():
  if Abbonamento == "Basic":
    st.sidebar.title("Funzionalità:")
    st.sidebar.subheader("1) Collegamento con Telegram ✅")
    st.sidebar.subheader("2) Addestramento RAG ✅")
    st.sidebar.subheader("3) Segna i messaggi non letti ✅")
    st.sidebar.subheader("4) Dashboard per il controllo del software ✅")
    st.sidebar.subheader("5) Manutenzione e miglioramento mensile ✅")
    st.sidebar.subheader("6) Collegamento canale TRFX ✅")
    st.sidebar.subheader("7) Risposte di recap ai clienti ✅")
    st.sidebar.subheader("8) Collegamento ai dati di mercato ❌")
    st.sidebar.subheader("9) Accesso alle notizie ❌")
    st.sidebar.subheader("10) Riepilogo situazione mercati ❌")
    st.sidebar.subheader("11) Lettura ed interpretazione immagini ❌")
  if Abbonamento == "Avanzato":
    st.sidebar.title("Funzionalità:")
    st.sidebar.subheader("1) Collegamento con Telegram ✅")
    st.sidebar.subheader("2) Addestramento RAG ✅")
    st.sidebar.subheader("3) Segna i messaggi non letti ✅")
    st.sidebar.subheader("4) Dashboard per il controllo del software ✅")
    st.sidebar.subheader("5) Manutenzione e miglioramento mensile ✅")
    st.sidebar.subheader("6) Collegamento canale TRFX ✅")
    st.sidebar.subheader("7) Risposte di recap ai clienti ✅")
    st.sidebar.subheader("8) Collegamento ai dati di mercato ✅")
    st.sidebar.subheader("9) Accesso alle notizie ✅")
    st.sidebar.subheader("10) Riepilogo situazione mercati ✅")
    st.sidebar.subheader("11) Lettura ed interpretazione immagini ❌")
  if Abbonamento == "Completo":
    st.sidebar.title("Funzionalità:")
    st.sidebar.subheader("1) Collegamento con Telegram ✅")
    st.sidebar.subheader("2) Addestramento RAG ✅")
    st.sidebar.subheader("3) Segna i messaggi non letti ✅")
    st.sidebar.subheader("4) Dashboard per il controllo del software ✅")
    st.sidebar.subheader("5) Manutenzione e miglioramento mensile ✅")
    st.sidebar.subheader("6) Collegamento canale TRFX ✅")
    st.sidebar.subheader("7) Risposte di recap ai clienti ✅")
    st.sidebar.subheader("8) Collegamento ai dati di mercato ✅")
    st.sidebar.subheader("9) Accesso alle notizie ✅")
    st.sidebar.subheader("10) Riepilogo situazione mercati ✅")
    st.sidebar.subheader("11) Lettura ed interpretazione immagini ✅")

Scritte()

def CostoAbbonamento():
  if (Abbonamento == "Basic"):
    return 600
  if (Abbonamento == "Avanzato"):
    return 850
  if (Abbonamento == "Completo"):
    return 1000

st.write('')

# Ora plottiamo anche un bel grafico a torta sulle componenti dei costi

QuotaLorda = CostoAbbonamento()/2

INPS = CostoAbbonamento()/100*78/100*26*2

Contributi = CostoAbbonamento()/100*78/100*5

Suddivisione = [QuotaLorda-(INPS + Contributi)/2,QuotaLorda-(INPS + Contributi)/2,INPS,Contributi]

Nomi = 'Manutenzione','Programmazione','INPS','Contributi'

def Quota(Parziale):
  return (100/CostoAbbonamento()*Parziale)

Quote = [Quota(QuotaLorda-(INPS+Contributi)/2),Quota(QuotaLorda-(INPS+Contributi)/2),Quota(INPS),Quota(Contributi)]

explode = (0.1, 0.1, 0, 0)  # only "explode" the 2nd slice

fig1, ax1 = plt.subplots()
ax1.pie(Quote, explode=explode, labels=Nomi, autopct='%1.1f%%',
        shadow=True, startangle=90)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


st.write('# Consumo giornaliero atteso')

st.bar_chart(ArrayCost, x = 'Giorni', y = 'Euro')

st.write("# Parcella per PROGRAMMAZIONE e MANUTENZIONE")

st.write("### Costo mensile del servizio:",CostoAbbonamento())

st.pyplot(fig1)

def CalcoloPercentuale(numero):
  return (CostoAbbonamento()/100*numero)

ArrayCost = pd.DataFrame({
'Euro': [cost*4,CalcoloPercentuale(Quota(QuotaLorda-(INPS+Contributi)/2)),CalcoloPercentuale(Quota(QuotaLorda-(INPS+Contributi)/2)),CalcoloPercentuale(Quota(INPS)),CalcoloPercentuale(Quota(Contributi))],
'Spese': ['Infrastruttura','Nicola','Matteo','Ritenute INPS','Contributi']
})

st.bar_chart(ArrayCost, x = 'Spese', y = 'Euro')

st.write('# Totale costi MENSILI previsti:',CostoAbbonamento()+cost*4 )
