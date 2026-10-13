
        import typer
        from codeclaw.cli import app
        from typer.testing import CliRunner
        import autocomplete
        import readline

        # Créer un objet REPL liéger
        class REPL:
            def __init__(self, app):
                self.app = app
                self.runner = CliRunner(self.app)

            # Afficher un message prompt personnalisés
            def prompt(self, message=None):
                if not self.app.config["enable_sandbox"]:
                    return "No sandbox mode"
                current_dir = self.get_current_directory()"