# 📸 SnapClass: AI-Powered Attendance System

SnapClass takes attendance from a classroom photo or a short audio recording. Teachers upload the photo (or record the class), check the result, and save. Students sign in with their face, join subjects, and track their own attendance.

🔗 **[Live Demo](https://snapclass-faizan.streamlit.app/)**

## ✨ Features

### 🧑 Face Recognition
- Finds and recognizes students in classroom photos
- Creates 128-dimensional face embeddings with dlib
- Identifies students using a Linear SVM classifier
- Verifies each match with Euclidean distance
- Combines several photos into a single attendance session

### 🎙️ Voice Recognition
- Identifies students from recorded classroom audio
- Creates speaker embeddings with Resemblyzer
- Splits audio into segments with Librosa and matches them using similarity scores
- Students can register their voice while creating a profile

### 👩‍🏫 Teacher Dashboard
- Create and manage subjects
- Take attendance from photos or voice recordings
- Review and edit results before saving
- Share enrollment links and QR codes
- See attendance history and class statistics

### 🎓 Student Dashboard
- Register and log in with face recognition
- Join a subject using a code or QR link
- View enrolled subjects and attendance records
- Unenroll from a subject

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Machine Learning | Scikit-learn (Linear SVM) |
| Computer Vision | dlib, face_recognition_models |
| Voice | Resemblyzer, Librosa |
| Data | NumPy, Pandas |
| Frontend | Streamlit |
| Database | Supabase (PostgreSQL) |
| Auth | Face login, bcrypt |
| Other | Pillow, Segno (QR codes) |

## ⚙️ How It Works

**Face attendance**

1. A student registers by capturing their face
2. The embedding is stored in Supabase
3. A Linear SVM is trained on all registered students
4. The teacher uploads one or more classroom photos
5. Faces are detected, matched to student profiles, and verified by distance
6. The teacher reviews the list and confirms

**Voice attendance**

1. Students can register their voice (optional)
2. The teacher records the classroom audio
3. Librosa splits the audio into segments
4. Resemblyzer creates an embedding for each segment
5. Embeddings are compared with the registered voice profiles
6. Matched students are marked present after the teacher confirms

## 🚀 Getting Started

**1. Clone the repository**

```bash
git clone https://github.com/Faizan-2419/SnapClass.git
cd SnapClass
```

**2. Create a virtual environment**

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS / Linux:

```bash
source .venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

> `dlib-bin` is used so you don't need to compile dlib yourself. The `face_recognition_models` package is installed straight from GitHub, so you need Git installed.

**4. Set up Supabase**

Create a `.streamlit/secrets.toml` file:

```toml
SUPABASE_URL = "your-supabase-url"
SUPABASE_KEY = "your-supabase-key"
```

Then create these tables in your Supabase project: `teachers`, `students`, `subjects`, `subject_students`, `attendance_logs`.

Never commit `secrets.toml`. Add it to `.gitignore`.

**5. Run the app**

```bash
streamlit run app.py
```

## 📁 Project Structure

```text
SnapClass/
├── app.py
├── requirements.txt
└── src/
    ├── components/     # Reusable UI components
    ├── database/       # Supabase integration
    ├── pipeline/       # Face and voice recognition
    ├── screens/        # Teacher and student dashboards
    └── ui/             # Styling
```

## ⚠️ Limitations

- Face matching depends on lighting, camera angle, and photo quality
- Voice matching gets harder with background noise and many people talking at once
- Teachers always review results before saving, since no model is perfect

## 🔮 Future Work

- Liveness detection for face login, so a printed photo can't be used
- Better handling of noisy classroom audio
- Export attendance reports to CSV or PDF

## 💡 About the Project

I built SnapClass to see how AI could take over the boring parts of a classroom, like calling out names one by one. The part I enjoyed most was building two separate biometric pipelines, one for faces and one for voices, and then connecting both to a full working app with Streamlit and Supabase.

## 👤 Author

**Faizanur Rahman**
B.Tech, Computer Science & Engineering
Interested in AI, Machine Learning, Deep Learning, and Computer Vision.
