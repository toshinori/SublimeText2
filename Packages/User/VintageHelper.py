import sublime, sublime_plugin

class OnSaveComannd(sublime_plugin.EventListener):
  def on_post_save(self, view):
    if not view.settings().get('command_mode'):
      view.run_command('exit_insert_mode')


