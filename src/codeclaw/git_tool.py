import git

class GitTool:
    def __init__(self):
        self.git = git.Repo().clone(