## OOD (Out-of-Distribution) detektálási módszerek

### 1. Output alapú módszerek

**Maximum Softmax Probability (MSP)**
- a legnagyobb softmax valószínűség vizsgálata
- alacsony érték → valószínű OOD

**ODIN**
- temperature scaling
- bemenet kis perturbálása
- új softmax score alapján döntés

**Energy-based score**
- logit értékekből számolt energia
- magas energia → OOD

---

### 2. Feature space alapú módszerek

**Mahalanobis distance**
- osztályonkénti feature centroid számítása
- új minta távolságának mérése
- nagy távolság → OOD

**k-Nearest Neighbors (kNN)**
- embedding térben legközelebbi szomszéd keresése
- nagy távolság → OOD

---

### 3. Uncertainty alapú módszerek

**Monte Carlo Dropout**
- többszöri inference dropout használatával
- nagy predikciós szórás → OOD

**Deep Ensembles**
- több külön modell predikciója
- nagy eltérés a modellek között → OOD

---

### 4. Generatív / density alapú módszerek

**Autoencoder**
- rekonstrukciós hiba vizsgálata
- nagy hiba → OOD

**Variational Autoencoder (VAE)**
- valószínűségi modell az adatokra
- alacsony likelihood → OOD

**Normalizing Flows**
- explicit density becslés
- alacsony valószínűség → OOD

---

### 5. Tanítás közbeni módszerek

**Outlier Exposure**
- tanítás során OOD példák használata
- cél: OOD mintáknál magas bizonytalanság