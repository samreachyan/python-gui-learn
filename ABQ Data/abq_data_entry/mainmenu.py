
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from functools import partial


class GenericMainMenu(tk.Menu):
    """The Applications's mainn menu"""

    def __init__(self, parent, settings, callbacks, **kwargs):
        super().__init__(parent, **kwargs)

        self.settings = settings
        self.callbacks = callbacks
        self._build_menu()

    def show_about(self):
        """Show the about dialog"""

        about_message = 'ABQ Data Entry'
        about_detail = ('by Alan D Moore\n'
                        'For assistance please contact the author.')

        messagebox.showinfo(title='About',
                            message=about_message,
                            detail=about_detail)

    def on_theme_change(self, *args):
        """Pop up a message about theme changes"""
        message = "Change requires restart"
        detail = (
            "Theme changes do not take effect"
            " until application restart")
        messagebox.showwarning(
            title='Warning',
            message=message,
            detail=detail)

    def _build_menu(self):
        # The file menu
        file_menu = tk.Menu(self, tearoff=False)
        file_menu.add_command(
            label="Select file...",
            command=self.callbacks['file->open'],
            accelerator='Ctrl+O')
        file_menu.add_separator()
        file_menu.add_command(
            label="Quit",
            command=self.callbacks['file->quit'],
            accelerator='Ctrl+Q')

        self.add_cascade(
            label='File',
            menu=file_menu)

        options_menu = tk.Menu(self, tearoff=False)
        options_menu.add_checkbutton(
            label='Autofill Date',
            variable=self.settings['autofill date'])
        options_menu.add_checkbutton(
            label='Autofill Sheet data',
            variable=self.settings['autofill sheet data'])

        font_size_menu = tk.Menu(self, tearoff=False)
        for size in range(6, 17, 1):
            font_size_menu.add_radiobutton(
                label=size,
                value=size,
                variable=self.settings['font size'])

        options_menu.add_cascade(
            label='Font size',
            menu=font_size_menu)

        style = ttk.Style()
        themes_menu = tk.Menu(self, tearoff=False)
        for theme in style.theme_names():
            themes_menu.add_radiobutton(
                label=theme,
                value=theme,
                variable=self.settings['theme']
            )

        options_menu.add_cascade(
            label='Theme',
            menu=themes_menu)

        self.add_cascade(
            label='Options',
            menu=options_menu)

        go_menu = tk.Menu(self, tearoff=False)
        go_menu.add_command(label="Record List",
                            command=self.callbacks['show_recordlist'],
                            accelerator='Ctrl+L')
        go_menu.add_command(label="New Record",
                            command=self.callbacks['new_record'],
                            accelerator='Ctrl+N')

        self.add_cascade(
            label='Go',
            menu=go_menu)

        help_menu = tk.Menu(self, tearoff=False)
        help_menu.add_command(
            label='About...',
            command=self.show_about)

        self.add_cascade(
            label='Help',
            menu=help_menu)

        self.settings['theme'].trace('w', self.on_theme_change)

    def get_keybinds(self):
        return{
            '<Control-o>': self.callbacks['file->open'],
            '<Control-q>': self.callbacks['file->quit'],
            '<Control-n>': self.callbacks['new_record'],
            '<Control-l>': self.callbacks['show_recordlist']
        }

    def _bind_accelerators(self):
        keybinds = self.get_keybinds()
        for key, command in keybinds.items():
            self.bind_all(key, partial(self._argstrip, command))

    @staticmethod
    def _argstrip(function, *args):
        return function()


class WindowsMainMenu(GenericMainMenu):
    def _build_menu(self):
        # The file menu
        file_menu = tk.Menu(self, tearoff=False)
        file_menu.add_command(
            label="Select file...",
            command=self.callbacks['file->open'],
            accelerator='Ctrl+O')
        file_menu.add_separator()
        file_menu.add_command(
            label="Exit",
            command=self.callbacks['file->quit'])

        self.add_cascade(
            label='File',
            menu=file_menu)

        tools_menu = tk.Menu(self, tearoff=False)

        options_menu = tk.Menu(tools_menu, tearoff=False)
        options_menu.add_checkbutton(
            label='Autofill Date',
            variable=self.settings['autofill date'])
        options_menu.add_checkbutton(
            label='Autofill Sheet data',
            variable=self.settings['autofill sheet data'])

        font_size_menu = tk.Menu(self, tearoff=False)
        for size in range(6, 17, 1):
            font_size_menu.add_radiobutton(
                label=size,
                value=size,
                variable=self.settings['font size'])

        options_menu.add_cascade(
            label='Font size',
            menu=font_size_menu)

        style = ttk.Style()
        themes_menu = tk.Menu(self, tearoff=False)
        for theme in style.theme_names():
            themes_menu.add_radiobutton(
                label=theme,
                value=theme,
                variable=self.settings['theme']
            )

        options_menu.add_cascade(
            label='Theme',
            menu=themes_menu)

        tools_menu.add_separator()
        tools_menu.add_cascade(
            label='Options',
            menu=options_menu)

        self.add_cascade(
            label='Tools',
            menu=tools_menu)

        self.add_command(label="Record List",
                         command=self.callbacks['show_recordlist'],
                         accelerator='Ctrl+L')
        self.add_command(label="New Record",
                         command=self.callbacks['new_record'],
                         accelerator='Ctrl+N')

        help_menu = tk.Menu(self, tearoff=False)
        help_menu.add_command(
            label='About...',
            command=self.show_about)

        self.add_cascade(
            label='Help',
            menu=help_menu)

        self.settings['theme'].trace('w', self.on_theme_change)

    def get_keybinds(self):
        return{
            '<Control-o>': self.callbacks['file->open'],
            '<Control-n>': self.callbacks['new_record'],
            '<Control-l>': self.callbacks['show_recordlist']
        }


class LinuxMainMenu(GenericMainMenu):
    """The Applications's mainn menu"""

    def _build_menu(self):
        # The file menu
        file_menu = tk.Menu(self, tearoff=False)
        file_menu.add_command(
            label="Select file...",
            command=self.callbacks['file->open'],
            accelerator='Ctrl+O')
        file_menu.add_separator()
        file_menu.add_command(
            label="Quit",
            command=self.callbacks['file->quit'],
            accelerator='Ctrl+Q')

        self.add_cascade(
            label='File',
            menu=file_menu)

        # The edit menu
        edit_menu = tk.Menu(self, tearoff=False)
        edit_menu.add_checkbutton(
            label='Autofill Date',
            variable=self.settings['autofill date'])
        edit_menu.add_checkbutton(
            label='Autofill Sheet data',
            variable=self.settings['autofill sheet data'])

        self.add_cascade(
            label='Edit',
            menu=edit_menu)

        view_menu = tk.Menu(self, tearoff=False)

        font_size_menu = tk.Menu(self, tearoff=False)
        for size in range(6, 17, 1):
            font_size_menu.add_radiobutton(
                label=size,
                value=size,
                variable=self.settings['font size'])

        view_menu.add_cascade(
            label='Font size',
            menu=font_size_menu)

        style = ttk.Style()
        themes_menu = tk.Menu(self, tearoff=False)
        for theme in style.theme_names():
            themes_menu.add_radiobutton(
                label=theme,
                value=theme,
                variable=self.settings['theme']
            )

        view_menu.add_cascade(
            label='Theme',
            menu=themes_menu)

        self.add_cascade(
            label='View',
            menu=view_menu)

        go_menu = tk.Menu(self, tearoff=False)
        go_menu.add_command(label="Record List",
                            command=self.callbacks['show_recordlist'],
                            accelerator='Ctrl+L')
        go_menu.add_command(label="New Record",
                            command=self.callbacks['new_record'],
                            accelerator='Ctrl+N')

        self.add_cascade(
            label='Go',
            menu=go_menu)

        help_menu = tk.Menu(self, tearoff=False)
        help_menu.add_command(
            label='About...',
            command=self.show_about)

        self.add_cascade(
            label='Help',
            menu=help_menu)

        self.settings['theme'].trace('w', self.on_theme_change)


class MacOsMainMenu(GenericMainMenu):
    def _build_menu(self):
        app_menu = tk.Menu(self, tearoff=False, name='apple')

        app_menu.add_command(
            label='About ABQ Data Entry',
            command=self.show_about)
        self.add_cascade(label='ABQ Data Entry', menu=app_menu)

        # The file menu
        file_menu = tk.Menu(self, tearoff=False)
        file_menu.add_command(
            label="Select file...",
            command=self.callbacks['file->open'],
            accelerator='Cmd+o')
        file_menu.add_separator()
        file_menu.add_command(
            label="Quit",
            command=self.callbacks['file->quit'],
            accelerator='Cmd+q')

        self.add_cascade(
            label='File',
            menu=file_menu)

        # The edit menu
        edit_menu = tk.Menu(self, tearoff=False)
        edit_menu.add_checkbutton(
            label='Autofill Date',
            variable=self.settings['autofill date'])
        edit_menu.add_checkbutton(
            label='Autofill Sheet data',
            variable=self.settings['autofill sheet data'])

        self.add_cascade(
            label='Edit',
            menu=edit_menu)

        view_menu = tk.Menu(self, tearoff=False)

        font_size_menu = tk.Menu(self, tearoff=False)
        for size in range(6, 17, 1):
            font_size_menu.add_radiobutton(
                label=size,
                value=size,
                variable=self.settings['font size'])

        view_menu.add_cascade(
            label='Font size',
            menu=font_size_menu)

        style = ttk.Style()
        themes_menu = tk.Menu(self, tearoff=False)
        for theme in style.theme_names():
            themes_menu.add_radiobutton(
                label=theme,
                value=theme,
                variable=self.settings['theme']
            )

        view_menu.add_cascade(
            label='Theme',
            menu=themes_menu)

        self.add_cascade(
            label='View',
            menu=view_menu)

        window_menu = tk.Menu(self, name='window', tearoff=False)

        window_menu.add_command(label="Record List",
                                command=self.callbacks['show_recordlist'],
                                accelerator='Cmd+l')
        window_menu.add_command(label="New Record",
                                command=self.callbacks['new_record'],
                                accelerator='Cmd+n')

        self.add_cascade(
            label='Window',
            menu=window_menu)

    def get_keybinds(self):
        return{
            '<Command-o>': self.callbacks['file->open'],
            '<Command-n>': self.callbacks['new_record'],
            '<Command-l>': self.callbacks['show_recordlist']
        }


def get_main_menu_for_os(os_name):
    menus = {
        'Linux': LinuxMainMenu,
        'Darwin': MacOsMainMenu,
        'freebsd7': LinuxMainMenu,
        'Windows': WindowsMainMenu
    }
    return menus.get(os_name, GenericMainMenu)
