import abc


class TurbulenceProfile(abc.ABC):

    def __init__(self, amplitude, q_vector):

        self.amplitude = amplitude
        self.q_vector = q_vector

        super().__init__()

    @abc.abstractmethod
    def profile(self, x, y, phi):
        pass

