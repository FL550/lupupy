"""Lupusec temperature and humidity device."""

from lupupy.devices import LupusecDevice
import re

regex_temp = re.compile("{WEB_MSG_TS_DEGREE}(\d+\.\d+)")
regex_humi = re.compile("{WEB_MSG_RH_HUMIDITY}(\d+)")


class LupusecTemperatureSensor(LupusecDevice):
    """Class to represent a temperature and humidity sensor."""

    @property
    def status(self):
        #     """
        #     Get sensor state.
        print(self._json_state)
        m = regex_temp.search(self._json_state.get("status"))
        self._temperature = m.group(1) if m else None
        m = regex_humi.search(self._json_state.get("status"))
        self._humidity = m.group(1) if m else None
        return f"{self.temperature} {self.humidity}"

    @property
    def temperature(self):
        """Get sensor temperature."""
        return self._temperature

    @property
    def humidity(self):
        """Get sensor humidity."""
        return self._humidity
