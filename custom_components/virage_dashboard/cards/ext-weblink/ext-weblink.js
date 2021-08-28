class ExtWebLink extends HTMLElement {
  set hass(hass) {
    if (!this.config.icon) {
      this.config.icon = "mdi:wifi";
    }
    if (!this.config.entity) {
      var state = "";
    } else {
      if (hass.states[this.config.entity].attributes.unit_of_measurement) {
        var state = hass.states[this.config.entity].state+' '+hass.states[this.config.entity].attributes.unit_of_measurement;
      } else {
        var state = hass.states[this.config.entity].state
      }
    }
    if (this.config.name) {
      var name = this.config.name;
    } else {
      var name = hass.states[this.config.entity].attributes.friendly_name;
    }
    if (!this.config.url) {
      this.config.url = "#";
    } 
    this.innerHTML =`
      <style>
        a {
          align-items: right;
          color: var(--primary-color);
          text-decoration-line: none;
          padding-top: 0px;
          padding-right: 0px;
          padding-bottom: 2px;
          padding-left: 0px;

        }
        hui-generic-row {
          align-items: center;
          color: var(--primary-color);
          text-decoration-line: none;
					margin: 0px;
        }
        ha-icon .innline {
          padding-top: 0px;
          padding-right: 10px;
          padding-bottom: 2px;
          padding-left: 0px;
          color: var(--paper-item-icon-color);
          text-align: right;
					align: right;
        }
        ha-icon {
          padding-top: 0px;
          padding-right: 10px;
          padding-bottom: 2px;
          padding-left: 20px;
          color: var(--paper-item-icon-color);
					text-align: right;
					align: right;
        }

        div {
          flex: 1;
          white-space: nowrap;
          overflow: hidden;
          text-overflow: ellipsis;
        }
        div .state {
          text-align: right;
        }
        div .name {
          text-align: centre;
          overflow: visible;
          padding-top: 5px;
          padding-right: 0px;
          padding-bottom: 0px;
          padding-left: 3px;
					font-size: 12px;
          
        }
        div .main {
          display: flex;
        }
      </style>
      <div class="main">
          <ha-icon icon="${this.config.icon}"></ha-icon>
          <div class="name">${name}</div>
          <a href="${this.config.url}" target="_blank"><ha-icon icon="mdi:open-in-new" class="innline"></ha-icon></a>

        
      </div>
    `;
  }
  setConfig(config) {
    this.config = config;
  }

  getCardSize() {
    return 1;
  }
}
customElements.define('ext-weblink', ExtWebLink);