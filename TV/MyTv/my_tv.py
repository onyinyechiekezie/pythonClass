class Television:

    def __init__(self):
        self._is_on = False
        self._volume_level = 0
        self._channel = 1
        self._is_mute = False


    @property
    def is_on(self):
        return self._is_on

    @is_on.setter
    def is_on(self, value):
        self._is_on = value
        if self._is_on:
            self._volume_level = 0
            self._channel = 1


    @property
    def volume(self):
        return self._volume_level

    @property
    def is_mute(self, value):
        return self._is_mute

    @is_mute.setter
    def is_mute(self, value):
        if self._is_on:
            self._is_mute = value
            if value:
                self._volume_level = 0


    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        if self._is_on:
            if 1 <= value <= 100:
                self._channel = value
            raise ValueError("Channel must be between 1 and 100")

    # @channel.setter
    # def channel(self, channel):
    #     if self.is_on and channel <= 100 or self.channel > 1:
    #         self.channel = channel

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False
        # self.volume_level = 0
        # self.channel = 1

    def increase_volume(self):
        if self._is_on and 0 <= self._volume_level <= 100:
            self._volume_level += 1
        raise ValueError("Volume must be between 0 and 100")

    def decrease_volume(self):
        if self._is_on and 0 < self._volume_level <= 100:
            self._volume_level -= 1
        raise ValueError("Volume must be between 0 and 100")

    def increase_channel(self):
        if self._is_on and 0 < self._channel <= 100:
            self._channel += 1
        raise ValueError("Channel must be between 0 and 100")

    def decrease_channel(self):
        if self._is_on and 0 < self._channel <= 100:
            self._channel -= 1
        raise ValueError("Channel must be between 0 and 100")

    def mute(self):
        if self.is_on and self._is_mute:
            self._volume_level = 0


    def unmute(self):
        if self.is_on and self._is_mute == True:
            self._volume_level += 1














