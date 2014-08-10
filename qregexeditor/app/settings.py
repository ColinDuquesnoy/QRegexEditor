"""
This module contains the code for accessing the application
settings
"""
from pyqode.qt import QtCore


class Settings():
    def __init__(self):
        self._settings = QtCore.QSettings('QRegexEditor')

    @property
    def window_geometry(self):
        return self._settings.value("geometry")

    @window_geometry.setter
    def window_geometry(self, value):
        self._settings.setValue("geometry", value)

    @property
    def window_state(self):
        return self._settings.value("state")

    @window_state.setter
    def window_state(self, value):
        self._settings.setValue("state", value)

    @property
    def show_quick_ref(self):
        return bool(self._settings.value('show_quick_ref', 0))

    @show_quick_ref.setter
    def show_quick_ref(self, value):
        self._settings.setValue('show_quick_ref', value)

    @property
    def compile_flags(self):
        return int(self._settings.value('compile_flags', 0))

    @compile_flags.setter
    def compile_flags(self, value):
        self._settings.setValue('compile_flags', value)

    @property
    def regex(self):
        return self._settings.value('last_pattern', '')

    @regex.setter
    def regex(self, value):
        self._settings.setValue('last_pattern', value)

    @property
    def string(self):
        return self._settings.value('last_string', '')

    @string.setter
    def string(self, value):
        self._settings.setValue('last_string', value)
