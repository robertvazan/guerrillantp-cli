# This script generates and updates project configuration files.

# Run this script with rvscaffold in PYTHONPATH
import rvscaffold as scaffold

class Project(scaffold.Net):
    def script_path_text(self): return __file__
    def repository_name(self): return 'guerrillantp-cli'
    def root_namespace(self): return 'GuerrillaNtp.Cli'
    def pretty_name(self): return 'GuerrillaNtp CLI'
    def nuget_description(self): return 'Command-line interface to GuerrillaNtp SNTP client.'
    def inception_year(self): return 2014
    def project_status(self): return self.stable_status()

    def dependencies(self):
        yield from super().dependencies()
        yield self.use('GuerrillaNtp:3.1.0')

    def documentation_links(self):
        yield from super().documentation_links()
        yield 'GuerrillaNtp library', 'https://guerrillantp.machinezoo.com/'

Project().generate()
