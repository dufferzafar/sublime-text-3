# Python's stdlib
import os
import sys

# Sublime Text API
import sublime
import sublime_plugin

# A git repo placed in the current folder
# https://github.com/timothycrosley/isort/
from .isort.isort import SortImports


class IsortCommand(sublime_plugin.TextCommand):
    view = None

    def get_region(self, view):
        return sublime.Region(0, view.size())

    def get_buffer_contents(self, view):
        return view.substr(self.get_region(view))

    def set_view(self):
        self.view = sublime.active_window().active_view()
        return self.view

    def get_view(self):
        if self.view is None:
            return self.set_view()

        return self.view

    def set_cursor_back(self, begin_positions):
        view = self.get_view()
        for pos in begin_positions:
            view.sel().add(pos)

    def get_positions(self):
        pos = []
        for region in self.get_view().sel():
            pos.append(region)
        return pos

    def run(self, edit):
        view = self.get_view()
        current_positions = self.get_positions()

        contents = self.get_buffer_contents(view)

        isort_settings = self.get_view().settings().get('isort') or {}

        new = SortImports(file_contents=contents, **isort_settings).output
        view.replace(edit, self.get_region(view), new)

        # Our sel has moved now.. (?)
        remove_sel = view.sel()[0]
        view.sel().subtract(remove_sel)
        self.set_cursor_back(current_positions)


class Isort(sublime_plugin.EventListener):

    def on_pre_save(self, view):
        if view.settings().get("isort_on_save") is True:
            view.run_command("isort")
