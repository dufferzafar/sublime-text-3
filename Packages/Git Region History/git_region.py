# Python's stdlib
import os
import subprocess

# Sublime Text API
import sublime
import sublime_plugin

GIT_LOG = [
    "git",
    "--no-pager", "log", "--no-expand-tabs", "-p", "-L{l1},{l2}:{f}"
]


class GitRegionHistoryCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        # If some text is selected, only work on that
        sel = self.view.substr(self.view.sel()[0]).strip()
        if not sel:
            sublime.status_message("Select a region to view it's history")

        region = self.view.sel()[0]
        lines = self.view.line(region)
        l1, _ = self.view.rowcol(lines.begin())
        l2, _ = self.view.rowcol(lines.end())

        filename = os.path.basename(self.view.file_name())
        filepath = os.path.dirname(self.view.file_name())

        print(l1, l2, filename)
        GIT_LOG[-1] = GIT_LOG[-1].format(l1=l1, l2=l2, f=filename)

        # print(GIT_LOG)

        try:
            out = subprocess.check_output(GIT_LOG, cwd=filepath)
            # print(out)
        except subprocess.CalledProcessError:
            out = ""

        if out:
            new = self.view.window().new_file()
            new.set_scratch(True)
            new.set_name("Region History: " + GIT_LOG[-1])
            new.set_syntax_file('Packages/GitSavvy/syntax/show_commit.sublime-syntax')  # noqa
            new.run_command("append", {"characters": out.decode("utf8")})
            new.set_read_only(True)
