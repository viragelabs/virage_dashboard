import logging

from .load_plugins import load_plugins
from .load_dashboard import load_dashboard
from .const import DOMAIN
from homeassistant.components import frontend

from collections import OrderedDict
from typing import Any, Mapping, MutableMapping, Optional

from homeassistant.helpers import discovery


_LOGGER = logging.getLogger(__name__)

async def async_setup(hass, config):
    load_plugins(hass, DOMAIN)

    return True

async def async_setup_entry(hass, config_entry):

    load_dashboard(hass, config_entry)

    return True

async def async_remove_entry(hass, config_entry):
    _LOGGER.warning("Virage is now uninstalled.")

    frontend.async_remove_panel(hass, "virage-dashboard")
