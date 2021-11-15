# Virage Dashboard

An integration to easily track, set up and label Virage Laboratories devices within Home Assistant.  The integration can be installed through HACS, or by copying the contents of https://github.com/viragelabs/virage_dashboard/tree/main/custom_components to the custom_components folder in your Home Assistant instance.

This integration has two components - first, five automations (included as blueprints).  One automation installs new motion sensors or door contacts, the second listens to these after they are installed.  The third monitors installed sensors for battery conditon and tamper state.  The remaining two allow you to easily set up a three-way or four-way switch using Virage Laboratories switches, plugs or dimmers.  These are installed along with the integration, or may be manually installed (see below).

The second component is the Virage Dashboard (accessible via the side bar) that allows you to see all of your Virage Laboratories devices in one place (light switches, dimmers, electrical plugs, RF receivers, door/window contacts, motion sensors etc.), set up and name new ones, and access the administration pages of WiFi-enabled Virage devices. Note that the dashboard installs several custom cards, including https://github.com/iantrich/config-template-card [![Config Template Card]]

## Automations

If you do not want to install the full integration, you may install the automations separately.  The automations are included in this repository as Blueprints, which can be easily installed in Home Assistant:

In Home Assistant, go to the Configuration menu, then to Blueprints.  Click the Import Blueprint button, and paste the following URLs (one at a time) into the space provided, or click the Import Blueprint buttons to be taken there automatically:

https://github.com/viragelabs/virage_dashboard/blob/main/custom_components/virage_dashboard/blueprints/sensor_install.yaml<p>
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fviragelabs%2Fvirage_dashboard%2Fblob%2Fmain%2Fcustom_components%2Fvirage_dashboard%2Fblueprints%2Fsensor_install.yaml)

https://github.com/viragelabs/virage_dashboard/blob/main/custom_components/virage_dashboard/blueprints/sensor_data.yaml<p>
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fviragelabs%2Fvirage_dashboard%2Fblob%2Fmain%2Fcustom_components%2Fvirage_dashboard%2Fblueprints%2Fsensor_data.yaml)

Click Preview Blueprint, then Import Blueprint (repeat this for each URL above).
  
![image](https://github.com/viragelabs/virage_dashboard/blob/main/images/importdialog.PNG)

After installing either the full integration, or just the automations, you should then see the imported blueprints shown the in the list of available blueprints in your Home Assistant.  Click Create Automation beside one of the blueprints. 

![image](https://github.com/viragelabs/virage_dashboard/blob/main/images/blueprintlist.PNG)

Enter a description in the space provided and click Save.  <b>Do not</b> change the name of the automation.  Note that the Save button will not appear until you type something in the Description field.

![image](https://github.com/viragelabs/virage_dashboard/blob/main/images/createautomation.PNG)
  
Both automations should now be listed in the Automations list in your Home Assistant.
  
## Integration
  
Whether you install it via HACS or manually, once installed, the integration will create a new icon in the sidebar of your Home Assistant installation (as well as an entry in the Integrations area of Home Assistant).  Clicking on this icon will open the Virage Dashboard.  The dashboard displays all of the installed Virage Laboratories devices in one screen, organized by device type.  It also allows you to set up and name new door/window contacts or motion sensors via an installed VirageBridge device, as well as access the administration interfaces of WiFi-enabled Virage devices.
  
Note that Virage Laboratories light switches, dimmers, bridges and electrical plugs are installed in Home Assistant via their built-in web interfaces (see product documentation for more details).  Once you have configured them, they should be automatically detected by Home Assistant and installed.  Note that it may take up to 5 minutes for a newly detected WiFi device to appear in your Virage Dashboard.
