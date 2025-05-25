from pyOpenBCI import OpenBCICyton
import numpy as np
from queue import Queue
import time

class EEGAcquisition:
    def __init__(self, sample_rate=250, port='COM3'):
        self.sample_rate = sample_rate
        self.data_queue = Queue()
        self.board = None
        self.port = port

    def stream_callback(self, sample):
        """Callback to handle incoming EEG samples."""
        self.data_queue.put(np.array(sample.channels_data))

    def start_stream(self):
        """Start streaming EEG data from OpenBCI."""
        try:
            self.board = OpenBCICyton(port=self.port, daisy=False)
            self.board.start_stream(self.stream_callback)
            print("EEG streaming started.")
        except Exception as e:
            print(f"Error starting EEG stream: {e}")
            raise

    def stop_stream(self):
        """Stop EEG streaming."""
        if self.board:
            self.board.stop_stream()
            self.board.disconnect()
            print("EEG streaming stopped.")

    def get_data(self, num_samples):
        """Retrieve EEG data from queue."""
        data = []
        while len(data) < num_samples and not self.data_queue.empty():
            data.append(self.data_queue.get())
        return np.array(data) if data else None