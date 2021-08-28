import logging
import os
import shutil
from homeassistant.components.frontend import add_extra_js_url

DATA_EXTRA_MODULE_URL = 'frontend_extra_module_url'

_LOGGER = logging.getLogger(__name__)

def load_plugins(hass, name):

    add_extra_js_url(hass, "/virage_dashboard/cards/config-template-card/config-template-card.js")
    add_extra_js_url(hass, "/virage_dashboard/cards/auto-entities/auto-entities.js")
    add_extra_js_url(hass, "/virage_dashboard/cards/ext-weblink/ext-weblink.js")
    add_extra_js_url(hass, "/virage_dashboard/cards/vertical-stack-in-card/vertical-stack-in-card.js")
    hass.http.register_static_path("/virage_dashboard/cards", hass.config.path(f"custom_components/{name}/cards"), True)
    
    for fname in os.listdir(hass.config.path("custom_components/virage_dashboard/blueprints")):
     if not os.path.isfile(hass.config.path("blueprints/automation/viragelabs/"+fname)):
         if fname.endswith('.yaml'):
             _LOGGER.debug("Copy: "+fname)
             os.makedirs(hass.config.path("blueprints/automation/viragelabs"), exist_ok=True)
             shutil.copy2(
                 hass.config.path("custom_components/virage_dashboard/blueprints/"+fname),
                 hass.config.path("blueprints/automation/viragelabs")
                
         )

