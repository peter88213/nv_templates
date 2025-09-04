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
from pathlib import Path
import webbrowser

from nvtemplates.nvtemplates_locale import _
from nvlib.controller.plugin.plugin_base import PluginBase
from nvtemplates.template_manager import TemplateManager
import tkinter as tk


class Plugin(PluginBase):
    """A 'Story Templates' plugin class."""
    VERSION = '@release'
    API_VERSION = '5.18'
    DESCRIPTION = 'A "Story Templates" manager'
    URL = 'https://github.com/peter88213/nv_templates'
    HELP_URL = f'{_("https://peter88213.github.io/nvhelp-en")}/nv_templates/'

    FEATURE = _('Story Templates')

    def disable_menu(self):
        """Disable menu entries when no project is open.
        
        Overrides the superclass method.
        """
        self.templatesMenu.entryconfig(f"{_('Load')}...", state='disabled')
        self.templatesMenu.entryconfig(f"{_('Save')}...", state='disabled')

    def enable_menu(self):
        """Enable menu entries when a project is open.
        
        Overrides the superclass method.
        """
        self.templatesMenu.entryconfig(f"{_('Load')}...", state='normal')
        self.templatesMenu.entryconfig(f"{_('Save')}...", state='normal')

    def install(self, model, view, controller):
        """Add a submenu to the 'Tools' menu.
        
        Positional arguments:
            model -- reference to the novelibre main model instance.
            view -- reference to the novelibre main view instance.
            controller -- reference to the novelibre main controller instance.

        Extends the superclass method.
        """
        super().install(model, view, controller)
        self.templateManager = TemplateManager(model, view, controller)
        self._icon = self._get_icon('templates.png')

        # Create "Story Templates" submenu.
        self.templatesMenu = tk.Menu(self._ui.toolsMenu, tearoff=0)
        self.templatesMenu.add_command(
            label=f"{_('Load')}...",
            command=self.load_template,
        )
        self.templatesMenu.add_command(
            label=f"{_('Save')}...",
            command=self.save_template,
        )
        self.templatesMenu.add_command(
            label=_('Open folder'),
            command=self.open_folder,
        )

        # Add an entry to the "File > New" menu.
        self._ui.newMenu.add_command(
            label=_('Create from template...'),
            image=self._icon,
            compound='left',
            command=self.new_project,
        )

        # Create Tools menu entry.
        self._ui.toolsMenu.add_cascade(
            label=self.FEATURE,
            image=self._icon,
            compound='left',
            menu=self.templatesMenu,
        )

        # Add an entry to the Help menu.
        self._ui.helpMenu.add_command(
            label=_('Templates plugin Online help'),
            image=self._icon,
            compound='left',
            command=self.open_help,
        )

    def load_template(self):
        self.templateManager.load_template()

    def lock(self):
        """Disable menu entries when the project is locked.
        
        Overrides the superclass method.
        """
        self.templatesMenu.entryconfig(
            f"{_('Load')}...",
            state='disabled',
        )

    def new_project(self):
        self.templateManager.new_project()

    def open_folder(self):
        self.templateManager.open_folder()

    def open_help(self, event=None):
        webbrowser.open(self.HELP_URL)

    def save_template(self):
        self.templateManager.save_template()

    def unlock(self):
        """Enable menu entries when the project is unlocked.
        
        Overrides the superclass method.
        """
        self.templatesMenu.entryconfig(
            f"{_('Load')}...",
            state='normal',
        )

    def _get_icon(self, fileName):
        # Return the icon for the main view.
        if self._ctrl.get_preferences().get('large_icons', False):
            size = 24
        else:
            size = 16
        try:
            homeDir = str(Path.home()).replace('\\', '/')
            iconPath = f'{homeDir}/.novx/icons/{size}'
            icon = tk.PhotoImage(file=f'{iconPath}/{fileName}')
        except:
            icon = None
        return icon

