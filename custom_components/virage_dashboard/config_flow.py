import logging
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback

_LOGGER = logging.getLogger(__name__)

@config_entries.HANDLERS.register("virage_dashboard")
class VirageDashboardConfigFlow(config_entries.ConfigFlow):
    async def async_step_user(self, user_input=None):
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")
        return self.async_create_entry(title="", data={})
