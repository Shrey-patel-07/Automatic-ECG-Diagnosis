# Neural Not works

Shrey Patel

Tirth Patel

Perin Modi

VInit Chokshi

Karan Patel

# Abstract

The project revolves around analyzing electrocardiogram (ECG) data to predict the presence of cardiac diseases. The dataset consists of 827 records, each containing 4096 samples (cycles) of 12 leads of ECG. The primary objective is to study these leads and develop a predictive model to determine if a patient exhibits symptoms indicative of cardiac diseases.

The data is stored in .hdf5 files in a standardized format. Given a .hdf5 file containing ECG data, the goal is to predict whether the patient has a high likelihood of having cardiac diseases. This abstract provides an overview of the project's scope and aims, emphasizing the importance of utilizing ECG data for early detection and intervention in cardiac health.

![WhatsApp Image 2024-03-16 at 16.06.44.jpeg](Neural%20Not%20works%20f8834496dca84531a2009d370a685e3a/WhatsApp_Image_2024-03-16_at_16.06.44.jpeg)

![WhatsApp Image 2024-03-16 at 23.22.02.jpeg](Neural%20Not%20works%20f8834496dca84531a2009d370a685e3a/WhatsApp_Image_2024-03-16_at_23.22.02.jpeg)

## **Understanding ECG(Electro Cardiogram)**

### First-degree atrioventricular (AV) block

First-degree atrioventricular (AV) block, also known as first-degree heart block, is **a condition that causes a delay in conduction through the AV node**. This is defined by an electrocardiogram (ECG) that shows a PR interval of more than 0.20 seconds, without disrupting atrial to ventricular conduction. 

![first-degree-heart-block-av.png](Neural%20Not%20works%20f8834496dca84531a2009d370a685e3a/first-degree-heart-block-av.png)

### Right bundle branch block (RBBB)

Right bundle branch block (RBBB) is **a heart condition that occurs when there is a disruption in the electrical signals that travel through the right bundle branch of the heart's electrical conduction system**. This prevents the right ventricle from being directly activated by the impulses, which can cause an irregular heartbeat. RBBB can be complete or incomplete, and usually doesn't cause symptoms unless you have another heart condition. 

![21692-right-bundle-branch-block-illustration.jpg](Neural%20Not%20works%20f8834496dca84531a2009d370a685e3a/21692-right-bundle-branch-block-illustration.jpg)

### Left bundle branch block (LBBB)

A delay or blockage of electrical impulses to the left side of the heart.

Left bundle branch block sometimes makes it harder for the heart to pump blood efficiently through the circulatory system.

Most people don't have symptoms. If symptoms occur, they include fainting or a slow heart rate.

If there's an underlying condition, such as heart disease, that condition needs treatment. In patients with heart failure, a pacemaker can also relieve symptoms as well as prevent death.

### Sinus bradycardia (SB)

Sinus bradycardia is **a heart rhythm that's slower than normal, with a resting heart rate of 60 beats per minute (bpm) or less**

. It occurs when the sinoatrial node fires less than 60 times per minute. Sinus bradycardia can be normal in some people, such as athletes and older adults. In other cases, it can be a symptom of certain heart conditions or problems.

![22473-sinus-bradycardia.jpg](Neural%20Not%20works%20f8834496dca84531a2009d370a685e3a/22473-sinus-bradycardia.jpg)

### Atrial fibrillation (AFib)

Atrial fibrillation (AFib) is **a heart condition that causes an irregular and often very fast heart rate**

. It's the most common type of treated heart arrhythmia, which is when the heart beats too slowly, too fast, or in an irregular way. AFib can happen in brief episodes, or it may be a permanent condition.

![shutterstock_89144557.webp](Neural%20Not%20works%20f8834496dca84531a2009d370a685e3a/shutterstock_89144557.webp)

### Sinus tachycardia (ST)

Sinus tachycardia is **a normal heart rhythm where the heart beats faster than normal, often in response to exercise or stress**. It's characterized by an increased rate of electrical discharge from the sinoatrial (SA) node, which results in a heart rate higher than the upper limit of normal. The normal resting heart rate for an adult is 60–90 bpm, while sinus tachycardia is when the heart rate is above 100 bpm.

![WhatsApp Image 2024-03-16 at 16.06.58.jpeg](Neural%20Not%20works%20f8834496dca84531a2009d370a685e3a/WhatsApp_Image_2024-03-16_at_16.06.58.jpeg)

# UNDERSTANDING THE DATA

**ECG Leads Explained**

- **Standard Limb Leads (I, II, III):** Form an imaginary triangle (Einthoven's Triangle) around the heart, providing a view of electrical activity from different angles.
- **Augmented Limb Leads (aVR, aVL, aVF):** Offer additional perspectives on the heart's frontal plane.
- **Precordial Leads (V1-V6):** Placed across the chest, these leads give a view of electrical activity in the horizontal plane.

**Conditions and Their Impact on ECG Leads**

- **1st Degree AV Block (1dAVb):**
    - **Key ECG Change:** Prolonged PR interval (greater than 0.2 seconds) seen consistently across multiple leads. This indicates a delay in conduction from the atria to the ventricles.
- **Right Bundle Branch Block (RBBB):**
    - **Key ECG Changes:**
        - Wide QRS complex (greater than 0.12 seconds)
        - 'RSR' pattern (sometimes referred to as a "bunny ears" pattern) in V1 and V2.
        - Wide, slurred S wave in leads I, V5, and V6.
- **Left Bundle Branch Block (LBBB):**
    - **Key ECG Changes:**
        - Wide QRS complex (greater than 0.12 seconds)
        - Broad, often notched or slurred R waves in leads I, aVL, V5, and V6.
        - Deep S waves in V1 and V2.
- **Sinus Bradycardia (SB):**
    - **Key ECG Change:** Slow heart rate (less than 60 beats per minute) with normal P waves, PR intervals, and QRS complexes. All leads would show this slower rate.
- **Atrial Fibrillation (AF):**
    - **Key ECG Changes:**
        - Irregularly irregular rhythm (no consistent pattern in the distance between heartbeats).
        - Absent P waves, replaced by chaotic, fibrillatory waves.
        - QRS complexes may be normal or wide depending on other underlying conditions.
- **Sinus Tachycardia (ST):**
    - **Key ECG Change:** Fast heart rate (greater than 100 beats per minute) with normal P waves, PR intervals, and QRS complexes. Again, changes would appear consistently across the leads.

**Important Considerations:**

- **Complexity:** Real-world ECG interpretation is more complex than just identifying isolated changes. Doctors consider multiple factors, including the patient's clinical presentation, to arrive at an accurate diagnosis.
- **Variations:** There can be variations in ECG patterns depending on the severity of the condition and the presence of other underlying heart problems.

**For further understanding, I highly recommend searching for images of ECG tracings for each of the mentioned conditions. This will help you visualize the specific changes in different leads.**

## Methods

- Data:
    - The testing dataset used in the paper is publicly available and can be downloaded from the provided sources.
    - Part of the training data (CODE-15% dataset) is openly available, while the full CODE dataset used for training is available upon request for research purposes.
- Model Architecture:
    - The model used is a residual neural network (ResNet) implemented in Keras.
    - The architecture of the model is defined in the [model.py](http://model.py/) module.
    - The model takes an input tensor of shape (N, 4096, 12), where N is the batch size, 4096 is the number of ECG data points sampled at 400Hz, and 12 represents the 12 different ECG leads.
    - All signal are represented as 32 bits floating point numbers at the scale 1e-4V: so if the signal is in V it should be multiplied by 1000 before feeding it to the neural network model.
    - The output of the model is a tensor of shape (N, 6), where each entry represents the probability of a specific abnormality being present.
    
    ![Untitled](Neural%20Not%20works%20f8834496dca84531a2009d370a685e3a/Untitled.png)
    

![Untitled](Neural%20Not%20works%20f8834496dca84531a2009d370a685e3a/Untitled%201.png)

- Training:
    - The [train.py](http://train.py/) script is used for training the neural network.
    - The script takes the path to the HDF5 file containing the ECG tracings and the path to the CSV file with the corresponding labels.
    - Pre-trained models obtained using this script are available for download.
- Prediction:
    - The [predict.py](http://predict.py/) script is used for generating predictions on a given dataset using a trained model.
    - The script takes the path to the HDF5 file with ECG tracings, the path to the trained model, and optionally, the path to the output file for saving the predictions.
- Evaluation:
    - The generate_figures_and_tables.py script is used to generate figures and tables from the paper.
    - It analyzes the predictions obtained from the trained models and generates visualizations and performance metrics.

## Results:

### Test Accuracy : 84.3375%

## Features to be extracted  for Analysis:

1. Rhythm 
2. Rate 
3. Axis
4. PR interval 
5. Q wave 
6. QRS complex
7. QT interval
8. ST interval
9. T wave

- **Heart Rate (HR):** Calculate HR (beats per minute) using R-peaks. - T
- **Intervals:** Calculate PR interval, QRS duration, QT interval.
- **Wave Amplitudes:** Calculate P-wave, QRS complex, T-wave amplitudes.
- **Time Domain:** Calculate SDNN, RMSSD, pNN50, etc.
- **Frequency Domain:** Calculate power in LF, HF, and the LF/HF ratio.

It contain annotations about 6 different ECGs abnormalities:

- 1st degree AV block (1dAVb);
- right bundle branch block (RBBB);
- left bundle branch block (LBBB);
- sinus bradycardia (SB);
- atrial fibrillation (AF); and,
- sinus tachycardia (ST).

1. **1st Degree AV Block (1dAVb):** This condition involves a delay in the conduction of electrical signals between the atria and ventricles of the heart. It's characterized by a prolonged PR interval on the ECG, meaning there's a delay in the time it takes for the electrical impulse to travel from the atria to the ventricles.
2. **Right Bundle Branch Block (RBBB):** RBBB occurs when there is a delay or blockage in the electrical impulses traveling through the right bundle branch of the heart's electrical conduction system. This results in a widening of the QRS complex on the ECG, typically seen as a broad, slurred S wave in leads V1 and V2.
3. **Left Bundle Branch Block (LBBB):** LBBB is similar to RBBB but involves blockage or delay in the electrical impulses traveling through the left bundle branch. It also results in a widened QRS complex, often with an additional R wave (called R' wave) in lateral leads (I, aVL, V5, V6) and a broad, monophasic S wave in V1.
4. **Sinus Bradycardia (SB):** Sinus bradycardia is a rhythm in which the heart beats at a slower rate than normal. It originates from the sinus node, the heart's natural pacemaker, but the rate is slower than the typical range (usually below 60 beats per minute in adults).
5. **Atrial Fibrillation (AF):** AF is a common heart rhythm disorder characterized by irregular and often rapid heart rate. Instead of a coordinated contraction of the atria, they quiver (fibrillate) irregularly, leading to irregular ventricular response. This appears on ECG as irregularly irregular rhythm without distinct P waves, and irregularly spaced QRS complexes.
6. **Sinus Tachycardia (ST):** Sinus tachycardia is a rhythm originating from the sinus node but with an elevated heart rate. It's a response to various physiological or pathological conditions, such as exercise, fever, anxiety, or certain medications. It's characterized by a heart rate greater than 100 beats per minute with normal P waves and QRS complexes.