import json

class JsonHandler:
    def __init__(self, json_file):
        with open(json_file) as json_data:
            self.json_data = json.load(json_data)
        try:
            self.monte_carlo_is_active = self.json_data['monte_carlo']['active']
        except:
            self.monte_carlo_is_active = False
        try:
            self.plot_trajectory = self.json_data['plot_trajectory']
        except:
            self.plot_trajectory = False

        self.keys = list(dict(self.json_data).keys())