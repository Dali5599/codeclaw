import os
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
from codeclaw.config import get_config

class Workspace:
    def __init__(self):
        self.app_name = get_config().app_name
        self.version = get_config().version
        self.sandbox_enabled = get_config().enable_sandbox

    def create_file_tree_api(self):
        self.api = Flask(__name__)
        self.api.route('/', methods=['POST', 'GET'], defaults={'file': ''})
            def index(file=None):
                if file is not None:
                    return send_file(self._get_file_path(file), as_attachment=True, attachment_filename= os.path.basename(file))
                else:
                    return self.api.send_static_file('index.html')

        self.api.route('/upload', methods=['POST'], defaults={'file': ''})
            def upload(file=None):
                if file is not None:
                    with open(os.path.join(self._get_root_path(), 'files', secure_filename(file)), 'wb') as f:
                        f.write(request.files['file'].data)

                    return self.api.send_static_file('index.html')
                else:
                    return "File uploaded successfully!", 201

        self.api.route('/download/<string:filename>', methods=['GET'])
            def download(filename):
                file_path = os.path.join(self._get_root_path(), 'files', filename)
                if not os.path.exists(file_path):
                    raise FileNotFoundError(f"File {filename} not found")
                return send_file(file_path, as_attachment=True, attachment_filename=os.path.basename(filename))

        self.api.run(debug=False)
    
    def _get_root_path(self):
        return os.path.dirname(os.path.abspath(__file__))
    
    def _get_file_path(self, file_name):
        return os.path.join(self._get_root_path(), 'files', file_name)

if __name__ == '__main__':
    workspace = Workspace()
    workspace.create_file_tree_api()
