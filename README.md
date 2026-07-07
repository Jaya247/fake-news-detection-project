# 🛡️ TruthCheck - Fake News Detector

An AI-powered news verification web application that checks the credibility of statements by cross-referencing them with real-time news articles.

## 🔗 Live Demo
- **Frontend:** [fake-news-detection-project-tau.vercel.app](https://fake-news-detection-project-tau.vercel.app/)
- **Backend API:** [fake-news-detection-project-xd98.onrender.com](https://fake-news-detection-project-xd98.onrender.com)

## 📋 Features
- User authentication (Register/Login)
- Enter any news statement and get an instant credibility check
- Verification results: **Likely True**, **Likely False**, or **Uncertain**
- Confidence score with supporting news sources
- Daily usage limit for free users (5 checks/day) with a premium plans preview
- Clean, cyberpunk-themed responsive UI

## 🛠️ Technologies Used

**Frontend:**
- HTML, Tailwind CSS, JavaScript
- Font Awesome icons

**Backend:**
- Python, Flask, Flask-CORS
- SQLite (user accounts & usage tracking)
- NLTK (text processing)
- scikit-learn (TF-IDF vectorization + cosine similarity)
- NewsAPI (real-time news article retrieval)

**Deployment:**
- Frontend hosted on **Vercel**
- Backend hosted on **Render**

## ⚙️ How It Works
1. User enters a claim/statement to verify
2. Backend extracts keywords and fetches related articles from NewsAPI
3. TF-IDF + cosine similarity compares the statement against retrieved articles
4. A verification result with confidence score and top sources is returned

## 🚀 Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/Jaya247/fake-news-detection-project.git
   cd fake-news-detection-project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root folder:
   ```
   NEWS_API_KEY=your_newsapi_key_here
   ```
   Get a free API key from [newsapi.org](https://newsapi.org/register).

4. Run the backend server:
   ```bash
   python main.py
   ```

5. Open `index.html` in your browser.

## 🔒 Security Note
API keys are managed via environment variables (`.env`) and are never committed to the repository (see `.gitignore`). Use `.env.example` as a reference for required variables.

## 📄 License
This project is free to use under the MIT License.
