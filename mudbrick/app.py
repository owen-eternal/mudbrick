import os
from .templates import gitignore_file
from .templates import styles_file, config_file
from .templates import base_file, index_file, wsgi_file
from .templates import component_file, init_file, models_file


class CreateDirectory:

    #create root directory
    def project_directory(self, path, project_name):
        #root directory
        root_directory = os.path.join(path, project_name )

        #Sub directories
        templates_directory = os.path.join(root_directory, 'templates')
        component_directory = os.path.join(root_directory, 'component')
        
        #list of subdirectories
        sub_directories = ['/templates', '/component', '/static']
        
        for sub in sub_directories:
            os.makedirs(root_directory + sub)
        
        return root_directory, templates_directory, component_directory
    
class CreateFiles:
    #write inside the files.
    def create_porject_files(self, project_name, f):

        #flask initialization module
        if f.name.endswith('__init__.py'):
            f.write(init_file(project_name))
        #flask database model file.
        elif f.name.endswith('models.py'):
            f.write(models_file)
        else:
            f.write(config_file)

    def component_files(self, f):
        if f.name.endswith('routes.py'):
            f.write(component_file)

    def create_root_files(self, project_name, f):
        #create wsgi file.
        #run app in debug mode
        if f.name.endswith('wsgi.py'):
            f.write(f"from {project_name} import create_app\n")
            f.write(wsgi_file)
        elif f.name.endswith('.gitignore'):
            f.write(gitignore_file)
          
    def template_files(self, f):
        #create template files
        if f.name.endswith('base.html'):
            f.write(base_file)
        elif f.name.endswith('styles.html'):
            f.write(styles_file)
        else:
            f.write(index_file)
        

class BuildProject(CreateDirectory, CreateFiles):
    #list of all the template files 
    root_path = os.getcwd()
    root_files = ['wsgi.py', '.gitignore', 'requirements.txt']
    templates_files = ['base.html', 'index.html', 'styles.html']
    app_component_files = ['__init__.py', 'routes.py']
    project_folder_files = ['__init__.py', 'models.py', 'config.py']

    def __init__(self, project_name):
        self.project_name = project_name

    @property
    def start_builder(self):
        #create project directory and return the path
        project_folder_path, templates_path, component_path  = self.project_directory(self.root_path, self.project_name)
        #build the project folder's files
        self.file_builder(project_folder_path, self.project_folder_files)
        #build app component files
        self.file_builder(component_path, self.app_component_files)
        #build project template files
        self.file_builder(templates_path, self.templates_files)
        #build the root folder's files
        self.file_builder(self.root_path, self.root_files) 

    def file_builder(self, path, files :list):
        #iterate through the list of files
        #and build the contents of the files
        for file in files:
            file_path = os.path.join(path, file)
            with open(file_path, 'w') as f:
                if path.endswith(self.root_path):
                    self.create_root_files(self.project_name, f) 

                elif path.endswith(self.project_name):
                    self.create_porject_files(self.project_name, f)

                elif path.endswith('component'):
                    self.component_files(f)

                else:
                    self.template_files(f)



    