
#  Life Expectancy Analysis with DBSCAN Clustering

##  Overview
Explore global life expectancy patterns by clustering countries using **DBSCAN**, based on health, economic, and demographic indicators like GDP, healthcare accessibility, and mortality rates. This project includes data preprocessing, feature scaling, cluster modeling, and insightful visualizations.

---

##  Table of Contents
- [⚙️ Installation](#-installation)  
- [🚀 Usage](#-usage)  
- [📁 Project Structure](#-project-structure)  
- [📊 Results](#-results)  
- [🤝 Contributing](#-contributing)  
- [📬 Contact](#-contact)  

---

##  Installation
```bash
git clone https://github.com/Srinithimahalakshmi/Life_expectancy.git
cd Life_expectancy

python3 -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
````

---

## Usage

1. Explore data preprocessing and clustering in the notebook:

   ```bash
   jupyter notebook model_training.ipynb
   ```
2. Run the Flask app to visualize clusters:

   ```bash
   python app.py
   ```
3. Visit the app in your browser at:

   ```
   http://127.0.0.1:5000
   ```

---

## Project Structure

```
Life_expectancy/
├── data/
│   └── life_expectancy.csv         # Dataset file
├── model/
│   └── dbscan_model.pkl            # Trained clustering model
├── static/                         # CSS, JS, images for frontend
├── templates/
│   └── index.html                  # Web interface template
├── app.py                          # Flask application script
├── model_training.ipynb            # Notebook for cluster analysis
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

---

## Results

* Countries grouped into clusters reflecting similar life expectancy attributes.
* Visual outputs such as scatter plots, geographic cluster maps, and silhouette score charts are available in the notebook and app interface.

---

## Contributing

Contributions are welcome! You can help by:

* Improving data preprocessing or feature selection
* Tuning DBSCAN or testing alternative clustering techniques (e.g., K-means, hierarchical)
* Enhancing visualizations or UX of the web interface

To contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m "Add feature..."`
4. Push your branch and open a Pull Request

---

## Contact

👤 **Maintainer**: Srinithi Mahalakshmi
📧 **Email**: [srinithiarumugam2003@gmail.com](mailto:srinithiarumugam2003@gmail.com)
🔗 **GitHub**: [Srinithimahalakshmi](https://github.com/Srinithimahalakshmi)

---

⭐ *If you find this project insightful, feel free to give it a star!*


```
