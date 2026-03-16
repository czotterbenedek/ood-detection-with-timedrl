## Self-Supervised Learning

### Alapötlet
- tanulás **címkézetlen adatokból**
- a modell **automatikusan generált feladatokat (pretext task)** old meg
- cél: **hasznos reprezentációk tanulása**

---

### Tanítási folyamat

**1. Pretraining**
- self-supervised feladat tanítása
- címkék helyett **adatból generált célok**
- eredmény: **pretrained encoder**

**2. Downstream task**
- a pretrained modell használata egy konkrét feladatra
- pl. klasszifikáció, regresszió
- két lehetőség:
  - **fine-tuning** (teljes modell továbbtanítása)
  - **feature extractor** használata

---

### Linear evaluation

- a **pretrained encoder fagyasztása**
- csak egy **lineáris osztályozó tanítása**
- cél: a tanult reprezentációk **minőségének mérése**

---

### Gyakori self-supervised módszerek

**Contrastive learning**
- hasonló minták közelítése
- különböző minták távolítása

**Masking alapú módszerek**
- input egy részének elrejtése
- a modell feladata a hiányzó rész predikciója

**Reconstruction alapú módszerek**
- input rekonstruálása
- pl. autoencoder

---

### Előnyök

- kevesebb **címkézett adat szükséges**
- jobb **általánosítás**
- hatékony **feature tanulás**