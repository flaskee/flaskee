# FlaskEE

The FlaskEE is an open-source project based on the Flask web framework. The main philosophy is the FlaskEE provides enterprise solutions to develop the microservices in modern software architecture.

## Getting Started

Download the FlaskEE project using command prompt if you haven't yet:

```
$ git clone https://github.com/flaskee/flaskee.git
```

### Prerequisites

Required system requirements:

```
1. Minimum memory - 2GB
2. Processor      - Pentium 800MHz or equivalent at minimum
3. Python 	  - 3.7 or above
```

### Installing

1. At the command prompt, install required pip dependencies:

```
$ pip install -r requirements.txt
```

2. Start a development server executing the following command on prompt:

```
$ sh serve.sh
```

3. Go to http://localhost:5000 and you can start development as service based.

### How to Use


1. Create your first REST API inside of the **flaskee/api** directory.

	Example: flaskee/api/users.py
```
from flask import Blueprint

from flaskee.api import route

bp = Blueprint('users', __name__, url_prefix='/users')

@route(bp, '/', methods=['GET'])
def users():
    return ['Jhon', 'Deo']
```

2. Now execute the following command on the prompt and test the result:

```
$ curl http://localhost:5000/api/users
```


## Authors

* **Nadeen Gamage** - *Core Developer* - [@nadeengamage](https://github.com/nadeengamage)


## License

This project is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details

## To-Do Roadmap

* Implement Authentication and Authorization module including modern security mechanisms such as OAuth2, JWT, SAML2, LDAP, etc..
* Health checking module of the API services.
