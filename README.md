
PHISHING URL

1. The phishing attacks are often made to get sensitive information from the user.
2. Several techniques are employed to clickbait the user, such as Bit squatting, Typo squatting, Mimicking trusted websites, Redirection, Visual Spoofing like Homograph, or homoglyph attacks.
3. These URLs can store sensitive information, deliver malware, and save IP addresses, browser fingerprints, and device metadata. These URLs are often redirecting users to other links.
4. Considering the overall increase in cyber threats, we were interested in analyzing the feartures that can spot spam URLs.

DATASET

1. Dataset Sources: The dataset is created by combining 4 dataset taken from different times frame to maintain the variation

           (235795, 56) records from UC Irvine ML repository 2023-24 [1]
           (11430, 56) from Kaggle  2021[2]
           (500,1)  from Phish Tank 2021 [3]
           (50000, 2) records from Kaggle 2023 [4]
2. Total Features: 56

DATA PREPROCESSING
1. Web crawling to get all the feature of the records of the dataset 2,3,4 to make it compatible with the first one.
2. Handling NULL values
3. Significance Test and dropping
4. Adding more features by using the existing features( Total features 65)
5. Significance test and dropping the features that were least 
 significant(Total features 56)
6. Additional feature Information:DotCount

          UpperCase letters count
          TitleLength using “Title”
          URL Entropy
          Keyword frequency features are created, such as Has login, Has password, Has secure, and so o
   <img width="89" alt="Capture" src="https://github.com/user-attachments/assets/1f4ade48-20c9-44d2-9407-c3cb9c927abf" />
n.

ARCHITECTURE


PERFORMANCE OF THE BASE MODELS

<img width="479" alt="Capturje" src="https://github.com/user-attachments/assets/21a92d27-192d-49c5-8b5a-0c217bc3658f" />

PERFORMANCE OF THE MODELS OVER THE YEARS

<img width="315" alt="Capturdfse" src="https://github.com/user-attachments/assets/4d585f25-4e9a-4210-a8b5-fcf7e501bcdf" />

HYPER-PARAMETER TUNING
1. Applied GridSearch to optimize the hyperparameters.
2. Since the model was already showing a good accuracy, no improvement has been noted.



ADVANCE HYPER-PARAMETER TUNING

New Advance Hyper-parameter tuning algorithm called Optuna was applied and again no increase or decrease of the accuracy has been noted.


FEATURE IMPORTANCE

<img width="345" alt="mdi" src="https://github.com/user-attachments/assets/608a082e-0397-4d1e-9b1f-e05edaec039a" />

MOST IMPORTANT FEATURE DETECTED

<img width="633" alt="MIF" src="https://github.com/user-attachments/assets/f8fc7054-066c-44be-8847-0ce3f42bb53f" />


