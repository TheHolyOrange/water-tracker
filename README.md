
# Water Tracker - AI-Powered Hydration Monitor

A smart hydration assistant that combines AI analysis with intuitive tracking.  
Log your daily water intake, receive personalized feedback from an AI model, and visualize your hydration patterns through an interactive dashboard.  

> Inspired by this YouTube tutorial: [Watch here](https://youtu.be/pEiq3sI8dYQ?si=goz3fin-z86KfFX5) 

## Features

### AI-Powered Hydration Tracking
- Get personalized feedback on your water intake from an AI assistant  
- Smart analysis of your daily hydration status  
- Recommendations on whether you need to drink more water  

### Interactive Dashboard  
- Visualize your water intake history with charts and tables  
- Track daily progress with an intuitive Streamlit interface  
- Easy logging of water consumption with a simple form  

### Data Persistence  
- Automatic storage of all water intake records in SQLite database  
- View complete history of your hydration patterns  
- Data organized by date and user for easy retrieval  
 
### Multi-User Support  
- Track water intake for multiple users  
- Each user maintains their own separate history  
- Easy switching between user profiles  


## Tech Stack

### Core
- **Python 3.9+** (Base language)
- **FastAPI** (REST API backend)
- **Streamlit** (Interactive dashboard)
- **SQLite** (Local database storage)

### AI Integration
- **Together.ai** (Qwen/Qwen3-235B-A22B-Instruct-2507-tput model)

### DevOps
- **dotenv** (Environment management)
- **Logging** (Activity tracking)

### Key Libraries
- `pandas` (Data analysis)  
- `uvicorn` (API server)  
- `python-dotenv` (Env variables) 

## Installation

1. **Clone the repository**:

```bash
  git clone https://github.com/TheHolyOrange/water-tracker.git
  cd water-tracker
```

2. **Set up Virtual Environment**:
```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate    # Windows
```

3. **Install Dependencies**:
```bash
    pip install -r requirements.txt
```

4. **API Key**:
```bash
    set TOGETHER_API_KEY=your_api_key_here # cmd
    $env:TOGETHER_API_KEY="your_api_key_here" #PowerShell
```

5. **Set Up DB**
```bash
    python src/database.py
```

6. **Run Application**:
```bash
    streamlit run src/dashboard.py
    uvicorn src.api:app --reload
```    
