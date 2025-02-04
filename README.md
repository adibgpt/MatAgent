# MatAgent: A Physics-Aware Multi-Agent LLM Framework for Materials Science Discovery

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

MatAgent is a cutting-edge, physics-aware multi-agent **Large Language Model (LLM)** framework designed to accelerate **materials science discovery and optimization**. This repository provides the source code and resources to facilitate **material property prediction, hypothesis generation, experimental data analysis, high-performance material discovery, data-driven experimentation, and literature review automation**.

## 🚀 Features
- **Material Property Prediction**: Predicts experimental material properties such as band gaps, superconducting critical temperatures, and mechanical properties.
- **Hypothesis Generation**: Uses AI-driven techniques to propose new materials with desired characteristics.
- **Experimental Data Analysis**: Automates the analysis of large-scale experimental datasets.
- **Accelerated Alloy & Polymer Discovery**: Integrates machine learning (ML) and density functional theory (DFT) to optimize material compositions.
- **Automated Literature Review**: Extracts and synthesizes insights from scientific papers to support research.
- **Multi-Agent AI Framework**: Uses LLM-based specialized agents for a closed-loop, autonomous research cycle.

## 📑 Project Structure
```
MatAgent/
│── data/               # Datasets used in the experiments
│── models/             # Pre-trained and fine-tuned models
│── notebooks/          # Jupyter notebooks for analysis and visualization
│── src/                # Core framework components
│   ├── agents/         # AI-driven agents for different tasks
│   ├── processing/     # Data preprocessing and feature engineering
│   ├── training/       # Machine learning model training scripts
│   ├── evaluation/     # Benchmarking and validation methods
│── scripts/            # Automated scripts for execution
│── results/            # Experiment outputs, visualizations, and reports
│── README.md           # Project documentation
│── requirements.txt    # Required dependencies
│── LICENSE             # License information
```

## 🔧 Installation
### Prerequisites
- Python 3.8+
- Pip or Conda for package management
- GPU (optional, recommended for faster model execution)

### Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/adibgpt/MatAgent.git
   cd MatAgent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download datasets (if applicable)**
   - Place datasets in the `data/` directory.

## 🛠️ Usage
### 1️⃣ Running Material Property Prediction
```bash
python src/agents/material_property.py --data_path data/materials.csv
```

### 2️⃣ Running Hypothesis Generation
```bash
python src/agents/hypothesis_generation.py --dataset data/superconductors.csv
```

### 3️⃣ Performing Experimental Data Analysis
```bash
python src/agents/data_analysis.py --experiment_file data/experimental_results.csv
```

### 4️⃣ Literature Review Automation
```bash
python src/agents/literature_review.py --topic "Perovskite Solar Cells"
```

For more detailed usage examples, refer to the **notebooks/** folder.

## 📊 Benchmarking & Performance
MatAgent has been tested across several **benchmarking categories**, including:
- **Material property prediction** (band gap, yield strength, etc.)
- **Superconducting materials discovery** (critical temperature prediction)
- **Experimental data analysis** (temperature dependence studies)
- **Automated literature review** (scientific text mining)

Check the **results/** directory for performance metrics and evaluation reports.

## 📝 Citation
If you use MatAgent in your research, please cite our paper:
```
@article{MatAgent2025,
  title   = {MatAgent: A Physics-Aware Multi-Agent LLM Framework for Accelerating Materials Science Discovery},
  author  = {Anonymous},
  journal = {ICLR 2025 Submission},
  year    = {2025}
}
```

## 📜 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing
We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-new`).
3. Commit changes (`git commit -m "Added new feature"`).
4. Push to your fork (`git push origin feature-new`).
5. Submit a pull request.

## 🔗 Resources & Acknowledgments
- [Materials Informatics Research](https://www.nature.com/subjects/materials-informatics)
- [LangChain](https://www.langchain.com/)
- [OpenAI's GPT Models](https://openai.com/)
- [Firecrawl](https://firecrawl.ai/)

---
For any questions, please reach out via GitHub Issues or Discussions.

🌟 **Star this repository if you find it useful!**
