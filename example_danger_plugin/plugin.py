from danger_python.plugins import DangerPlugin


class ExampleDangerPlugin(DangerPlugin):
    def hello(self):
        created = len(self.danger.git.created_files)
        modified = len(self.danger.git.modified_files)
        deleted = len(self.danger.git.deleted_files)
        self.message(f"Created files count: {created}")
        self.message(f"Modified files count: {modified}")
        self.message(f"Deleted files count: {deleted}")
