# 🚀 PDF to Instant Study Notes with Google Gemini

**No Copy-Pasting, No Storage Hassles! 📚💡**  

## 🌟 Introduction  
Ever struggled with extracting key questions from PDFs and formatting them for study? This AI-powered tool automates the entire process:  

✅ **Extracts questions from any PDF**  
✅ **Generates structured answers using Google Gemini AI**  
✅ **Formats everything into a clean, shareable web page**  
✅ **No need for Word files, screenshots, or extra storage!**  

What started as a personal frustration is now a **game-changer** for students & educators. Just upload, get AI-powered notes, and share a simple link!  

---

## 🔧 Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/MoutasimQazi/PDF-to-Instant-Study-Notes-with-Google-Gemini.git
cd Gemini-PDF-StudyNotes
```

### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Google Gemini API  
- Sign up for **Google AI API** and get a **GEMINI_API_KEY**.  
- Add your API key as an environment variable:  
  ```bash
  export GEMINI_API_KEY="your-api-key-here"
  ```  

---

## 🚀 How It Works  

1️⃣ **Upload a PDF**  
2️⃣ **Extracts all questions** from the document  
3️⃣ **Google Gemini AI generates structured answers**  
4️⃣ **Creates a formatted web page** with password protection  
5️⃣ **Share the link**—no extra storage required!  

---

## 🎯 Usage  

### Extract Questions & Get AI-Powered Answers  
```bash
python main.py --pdf example.pdf
```

The output HTML file will be generated and can be shared directly.  

---

## 📌 Features  
✔️ **AI-Powered Question Extraction** – No manual copy-pasting  
✔️ **Automated Answer Generation** – Structured & reliable responses  
✔️ **Instant Web Page Creation** – Just one link to share  
✔️ **Minimal Storage Usage** – No Word files or screenshots needed  

---

## 🌟 File Structure  
```
📚 Gemini-PDF-StudyNotes
│── main.py          # Main script for processing PDFs & generating HTML
│── requirements.txt # Required dependencies
│── README.md        # Project documentation
```

---

## 🔒 Password Protection  
- The generated HTML file is password-protected.  
- Default password: `dontstudy`  
- Modify the password inside `main.py` if needed.  

---

## 💪 Contributing  
Feel free to fork this project, open issues, or submit PRs to improve functionality!  

---

## 🌇 License  
This project is licensed under the **MIT License**. See `LICENSE` for more details.  

---

## 💡 Let's Connect!  
Have ideas to improve this tool? Want to collaborate? Reach out!  


