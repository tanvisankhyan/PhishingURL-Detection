import re
import joblib  
import numpy as np

def analyze_html(html):
    HasTitle = 1 if '<title>' in html and '</title>' in html else 0
    TitleLength = len(re.search(r'<title>(.*?)</title>', html).group(1)) if HasTitle else 0
    HasFavicon = 1 if re.search(r'<link[^>]+rel=["\']?icon["\']?', html, re.IGNORECASE) else 0
    IsResponsive = 1 if re.search(r'<meta[^>]+name=["\']?viewport["\']?', html, re.IGNORECASE) else 0
    HasDescription = 1 if re.search(r'<meta[^>]+name=["\']?description["\']?', html, re.IGNORECASE) else 0
    NoOfPopup = len(re.findall(r'popup|window\.open|alert', html, re.IGNORECASE))  
    NoOfiFrame = len(re.findall(r'<iframe', html, re.IGNORECASE))
    HasSocialNet = 1 if any(social in html.lower() for social in ['facebook', 'twitter', 'linkedin', 'instagram']) else 0
    HasSubmitButton = 1 if re.search(r'<(button|input)[^>]+type=["\']?submit["\']?', html, re.IGNORECASE) else 0
    HasHiddenFields = 1 if re.search(r'<input[^>]+type=["\']?hidden["\']?', html, re.IGNORECASE) else 0
    HasCopyrightInfo = 1 if re.search(r'©|&copy;|copyright', html, re.IGNORECASE) else 0
    NoOfImage = len(re.findall(r'<img', html, re.IGNORECASE))
    NoOfCSS = len(re.findall(r'<link[^>]+rel=["\']?stylesheet["\']?', html, re.IGNORECASE))
    NoOfJS = len(re.findall(r'<script[^>]+src=["\']?', html, re.IGNORECASE))
    # Count empty <a href="">
    NoOfEmptyRef = len(re.findall(r'<a\s+[^>]*href=["\']?["\']?', html, re.IGNORECASE))
    # Count total <a href="...">
    TotalRef = len(re.findall(r'<a\s+[^>]*href=["\']?[^"\'>]+["\']?', html, re.IGNORECASE)) + NoOfEmptyRef
    
    return np.array([
        HasTitle,
        HasFavicon,
        IsResponsive,
        HasDescription,
        NoOfPopup,
        NoOfiFrame,
        HasSocialNet,
        HasSubmitButton,
        HasHiddenFields,
        HasCopyrightInfo,
        NoOfImage,
        NoOfCSS,
        NoOfJS,
        NoOfEmptyRef,
        TitleLength,
        TotalRef
    ]).reshape(1, -1)  # Reshaping for a single sample

# Load the model
model_path = 'Saved Models/LR_forHTML.pkl' 
model = joblib.load(model_path)  

# Get user input (for a one-line HTML string)
html_code = input("Enter the HTML code in one line: ")

# Get features
features = analyze_html(html_code)

# Print the feature array
print("Feature Array:", features)

# Make predictions
predictions = model.predict(features)

# Print the results
print("Model Predictions:", predictions)
