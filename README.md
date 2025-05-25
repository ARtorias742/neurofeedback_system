# Neurofeedback Training System

A real-time neurofeedback system using EEG data from OpenBCI, processed with MNE-Python, and visualized with PsychoPy.

## Requirements
- OpenBCI Cyton or Ganglion board
- Python 3.8+
- Dependencies: `pip install -r requirements.txt`

## Setup
1. Connect OpenBCI board (update `port` in `main.py` if needed).
2. Adjust `config.yaml` for your EEG channels and thresholds.
3. Run `python src/main.py`.

## Features
- Streams EEG data in real-time.
- Filters signals and extracts alpha band power.
- Provides visual feedback via a dynamic bar.

## Notes
- Calibrate `threshold_alpha` in `config.yaml` based on baseline EEG recordings.
- Ensure OpenBCI drivers are installed.