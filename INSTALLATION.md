# Installation Requirements

## Software
- Windows, Linux, or macOS (use an operating system supported by the selected GPU library)
- Python 3.10 or later (confirm the version used by the project)
- pip
- A code editor such as Visual Studio Code or PyCharm
- Git (optional)

## Hardware
- Minimum: a computer capable of running Python.
- GPU acceleration: a compatible NVIDIA GPU and matching NVIDIA driver/CUDA environment if the implementation uses a CUDA-based library.
- CPU execution may be used for development or testing if the code includes a CPU backend.

## Python packages
The exact dependencies must match the project's imports. Common possible packages include:
- numpy – numerical array operations
- biopython – biological sequence utilities, if used
- cupy-cuda12x – GPU array operations on supported CUDA 12 environments, if the code uses CuPy

Do not install optional packages blindly. Check the project's actual imports and CUDA version first.

## Setup
1. Install Python and confirm it is available:
   `python --version`
2. Open a terminal in the project folder.
3. Create a virtual environment:
   `python -m venv .venv`
4. Activate it:
   - Windows PowerShell: `.venv\Scripts\Activate.ps1`
   - Windows CMD: `.venv\Scripts\activate.bat`
   - macOS/Linux: `source .venv/bin/activate`
5. Install dependencies listed in the project's `requirements.txt`:
   `python -m pip install -r requirements.txt`
6. Run the entry-point file specified by the project, for example:
   `python main.py`

## GPU verification
If the project uses CUDA, verify that the GPU driver, CUDA runtime, and Python GPU package are mutually compatible. The exact verification command depends on the library selected by the source code.
