import mne
import numpy as np
import yaml

class EEGProcessor:
    def __init__(self, config_path='config/config.yaml'):
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        self.sample_rate = self.config['eeg']['sample_rate']
        self.channels = self.config['eeg']['channels']
        self.lowcut = self.config['filtering']['lowcut']
        self.highcut = self.config['filtering']['highcut']
        self.notch = self.config['filtering']['notch']
        self.alpha_band = self.config['frequency_bands']['alpha']

    def preprocess(self, raw_data):
        """Apply filtering to EEG data."""
        if raw_data is None or raw_data.size == 0:
            return None
        # Create MNE Raw object
        info = mne.create_info(ch_names=self.channels, sfreq=self.sample_rate, ch_types='eeg')
        raw = mne.io.RawArray(raw_data.T * 1e-6, info)  # Convert uV to V
        # Apply notch filter
        raw.notch_filter(self.notch)
        # Apply bandpass filter
        raw.filter(self.lowcut, self.highcut)
        return raw.get_data()

    def compute_band_power(self, data):
        """Compute power in alpha band."""
        if data is None:
            return 0.0
        # Compute PSD using Welch's method
        psds, freqs = mne.time_frequency.psd_array_welch(
            data, sfreq=self.sample_rate, fmin=self.alpha_band[0], fmax=self.alpha_band[1]
        )
        # Average power across channels
        return np.mean(psds) * 1e12  # Convert to uV^2