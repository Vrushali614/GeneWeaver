# GeneWeaver Module Explanations

The following are simple explanations of the logical modules proposed for the project. Replace these names with the exact filenames and functions in the supplied source code.

## 1. main.py – Main Controller
Starts the application and connects the input, validation, alignment, and result stages.

## 2. input_handler.py – Input Handler
Accepts sequence data from the user or from supported input files.

## 3. validation.py – Sequence Validation
Checks that required inputs are present and contain only symbols accepted by the application.

## 4. preprocessing.py – Sequence Preprocessing
Cleans and prepares sequence data in the format required by the alignment algorithm.

## 5. alignment.py – Alignment Engine
Performs the core sequence comparison/alignment. The exact algorithm and scoring rules must be documented from the implementation.

## 6. gpu_acceleration.py – GPU Processing
Provides GPU-based computation if the project includes a compatible GPU backend. It may prepare data for GPU processing and call GPU operations. If this file or functionality is absent, remove this module from the final documentation.

## 7. results.py – Result Display
Formats and displays the alignment output and any scores or comparison details produced by the program.

## Module workflow
Input → Validation → Preprocessing → Alignment (CPU/GPU backend) → Results
