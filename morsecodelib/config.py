"""
Configuration options for morsecodelib

Will change to some config-file reader later, maybe.
"""


class Config(object):
    def __init__(self):
        self.SAMPLE_RATE = 22050
        self.FREQUENCY = 600

        self.WORDS_PER_MINUTE = 15

    @property
    def DIT_DURATION(self):
        # PARIS @ 20WPM = 60ms/dit, so a dit at 15 WPM = 0.060s * 20/15
        return 20 * 0.060 / self.WORDS_PER_MINUTE

    @property
    def DAH_DURATION(self):
        return self.DIT_DURATION * 3.0


config = Config()
