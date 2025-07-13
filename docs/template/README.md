[![Download the latest release](docs/img/download-button.png)](https://github.com/peter88213/nv_templates/raw/main/dist/nv_templates_v0.99.0.pyzw)
[![Changelog](docs/img/changelog-button.png)](docs/changelog.md)
[![News/Feedback](docs/img/news-button.png)](https://github.com/peter88213/novelibre/discussions)
[![Online help](docs/img/help-button.png)](https://peter88213.github.io/nvhelp-en/nv_templates/)


# ![T]( icons/templates.png)nv_templates

The [novelibre](https://github.com/peter88213/novelibre/) Python program helps authors organize novels.

*nv_templates* is a plugin for managing Markdown "Story Templates".

![Screenshot](docs/Screenshots/screen01.png)

![Screenshot](docs/Screenshots/structure01.png)

## Features

In *novelibre*, you can define a narrative structure with *stages* on two different levels. *nv_templates* faciliates the reuse of narrative structures.

- Load the narrative structure from a Markdown template file:
    - When loading a template into an empty project, a whole story framework is created.
    - When loading a template into a project that has already chapters, a list of stages is created in an "unused" chapter.
- Save the narrative structure to a Markdown template file. 


## Requirements

- [novelibre](https://github.com/peter88213/novelibre/) version 5.18+

## Download and install

---

**Note**

The plugin comes with sample templates which are automatically
copied into the *templates* folder of the *novelibre* installation. 
Existing files are overwritten. So if you customize your templates, 
better rename them.  

---

### Default: Executable Python zip archive

Download the latest release [nv_templates_v0.99.0.pyzw](https://github.com/peter88213/nv_templates/raw/main/dist/nv_templates_v0.99.0.pyzw)

- Launch *nv_templates_v0.99.0.pyzw* by double-clicking (Windows/Linux desktop),
- or execute `python nv_templates_v0.99.0.pyzw` (Windows), resp. `python3 nv_templates_v0.99.0.pyzw` (Linux) on the command line.

#### Important

Many web browsers recognize the download as an executable file and offer to open it immediately. 
This starts the installation.

However, depending on your security settings, your browser may 
initially  refuse  to download the executable file. 
In this case, your confirmation or an additional action is required. 
If this is not possible, you have the option of downloading 
the zip file. 


### Alternative: Zip file

The package is also available in zip format: [nv_templates_v0.99.0.zip](https://github.com/peter88213/nv_templates/raw/main/dist/nv_templates_v0.99.0.zip)

- Extract the *nv_templates_v0.99.0* folder from the downloaded zipfile "nv_templates_v0.99.0.zip".
- Move into this new folder and launch *setup.pyw* by double-clicking (Windows/Linux desktop), 
- or execute `python setup.pyw` (Windows), resp. `python3 setup.pyw` (Linux) on the command line.

---

[Changelog](docs/changelog.md)

## Usage

See the [online manual](https://peter88213.github.io/nvhelp-en/nv_templates/)

## Credits

- The notes in the *Hero's journey* sample template are from the
  [Wikipedia page](https://en.wikipedia.org/wiki/Hero%27s_journey) on this topic.
- The notes in the *Save The Cat* sample template are based on the
  [Wikipedia page](https://en.wikipedia.org/wiki/Save_the_Cat!:_The_Last_Book_on_Screenwriting_You%27ll_Ever_Need) 
  on this topic.
- The icons are based on the [Eva Icons](https://akveo.github.io/eva-icons/#/), published under the [MIT License](http://www.opensource.org/licenses/mit-license.php). The original black and white icons were colored for this plugin by the maintainer. 


## License

This is Open Source software, and the *nv_templates* plugin is licensed under GPLv3. See the
[GNU General Public License website](https://www.gnu.org/licenses/gpl-3.0.en.html) for more
details, or consult the [LICENSE](https://github.com/peter88213/nv_templates/blob/main/LICENSE) file.
