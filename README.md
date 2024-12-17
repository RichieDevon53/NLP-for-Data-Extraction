# NLP-for-Data-Extraction

# Instruction Document

## Purpose
This application is a **Data Extractor** that utilizes deep learning to extract specific information such as the quantity of items, item names, patterns, and locations from an input sentence. It employs a pre-trained model and tokenizer for sequence prediction.

[Drive Link for Extracted Model](https://drive.google.com/file/d/1FF3NSg7EKEvO-OfRP7xQlUTJnVn-DY_I/view?usp=drive_link) 
---

## Setup Instructions

### 1. Environment Setup
1. Install Python (>=3.8).
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/MacOS
   venv\Scripts\activate      # For Windows
   ```

### 2. Install Dependencies
Install the required Python packages from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 3. Prepare Model and Tokenizer Files
Ensure the following files are placed in the same directory as `app.py`:
- `model.h5` - The pre-trained deep learning model.
- `tokenizer.pickle` - The tokenizer used for text preprocessing.

---

## Running the Application
1. Execute the script to launch the GUI application:
   ```bash
   python app.py
   ```

2. The application will open a window with the title "Data Extractor".

3. Enter a sentence in the input field and click the **"Extract Data"** button. The application will process the input and display the extracted data in the following categories:
   - JUMLAH BARANG (Quantity)
   - NAMA BARANG (Item Name)
   - MOTIF (Pattern)
   - LOKASI (Location)

---

## Technical Notes
- The deep learning model uses the TensorFlow framework.
- The `customtkinter` library provides a modern GUI layout.
- The model expects sentences with a maximum of 20 tokens. Sentences exceeding this length will be truncated or padded.

---

## Troubleshooting
- **Missing Dependencies:** Ensure all packages listed in `requirements.txt` are correctly installed.
- **File Not Found Error:** Verify the presence of `model.h5` and `tokenizer.pickle` in the project directory.
- **Invalid Input Format:** The input sentence should be clear and concise for accurate data extraction.

---

If you have additional questions or need further assistance, feel free to ask!
