"""Provide a service class for novelibre template management.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_templates
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
from pathlib import Path
from tkinter import filedialog

from nvlib.controller.services.service_base import ServiceBase
from nvlib.novx_globals import Error
from nvlib.novx_globals import norm_path
from nvtemplates.md_template import MdTemplate
from nvtemplates.nvtemplates_locale import _


class TemplateManager(ServiceBase):

    def __init__(self, model, view, controller):
        super().__init__(model, view, controller)
        try:
            homeDir = str(Path.home()).replace('\\', '/')
            self.templateDir = f'{homeDir}/.novx/templates'
        except:
            self.templateDir = '.'

    def load_template(self):
        """Create a structure of "Todo" chapters and scenes from a Markdown file."""
        if self._ctrl.check_lock():
            return

        fileName = filedialog.askopenfilename(
            filetypes=[(MdTemplate.DESCRIPTION, MdTemplate.EXTENSION)],
            defaultextension=MdTemplate.EXTENSION,
            initialdir=self.templateDir
            )
        if fileName:
            try:
                templates = MdTemplate(fileName, self._mdl, self._ctrl)
                templates.read()
            except Error as ex:
                self._ui.show_error(str(ex), title=_('Template loading aborted'))

    def new_project(self):
        """Create a novelibre project instance."""
        self._ctrl.create_project()
        self.load_template()

    def open_folder(self):
        """Open the templates folder with the OS file manager."""
        try:
            os.startfile(norm_path(self.templateDir))
            # Windows
        except:
            try:
                os.system('xdg-open "%s"' % norm_path(self.templateDir))
                # Linux
            except:
                try:
                    os.system('open "%s"' % norm_path(self.templateDir))
                    # Mac
                except:
                    pass

    def save_template(self):
        """Save a structure of "Todo" chapters and scenes to a Markdown file."""
        fileName = filedialog.asksaveasfilename(
            filetypes=[(MdTemplate.DESCRIPTION, MdTemplate.EXTENSION)],
            defaultextension=MdTemplate.EXTENSION,
            initialdir=self.templateDir
            )
        if not fileName:
            return

        try:
            templates = MdTemplate(fileName, self._mdl, self._ctrl)
            templates.write()
        except Error as ex:
            self._ui.show_error(str(ex), title=_('Cannot save template'))

        self._ui.set_status(_('Template saved.'))

