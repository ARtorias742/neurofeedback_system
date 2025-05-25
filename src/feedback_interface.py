from psychopy import visual, core, event
import yaml

class FeedbackInterface:
    def __init__(self, config_path='config/config.yaml'):
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        self.threshold = self.config['feedback']['threshold_alpha']
        self.update_rate = self.config['feedback']['update_rate']
        # Initialize PsychoPy window
        self.win = visual.Window([800, 600], units='norm', color=(0, 0, 0))
        # Feedback bar
        self.bar = visual.Rect(self.win, width=0.1, height=0.0, pos=(0, 0), fillColor='green')

    def update_feedback(self, alpha_power):
        """Update visual feedback based on alpha power."""
        # Scale bar height based on alpha power relative to threshold
        height = min(max((alpha_power / self.threshold) * 0.8, 0.1), 0.8)
        self.bar.height = height
        self.bar.draw()
        self.win.flip()

    def close(self):
        """Close PsychoPy window."""
        self.win.close()
        core.quit()