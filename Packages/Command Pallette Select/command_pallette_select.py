import sublime
import sublime_plugin


class SelectCommandPaletteTextCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.window.run_command("show_overlay", {"overlay": "command_palette"})
        self.window.run_command("select_all")
