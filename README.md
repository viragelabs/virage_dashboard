# Virage Dashboard

An integration to easily set up and label Virage rf sensors and contacts using the VirageBridge with Home Assistant.

This integration has two components - first, two automations.  One automation installs new sensors, the second manages the sensors after they are installed.

These automations are included in this repository as Blueprints, which can be easily installed in Home Assistant in one of two ways:

In Home Assistant, go to the Configuration menu, then to Blueprints.  Click the Import Blueprint button, and paste the following URLs (one at a time) into the space provided:

https://github.com/viragelabs/virage_dashboard/blob/main/blueprints/sensor_install.yaml

https://github.com/viragelabs/virage_dashboard/blob/main/blueprints/sensor_data.yaml



Click Preview Blueprint, then Import Blueprint (repeat this for each URL above).  You should then see 
