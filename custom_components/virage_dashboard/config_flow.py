import logging
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback

_LOGGER = logging.getLogger(__name__)

# Configuration:
LANGUAGE = "language"
LANGUAGES = [
    "English",
    "Danish",
    "German",
    "Spanish",
    "French",
    "Italian",
    "Norwegian",
    "Romanian",
    "Swedish",
    "Dutch",
]
SIDEPANEL_TITLE = "sidepanel_title"
SIDEPANEL_ICON = "sidepanel_icon"
THEME = "theme"
PRIMARY_COLOR = "primary_color"
THEME_OPTIONS = [
    "Auto Mode (Dark/Light)",
    "Dark Mode",
    "Light Mode",
    "Auto Mode (Black/White)",
    "Black Mode",
    "White Mode",
    "HA selected theme"
]
CUSTOMIZE_PATH = "customize_path"

@config_entries.HANDLERS.register("virage_dashboard")
class VirageDashboardConfigFlow(config_entries.ConfigFlow):
    async def async_step_user(self, user_input=None):
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")
        return self.async_create_entry(title="", data={})
