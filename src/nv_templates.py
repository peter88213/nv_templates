"""A "Story Templates" plugin for novelibre.

Requires Python 3.7+
Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_templates
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""
import webbrowser

from nvtemplates.nvtemplates_locale import _
from nvlib.controller.plugin.plugin_base import PluginBase
from nvtemplates.template_service import TemplateService
from nvlib.gui.menus.nv_menu import NvMenu


class Plugin(PluginBase):
    """A 'Story Templates' plugin class."""
    VERSION = '@release'
    API_VERSION = '5.44'
    DESCRIPTION = 'A "Story Templates" manager'
    URL = 'https://github.com/peter88213/nv_templates'
    HELP_URL = f'{_("https://peter88213.github.io/nvhelp-en")}/nv_templates/'

    FEATURE = _('Story Templates')

    def disable_menu(self):
        self.pluginMenu.disable_menu()

    def enable_menu(self):
        self.pluginMenu.enable_menu()

    def install(self, model, view, controller):
        """Add a submenu to the 'Tools' menu.
        
        Positional arguments:
            model -- reference to the novelibre main model instance.
            view -- reference to the novelibre main view instance.
            controller -- reference to the novelibre main controller instance.

        Extends the superclass method.
        """
        super().install(model, view, controller)
        self.templateService = TemplateService(model, view, controller)
        self._icon = self._get_icon('templates.png')

        #--- Configure the main menu.

        # Create "Story Templates" submenu.
        self.pluginMenu = NvMenu()

        label = f"{_('Load')}..."
        self.pluginMenu.add_command(
            label=label,
            command=self.load_template,
        )
        self.pluginMenu.disableOnClose.append(label)
        self.pluginMenu.disableOnLock.append(label)

        label = f"{_('Save')}..."
        self.pluginMenu.add_command(
            label=label,
            command=self.save_template,
        )
        self.pluginMenu.disableOnClose.append(label)

        label = _('Open folder')
        self.pluginMenu.add_command(
            label=label,
            command=self.open_folder,
        )

        # Add an entry to the "File > New" menu.
        label = _('Create from template...')
        self._ui.newMenu.add_command(
            label=label,
            image=self._icon,
            compound='left',
            command=self.new_project,
        )

        # Create Tools menu entry.
        label = self.FEATURE
        self._ui.toolsMenu.add_cascade(
            label=label,
            image=self._icon,
            compound='left',
            menu=self.pluginMenu,
        )

        # Add an entry to the Help menu.
        label = _('Templates plugin Online help')
        self._ui.helpMenu.add_command(
            label=label,
            image=self._icon,
            compound='left',
            command=self.open_help,
        )

    def load_template(self):
        self.templateService.load_template()

    def lock(self):
        self.pluginMenu.lock()

    def new_project(self):
        self.templateService.new_project()

    def open_folder(self):
        self.templateService.open_folder()

    def open_help(self, event=None):
        webbrowser.open(self.HELP_URL)

    def save_template(self):
        self.templateService.save_template()

    def unlock(self):
        self.pluginMenu.unlock()

