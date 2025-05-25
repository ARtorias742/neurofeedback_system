from eeg_acquisition import EEGAcquisition
from signal_processing import EEGProcessor
from feedback_interface import FeedbackInterface
import time
import numpy as np

def main():
    # Initialize components
    eeg = EEGAcquisition(port='COM3')  # Adjust port as needed
    processor = EEGProcessor()
    feedback = FeedbackInterface()
    
    try:
        # Start EEG streaming
        eeg.start_stream()
        time.sleep(1)  # Wait for stream to stabilize
        
        while True:
            # Get data
            data = eeg.get_data(processor.config['eeg']['buffer_size'])
            if data is not None:
                # Process data
                filtered_data = processor.preprocess(data)
                alpha_power = processor.compute_band_power(filtered_data)
                print(f"Alpha power: {alpha_power:.2f} uV^2")
                # Update feedback
                feedback.update_feedback(alpha_power)
            
            # Check for quit
            if 'escape' in event.getKeys():
                break
            time.sleep(processor.config['feedback']['update_rate'])
    
    except KeyboardInterrupt:
        print("Stopping neurofeedback system...")
    
    finally:
        eeg.stop_stream()
        feedback.close()

if __name__ == "__main__":
    main()