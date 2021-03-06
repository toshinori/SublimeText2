import sublime, sublime_plugin

class OnSaveComannd(sublime_plugin.EventListener):
  def on_post_save(self, view):
    if not view.settings().get('command_mode'):
      view.run_command('hide_auto_complete')
      view.run_command('exit_insert_mode')

class HideAutoCompleteAndExitInsertModeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    if not self.view.settings().get('command_mode'):
      self.view.run_command('hide_auto_complete')
      self.view.run_command('exit_insert_mode')

class HideAutoCompleteAndSave(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.run_command('hide_auto_complete')
    self.view.run_command('save')

class RunAndExitVisualModeCommand(sublime_plugin.TextCommand):
  def run(self, edit, command):
    self.view.run_command(command)
    self.view.run_command("exit_visual_mode")

class ToggleCommentAndExitVisualModeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.run_command('toggle_comment', {"block": False})
    self.view.run_command("exit_visual_mode")
