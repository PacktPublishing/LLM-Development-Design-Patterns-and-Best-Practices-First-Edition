# Installation Guide

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- 8GB+ RAM (for model loading)
- 5GB+ free disk space (for model downloads)

## Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/safety-api.git
   cd safety-api
   ```

2. **Create a virtual environment (recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually if you don't have a requirements file:
   ```bash
   pip install torch transformers fastapi uvicorn pydantic
   ```

4. **Download models (automatically on first run)**:
   ```bash
   python -c "from transformers import AutoModel; AutoModel.from_pretrained('facebook/roberta-hate-speech-dynabench-r4-target')"
   ```

## Hardware Recommendations

- For better performance, use a machine with:
  - 16GB+ RAM
  - NVIDIA GPU with CUDA support
  - SSD storage

## Troubleshooting

- **Out of memory errors**:
  - Try reducing batch size in the code
  - Use `pip install torch --extra-index-url https://download.pytorch.org/whl/cu117` for GPU support

- **Slow performance**:
  - Add `device_map="auto"` when loading models
  - Enable GPU if available