import os
from jinja2 import Environment, FileSystemLoader

# Defina as variáveis de ambiente conforme necessário
os.environ['POSTGRES_USER'] = 'your_postgres_user'
os.environ['POSTGRES_PASSWORD'] = 'your_postgres_password'
os.environ['MONGO_INITDB_ROOT_USERNAME'] = 'your_mongo_user'
os.environ['MONGO_INITDB_ROOT_PASSWORD'] = 'your_mongo_password'

# Defina quais serviços estão ativados
enabled_services = {
    'app_enabled': True,
    'postgres_enabled': True,
    'rabbitmq_enabled': False,
    'mongodb_enabled': True,
}

# Carregue o template Jinja2
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('docker-compose.template.yaml')

# Renderize o template com os serviços habilitados
rendered_template = template.render(**enabled_services)

# Salve o resultado no arquivo docker-compose.yml
with open('docker-compose.yaml', 'w') as f:
    f.write(rendered_template)
